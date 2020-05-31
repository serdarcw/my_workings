#!/bin/bash
clear
input="/Users/ODG/Desktop/git_dir/my_workings/serkan.txt"

while IFS= read -r line
do
	new=$( echo $line | awk -F' ' '{print $4}')
	echo "**** **** **** $new"
done < "$input"
