#!/usr/bin/env python3
# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
#
# Copyright (c) 2021 Philip Loche
#
# Released under the GNU Public Licence, v2 or any higher version
# SPDX-License-Identifier: GPL-2.0-or-later


# CPU TDP per Core in Watts
CPU = {
    "Intel(R) Xeon(R) CPU           X5570  @ 2.93GHz": 95 / 4,
    "Intel(R) Xeon(R) CPU E5-2680 v2 @ 2.80GHz": 115 / 10,
    "Intel(R) Xeon(R) Silver 4114 CPU @ 2.20GHz": 85 / 10,
    "Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz": 125 / 16,
    "Intel(R) Core(TM) i5-2400S CPU @ 2.50GHz": 65 / 4,
    "Intel(R) Core(TM) i7-7700 CPU @ 3.60GHz": 65 / 4,
    "Intel(R) Core(TM) i5-8500 CPU @ 3.00GHz": 65 / 6,
    "Intel(R) Core(TM) i7-8700K CPU @ 3.70GHz": 95 / 6,
    "AMD Ryzen Threadripper 1950X 16-Core Processor": 180 / 16,
    "AMD Ryzen Threadripper 3970X 32-Core Processor": 280 / 32,
    "N/A": 0,
}

# GPU TDP in Watts
GPU = {
    "NVIDIA Tesla M2070": 225,
    "NVIDIA Tesla M2070-Q": 225,
    "NVIDIA Tesla K20Xm": 235,
    "NVIDIA GeForce GTX 1080": 180,
    "NVIDIA GeForce GTX 1080 Ti": 250,
    "NVIDIA GeForce RTX 2080 Ti": 250,
    "N/A": 0,
}