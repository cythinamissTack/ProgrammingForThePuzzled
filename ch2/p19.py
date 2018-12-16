#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 15:18:45 2018

@author: sahashi
"""

sched2 = [(6.0,8.0), (6.5,12.0), (6.5,7.0), (7.0,8.0), 
         (7.5,10.0), (8.0,9.0), (8.0,10.0), (9.0,12.0),
         (9.5,10.0), (10.0,11.0), (10.0,12.0), (11.0,12.0)]

def bestTimeToPartySmart(schedule):
    times = []
    for c in schedule:
        times.append((c[0], 'start'))
        times.append((c[1], 'end'))
    
    def sortList(tlist):
        for ind in range(len(tlist)-1):
            iSm = ind
            for i in range(ind, len(tlist)):
                if tlist[iSm][0] > tlist[i][0]:
                    iSm = i
            tlist[ind], tlist[iSm] = tlist[iSm], tlist[ind]
        
    sortList(times)
    
    def chooseTime(times):
        rcount = 0
        maxcount = time = 0
        for t in times:
            if t[1] == 'start':
                rcount += 1
            elif t[1] == 'end':
                rcount -= 1
            if rcount > maxcount:
                maxcount = rcount
                time = t[0]
        return maxcount, time
        
    maxcount, time = chooseTime(times)
    
    print('Best time to attend the party is at', time, 'o\'clock',
          ':', maxcount, 'celebrities will be attending!')

bestTimeToPartySmart(sched2)    
