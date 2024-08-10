#!/bin/bash

# For Loop
for i in {1..5}
do
    echo "This is for loop output number $i"
done

for out in 1 2 3 4 5 6 hello world
do
    echo "This is for loop output with output as $out"
done



# While Loop
# declare -i num=1;
num=1
while [ $num -le 10 ]
do
    echo "This is num => $num"
    # $((num++));
    num=$((num+1))
done


# Until Loop
num=1
until [ $num -eq 20 ]
do
    echo "This is num value in until loop => $num"
    ((num+=1))
done