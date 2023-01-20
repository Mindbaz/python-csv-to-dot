#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from csv_to_dot.csv_to_dot import CsvToDot;


class CsvToDot__flat_edges_to_dotTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            c = CsvToDot ();
            c._edges = {
                'random-node-1': [
                    'random-node-2',
                    'random-node-3'
                ],
                'random-node-2': [
                    'random-node-3'
                ]
            };
            
            ret = c._flat_edges_to_dot ();

            self.assertEqual ( ret, [
                'random-node-1 -> random-node-2;',
                'random-node-1 -> random-node-3;',
                'random-node-2 -> random-node-3;'
            ] );
            

            

if __name__ == '__main__':
    unittest.main ();
