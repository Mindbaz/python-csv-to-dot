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


class CsvToDot__csv_readerTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._get_fh_csv', return_value = 'random-fh' ) as get_fh:
                with patch ( 'csv_to_dot.csv_to_dot.reader', side_effect = RMock ) as reader_init:
                    c = CsvToDot ();

                    ret = c._csv_reader (
                        local_file = 'random-local-file',
                        delimiter = 'random-delimiter'
                    );
                    
                    self.assertTrue ( isinstance ( ret, RMock ) );

                    get_fh.assert_called_once_with (
                        local_file = 'random-local-file'
                    );
                    reader_init.assert_called_once_with (
                        'random-fh',
                        delimiter = 'random-delimiter'
                    );

            

if __name__ == '__main__':
    unittest.main ();
