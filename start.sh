#!/bin/bash

# This script starts all the services necessary for the ctf, including a PHP webserver and netcat servers

php -S localhost:4001 -t www/ &

# Then just sleep until killed by systemd
sleep infinity
