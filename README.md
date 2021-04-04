# GMX power usage - Get an estimate power usage of your GROMACS MD simulation

Estimate the power usage of a molecular
dynamics simulation using the thermal design power (TDP) of your
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
    pu = gmx_power_usage.PowerUsage("md.log", verbose=True)
```

To add your own hardware change the the `CPU` (per core) and `GPU` dictionaries 
in [gmx_power_usage/TDP.py](gmx_power_usage/TDP.py)  and reinstall the package.