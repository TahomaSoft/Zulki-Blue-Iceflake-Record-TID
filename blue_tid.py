'''
Compute a record id for bluesky social that is TID compliant
(time-based record id,
https://github.com/bluesky-social/atproto/discussions/1910
https://github.com/bluesky-social/atproto/discussions/2387
https://play.golang.com/p/imLamcQJ4Id)
https://atproto.com/specs/record-key#record-key-type-tid
'''

import time
import math
import numpy as np


# epoch time part

u_time_one = time.time()

u_time_micros = math.trunc (u_time_one * (10**6))

bits_len = u_time_micros.bit_length()

bit_diff = 64 - bits_len

print (bits_len,u_time_micros)



t_part = np.uint64(u_time_micros)
print (bin(u_time_micros))
print (bin(t_part))

# t_part_shifted = t_part << bit_diff

# print (bin(t_part_shifted))

mask_zero = np.uint64(0)

print (mask_zero | t_part)

# 10 bit part is max val of 1024

# generate another time difference to put as left end of 'random part'

u_time_two = time.time()

tinytics=math.frexp(u_time_two - u_time_one)

p = [tinytics[0],tinytics[1]]

tinytics_man = math.frexp(tinytics[0])

q = [tinytics_man[0],tinytics_man[1]]

# 
print (tinytics, tinytics_man)
print ()
print (p,q)

dist = math.dist(p,q)

print (np.uint64(dist))






