#!/bin/sh -l
# entrypoint.sh
echo "::debug ::Debug Message"
echo "Hello $1"
time=$(date)
echo "::set-output name=time::$time"
echo "::group::Some expandable logs"
echo 'Stuff 1'
echo 'Stuff 2'
echo 'Stuff 3'
echo "::endgroup::"