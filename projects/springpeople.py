from sys import argv
from os.path import exists
import linecache

prefix = raw_input("Please provide an input prefix file:")
#script, prefix = argv

#Reading the original file
originalfile = open(prefix)
txt = originalfile.read()

oldfilename = prefix+".old.txt"
newfilename = prefix+".new.txt"

#Creating the old and new master files
try:
    oldmasterfile = open(oldfilename, 'w')
    newmasterfile = open(newfilename, 'w')

except:
    print "Error opening one of the files", type(e)

#Returns the account details of line from master file
def get_number(one_line):
    line = txt.split('\n')[one_line-1]
    #line = linecache.getline(txt, one_line)
    number = line.split(' ')[0]
    return number

def get_balance(one_line):
    line = txt.split('\n')[one_line-1]
    #line = linecache.getline(txt, one_line)
    balance = line.split(' ')[1]
    return balance

def get_accountholder(one_line):
    line = txt.split('\n')[one_line-1]
    #line = linecache.getline(txt, one_line)
    accountholder = line.split(' ')[2]
    return accountholder

#Display customer information
line = int(raw_input ("Enter line numer: "))

print "Account number of the customer: %s" %get_number(line)
print "Account holder: %s" %get_accountholder(line)
print "Balance available for the customer: %s" %get_balance(line)

#Prompts for transactions
transaction = raw_input(
"""
d - deposit
w - withdrawal
c - close
a - advance to next customer
Please enter a transaction code from above:"""
)

if transaction == "d":
    deposit = int(raw_input("Enter the amount to be deposited:"))

if transaction == "w":
    withdraw = int(raw_input("Enter the amount of withdrawal:"))

if transaction == "c":
    close = str(raw_input("Are you sure?"))

#Completing the transaction

if transaction == "d":
    newbalance = int(get_balance(line)) + deposit

if transaction == "w":
    newbalance = int(get_balance(line)) - withdraw

if transaction == "a":
    newbalance = int(get_balance(line))

newline = get_number(line) + " " + str(newbalance) + " " + get_accountholder(line)
#Writing the file back to the new master file
newmasterfile.write(newline)
newmasterfile.close()
