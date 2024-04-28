import time
import math

class bsky_tid_obj:
    '''
    Blue Sky - ATProto TID Generator
    spec: https://atproto.com/specs/record-key#record-key-type-tid

    Generate unique record id for bluesky posts, following
    more restrictive TID (time stamp identifier) format
    
    '''

    # Setup constants

    MAX_TID = (2**63)
    MAXY_MASK_64b = (2**63) +1
    FINAL_STRING_LENGTH = 13
    FIRST_BIT = 0b0
    EPOCH_MAX = (2**53)  # Max value for epoch as microseconds since UNIX epoch
    RANDO_MAX = (2**10)  # Max value for random part appended to Epoch/time 53 bits


    # Setup class-wide variables
    obj_seq = 0 # object sequence counter
    
    def __init__(self):
        '''
        '''
        
        
    
    def print_max(self):
        epoch_fracSeconds = time.time()
        epoch_uSeconds = math.trunc (time.time() * (10**6))

        self.obj_seq = self.obj_seq +1
        print ("foo talks:", self.MAX_TS)
        print (epoch_fracSeconds)
        print (epoch_uSeconds)
        print (self.obj_seq)
        
        return
    


