#!/bin/python

import math

def bsky_b32_lookup (integer2map):

    bskybase32_lookup = {
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

    mapped_int = bskybase32_lookup.get(integer2map)

    return (mapped_int)


'''
Test program so far to encode a number into atproto-bsky base32
format
'''
BASE = 32
TESTVAL = 8675309

remainder = BASE *2 # goofy start
quotient = BASE *2 #  GOOFY start

remainder_list = []
quotient_list = []


dividend = TESTVAL
divisor = BASE


while quotient > 0:

    quotient = math.trunc(dividend/divisor)
    quotient_list.insert(0,quotient)

    remainder = dividend % divisor
    remainder_list.insert(0,remainder)

    print ("quotient, remainder, dividend, divisor: "
           ,quotient, remainder, dividend, divisor)

    dividend = quotient 


print ("Quotient List: ", quotient_list)
print ("Remainder List: ", remainder_list)


b32_entry = remainder_list

print (b32_entry)

byte_string = ""

for i in b32_entry:
    j = bsky_b32_lookup (i)
    print (i,j)
    byte_string += j

print (byte_string)
