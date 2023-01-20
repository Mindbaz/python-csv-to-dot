#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from csv_to_dot.csv_to_dot import CsvToDot;


def r_mock ( node ):
    return node.replace (
        'node',
        'key'
    );

class CsvToDot__add_edgeTest ( unittest.TestCase ):
    def test_n1_not_already_set ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._get_node_key', side_effect = r_mock ) as get_node_key:
                c = CsvToDot ();
                c._edges = {
                    'random-key-2': [],
                    'random-key-3': []
                };
                
                c._add_edge (
                    n1 = 'random-node-1',
                    n2 = 'random-node-2'
                );
                
                self.assertEqual ( c._edges, {
                    'random-key-1': [
                        'random-key-2'
                    ],
                    'random-key-2': [],
                    'random-key-3': []
                } );

                self.assertEqual ( get_node_key.call_count, 2 );
                get_node_key.assert_any_call ( node = 'random-node-1' );
                get_node_key.assert_any_call ( node = 'random-node-2' );

                
    def test_n1_already_set ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._get_node_key', side_effect = r_mock ) as get_node_key:
                c = CsvToDot ();
                c._edges = {
                    'random-key-1': [
                        'another-key-1',
                        'another-key-2',
                        'another-key-3'
                    ],
                    'random-key-2': []
                };
                
                c._add_edge (
                    n1 = 'random-node-1',
                    n2 = 'random-node-2'
                );
                
                self.assertEqual ( c._edges, {
                    'random-key-1': [
                        'another-key-1',
                        'another-key-2',
                        'another-key-3',
                        'random-key-2'
                    ],
                    'random-key-2': []
                } );

                self.assertEqual ( get_node_key.call_count, 2 );
                get_node_key.assert_any_call ( node = 'random-node-1' );
                get_node_key.assert_any_call ( node = 'random-node-2' );


            

if __name__ == '__main__':
    unittest.main ();
