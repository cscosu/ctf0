#!/bin/bash

# This script starts all the services necessary for the ctf, including a PHP webserver and netcat servers

php -S localhost:4001 -t www/ &
ncat -c "./reversing/00-di-why/pw_man.py ./reversing/00-di-why/pw_db.txt" -k -l 4003

# Then just sleep until killed by systemd
sleep infinity
