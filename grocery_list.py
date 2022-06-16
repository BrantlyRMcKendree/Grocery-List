
#below I created a blank dictionary.

grocery_item = {}

#below I have created a blank list for grocery_history.

grocery_history = []

#Below is an item based for loops. Stop is a variable used in creating my while loop.

stop = 'c'

#Below is a while loop, which is only true if stop = c or C.


while stop == 'c' or stop == 'C':
  
  

  
    item_name = input('Item name:\n')

    quantity = input('Quantity purchased:\n')
 
    cost = input('Price per item:\n')

#above I modified the values of groceryitem dictionary from inputs.
# Below I was adding the values from above to my dictionary.

  
    grocery_item = {'name':item_name, 'number':int(quantity), 'price':float(cost)}
    
# below I added the entire dictionary to grocery history list
   
    grocery_history.append(grocery_item)
   
    stop=(input('Would you like to enter another item?\nType c for continue or q to quit:\n'))
   
grand_total = 0.00

#Below I have a index based range for grocery_history.

for items in range(0,len(grocery_history)):
  
#below I am accesing the value of the iteration of the list and using its dictionary key.
#My above stated comment covers both lists and dictionary access.  

  item_total = ((grocery_history[items]['number']) * (grocery_history[items]['price']))
  
  grand_total = item_total + grand_total
  
  print(str(grocery_history[items]['number']) + ' ' + (grocery_history[items]['name']) + ' @ ' +  '$' + str(grocery_history[items]['price']) + ' ea ' + '$' + str(item_total))

#Print the grand total

  item_total = 0

print('Grand total: $' + str(grand_total))
