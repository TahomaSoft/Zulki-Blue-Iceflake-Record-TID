import time
import math
import itertools

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

        self.obj_seq = self.obj_seq +1
        if self.obj_seq == 10:
            self.obj_seq =0
            
        print ("foo talks:", self.MAX_TID)
        print (epoch_fracSeconds)
        print (epoch_uSeconds)
        print ("bit length: ", epoch_uSeconds.bit_length())
        print (self.obj_seq)

        bit_test = self.MAXY_MASK_64b | epoch_uSeconds
        print ("masky mask: ", bin (self.MAXY_MASK_64b))
        print ("masky mask bit length: ", self.MAXY_MASK_64b.bit_length())
        
        print (bin (epoch_uSeconds))
        print (bin (bit_test))
        print (bit_test.bit_length())
        sbit_test = bit_test ^ self.MAXY_MASK_64b
        print (sbit_test.bit_length())
        print (bin(sbit_test))


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
    


