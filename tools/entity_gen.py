#!/usr/bin/env python
# -*- coding: utf-8 -*-

from optparse import OptionParser
import sys
import os

from entity_gen.generator import *

#os.chdir(os.path.dirname(__file__))

parser = OptionParser()
(options, args) = parser.parse_args()

if len(args) < 1:
    print 'entity_gen.py YOUR.entity_def'
    quit()

d = {
    'ENTITY_DEF': [],
}

execfile(args[0], d, d)

print(d['ENTITY_DEF'])

generator = AndroidGenerator(d['PACKAGE'], os.path.dirname(os.path.realpath(args[0])))
for e in d['ENTITY_DEF']:
    e.accept(generator)
