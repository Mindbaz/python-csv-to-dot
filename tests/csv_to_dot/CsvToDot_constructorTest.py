#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from csv_to_dot.csv_to_dot import CsvToDot;

class CsvToDot_constructorTest ( unittest.TestCase ):
    def test_constructor ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            c = CsvToDot ();
            
            init_resources.assert_called_once_with ();
        
        
        
if __name__ == '__main__':
    unittest.main ();
