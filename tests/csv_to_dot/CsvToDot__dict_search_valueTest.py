#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from csv_to_dot.csv_to_dot import CsvToDot;


class CsvToDot__dict_search_valueTest ( unittest.TestCase ):
    def test_value_found ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            c = CsvToDot ();
            
            ds = {
                'random-key-1': 'random-value-1',
                'random-key-2': 'random-value-2',
                'random-key-3': 'random-value-3'
            };

            ret = c._dict_search_value (
                d = ds,
                value = 'random-value-1'
            );

            self.assertEqual ( ret, 'random-key-1' );

            
    def test_value_not_found ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            c = CsvToDot ();
            
            ds = {
                'random-key-1': 'random-value-1',
                'random-key-2': 'random-value-2',
                'random-key-3': 'random-value-3'
            };

            ret = c._dict_search_value (
                d = ds,
                value = 'random-value-123'
            );

            self.assertEqual ( ret, None );

            

if __name__ == '__main__':
    unittest.main ();
