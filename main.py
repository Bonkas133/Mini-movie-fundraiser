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

#checks that user response is not blank


def not_blank(question):
  while True:
    response = input(question)
    if response == " " or response == "" or response =="  " or response=="   " or response =="    ":
      print("You can't enter blank, try again.")
    else:
      return response


def num_check(question):
  while True:
    try:
      response = int(input(question))
      return response

    except ValueError:
      print("Please enter an integer.")
#checks user's age to be correct

#set maximum amount of tickets to be sold


def calc_ticket_price(var_age):
  if var_age < 16:
    price = 7.5

  elif var_age < 65:
    price = 10.5

  else:
    price = 6.5

  return price

#main functions go here
MAX_TICKETS = 3
tickets_sold = 0
#Ask user if they want to see the instructions
want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
  print("Instructions")
elif want_instructions == "no":
  print("Moving on...")



while tickets_sold < MAX_TICKETS:
  name = not_blank("Please enter name or enter 'xxx' to quit: ")
  if name == "xxx":
    break
  age = num_check("Please enter your age: ")
  if 12 <= age <=120:
    pass
  elif age < 12:
    print("You are too young for this movie")
    continue
  else:
    print("You need to enter a number")
    continue

  ticket_cost = calc_ticket_price(age)
  print("Age: {}, Ticket Price: ${:.2f}".format(age, ticket_cost))
  tickets_sold += 1
if tickets_sold ==MAX_TICKETS:
  print("all tickets sold")
else:
  print("You have sold {} ticket/s.  There is {} ticket/s remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))




