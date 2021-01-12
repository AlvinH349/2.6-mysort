def my_sort(list1):

  for i in range(len(list1)):
    for j in range(i+1, len(list1)): 
      if list1[i] > list1[j]: 
        list1[i], list1[j] = list1[j], list1[i] 

  print(list1)

my_sort([3,1,2])