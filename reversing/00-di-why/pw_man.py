#!/usr/bin/env python3

import sys


KEY    = b'\x7b\x36\x14\xf6\xb3\x2a\x4d\x14\x19'
SECRET = b'\x13\x59\x7a\x93\xca\x49\x22\x79\x7b'


def authenticate(password):
    '''
    Authenticates the user by checking the given password
    '''

    # Convert to the proper data type
    password = password.encode()

    # We can't proceed if the password isn't even the correct length
    if len(password) != len(SECRET):
        return False

    tmp = bytearray(len(SECRET))
    for i in range(len(SECRET)):
        tmp[i] = password[i] ^ KEY[i]

    return tmp == SECRET


def get_pw_db(file_name):
    '''
    Constructs a password database from the given file
    '''

    pw_db = {}

    with open(file_name) as f:
        for line in f.readlines():
            entry, pw = line.split('=', 1)
            pw_db[entry.strip()] = pw.strip()

    return pw_db


def main():
    '''
    Main entry point of the program. Handles I/O and contains the main loop
    '''

    print('Welcome to pw_man version 1.0')
    password = input('password: ')

    if not authenticate(password):
        print('You are not authorized to use this program!')
        sys.exit(1)

    pw_db = get_pw_db(sys.argv[1])
    print('Passwords loaded.')

    while True:

        print('Select the entry you would like to read:')
        for entry in pw_db.keys():
            print('--> {}'.format(entry))

        selected = input('Your choice: ')

        try:
            print('password for {}:    {}'.format(selected, pw_db[selected]))
        except KeyError:
            print('unrecognized selection: {}'.format(selected))
            print('please')


if __name__ == '__main__':
    main()
