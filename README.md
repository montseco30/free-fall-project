# Physics Free-Fall & Terminal Velocity Simulator

## Overview
This project models a 1D vertical free-fall under gravity and air resistance forces. It runs multiple simulations across object masses and drag coefficients to compare how the final velocity relates to mass.

## Environment Setup
Recreate the software environment using Mamba:
```bash
mamba env create -f environment.yml
mamba activate freefall-env
```
## Running Tests
Run unit tests locally using `pytest`:
```bash
pytest
```

Continuous integration is configured through github actions (`.github/workflow/ci.yml) to run `pytest` automatically on every push to `main`.

## SLURM Cluster Execution and Accounting
run the simulation batch job on great lakes hps cluster:
```bash
sbatch run_free_fall.sh
```

### Resource Justification
- CPUs (`--cpus-per-task=1`): The 1d free fall model is a numerical simulation that runs on a single thread
- Memory (`--mem=1G`): Data structures and output arrays created during integration required less than 100 MB
- Time (`--time=00:05:00) the program computes in seconds, but the 5 minutes were alloted to provide a comfortable margin.

The resource accounting record for job `65761922` is saved in `sacct_record.txt`

## AI Usage Disclaimer
I used Gemini to help with changing from unittest to pytest, to help with github issues like shell initialization and git merge. All of the code and logic were created on my own part, then verified they worked correctly.