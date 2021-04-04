#!/usr/bin/env python3
# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
#
# Copyright (c) 2021 Philip Loche
#
# Released under the GNU Public Licence, v2 or any higher version
# SPDX-License-Identifier: GPL-2.0-or-later


# CPU TDP per Core in Watts
CPU = {
    "Intel(R) Xeon(R) CPU E5-2680 v2 @ 2.80GHz": 115 / 10,
    "Intel(R) Core(TM) i7-8700K CPU @ 3.70GHz": 95 / 6,
    "AMD Ryzen Threadripper 1950X 16-Core Processor": 180 / 16,
    "AMD Ryzen Threadripper 3970X 32-Core Processor": 280 / 32,
}

# GPU TDP in Watts
GPU = {
    "NVIDIA Tesla K20Xm": 235,
    "NVIDIA GeForce GTX 1080": 180,
    "NVIDIA GeForce RTX 2080 Ti": 250,
}