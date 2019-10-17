#!/bin/sh

apt install -y xvfb
mv geckodriver /usr/bin/

cp searchrecon.py "/usr/bin/searchrecon"

