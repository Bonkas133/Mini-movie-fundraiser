#functions here
#Checks user has entered yes or no to a question
def yes_no(question):
  while True:
    response = input(question).lower()
    if response == "yes" or response == "y":
      return "yes"
    elif response == "no" or response == "n":
      return "no"
    else:
      print("Please enter yes or no")

      
#main routine starts here


  
def num_check(question):
  while True:
    try:
      response = int(input(question))
      return response

    except ValueError:
      print("Please enter an integer.")
#checks user's age to be correct

#set maximum amount of tickets to be sold
MAX_TICKETS = 3
tickets_sold = 0
#Ask user if they want to see the instructions
want_instructions = yes_no("Do you want to read the instructions?")

if want_instructions == "yes":
  print("KINSTRUCtizons")
print()



while True:
  name = input("Please enter name or enter 'xxx' to quit: ")
  if name == "xxx":
    break
  else:
    break
while True:
  age = num_check("Please enter your age: ")
  if 12 <= age <=120:
    break
  elif age < 12:
    print("You are too young for this movie")
    continue
  else:
    print("You need to enter a number")
    continue

  
  tickets_sold += 1
if tickets_sold ==MAX_TICKETS:
  print("all tickets sold")
else:
  print("You have sold {} ticket/s.  There is {} ticket/s remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))




