#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from csv_to_dot.csv_to_dot import CsvToDot;

class CsvToDot__init_resourcesTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_j2' ) as init_j2:
            c = CsvToDot ();
            
            init_j2.assert_called_once_with ();


if __name__ == '__main__':
    unittest.main ();
