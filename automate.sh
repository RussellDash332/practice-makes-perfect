#!/bin/bash
for dir in 01 02 03 04 05 06 07 08 09
do
    cd $dir
    make -B
    cd ..
done

cd 08 && make q && cd ..

for mock in Midterm Finals
do
    cd Mock/$mock
    make -B
    cd ../..
done