#!/usr/bin/env python3
# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
#
# Copyright (c) 2021 Philip Loche
#
# Released under the GNU Public Licence, v2 or any higher version
# SPDX-License-Identifier: GPL-2.0-or-later

import math
import os
import re

from . import TDP

# Conversion factor
joule_to_kWh = 2.7777777778e-7

# Regular expression commands
CPU_regex = re.compile(r"(?<=Brand: )(.*)")
GPU_regex = re.compile(r"(?<=#0: )(.*)")


class PowerUsage(object):
    """Calculates the power usage of an GROMACS simulation based in the information given 
    the log file.

    Parameters
    ----------
    log_file : str
        The log file for analysis

    verbose : bool
        Print information such as CPU & GPU vendor.

    Attributes
    ----------
    E : float
        power usage of the simulation (kWh)
    CPU : str
        CPU vendor
    N_CPU : int
        number of CPUs
    E_CPU : float
        The power usage of all GPUs (kWh)
    GPU : str
        GPU vendor (only if used)
    N_GPU : int 
        number of GPUs (only if used)
    E_GPU : float
        power usage of all GPUs (kWh) (only if used)
    Core_t : float
        total kernel time (s)
    Wall_t : float
        total simulation time (s)

    Raises
    ------
    AttributeError if `log_file` does not contain time information.
    """
    def __init__(self, log_file, verbose=False):
        self.log_file = log_file
        self.verbose = verbose
        
        with open(self.log_file, "r") as log:

            GPU_used = False

            log_lines = log.readlines()
            for i_line, line in enumerate(log_lines):
                line = line.strip()
                if len(line) == 0:
                    continue

                elif line.startswith("Brand:"):
                    self.CPU = CPU_regex.findall(line)[0].strip()

                elif line.startswith("GPU info:"):
                    GPU_used = True
                    self.N_GPU = int(log_lines[i_line + 1].split()[-1])
                    self.GPU = GPU_regex.findall(log_lines[i_line + 2])[0].split(",")[0]

                elif line.startswith("Time:"):
                    t = line.split()
                    self.Core_t = float(t[1])
                    self.Wall_t = float(t[2])
                    break  # The time information is the last information in the log

        if not hasattr(self, "Core_t"):
            raise AttributeError("`log_file` does not contain time information.")

        self.N_CPU = int(math.ceil(self.Core_t / self.Wall_t))

        self.E_CPU = TDP.CPU[self.CPU] * self.Core_t * joule_to_kWh
        self.E_GPU = 0
        if GPU_used:
            self.E_GPU = TDP.GPU[self.GPU] * self.Wall_t * joule_to_kWh

        self.E = self.E_CPU + self.E_GPU
