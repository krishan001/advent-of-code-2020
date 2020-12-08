#!/bin/bash

mkdir "Day$1"
cp -a "Day_X/". "Day$1"
cd "Day$1"
mv "dayx_input_test.txt" "day$1_input_test.txt"
mv "dayx_input.txt" "day$1_input.txt"
mv "dayx_test.py" "day$1_test.py"
mv "dayx.py" "day$1.py"
sed -i "s/dayx/day$1/g" day$1_test.py


