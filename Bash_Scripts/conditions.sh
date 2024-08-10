#!/bin/bash

read -p "Type your number: " var

if [ $var -le 20 ]; then
    echo "$var is less than 20"
else if [ $var -eq 20 ]
    echo "Number is: $var"
else
    echo "$var is greater than 20"
fi