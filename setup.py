#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2023 Mindbaz
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import os;
from setuptools import setup;

with open ( os.path.join ( os.path.dirname ( os.path.abspath ( __file__ ) ), 'README.md' ) , 'r', encoding='utf-8' ) as fh:
    long_description = fh.read ();

from csv_to_dot import __version__;

setup (
    name = 'csv-to-dot',
    version = __version__,
    description = 'Convert a 2 columns CSV file to a .dot, who can be converted with Graphviz to .jpg, .ps, ...',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Mindbaz/python-csv-to-dot',
    author = 'Valentin Henon',
    author_email = 'vhenon@mindbaz.com',
    python_requires = '>=3.7',
    keywords = 'graphviz',
    license = 'GPLv3',
    packages = [
        'csv_to_dot',
        'csv_to_dot.resources',
        'entry_points_csv_to_dot'
    ],
    package_data = {
        '': [
            '*.j2'
        ]
    },
    install_requires = [
        'Jinja2'
    ],
    tests_require = [
        'nose',
        'coverage'
    ],
    test_suite = 'tests',
    entry_points = {
        'console_scripts': [
            'csv_to_dot = entry_points_csv_to_dot.csv_to_dot:run'
        ]
    },
    zip_safe = False,
    classifiers = [
        "Programming Language :: Python :: 3.9"
    ],
);
