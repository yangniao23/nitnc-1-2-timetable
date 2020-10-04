#!/usr/bin/env python3
import json

class timetable:
    def __init__(self):
        self.jsondata = {}
        self.timetable = []
    
    def readjson(self, path):
        try:
            self.jsondata = json.load(open(path, 'r'))
            #self.timetable = [[lecture for lecture in self.jsondata['timetable'][onedata]] for onedata in self.jsondata['timetable']]
            self.timetable = self.jsondata['timetable']
    
        except:
            print("Error! Timetable could not reading.")
            exit(1)

    
    
timetable = timetable()
timetable.readjson('timetable-2020-1-2.json')
print(timetable.timetable)