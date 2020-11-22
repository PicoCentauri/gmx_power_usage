#!/usr/bin/env python3
# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
#
# Copyright (c) 2020 Philip Loche
#
# Released under the GNU Public Licence, v2 or any higher version
# SPDX-License-Identifier: GPL-2.0-or-later

import math
import os
import re

# Conversion factor
joule_to_kWh = 2.7777777778e-7

# Regular expression commands
CPU_regex = re.compile(r"(?<=Brand: )(.*)")
GPU_regex = re.compile(r"(?<=#0: )(.*)")

# CPU TDP per Core in Watts
CPU_dict = {
    "Intel(R) Xeon(R) CPU E5-2680 v2 @ 2.80GHz": 115 / 10,
    "Intel(R) Core(TM) i7-8700K CPU @ 3.70GHz": 95 / 6,
    "AMD Ryzen Threadripper 1950X 16-Core Processor": 180 / 16,
    "AMD Ryzen Threadripper 3970X 32-Core Processor": 280 / 32,
}

# GPU TDP in Watts
GPU_dict = {
    "NVIDIA Tesla K20Xm": 235,
    "NVIDIA GeForce GTX 1080": 180,
    "NVIDIA GeForce RTX 2080 Ti": 250,
}


def power_usage(log_file, verbose=False):
    """Calculates the power usage of an GROMACS simulation based in the information given 
    the log file.

    Parameters
    ----------
    log_file : str
        The log file for analysis
        
    verbose : bool
        Print information such as CPU & GPU vendor.
        
    Returns
    -------
    E : float
        The power usage of the simulation (kWh)
        
        
    Raises
    ------
    AttributeError if `log_file` does not contain time information.
    """

    with open("md.log", "r") as log:

        GPU_used = False

        log_lines = log.readlines()
        for i_line, line in enumerate(log_lines):
            line = line.strip()
            if len(line) == 0:
                continue

            elif line.startswith("Brand:"):
                CPU = CPU_regex.findall(line)[0].strip()

            elif line.startswith("GPU info:"):
                GPU_used = True
                N_GPU = int(log_lines[i_line + 1].split()[-1])
                GPU = GPU_regex.findall(log_lines[i_line + 2])[0].split(",")[0]

            elif line.startswith("Time:"):
                t = line.split()
                Core_t = float(t[1])
                Wall_t = float(t[2])
                break  # The time information is the last information in the log

    if "Core_t" not in locals():
        raise AttributeError("`log_file` does not contain time information.")

    N_CPU = int(math.ceil(Core_t / Wall_t))

    E_CPU = CPU_dict[CPU] * Core_t * joule_to_kWh
    E_GPU = 0
    if GPU_used:
        E_GPU = GPU_dict[GPU] * Wall_t * joule_to_kWh

    E = E_CPU + E_GPU
    if verbose:
        print(f"Total simulation time = {Wall_t:.2e} s")
        print(f"E_CPU = {E_CPU:.2e} kWh ({N_CPU} x {CPU})")
        if GPU_used:
            print(f"E_GPU = {E_GPU:.2e} kWh ({N_GPU} x {GPU})")
            print(f"E_total = {E} kWh")

    return E
