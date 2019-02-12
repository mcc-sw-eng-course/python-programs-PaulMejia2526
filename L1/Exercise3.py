def removeDuplicates(list):
   "This prints a passed string into this function"
   newList = []
   for item in list:
       if item not in newList:
           newList.append(item)

   return newList;

def removeDuplicatesSet(list):
   "This prints a passed string into this function"
   newSet = set(list)
   return newSet;

while(True):
    userInput = input("Enter list (Each item is , separated)")
    list = userInput.split(",")
    newList = removeDuplicates(list)
    newSet = removeDuplicatesSet(list)
    print ("New list with no duplicates (Array):")
    print (newList)
    print ("New list with no duplicates (Set):")
    print (newSet)