#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from csv_to_dot.csv_to_dot import CsvToDot;


class CsvToDot__create_node_keyTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            c = CsvToDot ();
            c._node_indice = 123;
            c._node_key_tpl = 'random node key tpl with : {}';

            ret = c._create_node_key ();

            self.assertEqual ( ret, 'random node key tpl with : 124' );
            self.assertEqual ( c._node_indice, 124 );
            

            

if __name__ == '__main__':
    unittest.main ();
