#!/bin/python

import time
import math



MAX_TS = 0b11111111111111111111111111111111111111111111111111111
MAX_CI = 0b1111111111

# 64 bit string, first bit=0, all others=1
MAX_TID      = 0b0111111111111111111111111111111111111111111111111111111111111111
OVER_MAX_TID = 0b1111111111111111111111111111111111111111111111111111111111111111

first_bit = 0b0

Maxy_tid = (2**63)
mask_val = (2**63)+1

print (MAX_TS)
print ("MAX_TID: ", MAX_TID)
print ("Maxy tid: " , Maxy_tid)
print (OVER_MAX_TID)
print ("Max TID BitLength: ", MAX_TID.bit_length())

print ("Max TID Bit Count: ", MAX_TID.bit_count())



print ("Over Max TID BitLength: ", OVER_MAX_TID.bit_length())
print ("Over Max TID Bit Count: ", OVER_MAX_TID.bit_count())

print ("Max TS BitLenth: ", MAX_TS.bit_length())

print ("Max CI bit length:", MAX_CI.bit_length())
u_time_one = time.time()

u_time_micros = math.trunc (u_time_one * (10**6))
