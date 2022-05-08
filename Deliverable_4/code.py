# Financial Tracker by Chinonyerem Ukaegbu and Fatima Nadeem
# Software Engineering Project
# 8 May 2022


journalList = [] # list of all journals in use during runtime
list_of_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

from tabulate import tabulate


# Main System class

class System:

  def __init__(self, id):
    self.ID = id

  def displayErrorMessage(self):
    pass

  def displaySuccessMessage(self):
    pass

  def registration(self):
    pass

  def loginaccount(self):
    pass

  def logoutaccount(self):
    pass



# Journal class

class Journal:

  def __init__(self, ID, name="", startDate="", endDate="", description=""):
    self.ID = ID
    self.transactionList = []
    self.name = name
    self.startDate = startDate
    self.endDate = endDate
    self.description = description
    self.transaction_ID_counter = 1 # ID counter for transactions, increments when new transaction is created

  def setName(self, name):
    self.name = name

  def getName(self):
    return self.name

  def setStartDate(self, startDate):
    self.startDate = startDate

  def getStartDate(self):
    return self.startDate

  def setEndDate(self, endDate):
    self.endDate = endDate

  def getEndDate(self):
    return self.endDate

  def setDescription(self, description):
    self.description = description

  def addTransaction(self, transactionX):
    self.transactionList.append(transactionX)

  def deleteTransaction(self, transactionY):
    self.transactionList.remove(transactionY)

  def resetAttributes(self):
    self.startDate = " "
    self.endDate = " "
    self.description = " "

  def increaseTranscationID(self):
    self.transaction_ID_counter+=1



# Transaction class

class Transaction:

  def __init__(self, ID, category, isExpenditure, isRevenue, amount):
    self.ID = ID
    self.category = category
    self.isExpenditure = isExpenditure
    self.isRevenue = isRevenue
    self.amount = amount

  def changetype(self, type):
    if type=="Expenditure":
      self.isExpenditure = True
      self.isRevenue = False
    else:
      self.isExpenditure = False
      self.isRevenue = True

  def setname(self, name):
    self.name = name

  def getname(self):
    return self.name

  def gettype(self):
    if self.isExpenditure == True:
      return "Expenditure"
    if self.isRevenue == True:
      return "Revenue"

  def setamount(self, amount):
    self.amount = amount

  def getamount(self):
    return self.amount



# User class

class User:
  def __init__(self, ID, name, email, password):
    self.ID = ID
    self.name = name
    self.email = email
    self.password = password
    self.loginStatus = False
    self.journalList = []

  def verifyLogin(self):
    if(loginStatus == True):
      return True

    else:
      return False

  def logout(self):
    loginStatus = False;

  def deleteAcount(self):
    pass
    
  def createJournal(self, journalX):
    self.journalList.append(journalX)

  def editJournal(self):
    pass

  def deleteJournal(self, journalY):
    self.journalList.remove(journalY)

  def saveInfo(self):
    pass



# User Info class

class UserInfo:
  def __init__(self, ID, name, email, password):
    self.__ID = ID
    self.__name = name
    self.__email = email
    self.__password = password

  def displayUserInfo(self):
    print("ID: " + str(self.__ID))
    print("Name: " + self.__name)
    print("Email: " + self.__email)

  def getID(self):
    return self.__ID

  def setID(self, new_ID):
    self.__ID = new_ID

  def getName(self):
    return self.__name

  def setName(self, new_name):
    self.__name = new_name

  def getEmail(self):
    return self.__email

  def setID(self, new_email):
    self.__email = new_email
  
  def getPassword(self):
    return self.__password

  def setPassword(self, new_password):
    self.__password = new_password



# Notification class

class Notification:

  def __init__(self, ID, createdOn, notificationType, details):
    self.ID = ID
    self.createdOn = createdOn
    self.notificationType = notificationType
    self.details = details

  def sendNotification(self):
    displayNotificationType()
    display()

  # reasoning behind this is that instead of the notification 
  # just displaying the error, it displays "Success" or "Error" 
  # and then the details. So we can call both print fuctions
  def displayNotificationType(self): 
    print(self.notificationType)

  def display(self):
    print(self.details)
  
