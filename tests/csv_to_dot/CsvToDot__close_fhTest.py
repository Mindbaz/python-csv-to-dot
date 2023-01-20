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
    
    def close ( self, *args, **kargs ):
        print ( 'RMock : close' );
        pass;


class CsvToDot__close_fhTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            with patch ( 'tests.csv_to_dot.CsvToDot__close_fhTest.RMock.close' ) as close:
                c = CsvToDot ();
                c._csv_fh = RMock ();
                
                c._close_fh ();
                
                self.assertEqual ( c._csv_fh, None );
                close.assert_called_once_with ();

                
    def test_close_raise_exception ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            with patch ( 'tests.csv_to_dot.CsvToDot__close_fhTest.RMock.close', side_effect = Exception ( 'Random exception' ) ) as close:
                c = CsvToDot ();
                c._csv_fh = RMock ();
                
                c._close_fh ();
                
                self.assertTrue ( isinstance ( c._csv_fh, RMock ) );
                close.assert_called_once_with ();


            

if __name__ == '__main__':
    unittest.main ();
