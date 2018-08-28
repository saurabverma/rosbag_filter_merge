#!/usr/bin/env python

# Usage:
# rosbag_merge_filter.py <output file>.bag <list of input files>.bag -v -t <topics to collect from input bag files> -nt <new name for topic>
# Ex. rosbag_merge_filter.py output_bag.bag *.bag -v -t /velodyne_straight/velodyne_points -nt /velodyne_points

import sys
import argparse
from fnmatch import fnmatchcase
from rosbag import Bag

def merge():

	# Setting arguments
	parser = argparse.ArgumentParser(description='Merge one or more bag files with the possibilities of filtering topics.')
	parser.add_argument('outputbag', help='output bag file with topics merged')
	parser.add_argument('inputbag', nargs='+', help='input bag files')
	parser.add_argument('-v', '--verbose', action="store_true", default=False, help='verbose output')
	parser.add_argument('-t', '--topics', default="*", help='string interpreted as a list of topics (wildcards \'*\' and \'?\' allowed) to include in the merged/filtered bag file')
	parser.add_argument('-nt', '--new_topic', default=False, help='store all the potentially found topics with this "new_topic" name in the merged/filtered bag file')
	args = parser.parse_args()

	# Varialbe initialisation
	topics = args.topics.split(' ')
	total_included_count = 0
	total_skipped_count = 0

	if (args.verbose):
		print("Writing bag file: " + args.outputbag)
		print("Matching topics against patters: '%s'" % ' '.join(topics))

	# Start the process
	with Bag(args.outputbag, 'w') as o:
		for ifile in args.inputbag:
			matchedtopics = []
			included_count = 0
			skipped_count = 0

			if (args.verbose):
				print("> Reading bag file: " + ifile)

			# Read each potentially available bag file
			with Bag(ifile, 'r') as ib:
				for topic, msg, t in ib:
					if any(fnmatchcase(topic, pattern) for pattern in topics):
						if not topic in matchedtopics:
							matchedtopics.append(topic)
							if (args.verbose):
								print("Including matched topic '%s'" % topic)

						if args.new_topic: # If required, store with new topic name
							o.write(args.new_topic, msg, t)
						else: # otherwise, continue as it is
							o.write(topic, msg, t)
						included_count += 1
					else:
						skipped_count += 1

			total_included_count += included_count
			total_skipped_count += skipped_count
			if (args.verbose):
				print("< Included %d messages and skipped %d" % (included_count, skipped_count))

	if (args.verbose):
		print("Total: Included %d messages and skipped %d" % (total_included_count, total_skipped_count))

if __name__ == "__main__":
	merge()