# Error Notification child class

# class ErrorNotification:
#   def __init__(self, ID, createdOn, notificationType, details):
#     Notification.__init__(self, ID, createdOn, notificationType, details)


# # Success Notification child class

# class SuccessNotification:
#   def __init__(self, ID, createdOn, notificationType, details):
#     Notification.__init__(self, ID, createdOn, notificationType, details)

# we can probably get rid of the child classes because the notificationType seems sufficient



# Prospective User class

class ProspectiveUser:
  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password
    self.u1 = User(0, self.name, self.email, self.password)

  def register(self):
    u1.ID = ID_counter
    ID_counter+=1

  def checkID(self, ID_check):
    if(ID_check == "foo"):
      return True
    else:
      return False

  def checkPassword(self, password_check):
    if(password_check == "foo"):
      return True
    else:
      return False

  def login(self, ID_login, password_login):
    if(checkID(ID_login) == False):
      print("Username is incorrect")
      return False

    elif(checkPassword(password_login) == False):
      print("Incorrect password")
      return False

    else:
      return True

  def addValidUser(self):
    pass



# Admin class

class Admin:
  def __init__(self, ID, name):
    self.ID = ID
    self.name = name

  def addUser(self, name, email):
    newUser = ProspectiveUser(name, email)
    newUser.register()

  def deleteUser(self, User):
    UserList.remove(User)


input_journal = Journal(1) # Initialize input_journal variable which will be used to modify journals



def displayMenu():
  print("What would you like to do?")
  print("1: Create a new journal")
  print("2: View all journals")
  print("3: View all transactions in a journal")
  print("4: Add Transaction")
  print("5: Delete Journal")
  print("6: Delete Transaction")
  print("7: Edit Journal")
  print("8: Edit Transaction")
  print("9: View Report")
  print("Q: Quit")


# function to iterate over all journals and print transactions based on the month the journal starts
def checkMonth(month, journal_to_check, housingTotal, transportationTotal, diningTotal, clothingTotal, entertainmentTotal, groceriesTotal, travelTotal, otherTotal, revenueTotal):

  if(month in journal_to_check.startDate):
    for y in journal_to_check.transactionList:
      if(y.category == "Housing"):
        housingTotal+=int(y.amount) # increment total for housing. This way, if there are multiple entries in the same category, the total is computed

      elif(y.category == "Transportation"):
        transportationTotal+=int(y.amount)

      elif(y.category == "Dining"):
        diningTotal+=int(y.amount)

      elif(y.category == "Clothing"):
        clothingTotal+=int(y.amount)

      elif(y.category == "Entertainment"):
        entertainmentTotal+=int(y.amount)

      elif(y.category == "Groceries"):
        groceriesTotal+=int(y.amount)

      elif(y.category == "Travel"):
        travelTotal+=int(y.amount)

      elif(y.category == "Other"):
        otherTotal+=int(y.amount)

      elif(y.category == "Revenue"):
        revenueTotal+=int(y.amount)

    print("Transactions in " + month + ":")
    print()    

    print("Housing: " + str(housingTotal) + " AED")
    print("Transportation: " + str(transportationTotal) + " AED")
    print("Dining: " + str(diningTotal) + " AED")
    print("Clothing: " + str(clothingTotal) + " AED")
    print("Entertainment: " + str(entertainmentTotal) + " AED")
    print("Groceries: " + str(groceriesTotal) + " AED")
    print("Travel: " + str(travelTotal) + " AED")
    print("Other: " + str(otherTotal) + " AED")
    print("Revenue: " + str(revenueTotal) + " AED")
    print()
    print()


