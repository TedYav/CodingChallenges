"""

   Given an array of timestamps:
      { time: 1440084737,  count: 4,  type: "enter" }
   Return timestamps: beginning to end
   
   Brute Force -> Enumerate all seconds in last year, count number of people in each, return

   Better Solution: Treat entering and exiting as delta values
      E.G.
         1: 4 enter --> 4 people
         2: 2 leave --> 2 people
         3: 10 enter -> 12 people

   Solution: sort, count changes

"""
1 1 enter
1 1 enter
1 1 enter
1 3 exit

1
2
3
0
max = 3
max = 0

# O(nlogn)

def busiest_time(times):
#    {'time: int, 'count': int, 'type' : 'enter/exit'}
   if times is None or len(times) < 1: return None
   
   times = sorted(times, key=lambda t: t['time'])
   times.append({'time': times[-1]['time'] + 1, 'count':1, 'type':'exit'})
   num_people = 0
   
   current_time = times[0]['time']
   
   current_max = 0
   current_max_start = current_time
   current_max_end = -1
   
   for entry in times:
      if entry['time'] > current_time:
         if num_people > current_max:
            current_max = num_people
            current_max_start = current_time
            current_max_end = -1
         elif num_people < current_max and current_max_end == -1:
            current_max_end = current_time
         current_time = entry['time']
      
      if entry['type'] == 'enter':
         num_people += entry['count']
      
      elif entry['type'] == 'exit':
         num_people -= entry['count']
   
   return (current_max_start,current_max_end)
        
   count = 0
   maxCount = 0
   maxPeriod = [0,0]
   for i from 0 to n-1:
      #update count:
      if (data[i].type == "enter"):
         count += data[i].count
      else if (data[i].type == "exit"):
         count -= data[i].count

      #check for other entry with same time:
      if (i < n-1 AND data[i].time == data[i+1].time):
         continue

      #update maximum
      if (count > maxCount):
         maxCount = count
         maxPeriod[0] = data[i].time
         if (i < n-1):
            maxPeriod[1]= data[i+1].time
         else:
            maxPeriod[1] = data[i].time
   return maxPeriod