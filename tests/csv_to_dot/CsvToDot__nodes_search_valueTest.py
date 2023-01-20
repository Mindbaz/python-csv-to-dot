#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from csv_to_dot.csv_to_dot import CsvToDot;


class CsvToDot__nodes_search_valueTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._dict_search_value', return_value = 'random-returns' ) as dict_search_value:
                c = CsvToDot ();
                c._nodes = 'random-nodes';
                
                ret = c._nodes_search_value (
                    value = 'random-value'
                );
                
                self.assertEqual ( ret, 'random-returns' );
                dict_search_value.assert_called_once_with (
                    d = 'random-nodes',
                    value = 'random-value'
                );


            

if __name__ == '__main__':
    unittest.main ();
