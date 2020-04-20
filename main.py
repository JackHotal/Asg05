import pickle
from coffee import Coffee
import sys

mainmenu = "\nMain Menu\nA)dd calculations to an existing file\nL)oad a file and view results\nP)rint current results\nR)eset and perform new EOQ calculations\nS)ave current calculations to a file\nQ)uit:\n"
question = "\nEnter q to quit and display the results, or enter the name of a coffee\n"
nofile = "\nThe file doesn't exists\n"
nocalc = "\nThere are no calculations to display\nLoad a file or perform new calculations\n"


def validate(vString):
    while True: 
        try: 
            if int(float(vString)) >= 0:
                vString = int(float(vString))
                break
            else: 
                vString = input("Negative values are not accepted. Please provide a positive value:\n")
        except ValueError:
            vString = input("Non-numeric values are not accepted. Please provide a numeric value:\n")
    return vString


def getParam():
    d = float(validate(input("How many pounds of coffee per year do you need to stock (D)?\n")))
    c = float(validate(input("What is your unit cost (C)?\n")))
    return d, c
        
        
def printResults(dataList):
    totalQ = 0
    print('**********\n\nThe Results of EOQ Calculation\n\n**********\nBrand\t\tC($)\t\tDemand\t\tQ(lbs)\t\tTAC($)\t\tT (weeks)')
    for coffee in dataList:
        #print("{0}\t\t{1:.2f}\t\t\t{2:.2f}\t\t\t{3:.2f}".format((B.d),(B.c),(B.Q()),(B.T())))
        print(coffee.__str__())
        totalQ += coffee.Q()
    print("\nIf you purchase all of the coffee, you will need space to hold {0:.2f} lbs. of cofffee.".format(totalQ))
    print("\n")

def askData(dataList):    
    print(question)
    coffeeName = input()
    while (coffeeName.lower() !="q"):
        d, c = getParam()
        coffee = Coffee(coffeeName, d, c)
        dataList.append(coffee)
       # q, tac, t = coffeecalcEOQ(d, c, k, h)
       # dataList.append([coffeeName, d, c, k, h, q, tac, t]) 
        print(question)
        coffeeName = input()        
    printResults(dataList)    
      
def load_data(filename='coffeeObjects'):
    #dataList = []
    #with open (filename, 'r') as fp:
        #dataList = json.load(fp)    
    coffeeObjects = pickle.load(open(filename, 'rb'))
    return coffeeObjects
        
def store_data(dataList, filename='coffeeObjects'):
    #with open(filename, 'w') as fp:
        #json.dump(dataList, fp)
    pickle.dump(dataList, open(filename, 'wb'))
        
        
#def open_database(filename, db):
    #""" Read account information from a given text file and store it
    #in the given list. """
    #with open(filename) as f: # Open file to read
        #for line in f:
            #line.strip()
            #number, name, balance = line.split(",")     #This is another clever way to write things into a list
            #db.append(BankAccount(int(number), str(name), float(balance))) #This reads the text but adds objects to the db by calling BankAccount constructor. We do not return db as db is a reference type. But we could also do that. 
                
def main():
    print("Welcome to the EOQ Calculator prepared by Jack Hotaling\n\n")
    #coffeeList = []
    #try:
        #open_database('coffeeList.txt', coffeeList)
        #printObjects(coffeeList)
    #except Exception:   
        #print('Error in coffee database')    
        
    done = False
    while not done:
        cmd = input(mainmenu)
        if cmd.lower() == 'r':
            dataList = []
            askData(dataList)
        elif cmd.lower() == 'a':
            try:
                askData(dataList)
            except UnboundLocalError: 
                print(nocalc)
        elif cmd.lower() == 's':
            try:
                filename= input('Enter file name: ')
                if filename: store_data(dataList, filename)
                else: print("Please enter a file name")
                #store_data(dataList)               
            except UnboundLocalError: 
                print(nocalc)
                input("Hit enter to go to the main menu")
            except: pass
        elif cmd.lower() == 'p':
            try:
                printResults(dataList)
            except UnboundLocalError: 
                print(nocalc)
                input("Hit enter to go to the main menu")
            except: pass
        elif cmd.lower() == 'l':
            while True:  
                try:
                    filename = input('Enter a file name: ')
                    if filename: 
                        dataList = load_data(filename)
                        printResults(dataList)
                        break
                    else:
                        print("Please provide a valid filename") 
                except FileNotFoundError:
                    print("Please provide a valid filename (not found)")    
        elif cmd.lower() == 'q':
            done = True

if __name__ == '__main__':
    main()
