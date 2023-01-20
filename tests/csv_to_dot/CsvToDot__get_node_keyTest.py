#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from csv_to_dot.csv_to_dot import CsvToDot;


class CsvToDot__get_node_keyTest ( unittest.TestCase ):
    def test_key_found ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._nodes_search_value', return_value = 'random-key' ) as search_key:
                with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._create_node_key' ) as create_key:
                    c = CsvToDot ();
                    
                    ret = c._get_node_key (
                        node = 'random-node'
                    );

                    self.assertEqual ( ret, 'random-key' );
                    search_key.assert_called_once_with (
                        value = 'random-node'
                    );
                    create_key.assert_not_called ();

                    
    def test_key_unexists ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._nodes_search_value', return_value = None ) as search_key:
                with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._create_node_key', return_value = 'another-key' ) as create_key:
                    c = CsvToDot ();
                    c._nodes = {
                        'random-key': 'random-node'
                    };
                    
                    ret = c._get_node_key (
                        node = 'another-node'
                    );
                    
                    self.assertEqual ( ret, 'another-key' );
                    self.assertEqual ( c._nodes, {
                        'random-key': 'random-node',
                        'another-key': 'another-node'
                    } );
                    search_key.assert_called_once_with (
                        value = 'another-node'
                    );
                    create_key.assert_called_once_with ();
            

            

if __name__ == '__main__':
    unittest.main ();
