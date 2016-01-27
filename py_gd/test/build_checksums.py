#!/usr/bin/env python

"""
this script can be run to build checksums for all the images generated by the tests

the output can be cut&pasted into the test file

and updated when neccessary.

"""

import sys, os, hashlib

images_dir = "test_images_output"
checksums = {}
for name in os.listdir("test_images_output"):
    n = os.path.join("test_images_output", name)
    checksums[name] = hashlib.md5(open(n,'rb').read()).hexdigest()

print str(checksums)
