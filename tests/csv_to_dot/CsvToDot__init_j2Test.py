#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from csv_to_dot.csv_to_dot import CsvToDot, RESOURCE_PATH;


class RMock ( object ):
    def __init__ ( self, *args, **kargs ):
        print ( 'RMock : __init__' );
        pass;
    
    def get_template ( self, *args, **kargs ):
        print ( 'RMock : get_template' );
        pass;
    

class CsvToDot__init_j2Test ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'csv_to_dot.csv_to_dot.CsvToDot._init_resources' ) as init_resources:
            with patch ( 'csv_to_dot.csv_to_dot.jinja2.FileSystemLoader', side_effect = RMock ) as j2_fs_load:
                with patch ( 'csv_to_dot.csv_to_dot.jinja2.Environment', side_effect = RMock ) as j2_env:
                    with patch ( 'tests.csv_to_dot.CsvToDot__init_j2Test.RMock.get_template', return_value = 'random-tpl' ) as get_tpl:
                        c = CsvToDot ();
                        
                        c._init_j2 ();

                        self.assertEqual ( c._dot_tpl, 'random-tpl' );
                        j2_fs_load.assert_called_once_with (
                            RESOURCE_PATH
                        );

                        for call in j2_env.call_args_list:
                            args, kwargs = call;
                            self.assertTrue ( isinstance ( kwargs [ 'loader' ], RMock ) );
                        
                        get_tpl.assert_called_once_with (
                            'graf.dot.j2'
                        );


if __name__ == '__main__':
    unittest.main ();
