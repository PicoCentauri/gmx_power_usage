# GMX power usage - Get an estimate power usage of your GROMACS MD simulation

A small function to estimate the power usage of a molecular
dynamics simulation using the thermal design power (TDP) of the
CPU and GPU. 

# Installation

You'll need [Python3](https://www.python.org). To install the package for all
users type

```sh
    git clone https://github.com/PicoCentauri/gmx_power_usage.git
    cd gmx_power_usage
    pip3 install .
```

# Usage

```python
    import gmx_power_usage
    gmx_power_usage.power_usage("md.log", verbose=True)
```

The CPU (per core) and GPU TDPs are stored in the `CPU_dict` and `GPU_dict` 
dictionary. You can add your own hardware by 

```python
    gmx_power_usage.CPU_dict["my_cpu"] = <<cpus_tdp>>
    gmx_power_usage.GPU_dict["my_gpu"] = <<gpus_tdp>>
```