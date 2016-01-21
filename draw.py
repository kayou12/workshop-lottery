#!/usr/bin/env python

from collections import defaultdict
import csv
import random
import sys

def main():
    with open('input/moderators.txt', 'r') as mod_file:
        with open('input/attendees.txt', 'r') as att_file:
            mods = mod_file.read().splitlines()
            atts = att_file.read().splitlines()
            
            team_count = len(mods)
            
            # generating ranges of team numbers
            mod_teams = range(1, team_count+1)
            att_teams = [(t%team_count) + 1 for t in range(1, len(atts)+1)]
            
            # ordering the team numbers randomly
            random.shuffle(mod_teams)
            random.shuffle(att_teams)
            
            # merging the collections for moderators and attendees
            people = mods + atts
            teams = mod_teams + att_teams
            
            # joining the people and team numbers collections (no key, just side-by-side)
            people_teams = zip(people, teams)
            people_teams.sort(key=lambda pt: pt[0])
            
            # testing if the team numbers have been uniformly distributed
            team_population = defaultdict(int)
            for pt in people_teams:
                key = pt[1]
                team_population[key] +=1
            
            # writing output
            with open('output/teams.tsv', 'wb') as team_file:
                writer = csv.writer(team_file, delimiter='\t', quoting=csv.QUOTE_ALL)
                
                writer.writerow(['Name', 'Team number'])
                writer.writerows(people_teams)
                writer.writerows([[], []])
                writer.writerow(['Team', 'Number of members'])
                writer.writerows(sorted(team_population.items()))
            

if __name__ == '__main__':
    main()

