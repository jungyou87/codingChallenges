#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

givenList = [10, 15, 3, 7]
k=17
def numCheck (k, givenList):
  for i in range(len(givenList)):
    if (givenList[i] + givenList[i+1]) == k :
      return True
    elif (givenList[i] + givenList[i+2]) == k:
      return True
    elif (givenList[i] + givenList[i+3]) == k:
      return True
    elif (givenList[i+1] + givenList[i+2]) == k:
      return True
    elif (givenList[i+1] + givenList[i+3]) == k:
      return True
    elif (givenList[i+2] + givenList[i+3]) == k:
      return True
    else:
      return False