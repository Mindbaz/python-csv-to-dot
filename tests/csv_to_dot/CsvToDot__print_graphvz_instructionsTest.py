#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from csv_to_dot.csv_to_dot import CsvToDot;


class CsvToDot__print_graphvz_instructionsTest ( unittest.TestCase ):
    def test_local_file_no_ext ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            with patch ( 'csv_to_dot.csv_to_dot.sys.stdout.write' ) as write:
                c = CsvToDot ();
                
                c._print_graphvz_instructions (
                    local_file = 'random-local-file'
                );

                write.assert_called_once_with (
                    "Dot file created at : random-local-file\nRun command :\n  dot -T<EXT> random-local-file -o random-local-file.<EXT> # Replace <EXT> with required format\nNB : Require debian package : `graphviz`\n"
                );

                
    def test_local_file_with_ext ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            with patch ( 'csv_to_dot.csv_to_dot.sys.stdout.write' ) as write:
                c = CsvToDot ();
                
                c._print_graphvz_instructions (
                    local_file = 'random.local.file'
                );
                
                write.assert_called_once_with (
                    "Dot file created at : random.local.file\nRun command :\n  dot -T<EXT> random.local.file -o random.local.<EXT> # Replace <EXT> with required format\nNB : Require debian package : `graphviz`\n"
                );  
            

if __name__ == '__main__':
    unittest.main ();
