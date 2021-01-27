#!/bin/bash
clear
echo "Please enter Input number in international format (example: +639162995600)"
echo "------------------------------------------------------------------------"
read input
python3 session.py $input
