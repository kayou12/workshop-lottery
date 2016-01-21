#!/usr/bin/env python

from collections import defaultdict
import random
import sys

def main():
    with open('input/moderators.txt', 'r') as mod_file:
        with open('input/attendees.txt', 'r') as att_file:
            mods = mod_file.read().splitlines()
            atts = att_file.read().splitlines()
            
            team_count = len(mods)
            
            mod_teams = range(1, team_count+1)
            att_teams = [(t%team_count) + 1 for t in range(1, len(atts)+1)]
            
            random.shuffle(mod_teams)
            random.shuffle(att_teams)
                
            people = mods + atts
            teams = mod_teams + att_teams
            
            people_teams = zip(people, teams)
            
            # tests
            team_population = defaultdict(int)
            for pt in people_teams:
                team_population[pt[1]] +=1
            print team_population
            


if __name__ == '__main__':
    main()

