#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os;
import sys;
import jinja2;

from csv import reader;
from typing import Union;

from pprint import pprint;

#: Current module path
MODULE_PATH = os.path.dirname ( os.path.abspath ( __file__ ) );
#: Resource path
RESOURCE_PATH = os.path.join ( MODULE_PATH, 'resources' );


class CsvToDot:
    """Convert a 2 columns CSV file to a .dot, who can be converted with Graphviz to .jpg, .ps, ...
    
    Attributes:
        _csv_fh (handler): Protected. CSV file handler
        _node_indice (int): Protected. Indice to increment at each node
        _node_key_tpl (string): Protected. Template to create node key
        _nodes (dict): Protected. All nodes, key>label
        _edges (dict): Protected. Dict of list with all edges
        _dot_tpl (???): Protected. Jinja template for dot file
    """
    def __init__ ( self ):
        """Default constructor
        """
        """CSV file handler"""
        self._csv_fh = None;
        
        """Indice to increment at each node"""
        self._node_indice = 0;
        
        """Template to create node key"""
        self._node_key_tpl = 'A{:03d}';
        
        """All node, key>label"""
        self._nodes = {};
        
        """Dict of list with all edges"""
        self._edges = {};
        
        """Jinja template for dot file"""
        self._dot_tpl = None;
        
        self._init_resources ();
    
    
    def _init_resources ( self ):
        """Init resources used by system : init jinja2
        """
        ## Init jinja2
        self._init_j2 ();
    
    
    def _init_j2 ( self ):
        """Init jinja2
        """
        """Jinja2 environment"""
        env = jinja2.Environment (
            loader = jinja2.FileSystemLoader (
                RESOURCE_PATH
            )
        );
        
        self._dot_tpl = env.get_template (
            'graf.dot.j2'
        );
    
    
    def _dict_search_value ( self, d: dict, value: str ) -> Union[str,None]:
        """Search value on dict & returns key if exists
        
        Arguments:
            d (dict): Dictionnary to lookup
            value (string): Value to get key
        
        Returns:
            string|None: Key if found. None otherwise
        """
        try:
            return list ( d.keys () ) [ list ( d.values () ).index ( value ) ];
        except Exception as e:
            ## Value not found
            pass;
        return None;
    
    
    def _nodes_search_value ( self, value: str ) -> Union[str,None]:
        """Seach node key from value
        
        Arguments:
            value (string): Node value to get key
        
        Returns:
            string|None: Node key if found. None otherwise
        """
        return self._dict_search_value (
            self._nodes,
            value
        );
    
    
    def _create_node_key ( self ) -> str:
        """Create new node key
        
        Returns:
            string: Node key
        """
        ## Increment indice
        self._node_indice += 1;
        return self._node_key_tpl.format (
            self._node_indice
        );
    
    
    def __del__ ( self ):
        """Default destructor : close files handler
        """
        self._close_fh ()
    
    
    def _get_node_key ( self, node: str ) -> str:
        """Get/create a node key
        
        Arguments:
           node (string): Node label
        
        Returns:
           string: Key associated to label
        """
        """Key associated to label"""
        ret = self._nodes_search_value (
            value = node
        );
        
        if ( ret != None ):
            ## Key already exists
            return ret;
        
        ## Create new key & store node
        ret = self._create_node_key ();
        self._nodes [ ret ] = node;
        return ret;
    
    
    def _add_edge ( self, n1: str, n2: str ):
        """Store edge between n1 > n2
        
        Arguments:
            n1 (string): Node 1 : label
            n2 (string): Node 2 : label
        """
        """Node 1 : key"""
        key_n1 = self._get_node_key ( node = n1 );
        """Node 2 : key"""
        key_n2 = self._get_node_key ( node = n2 );
        
        if ( key_n1 not in self._edges ):
            self._edges [ key_n1 ] = [];
        
        self._edges [ key_n1 ].append ( key_n2 );
    
    
    def _get_fh_csv ( self, local_file: str ):
        """Open file handler : csv file (singleton)
        
        Arguments:
            local_file (string): Absolute local file path to csv file
        
        Returns:
            handler: Opened file
        """
        if ( self._csv_fh == None ):
            self._csv_fh = open ( local_file, 'r');
        return self._csv_fh;
    
    
    def _close_fh ( self ):
        """Close file handlers
        """
        try:
            ## Close : csv file
            close ( self._csv_fh );
            self._csv_fh = None;
        except Exception as e:
            pass;
    
    
    def _csv_reader ( self, local_file: str, delimiter: str ):
        """Create CSV reader
        
        Arguments:
            local_file (string): Absolute local file path to csv file
            delimiter (string): Csv delimiter
        
        Returns:
            csv.Reader: Csv reader 
        """
        return reader (
            self._get_fh_csv (
                local_file = local_file
            ),
            delimiter = delimiter
        );
    
    
    def _flat_edges_to_dot ( self ) -> list:
        """Convert all edges to a list for templating
        
        Returns:
            string[]: Edges for jinja2 templates
        """
        """Edges"""
        ret = [];
        
        for n1 in self._edges:
            for n2 in self._edges [ n1 ]:
                ret.append (
                    '{n1} -> {n2};'.format (
                        n1 = n1,
                        n2 = n2
                    )
                );
        
        return ret;
    
    
    def _flat_nodes_to_dot ( self ) -> list:
        """Convert all nodes to a list for templating
        
        Returns:
            string[]: Nodes for jinja2 templates
        """
        """Nodes"""
        ret = [];
        
        for label in self._nodes:
            ret.append (
                '{label} [label="{node}", color="blue", fontcolor="white"];'.format (
                    label = label,
                    node = self._nodes [ label ]
                )
            );
        
        return ret;
    
    
    def _print_dot ( self ):
        """Print dot file
        """
        print ( self._dot_tpl.render (
            edges = self._flat_edges_to_dot (),
            nodes = self._flat_nodes_to_dot (),
        ) );
            
    
    def run ( self, local_file: str, delimiter: str = ';' ):
        """Run process csv > dot
        
        Arguments:
            local_file (string): Absolute local file path to csv file
            delimiter (string): Csv delimiter. Default : ';'
        """
        
        ## Process .csv
        
        """CSV reader"""
        r_csv = self._csv_reader (
            local_file = local_file,
            delimiter = delimiter
        );
        
        for row in r_csv:
            self._add_edge (
                n1 = row [ 0 ],
                n2 = row [ 1 ]
            );
        
        ## Process : .dot
        
        self._print_dot ();