def graphReport():
  for x in journalList:

    housingTotal = 0
    transportationTotal = 0
    diningTotal = 0
    clothingTotal = 0
    entertainmentTotal = 0
    groceriesTotal = 0
    travelTotal = 0
    otherTotal = 0
    revenueTotal = 0

    checkMonth("January", x, housingTotal, transportationTotal, diningTotal, clothingTotal, entertainmentTotal, groceriesTotal, travelTotal, otherTotal, revenueTotal)
    checkMonth("February", x, housingTotal, transportationTotal, diningTotal, clothingTotal, entertainmentTotal, groceriesTotal, travelTotal, otherTotal, revenueTotal)
    checkMonth("March", x, housingTotal, transportationTotal, diningTotal, clothingTotal, entertainmentTotal, groceriesTotal, travelTotal, otherTotal, revenueTotal)
    checkMonth("April", x, housingTotal, transportationTotal, diningTotal, clothingTotal, entertainmentTotal, groceriesTotal, travelTotal, otherTotal, revenueTotal)
    checkMonth("May", x, housingTotal, transportationTotal, diningTotal, clothingTotal, entertainmentTotal, groceriesTotal, travelTotal, otherTotal, revenueTotal)
    checkMonth("June", x, housingTotal, transportationTotal, diningTotal, clothingTotal, entertainmentTotal, groceriesTotal, travelTotal, otherTotal, revenueTotal)
    checkMonth("July", x, housingTotal, transportationTotal, diningTotal, clothingTotal, entertainmentTotal, groceriesTotal, travelTotal, otherTotal, revenueTotal)
    checkMonth("August", x, housingTotal, transportationTotal, diningTotal, clothingTotal, entertainmentTotal, groceriesTotal, travelTotal, otherTotal, revenueTotal)
    checkMonth("September", x, housingTotal, transportationTotal, diningTotal, clothingTotal, entertainmentTotal, groceriesTotal, travelTotal, otherTotal, revenueTotal)
    checkMonth("October", x, housingTotal, transportationTotal, diningTotal, clothingTotal, entertainmentTotal, groceriesTotal, travelTotal, otherTotal, revenueTotal)
    checkMonth("November", x, housingTotal, transportationTotal, diningTotal, clothingTotal, entertainmentTotal, groceriesTotal, travelTotal, otherTotal, revenueTotal)
    checkMonth("December", x, housingTotal, transportationTotal, diningTotal, clothingTotal, entertainmentTotal, groceriesTotal, travelTotal, otherTotal, revenueTotal)

  mainMenu()




def tabulateJournals():
  journalTable = []

  # loop to populate the journal table which is a list of lists with details for each journal
  for i in range(len(journalList)):
    journalTable.append([])
    journalTable[i].append(journalList[i].ID)
    journalTable[i].append(journalList[i].name)
    journalTable[i].append(journalList[i].startDate)
    journalTable[i].append(journalList[i].endDate)

  print(tabulate(journalTable, headers=["ID","Name", "Start Date", "End Date"],tablefmt='psql'))
  print()



def tabulateTransactions(j2):
  transactionTable = []

  # loop to populate the transaction table which is a list of lists with details for each transaction in the journal j2
  for i in range(len(j2.transactionList)):
    transactionTable.append([])
    transactionTable[i].append(j2.transactionList[i].ID)
    transactionTable[i].append(j2.transactionList[i].category)
    transactionTable[i].append(j2.transactionList[i].amount)

  print(tabulate(transactionTable, headers=["ID","Category", "Amount"],tablefmt='psql')) # using tabulate module to display the transaction table
  print()




