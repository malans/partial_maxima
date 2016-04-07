# -*- coding: utf-8 -*-
import random

class Event:
    def __init__(self, index, excitement):
        self.index = index
        self.excitement = excitement

class EventList:
    def __init__(self, data_length = 1000000):
        self.data_length = data_length
        self.initialize_data()
        self.precomputed = {}
        self.precompute(0, self.data_length - 1)
        
    def initialize_data(self):
        self.events = [event(i, random.uniform(0,1)) for i in range(self.data_length)]
        
    def print_events(self):
        for event in self.events:
            print event.index, event.excitement
            
        
    def most_exciting_event(self, i0, i1):
        start = 0
        end = self.data_length - 1 
        
        while True:
            mid = (start + end) / 2
            if i0 <= mid < i1:
                max_first_half = self.precomputed[(i0, mid)]
                max_second_half = self.precomputed[(mid + 1, i1)]
                if max(max_first_half.excitement, max_second_half.excitement) == max_first_half.excitement:
                    print max_first_half.index, max_first_half.excitement                    
                    return max_first_half
                else:
                    print max_second_half.index, max_second_half.excitement
                    return max_second_half
            elif i1 <= mid:
                end = mid
            else:
                start = mid + 1
        
    def precompute(self, start, end):
        if start == end:
            return
            
        mid = (start + end) / 2
        maximum = self.events[mid]
        # first half
        for i in range(mid, start - 1, -1):
            if (i, mid) in self.precomputed:
                continue
            current = self.events[i]
            if current.excitement > maximum.excitement:
                self.precomputed[(i, mid)] = current
                maximum = current
            else:
                self.precomputed[(i, mid)] = maximum
                
        # second half
        maximum = self.events[mid + 1]
        for i in range(mid + 1, end + 1):
            if (i, mid) in self.precomputed:
                continue
            current = self.events[i]
            if current.excitement > maximum.excitement:
                self.precomputed[(mid + 1, i)] = current
                maximum = current
            else:
                self.precomputed[(mid + 1, i)] = maximum
        self.precompute(start, mid)
        self.precompute(mid + 1, end)
                
                
            
        
        
        
    
        
    
        