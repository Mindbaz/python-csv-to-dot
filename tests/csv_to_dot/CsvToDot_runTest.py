#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from csv_to_dot.csv_to_dot import CsvToDot;

DS = [
    [ 'random-node-1-1', 'random-node-1-2' ],
    [ 'random-node-2-1', 'random-node-2-2' ],
    [ 'random-node-3-1', 'random-node-3-2' ],
    [ 'random-node-4-1', 'random-node-4-2' ]
];

class CsvToDot_runTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._csv_reader', return_value = DS ) as csv_reader:
                with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._add_edge' ) as add_edge:
                    with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._close_fh' ) as close_fh:
                        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._print_dot' ) as print_dot:
                            c = CsvToDot ();

                            ret = c.run (
                                local_in_file = 'random-local-in-file'
                            );

                            csv_reader.assert_called_once_with (
                                local_file = 'random-local-in-file',
                                delimiter = ';'
                            );
                            self.assertEqual ( add_edge.call_count, 4 );
                            add_edge.assert_any_call ( n1 = 'random-node-1-1', n2 = 'random-node-1-2' );
                            add_edge.assert_any_call ( n1 = 'random-node-2-1', n2 = 'random-node-2-2' );
                            add_edge.assert_any_call ( n1 = 'random-node-3-1', n2 = 'random-node-3-2' );
                            add_edge.assert_any_call ( n1 = 'random-node-4-1', n2 = 'random-node-4-2' );
                            close_fh.assert_called_once_with ();
                            print_dot.assert_called_once_with (
                                local_file = None
                            );

                            
    def test_param_delimiter ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._csv_reader', return_value = DS ) as csv_reader:
                with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._add_edge' ) as add_edge:
                    with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._close_fh' ) as close_fh:
                        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._print_dot' ) as print_dot:
                            c = CsvToDot ();

                            ret = c.run (
                                local_in_file = 'random-local-in-file',
                                delimiter = 'rando-delimiter'
                            );

                            csv_reader.assert_called_once_with (
                                local_file = 'random-local-in-file',
                                delimiter = 'rando-delimiter'
                            );
                            self.assertEqual ( add_edge.call_count, 4 );
                            add_edge.assert_any_call ( n1 = 'random-node-1-1', n2 = 'random-node-1-2' );
                            add_edge.assert_any_call ( n1 = 'random-node-2-1', n2 = 'random-node-2-2' );
                            add_edge.assert_any_call ( n1 = 'random-node-3-1', n2 = 'random-node-3-2' );
                            add_edge.assert_any_call ( n1 = 'random-node-4-1', n2 = 'random-node-4-2' );
                            close_fh.assert_called_once_with ();
                            print_dot.assert_called_once_with (
                                local_file = None
                            );

                            
    def test_param_local_out_file ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._csv_reader', return_value = DS ) as csv_reader:
                with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._add_edge' ) as add_edge:
                    with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._close_fh' ) as close_fh:
                        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._print_dot' ) as print_dot:
                            c = CsvToDot ();

                            ret = c.run (
                                local_in_file = 'random-local-in-file',
                                local_out_file = 'random-local-out-file'
                            );

                            csv_reader.assert_called_once_with (
                                local_file = 'random-local-in-file',
                                delimiter = ';'
                            );
                            self.assertEqual ( add_edge.call_count, 4 );
                            add_edge.assert_any_call ( n1 = 'random-node-1-1', n2 = 'random-node-1-2' );
                            add_edge.assert_any_call ( n1 = 'random-node-2-1', n2 = 'random-node-2-2' );
                            add_edge.assert_any_call ( n1 = 'random-node-3-1', n2 = 'random-node-3-2' );
                            add_edge.assert_any_call ( n1 = 'random-node-4-1', n2 = 'random-node-4-2' );
                            close_fh.assert_called_once_with ();
                            print_dot.assert_called_once_with (
                                local_file = 'random-local-out-file'
                            );

                            

if __name__ == '__main__':
    unittest.main ();
