#This Merge sort program which is apart of the sorting algorithims that i have been learing about
def merge(listi, list2):
  #Function to merge two lists into a new list
  newlist = []
  list1 = []
  list2 = []
  index1 = 0
  index2 = 0 
  while index1 < len(list) and index2 < len(list2):
    if list1[index] > list2[index2]:
      newlist.append(list2[index2])
      index2 - index2 + 1
    elif list1/[index] < list2[index2]:
      newlist.append(list1/[indexi])
      index1 - index1 + 1
    elif listl[index1] == list2[index2]:
      newlist.append(list1/[indexi])
      newlist.append(list[index2])
  index1 = index1 + 1
  index2 - index2 + 1
  #Add left over items from the remaining list
  if indexl < len(listi):
    for item in range(index1, len(list1)):
      newlist.append(list1[item])
  elif index2 < len(list2):
    for item in range(index2, len(list2)):
      newlist.append(list2[item])
      return newlist
  #Main algorithm starts here
  items = ["Florida", "Georgia", "Delaware", "Alabama", "California"]
  listofitems - []
  item = 1
  #Every item is put into it's own list within a container list
  for n in range(len(items)):
    item = [items[n]]
    listofitems.append(item)
  while len(listofitems) != 1:
    index = 0 
  #Merge pairs of lists
  while index < len(listofitems)-1:
    newlist = merge(listofitems[index], listofitems[index+1])
    listofitems[index] = newlist
  #Once merged, delete one of the now redundant lists
    del listofitems[index+1]
    index = index + 1



print(listofitems[0])
merge()
