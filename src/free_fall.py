import csv
import time

def simulate_fall(mass, drag_coef, initial_height=1000.0, dt=0.001):
    """
    Simulates a falling object with air drag 
    mass: kg
    drag_coef: kg/m
    height: m
    """

    g = 9.81
    y = initial_height
    v = 0.0
    t = 0.0

    while y > 0:
        drag_force = drag_coef * (v ** 2)
        gravity_force = mass * g
        acc = g - (drag_force / mass)

        v += acc * dt
        y -= v * dt
        t += dt

    return t, v

def run_all_simulations(masses, drag_coefs):
    results = []
    for m in masses:
        for d in drag_coefs:
            fall_time, final_velocity = simulate_fall(mass=m, drag_coef=d)
            results.append({
                "mass": m,
                "drag": d,
                "fall_time": round(fall_time, 3),
                "terminal_velocity": round(final_velocity, 3)
            })
    return results


if __name__ == "__main__":
    num_sims = 1000

    start_time = time.time()
    print(f"Starting simulations with {num_sims} mass steps...")

    masses = [1.0 + i * (99.0 / num_sims) for i in range(num_sims)]
    drag_coefs = [0.01, 0.05, 0.1, 0.2]

    results = run_all_simulations(masses, drag_coefs)

    with open("free_fall_results.csv", "w", newline="") as f:
        writer = csv.DictWriter(f,fieldnames=["mass", "drag", "fall_time", "terminal_velocity"])
        writer.writeheader()
        writer.writerows(results)

    elapsed = time.time() - start_time

    print(f"Done! Ran {len(results)} total simulations in {elapsed:.2f} seconds.")