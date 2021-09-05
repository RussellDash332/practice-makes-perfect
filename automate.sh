#!/bin/bash
for dir in 01 02 03 04 05 06 07 08 09
do
	cd $dir
	make
    cd ..
done

cd 08 && make q && cd ..

for mock in Midterm Finals
do
    cd Mock/$mock
    make
    make s
    cd ../..
done