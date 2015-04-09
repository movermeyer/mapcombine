#!/usr/bin/env python3
from argparse import ArgumentParser
from mapcombine import outer_process

parser = ArgumentParser(description='MapCombine example')
parser.add_argument('--mapreduce', default='MapReduce',
                    help="Module that implements map_ and reduce_")
parser.add_argument('--filereader', default=None,
                    help="Module that implements DefaultFileReader")
parser.add_argument('--post', default=None,
                    help="Module that implements post_frame")
parser.add_argument('-t', '--thread', type=int, default=1,
                    help="Number of threads")
parser.add_argument('-b', '--block', type=int, default=1024,
                    help="Number of entries per block")
parser.add_argument('-v', '--verbose', action="store_true", default=False,
                    help="Verbose?")

args = parser.parse_args()
params = {}
jobs = [(args, params, 0),]

stuff = map(outer_process, jobs)
for i, res in enumerate(stuff):
  print(i, res["words"]['linen'], res["words"]['Rotherhithe'])
