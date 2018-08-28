#!/usr/bin/env python

# Designed by Mr. Saurab VERMA

import argparse
from rosbag import Bag


def filter():

	parser = argparse.ArgumentParser(description='Merge one or more bag files with the possibilities of filtering topics.')
	parser.add_argument('inputbag', help='input bag file')
	parser.add_argument('outputbag', help='output bag file with filtered topics')
	parser.add_argument('-v', '--verbose', action="store_true", default=False, help='verbose output')
	parser.add_argument('-t', '--topics', nargs='+', help='string interpreted as a list of  topic names to include in the filtered bag file; NOTE: mention exact topic names')
	parser.add_argument('-nt', '--new_topics', nargs='+', help='string interpreted as a list of new topic names for the capturing topics; NOTE: mention exact topic names')
	args = parser.parse_args()

    topics = args.topics.split(' ')
    new_topics = args.topics.split(' ')

    if (args.verbose):
        print("Writing bag file: " + args.outputbag)
        print("Matching topics against patters: '%s'" % ' '.join(topics))

	with Bag(args.outputbag, 'w') as outputBag:
		for topic, msg, t in Bag(args.inputbag):
			if topic == '/velodyne_straight/velodyne_points':
				outputBag.write('/velodyne_points', msg ,t)

if __name__ == "__main__":
    filter()
