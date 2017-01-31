"""

   Given: TimesA, TimesB --> sorted arrays of time spans
      There are no elements in common in both arrays
   Return Array of start and end time
      
   Example:
      Duration = 100
      TimesA = [(150,230),(240,340),(400,450),(460,700)]
      TimesB = [(200,300),(300,450),(500,600)]
      [150, 200] []
      Earliest Time: [500,600]
      
      len(TimesA) = n
      len(TimesB) = m
      
      TimesA:
         (150,230): d = 80
      
      TimesB:
         (200,300): d = 100
            Overlapping Duration: 30
      
      i = 0, j = 0
      For each element in TimesA:
         if TimesA[i].end < TimesB[j].begin:
            i += 1
         elif B ends before A:
            j += 1
         else:
            check overlapping time
      
      O(n + m)

"""

"""

   Duration = 100
      TimesA = [(150,230),(240,340),(400,450),(460,700)]
      TimesB = [(200,300),(300,450),(500,600)]
      
      i=0,j=0: (150,230) to (200,300): overlap 30
      i=1,j=0: (240,340) to (200,300): overlap 60
      i=1,j=1: (240,340) to (300,450): overlap 40
      i=2,j=1: (400,450) to (300,450): overlap 50
      i=2,j=2: (400,450) to (500,600): no overlap
      i=3,j=2: (460,700) to (500,600): return [500,600]

"""


def schedule_meeting(duration, times_a, times_b):
   if duration <= 0 or not times_a or not times_b: return []
   else:
      i = j = 0
      while i < len(times_a) and j < len(times_b):
         if times_a[i][1] < times_b[j][0]: # a ends before b begins
            i += 1
            continue
         elif times_b[j][1] < times_a[i][0]:
            j += 1
            continue
         
         start_time, end_time = overlap(times_a[i], times_b[j])
         if end_time - start_time >= duration:
               return [start_time, end_time]
         else:
            if times_a[i][1] < times_b[i][1]:
               i += 1
            else:
               j += 1

   return []

def overlap(time1, time2):
   start_time = max(time1[0],time2[0])
   end_time = min(time1[1],time2[1])
   return (start_time, end_time) # start + dur
            
            
            