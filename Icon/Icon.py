"""
# File: Icon.py
# Author: schilka
# Date: 2025-01-16

# Description:
# This is an auto RTL wrapper generator Tool.
# FrontEnd Design and development with scalable feature extensions

#Authorized Usage: 
# This file is licensed to {{ licensee_name }} for use solely in accordance with the 
# terms and conditions of the license agreement. Unauthorized copying or distribution 
# of this file, via any medium, is prohibited.
    
# Usage:
#  TBD
"""
class GenRtlWrap:
    
    def gen_wrap(self, dict_list):
        rtl_file = '"example_wrap.sv"'
        print(f'Generating RTL {rtl_file}')


class IconMain:
    
    def __init__(self):
        self.dict_t    = {
            'ip_name'  : '',
            'owner'    : '',
            'module'   : [],
            'mod_inst' : []
        }
        
    def parse_file(self, file):
        print (f'Parsing file {xls_file}')
        
        dict_list = []
        self.gen_jdb(dict_list)

    def gen_jdb(self, dict_list):
        jdb_file = '"example.json"'
        print (f'Generating JSON DB file: {jdb_file}')
        return jdb_file

    def parse_jdb(self, file):
        print('Parsing JDB file')
        print('Updating dic_t')
        return self.dict_t
        
        
xls_file = 'example.xlsx'
icon = IconMain()
jdb = icon.parse_file(xls_file)
rtldb = icon.parse_jdb(jdb)
grw   = GenRtlWrap()
grw.gen_wrap(rtldb)
