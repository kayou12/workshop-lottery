#!/usr/bin/env python

import sys

def main():
    with open('input/moderators.txt', 'rb') as mod_file:
        for mod in mod_file:
           sys.stdout.write(mod)

if __name__ == '__main__':
    main()

