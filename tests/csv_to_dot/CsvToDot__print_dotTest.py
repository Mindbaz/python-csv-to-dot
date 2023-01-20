#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from csv_to_dot.csv_to_dot import CsvToDot;


class RMock ( object ):
    def __init__ ( self, *args, **kargs ):
        print ( 'RMock : __init__' );
        pass;
    
    def render ( self, *args, **kargs ):
        print ( 'RMock : render' );
        pass;


class CsvToDot__print_dotTest ( unittest.TestCase ):
    def test_to_stdout ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._flat_edges_to_dot', return_value = 'random-flatten-edges' ) as flat_edges:
                with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._flat_nodes_to_dot', return_value = 'random-flatten-nodes' ) as flat_nodes:
                    with patch ( 'tests.csv_to_dot.CsvToDot__print_dotTest.RMock.render', return_value = 'random-render' ) as render:
                        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._print_dot_stdout' ) as print_to_stdout:
                            with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._print_dot_file' ) as print_to_file:
                                c = CsvToDot ();
                                c._nodes_opts = 'random-nodes-opts';
                                c._dot_tpl = RMock ();

                                ret = c._print_dot ();
                                
                                self.assertTrue ( ret );
                                flat_edges.assert_called_once_with ();
                                flat_nodes.assert_called_once_with ();
                                render.assert_called_once_with (
                                    edges = 'random-flatten-edges',
                                    nodes = 'random-flatten-nodes',
                                    nodes_opts = 'random-nodes-opts'
                                );
                                print_to_stdout.assert_called_once_with (
                                    content = "random-render\n"
                                );
                                print_to_file.assert_not_called ();

                                
    def test_to_file ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._flat_edges_to_dot', return_value = 'random-flatten-edges' ) as flat_edges:
                with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._flat_nodes_to_dot', return_value = 'random-flatten-nodes' ) as flat_nodes:
                    with patch ( 'tests.csv_to_dot.CsvToDot__print_dotTest.RMock.render', return_value = 'random-render' ) as render:
                        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._print_dot_stdout' ) as print_to_stdout:
                            with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._print_dot_file' ) as print_to_file:
                                c = CsvToDot ();
                                c._nodes_opts = 'random-nodes-opts';
                                c._dot_tpl = RMock ();

                                ret = c._print_dot (
                                    local_file = 'random-local-file'
                                );
                                
                                self.assertFalse ( ret );
                                flat_edges.assert_called_once_with ();
                                flat_nodes.assert_called_once_with ();
                                render.assert_called_once_with (
                                    edges = 'random-flatten-edges',
                                    nodes = 'random-flatten-nodes',
                                    nodes_opts = 'random-nodes-opts'
                                );
                                print_to_stdout.assert_not_called ();
                                print_to_file.assert_called_once_with (
                                    local_file = 'random-local-file',
                                    content = "random-render\n"
                                );

if __name__ == '__main__':
    unittest.main ();
