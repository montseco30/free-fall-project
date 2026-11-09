#!/bin/bash
#SBATCH --job-name=free_fall_sim
#SBATCH --account=compfor203f26s001_class
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=00:20:00
#SBATCH --mem=2GB
#SBATCH --output=free_fall_%j.out
#SBATCH --error=free_fall_%.err


module load python/3.14.7

source ~/.bashrc

mamba activate freefall-env

python src/free_fall.py