#!/bin/bash


# Method 1

# read using file.sh var1, var2
echo "This is variable 1 => $1"

echo "This is variable 2 => $2"



# Method 2

#echo "Type your input: "

#read var



# Method 3

read -p "Type your input: " var

echo "This is your input => $var"