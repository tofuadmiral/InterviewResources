import sys

# hold our raw data in an array
rawdata = []

for line in sys.stdin:
  rawdata.append(line)

numOptions=rawdata[0]
numQueries=rawdata[numOptions]

for i in xrange(1, numOptions):
  # loop through each option and make into a list itself
  rawdata[i]=[x.strip() for x in rawdata[i].split(',')]
  # 0 = city, 1 = supplier, 2 = price

# now do same for queries, can reuse i bc in another loop
for i in xrange(numQueries+1, len(rawdata)): # start from first query, go till end
  rawdata[i]=[x.strip() for x in rawdata[i].split(',')]

  # now look for city & append to list, so can print later, 0=city, 1=supplier 2=daystillcheckin
  returnprices=getPrices(rawdata[i][0], rawdata[i][1], rawdata, numOptions)

  # print the prices, but if we find none make sure to return none
  if not returnprices: # if return list is empty that means we didnt find any
    print("None")
  else:
    sortedlist=returnprices.sort() # sort defaults to ascending order
    for j in xrange(len(sortedlist)-1): # use j bc within other loop
      print(sortedList[j]+ ",")    # add a comma to the return prices, except for last item
    print(sortedlist[-1])          # print the last item, but with no comma 


# should be done here! below is the helper function to find the prices



# helper function to get price for the city given the city and days till checkin
def getPrices(city, days, rawdata, numOptions):
  returnprices=[] # return a list to be sorted later 
  pricefactor=1 # edit this later depending on supplier

  # now, do the processing and search work
  for k in xrange(1, numOptions):
    if rawdata[k][0]==city: # this means it's the right city, so add it to the returnprices
    
      # factor in days till check in for price and supplier
      # days must be an integer and its a string right now, so typecast it
      days = int(days)
      if rawdata[k][1]=="A":
        if days == 1:
          pricefactor=1.5 # increase by 50%
      elif rawdata[k][1]=="B":
        if days <3: # can't book the hotel 
          continue # continue in the loop bc it counts as a None
      elif rawdata[k][1]=="C":
        if days >= 7:
          pricefactor=0.9 #decreases by 10%
      else: # assume that it's D, not considering error of no supplier
        if days<7:
          pricefactor=1.1

      # now, add the price to the returnprices, make sure to typecast our string
      returnprices.append(int(rawdata[k][2])*pricefactor)






"""
some algorithm analysis! 
  time complexity:
    we run through every city, and for each city we look through each option
    thus, our time should be O(n*m), where n=queries and m=options
  space complexity:
    we're taking in our data but we're splitting it to a list, and then 
    we have a list of prices that we're adding onto and sorting later
    so that list must be O(m) extra space in the worst case, i.e. every option is a valid city for the query
    but then we overwrite this every time we call the function, so NOT O(n*m)




"""





