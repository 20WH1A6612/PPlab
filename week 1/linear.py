def search(arr, key):
      for i in range(len(arr)):
           if arr[i] == key:
               return i
       return -1
  
  arr = ['a', 'e', 'i', 'o', 'u']
  key = 'u'
  
  print("found" + str(search(arr, key)))
