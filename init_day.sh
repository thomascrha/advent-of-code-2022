#!/bin/bash

read -p 'What day do you want to setup: ' DAY_NUMBER
TEMPLATE='"""\n\n"""\nfrom rich import print\nimport numpy as np\n\ndef get_input():\n\twith open("./day$DAY_NUMBER.input") as input_file:\n\t\treturn input_file.read()\n\n\n\n'
mkdir day$DAY_NUMBER
touch day$DAY_NUMBER/{day$DAY_NUMBER-1.py,day$DAY_NUMBER-2.py,day$DAY_NUMBER.input}
echo -e "$TEMPLATE" >> day$DAY_NUMBER/day$DAY_NUMBER-1.py
echo -e "$TEMPLATE" >> day$DAY_NUMBER/day$DAY_NUMBER-2.py
