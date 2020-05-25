# Conda Environment

https://medium.com/@shandou/export-and-create-conda-environment-with-yml-5de619fe5a2

## Create `environment.yml` file via conda

`conda env export > environment_droplet.yml`

## Commit the yml file, git clone the repo onto the target OS, and create a conda environment from it as follows:

`conda env create -f environment.yml`

## A few other frequently used commands

```python
# list all the conda environment available
conda info --envs  

# Create new environment named as `envname`
conda create --name envname

# Remove environment and its dependencies
conda remove --name envname --all

# Clone an existing environment
conda create --name clone_envname --clone envname
```