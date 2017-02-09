"""

   Time Complexity: O(n) based on number of elements in dictionary

   1. allocate empty dictionary to store result = {}
   2. for each key in dictionary:
      call add_to_output(key,value,result)
   
      add_to_output(prefix,value,result)
         - if value is dict:
            for each key in dict, call add_to_output(prefix + '.' + key, value[key])
         - else:
            result[prefix + '.' + key] = value
   
   3. return result


   {} ==> {}
   {'a': 1} ==> {'a': 1}
   
   Example:
   {
     'Key1': '1',
     'Key2': {
       'a' : '2',
       'b' : '3',
       'c' : {
         'd' : '3',
         'e' : '1'
         }
       }
   }
   
   Result:
   {
      'Key1': '1',
      'Key2.a': // it works
   }

"""

def flatten_dict(input):
   if input is None or len(input) == 0: return {}
   else:
      result = {}
      stack = [('',input)]
      while stack:
         prefix,target = stack.pop()
         if isinstance(target, dict): # check this
            for key in target:
               stack.append((prefix + '.' + key, target[key]))
         else:
            result[prefix] = target
      return result