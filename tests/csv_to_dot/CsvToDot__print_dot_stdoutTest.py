#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from csv_to_dot.csv_to_dot import CsvToDot;


class CsvToDot__print_dot_stdoutTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            with patch ( 'csv_to_dot.csv_to_dot.sys.stdout.write' ) as write:
                c = CsvToDot ();
                
                c._print_dot_stdout (
                    content = 'random-content'
                );

                write.assert_called_once_with ( 
                    'random-content'
                );
                    
            

if __name__ == '__main__':
    unittest.main ();
