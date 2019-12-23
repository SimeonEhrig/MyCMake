# About

The container contains all necessary applications to build all examples in this project.

# Build

To generate or update the singularity recipe simply run the script `recipe.py` (the [HPCCM](https://github.com/NVIDIA/hpc-container-maker) package is required). Then you can build the singularity container.

```bash
# singularity >= 3.3 is required
singularity build --fakeroot cmake.sif recipe.def
```
