#!/usr/bin/env bash

# Filter and merge
# python_file outputBag inputBag -v -t <topics to include> -nt <new name of topic for storage>
~/docker_mount/bags/rosbag_handle_files/rosbag_merge_filter.py ~/docker_mount/bags/bag_rotone_hta.bag ~/docker_mount/bags/bag_rotone/HTA/* -v -t /velodyne_straight/velodyne_points -nt /velodyne_points
~/docker_mount/bags/rosbag_handle_files/rosbag_merge_filter.py ~/docker_mount/bags/bag_rotone_orss.bag ~/docker_mount/bags/bag_rotone/ORSS/* -v -t /velodyne_straight/velodyne_points -nt /velodyne_points
~/docker_mount/bags/rosbag_handle_files/rosbag_merge_filter.py ~/docker_mount/bags/bag_rotone_orloc.bag ~/docker_mount/bags/bag_rotone/ORLOC/* -v -t /velodyne_straight/velodyne_points -nt /velodyne_points
