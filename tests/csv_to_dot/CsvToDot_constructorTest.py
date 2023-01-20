#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from csv_to_dot.csv_to_dot import CsvToDot, RESOURCE_PATH;

class CsvToDot_constructorTest ( unittest.TestCase ):
    def test_constructor ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            c = CsvToDot ();

            self.assertEqual ( c._csv_fh, None );
            self.assertEqual ( c._node_indice, 0 );
            self.assertTrue ( type ( c._node_key_tpl ) is str );
            self.assertEqual ( c._nodes, {} );
            self.assertEqual ( c._edges, {} );
            self.assertEqual ( c._dot_tpl, None );
            self.assertTrue ( type ( c._nodes_opts ) is dict );
            
            self.assertTrue ( c._nodes_opts [ 'shape' ], 'box' );
            self.assertTrue ( c._nodes_opts [ 'style' ], 'filled' );
            self.assertTrue ( c._nodes_opts [ 'bg_color' ], 'blue' );
            self.assertTrue ( c._nodes_opts [ 'font_color' ], 'white' );
            
            init_resources.assert_called_once_with ();

            
    def test_set_params ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            c = CsvToDot (
                nodes_shape = 'random-shape',
                nodes_style = 'random-style',
                nodes_bg_color = 'random-bg-color',
                nodes_font_color = 'random-font-color'
            );
            
            self.assertTrue ( c._nodes_opts [ 'shape' ], 'random-shape' );
            self.assertTrue ( c._nodes_opts [ 'style' ], 'random-style' );
            self.assertTrue ( c._nodes_opts [ 'bg_color' ], 'random-bg-color' );
            self.assertTrue ( c._nodes_opts [ 'font_color' ], 'random-font-color' );

            
    def test_node_key_tpl ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            c = CsvToDot ();

            ret = c._node_key_tpl.format ( 1 );
            self.assertTrue ( '001' in ret );
            
            ret = c._node_key_tpl.format ( 12 );
            self.assertTrue ( '012' in ret );
            
            ret = c._node_key_tpl.format ( 123 );
            self.assertTrue ( '123' in ret );
    
    
    def test_resource_path ( self ):
        self.assertTrue ( type ( RESOURCE_PATH is str ) );
        self.assertTrue ( len ( RESOURCE_PATH ) > 0 );

        
if __name__ == '__main__':
    unittest.main ();
