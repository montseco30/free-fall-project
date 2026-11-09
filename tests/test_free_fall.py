import pytest 
from src.free_fall import simulate_fall


def test_no_drag_fall():
    # drag here is 0 because there is no air so it should match exact kinematics t = sqrt(2h/g)
    fall_time, final_v = simulate_fall(mass=10, drag_coef=0.0, initial_height=1000)
    kinematics_time = ((2 * 1000) / 9.81) ** (0.5)
    assert fall_time == pytest.approx(kinematics_time, abs=0.1)


def test_drag_slows_fall():
    # higher drag has to result in a longer fall time and lower the final velocity
    t_no_drag, v_no_drag = simulate_fall(mass=5.0, drag_coef=0.0)
    t_add_drag, v_add_drag = simulate_fall(mass=5.0, drag_coef=0.5)

    assert t_add_drag > t_no_drag

    assert abs(v_add_drag) < abs(v_no_drag)


def test_heavy_object_falls_faster():
    # when there is drag, heavier objects hit the ground with a higher terminal velocity
    t_light, _ = simulate_fall(mass=1.0, drag_coef=0.1)

    t_heavy, _ = simulate_fall(mass=50.0, drag_coef=0.1)

    assert t_heavy < t_light