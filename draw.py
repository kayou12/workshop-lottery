#!/usr/bin/env python

import random
import sys

def main():
    with open('input/moderators.txt', 'r') as mod_file:
        with open('input/attendees.txt', 'r') as att_file:
            mods = mod_file.read().splitlines()
            atts = att_file.read().splitlines()
            
            mod_teams = range(1, len(mods)+1)
            att_teams = [t%5+1 for t in range(1, len(atts)+1)]
            
            random.shuffle(mod_teams)
            random.shuffle(att_teams)
                
            people = mods + atts
            teams = mod_teams + att_teams
            
            people_teams = zip(people, teams)
            
            print people_teams
            
            # for i in range(mods_no):
            #     print '{0}\t{1}'.format(mods[i], mod_teams[i])
            
            # group_size = round(len(atts)/group_no)


if __name__ == '__main__':
    main()

