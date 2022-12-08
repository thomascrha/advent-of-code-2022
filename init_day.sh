#!/bin/bash


read -p 'What day do you want to setup: ' DAY_NUMBER
mkdir day$DAY_NUMBER
touch day$DAY_NUMBER/{day$DAY_NUMBER-1.py,day$DAY_NUMBER-2.py,day$DAY_NUMBER.input,day$DAY_NUMBER.md}
