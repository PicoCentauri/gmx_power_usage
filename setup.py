#!/usr/bin/env python3
# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
#
# Copyright (c) 2020 Philip Loche
#
# Released under the GNU Public Licence, v2 or any higher version
# SPDX-License-Identifier: GPL-2.0-or-later

from setuptools import setup, find_packages

VERSION = "0.1"  # NOTE: keep in sync with __version__ in gmx_power_usage.__init__.py


setup(name='gmx_power_usage',
      packages=find_packages(),
      version=VERSION,
      license='GPL 3',
      description='Calculates the power usage of an GROMACS simulation',
      author="Philip Loche",
      author_email="ploche@physik.fu-berlin.de",
      maintainer="Philip Loche",
      maintainer_email="ploche@physik.fu-berlin.de",
      python_requires='>=3.6',
)
