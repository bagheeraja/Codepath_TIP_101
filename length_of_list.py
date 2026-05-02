def list_length(lst: [list]):
   acc = 0
   
   for _ in lst:
       acc += 1

   return acc

lst = [2,4,6,8,10]

length = list_length(lst)

print(length)