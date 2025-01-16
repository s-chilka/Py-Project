"""
# File: CacheSubSystem.py
# Author: schilka
# Date: 2025-01-16

# Description:
# This is a Software model for a Generic Cache Controller Design

#Authorized Usage: 
# This file is licensed to {{ licensee_name }} for use solely in accordance with the 
# terms and conditions of the license agreement. Unauthorized copying or distribution 
# of this file, via any medium, is prohibited.
    
# Usage:
# Instructions on how to use the script, if applicable.
"""
import time
import random

class Transactor:
    
    def get_pkt(self):
        r_rw   = random.choice(['r','w'])
        r_addr = random.randint(1, 32)
        hex_values = ["#FF0000", "#0000FF"]
        r_data = random.choice(hex_values)
        
        instruction = {'rw':r_rw,'addr':r_addr,'data':r_data}
        return instruction

class Monitor:
    def __init__(self):
        self.data = []
        
    def display(self):
        print('Monitor Table:')
        print('txn\t opcode\t addr\t cache\t data\t\t t_delay')
        for item in self.data:
            txn  = item['txn']
            op   = item['opcode']
            addr = item['addr']
            hit  = item['cache']
            data = item['data']
            dly  = item['t_delay']
            
            print(f'{txn} \t {op} \t {addr} \t {hit} \t {data} \t {dly}')
        
    def update_tracker(self,data):
        self.data.append(data)
        
class Cache:
    def __init__(self, memaddr_width=32, cacheaddr_width=8):
        self.memaddr_width    = memaddr_width
        self.cacheaddr_width  = cacheaddr_width
        self.cache_size       = (2**self.cacheaddr_width)
        self.data             = [None]*self.cache_size
        for i in range(self.cache_size):
            self.data[i] = {'rw':None,'addr':None,'data':None}

    def cache_addr(self, phy_addr):
        return (phy_addr % (2**self.cacheaddr_width)) #direct mapped

    def hit_miss(self, key, value):
        """ 
        Verify if there is a Cache Address hit or miss
        """
        for d in self.data:
            if d.get(key) == value:
                return True
        return False
        
    def write(self, data):
        """ 
        Write operation to Cache Memory
        """
        self.hit_miss('addr',data['addr'])
        self.data.append(data)

    def read(self, data):
        """ 
        Read operation from Cache Memory
        """        
        if self.hit_miss('addr',data['addr']):
            return self.data[data['addr']]
        
class Memory:
    def __init__(self):
        self.data = []

    def write(self, data):
        print('Started writing to Memory.')
        self.data.append(data)

    def read(self, index):
        print('Started reading from Memory.')
        return self.data[index]    
        
class System:       
    def __init__ (self):
        self.mem   = Memory()
        self.cache = Cache()
        self.txtor = Transactor()
        self.mon   = Monitor()

    def write_back(self, data):
        self.cache.write(data)
        # Maybe kick-off writing to backing store asynchronously, but don't wait for it.
    
    def description(self):
        print (f"System instance")
        
    def sys_timer(self, start_time, end_time):
        t_delay = end_time-start_time
        formated_delay = "{:.2f}".format(t_delay)
        return formated_delay

    def start(self):
        
        n = 10
        for i in range(n):
            
            start_time = time.time()
                
            instruction = self.txtor.get_pkt()

            #determine hit or miss
            cache_rsp = self.cache.hit_miss('addr',instruction['addr'])
            if cache_rsp: hit_char = 'hit' 
            else: hit_char = 'miss'
                
            #determine read or write
            if instruction['rw'] == 'w':
                self.write_back(instruction)
            else:
                self.cache.read(instruction)
            
            end_time = time.time()
            
            #determine total delay of this transaction
            t_delay = self.sys_timer(start_time, end_time)
            
            self.mon.update_tracker({'txn':i,'opcode':instruction['rw'],
                                     'addr':instruction['addr'],'cache':hit_char,
                                     'data':instruction['data'],'t_delay':t_delay})
            
        print("Program Execution Time",self.sys_timer(start_time, end_time))
        
    def display_txn_table(self):
        self.mon.display()

sys = System()
sys.start()
sys.display_txn_table()