def createTransactionMain(j1): #j1 is the journal that the transaction will be saved in
  checker = False # variable initialized to False that only becomes True if the input is valid
  while(checker==False):
    print("Is the transaction expenditure or revenue?")
    print("1: Expenditure")
    print("2: Revenue")
    print()
    option_type = input("Option selected: ")
    print()

    if(option_type == "1"):
      checker = True
      input_transaction_is_expenditure = True # The transaction is either expenditure or revenue and so if one is true, the other is set to false
      input_transaction_is_revenue = False

      print("Select the category the transaction belongs to")
      print("1: Housing")
      print("2: Transportation")
      print("3: Dining")
      print("4: Clothing")
      print("5: Entertainment")
      print("6: Groceries")
      print("7: Travel")
      print("8: Other")
      print()
      option_category = input("Option selected: ")
      print()

      if(option_category == "1"):
        input_transaction_category = "Housing"

      elif(option_category == "2"):
        input_transaction_category = "Transportation"

      elif(option_category == "3"):
        input_transaction_category = "Dining"

      elif(option_category == "4"):
        input_transaction_category = "Clothing"

      elif(option_category == "5"):
        input_transaction_category = "Entertainment"

      elif(option_category == "6"):
        input_transaction_category = "Groceries"

      elif(option_category == "7"):
        input_transaction_category = "Travel"

      elif(option_category == "8"):
        input_transaction_category = "Other"


    elif(option_type == "2"):
      checker = True
      input_transaction_is_expenditure = False
      input_transaction_is_revenue = True
      input_transaction_category = "Revenue"

    else:
      print("Invalid input. Please select an option from the menu")

  if(checker==True):
    input_transaction_amount = input("Please enter the amount: ")
    print()

    input_transaction = Transaction(1, input_transaction_category, input_transaction_is_expenditure, input_transaction_is_revenue, input_transaction_amount)


    for x in journalList:
      if j1.name == x.name:
        input_transaction.ID = x.transaction_ID_counter # make sure all IDs are unique by referring to the ID counter we defined in Journal class
        x.increaseTranscationID()
        x.transactionList.append(copy.deepcopy(input_transaction))
        break

    print("Success! What would you like to do?")
    print("1: Create another transaction")
    print("2: Return to main menu")
    print()
    option_transaction = input("Option selected: ")
    print()

    if option_transaction == "1":
      createTransactionMain(j1)

    if(option_transaction == "2"):
      print("Returning to main menu")
      print()
      mainMenu()





def createJournalMain():


  input_journal_name = input("Please enter the journal name: ")
  input_journal.setName(input_journal_name)

  print("Please enter the start date")

  while(True):
    input_journal_start_day = input("Day: ")
    if(input_journal_start_day.isdigit()): # day can only be a number
      break
    else:
      print("Invalid format. Please enter a number")

  while(True):
    input_journal_start_month = input("Month: ")
    if(input_journal_start_month in list_of_months): # checks if input is in the list of months defined earlier
      break
    else:
      print("Invalid format. Please enter a month")

  while(True):
    input_journal_start_year = input("Year: ")
    if(input_journal_start_year.isdigit()):
      break
    else:
      print("Invalid format. Please enter a number")

  input_journal_start_date = input_journal_start_day + " " + input_journal_start_month + " " + input_journal_start_year
  input_journal.setStartDate(input_journal_start_date)

  print("Please enter the end date")

  while(True):
    input_journal_end_day = input("Day: ")
    if(input_journal_end_day.isdigit()):
      break
    else:
      print("Invalid format. Please enter a number")

  while(True):
    input_journal_end_month = input("Month: ")
    if(input_journal_end_month in list_of_months):
      break
    else:
      print("Invalid format. Please enter a month")

  while(True):
    input_journal_end_year = input("Year: ")
    if(input_journal_end_year.isdigit()):
      break
    else:
      print("Invalid format. Please enter a number")

  input_journal_end_date = input_journal_end_day + " " + input_journal_end_month + " " + input_journal_end_year
  input_journal.setEndDate(input_journal_end_date)

  input_journal_description = input("Please enter a brief description of the journal: ")
  input_journal.setDescription(input_journal_description)
  print()

  journalList.append(copy.deepcopy(input_journal)) # appends a deep copy of the newly created journal to the journalList which acts as our server during runtime

  checker = False

  while(checker==False):

    print("Success! Would you like to create a new transaction?")
    print("1: Yes")
    print("2: No")
    print()
    option = input("Option selected: ")
    print()

    if(option == "1"):
      checker = True
      createTransactionMain(input_journal)


    elif(option == "2"):
      checker = True
      input_journal.resetAttributes()
      mainMenu()

    else:
      print("Invalid input. Please select an option from the menu")




