#!/bin/python

from bsky_tid import  bsky_convert2_b32, bsky_tid_obj

TID_raw64bit_int=124355544444333

thingo = bsky_convert2_b32 (128383883333)

print (thingo)

test_tid_int = bsky_tid_obj()
test_tid_int.print_time_info()
test_tid_int.instance_debug()
bsky_tid_obj.class_debug()
bsky_tid_obj.staticmethod()
test_tid_int.time_update()
test_tid_int.time_update()
test_tid_int.tid_generate()
test_tid_int.tid_generate()
test_tid_int.tid_generate()
test_tid_int.tid_generate()

test2_tid_int = bsky_tid_obj()
test2_tid_int.instance_debug()
test2_tid_int.tid_generate()




