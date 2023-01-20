#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from csv_to_dot.csv_to_dot import CsvToDot;


class CsvToDot__get_fh_csvTest ( unittest.TestCase ):
    def test_csv_fh_none ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            with patch ( 'csv_to_dot.csv_to_dot.open', return_value = 'random-fh' ) as open_call:
                c = CsvToDot ();
                c._csv_fh = None;
                
                ret = c._get_fh_csv (
                    local_file = 'random-local-file'
                );

                self.assertEqual ( ret, 'random-fh' );
                self.assertEqual ( c._csv_fh, 'random-fh' );
                open_call.assert_called_once_with (
                    'random-local-file',
                    'r'
                );

                
    def test_csv_fh_set ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            with patch ( 'csv_to_dot.csv_to_dot.open', return_value = 'random-fh' ) as open_call:
                c = CsvToDot ();
                c._csv_fh = 'another-fh';
                
                ret = c._get_fh_csv (
                    local_file = 'random-local-file'
                );

                self.assertEqual ( ret, 'another-fh' );
                self.assertEqual ( c._csv_fh, 'another-fh' );
                open_call.assert_not_called ();

            

if __name__ == '__main__':
    unittest.main ();