def editJournalMain():
  edit_journal_success = False
  journal_to_edit = input("Please enter the name of the journal you would like to edit: ")
  print()
  for x in journalList:
    if(x.name == journal_to_edit):
      edit_journal_success = True
      print("What would you like to edit?")
      print("1: Name")
      print("2: Start Date")
      print("3: End Date")
      print("4: Description")
      print()
      option_edit = input("Option selected: ")
      print()
      new_value = input("Enter the new value: ")
      print()
    

      if(option_edit == "1"):
        x.name = new_value

      elif(option_edit == "2"):
        x.startDate = new_value

      elif(option_edit == "3"):
        x.endDate = new_value

      elif(option_edit == "4"):
        x.description = new_value

      else:
        print("Invalid input. Please select an option from the menu.")
        print()

  if(edit_journal_success==False):
    print("Invalid input. The journal doesn't exist.")
    print()

  if(edit_journal_success==True):
    print("Success!")
    print()

  mainMenu()



def editTransactionMain():
  find_journal = False
  transaction_location = input("Please enter the name of the journal that the transaction to be edited is in: ")
  print()
  for x in journalList:
    if(x.name == transaction_location):
      find_journal = True
      print()
      print("Transactions stored in " + x.name + ":")
      print()

      tabulateTransactions(x) # display transactions so user can know which the details of each transaction
      edit_transaction_success = False
      transaction_to_edit = input("Please enter the ID of the transaction to be edited: ")
      print()
      for y in x.transactionList:
        if(str(y.ID) == transaction_to_edit):
          edit_transaction_success = True
          print("What would you like to edit?")
          print("1: Category")
          print("2: Amount")
          print()
          option_edit = input("Option selected: ")
          print()

          if(option_edit == "1"):
            print("What would you like to change the category to?")
            print("1: Housing")
            print("2: Transportation")
            print("3: Dining")
            print("4: Clothing")
            print("5: Entertainment")
            print("6: Groceries")
            print("7: Travel")
            print("8: Other")
            print("9: Revenue")
            print()
            new_category = input("Option selected: ")
            print()

            if(new_category == "1"):
              y.category = "Housing"
              y.isExpenditure = True
              y.isRevenue = False

            elif(new_category == "2"):
              y.category = "Transportation"
              y.isExpenditure = True
              y.isRevenue = False

            elif(new_category == "3"):
              y.category = "Dining"
              y.isExpenditure = True
              y.isRevenue = False

            elif(new_category == "4"):
              y.category = "Clothing"
              y.isExpenditure = True
              y.isRevenue = False

            elif(new_category == "5"):
              y.category = "Entertainment"
              y.isExpenditure = True
              y.isRevenue = False

            elif(new_category == "6"):
              y.category = "Groceries"
              y.isExpenditure = True
              y.isRevenue = False

            elif(new_category == "7"):
              y.category = "Travel"
              y.isExpenditure = True
              y.isRevenue = False

            elif(new_category == "8"):
              y.category = "Other"
              y.isExpenditure = True
              y.isRevenue = False

            elif(new_category == "9"):
              y.category = "Revenue"
              y.isExpenditure = False
              y.isRevenue = True

            else:
              print("Invalid input. Please select an option from the menu.")
              print()

          elif(option_edit == "2"):
            new_amount = input("Please enter the new amount: ")
            print()
            if(new_amount.isdigit()):
              y.amount = new_amount
            else:
              print("Invalid input. Please enter a number.")
              print()

          else:
            print("Invalid input. Please select an option from the menu.")
            print()

      if(edit_transaction_success==False):
        print("Invalid input. The transaction doesn't exist.")
        print()

  if(find_journal==False):
    print("Invalid input. The journal doesn't exist.")
    print()

  if(find_journal==True):
    print("Success!")
    print()


  mainMenu()



# MAIN

# used copy to make deep copy
import os
import csv

import copy


journals_filesize = os.path.getsize("journals.txt")

# if there are no journals, there is no need to initialize the journal list
if journals_filesize == 0:
    print()

