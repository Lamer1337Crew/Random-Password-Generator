#!/usr/bin/env python
# -*- coding:utf-8 -*-

import string
import random

def random_password_genertor():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = 8
    return ''.join(random.choice(chars) for x in range(size,20))

def random_password_genertor_ico():
	random_password_genertor_ico = """
	#############################################################
	# PYTHON - Random Password Generetor By VanGans - SadCode.  #
	############################################################# 
	#                         CONTACT                           #
	#############################################################
	#               Coded By : VanGans - SadCode                #
	#          Mail Address : dawnysabun110@gmail.com           #
	#   Facebook : https://www.facebook.com/vangans.id          #
	#          Instagram : https://instagram/almahdi18id        #
	#############################################################
	"""
	print random_password_genertor_ico

random_password_genertor_ico()
print("Password : " + random_password_genertor())
