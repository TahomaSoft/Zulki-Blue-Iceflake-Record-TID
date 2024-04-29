'''// SPDX-License-Identifier: GPL-3.0-or-later
Author: Erik Beck (bacon@tahomasoft.com)
Date last revised: 29 April 2024

A set of functions to create a time-based ID (TID) record identifier
as part of programs to use the atproto of the Bluesky Social app.

This is the more restrictive TID form of the record key

https://atproto.com/specs/record-key

'''

import time
import math

STRING_LEN = 13

def bsky_convert2_b32 (TID_raw64bit_int):
    '''
    Function to encode a number into atproto-bsky base32 format
    Progressive divison method

    '''

    BASE = 32

    # TESTVAL = 8675309

    remainder = BASE *2 # goofy start
    quotient = BASE *2 #  GOOFY start

    remainder_list = []
    quotient_list = []


    dividend = TID_raw64bit_int
    divisor = BASE


    while quotient > 0:
        '''
        use successive division by 32
        store the quotient and remainder in a list
        Append both lists at the front
        Remainder list is the one that really matters
        Kept the quotient to check my work
        '''

        quotient = math.trunc(dividend/divisor)
        quotient_list.insert(0,quotient)

        remainder = dividend % divisor
        remainder_list.insert(0,remainder)
        
        dividend = quotient 

    b32_entry = remainder_list
    byte_string = ""

    for i in b32_entry:
        j = bskybase32_lookup (i)
        print (i,j)
        byte_string += j

    print (byte_string)
    fixed_string = check_padding (byte_string)
    print (fixed_string)
    return fixed_string

def check_padding (byte_string2check):
    '''if byte string is less than 13 (STRING_LEN) characters, need
    to front pad with integer zero, or, in this encoding, '2'.

    '''
    
    print (len(byte_string2check))
    if (len(byte_string2check))==STRING_LEN:
        # all good, return as is
        return byte_string2check

    elif (len(byte_string2check)) > STRING_LEN:
        # This is an error, stop program
        raise ValueError('byte string for TID over ', STRING_LEN)
        raise Exception('Stop program')

    elif (len(byte_string2check)) < STRING_LEN:
        # front pad with 2 
        pads  = STRING_LEN - len(byte_string2check)
        revised_string = byte_string2check
        
        while pads > 0:
            revised_string = '2' + revised_string
            pads = pads -1
        return revised_string
    
    else:
        raise Exception('Weird. Stop program')


def bskybase32_lookup (integer2map):
    '''
    Function to map the base32 power and remainder to the right character set
    for atproto
    '''
    b32_lookup = {
		  0:  '2',
		  1:  '3',
		  2:  '4',
		  3:  '5',
		  4:  '6',
		  5:  '7',
		  6:  'a',
		  7:  'b',
		  8:  'c',
		  9:  'd',
		  10: 'e',
		  11: 'f',
		  12: 'g',
		  13: 'h',
		  14: 'i',
		  15: 'j',
		  16: 'k',
		  17: 'l',
		  18: 'm',
		  19: 'n',
		  20: 'o',
		  21: 'p',
		  22: 'q',
		  23: 'r',
		  24: 's',
		  25: 't',
		  26: 'u',
		  27: 'v',
		  28: 'w',
		  29: 'x',
		  30: 'y',
		  31: 'z'
		  }

    mapped_int = b32_lookup.get(integer2map)

    return (mapped_int)



class bsky_tid_obj:
    '''
    Blue Sky - ATProto TID Generator
    spec: https://atproto.com/specs/record-key#record-key-type-tid

    Generate unique record id for bluesky posts, following
    more restrictive TID (time stamp identifier) format
    
    '''

    # Setup constants

    MAX_TID = (2**63)
    MAXY_MASK_64b = (2**63) 
    FINAL_STRING_LENGTH = 13
    FIRST_BIT = 0b0
    EPOCH_MAX = (2**53)  # Max value for epoch as microseconds since UNIX epoch
    RANDO_MAX = (2**10) -1   # Max value for random part appended to Epoch/time 53 bits
    RANDO_MASK_10b = (2**9)  # 512

    # Setup class-wide variables
    obj_seq = 0
    
    def __init__(self):
        '''
        '''
        
        
    
    def print_max(self):
        epoch_fracSeconds = time.time()
        epoch_uSeconds = math.trunc (time.time() * (10**6))

        # Counter to prevent generating multiple identical ids in the same microsecond
        
        self.obj_seq = self.obj_seq +1
        if self.obj_seq == 10:
            self.obj_seq =0
            
        bit_test = self.MAXY_MASK_64b | epoch_uSeconds

        sbit_test = bit_test ^ self.MAXY_MASK_64b


        # Generate some more info for unique id
        
        u_time_one = epoch_fracSeconds
        u_time_two = time.time()
        delta_tics = u_time_two - u_time_one
        tinytics=math.frexp(u_time_two - u_time_one)

        p = [tinytics[0],tinytics[1]]

        tinytics_man = math.frexp(tinytics[0])

        q = [tinytics_man[0],tinytics_man[1]]

        # 
        print (tinytics, tinytics_man)
        print ()
        print (p,q)

        dist = math.trunc(math.dist(p,q))
        print (dist)
        print (dist.bit_length())
        print (delta_tics)

        # Build a rando number less than 1024
        num_1 = self.obj_seq * 95
        num_2 = dist
        num_3 = num_1 + num_2
        print (num_3)
        rando_bits =  self.RANDO_MASK_10b | num_3
        print("Rando Bits:" , bin(rando_bits))
        print ("Rando Bits length: ", rando_bits.bit_length())
        print (self.RANDO_MAX)
        print (self.RANDO_MAX.bit_length())
        print (bin(self.RANDO_MAX))
        woffy = 0b1000000000
        print ("woofy: ", woffy)
        print ("woofy bit length: ", woffy.bit_length())
        append_rando = self.MAXY_MASK_64b | rando_bits
        print ("append rando: ", bin(append_rando))
        add_timo = append_rando | bit_test
        print ("timeo :" , bin(add_timo))
        print ("timeo bit length: ", add_timo.bit_length())

        flip_off_leadingbit = add_timo  ^ self.MAXY_MASK_64b
        print ("final: ", bin (flip_off_leadingbit), flip_off_leadingbit)
        print (flip_off_leadingbit.bit_length())
        print (epoch_uSeconds)

        return
    