else:

  # initialize journalList with journals and transactions from the last saved state of the system
  last_ID=0
  print()

  # open the file containing the list of journals, parse the input, create journals corresponding to the details and append them to our makeshift server, the journalList
  with open("journals.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
      last_ID = row[0]
      journalList.append(Journal(row[0], row[1], row[2], row[3], row[4]))

  input_journal.ID = int(last_ID) # set the ID of the input_journal to the last ID saved in the file so that when a new journal is created, the ID is incremented and no duplicate IDs exist


  # initialize each transaction list
  last_ID_transaction=0
  for x in journalList:
    with open("journal" + str(x.ID) + ".txt") as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      for row in csv_reader:
        last_ID_transaction = row[0]
        x.transactionList.append(Transaction(row[0], row[1], row[2], row[3], row[4]))
      x.transaction_ID_counter = int(last_ID_transaction) + 1
      last_ID_transaction = 0





print("Welcome to the Financial Tracker")
print()

def mainMenu():
  displayMenu()
  print()
  choice = input("Option selected: ")
  print()

  if choice == "1":
    # Create Journal

    if ((input_journal.ID == 1) and (len(journalList)!=0)):
      input_journal.resetAttributes()
      input_journal.ID+=1

    elif (input_journal.ID>1):
      input_journal.resetAttributes()
      input_journal.ID+=1


    createJournalMain()

  elif choice == "2":
    # View all journals

    tabulateJournals()

    mainMenu()

  elif choice == "Q":
    # Quit

    # save all the changes made in our makeshift server and store in the files
    f = open("journals.txt", "w") # open in write mode to overwrite existing content that most likely changed during runtime
    for x in journalList:
      f.write(str(x.ID) + "," + str(x.name) + "," + str(x.startDate) + "," + str(x.endDate) + "," + str(x.description) + "\n")

      g = open("journal" + str(x.ID) + ".txt", "w")

      for y in x.transactionList:
        g.write(str(y.ID) + "," + str(y.category) + "," + str(y.isExpenditure) + "," + str(y.isRevenue) + "," + str(y.amount) + "\n")

    f.close()
    g.close()
    print("Goodbye :)")

  elif choice == "3":
    # View all transactions in a journal

    journal_exists = False
    tabulateJournals()
    journal_is = input("Please enter the name of the journal: ")
    print()
    for x in journalList:
      if(x.name == journal_is):
        journal_exists = True
        print()
        print("Transactions stored in " + x.name + ":")
        print()

        tabulateTransactions(x)

    if(journal_exists==False):
      print("Invalid input. The journal doesn't exist.")
      print()

    mainMenu()


  elif choice == "4":
    # Add Transaction

    add_transaction_success = False
    tabulateJournals()
    journal_search = input("Great! Please enter the name of the journal that the transaction will be stored in: ")
    print()
    for x in journalList:
      if(x.name == journal_search):
        add_transaction_success=True
        createTransactionMain(x)

    if(add_transaction_success==False):
      print("Invalid input. The journal doesn't exist.")
      print()
      mainMenu()

  elif choice == "5":
    # Delete Journal

    delete_journal_success = False
    tabulateJournals()
    to_delete = input("Please enter the name of the journal you want to delete: ")
    print()
    for x in journalList:
      if(x.name == to_delete):
        delete_journal_success = True
        journalList.remove(x)
        print("Success!")
        print()

    if(delete_journal_success==False):
      print("Invalid input. The journal doesn't exist.")
      print()

    mainMenu()


  elif choice == "6":
    # Delete Transaction

    journal_select = False
    tabulateJournals()
    to_delete_from = input("Please enter the name of the journal you want to delete the transaction from: ")
    print()
    for x in journalList:
      if(x.name == to_delete_from):
        journal_select = True
        print()
        print("Transactions stored in " + x.name + ":")
        print()
        tabulateTransactions(x)

        delete_transaction_success = False
        to_delete_transaction = input("Please enter the ID of the transaction you want to delete: ")
        print()
        for y in x.transactionList:
          if(str(y.ID) == to_delete_transaction):
            delete_transaction_success = True
            x.transactionList.remove(y)

        if(delete_transaction_success==False):
          print("Invalid input. The transaction does not exist.")
          print()

    if(journal_select==False):
      print("Invalid input. The journal doesn't exist.")
      print()

    mainMenu()


  elif choice == "7":
    # Edit Journal

    tabulateJournals()
    editJournalMain()

  elif choice == "8":
    # Edit Transaction

    tabulateJournals()
    editTransactionMain()

  elif choice == "9":
    # View Report

    graphReport()
          
  else:
    print("Invalid input. Please select an option from the menu.")
    print()
    mainMenu()

mainMenu()