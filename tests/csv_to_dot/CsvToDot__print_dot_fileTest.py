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
        print ( 'OpenMock : __init__' );
        pass;
    
    def __open__ ( self, *args, **kargs ):
        print ( 'OpenMock : __open__' );
        pass;
    
    def __enter__ ( self, *args, **kargs ):
        print ( 'OpenMock : __enter__' );
        pass;
    
    def __exit__ ( self, *args, **kargs ):
        print ( 'OpenMock : __exit__' );
        pass;
    
    def write ( self, *args, **kargs ):
        print ( 'OpenMock : write' );
        pass;


class CsvToDot__print_dot_fileTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            with patch ( 'csv_to_dot.csv_to_dot.open', side_effect = RMock ) as open_call:
                with patch ( 'tests.csv_to_dot.CsvToDot__print_dot_fileTest.RMock.__enter__', return_value = RMock ) as enter:
                    with patch ( 'tests.csv_to_dot.CsvToDot__print_dot_fileTest.RMock.write' ) as write:
                        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._print_graphvz_instructions' ) as print_instrucs:
                            c = CsvToDot ();
                            
                            c._print_dot_file (
                                local_file = 'random-local-file',
                                content = 'random-content'
                            );
                            
                            open_call.assert_called_once_with (
                                'random-local-file',
                                'w'
                            );
                            write.assert_called_once_with (
                                'random-content'
                            );
                            print_instrucs.assert_called_once_with (
                                local_file = 'random-local-file'
                            );
            

if __name__ == '__main__':
    unittest.main ();
