# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.  
  
# Student ID: 20220218 | W1998814          # Date:  2023/04/20

# variables
credit_range = [0,20,40,60,80,100,120]
credit_pass=0
credit_defer=0
credit_fail=0
credit_total=0
ans = 0

file_object = 0
#lists
ProgressList = []
MTrailerList = []
RetrieverList = []

ExcludedList = []
i = []

ans1 = []
ans2 = []
ans3 = []
ans4  = []

#program

def histogram(): # This function is for the histogram (Part 2) and List [Extension] Part 3.
    global ProgressList, MTrailerList, RetrieverList,ExcludedList, i

    #Histogram , List (extension) 
    print("-"*70)

    print("Histogram")
    print("Progress ",len(ProgressList),"  : ",len(ProgressList)*"*")
    print("Trailer  ",len(MTrailerList),"  : ",len(MTrailerList)*"*")
    print("Retriever",len(RetrieverList),"  : ",len(RetrieverList)*"*")
    print("Excluded ",len(ExcludedList),"  : ",len(ExcludedList)*"*")
    print("")
    print(len(ProgressList) + len(MTrailerList) + len(RetrieverList) + len(ExcludedList), "outcome in total")
    print("-"*70)

    #Adding the part 2
    print("Part 2: \n")
    if len(ProgressList) != 0:
        print("Progress - ", *ProgressList)
    if len(MTrailerList) != 0:
        print("Progress (module trailer) - ", *MTrailerList)
    if len(RetrieverList) != 0:
        print("Module retriever - ",*RetrieverList)
    if len(ExcludedList) != 0:
        print("Exclude - ",*ExcludedList)
    print("-"*70)



    


def text_file():  # This function is for generate the text file to the Histogram.
    global  ans1,ans2,ans3,ans4, ProgressList,MTrailerList,RetrieverList,ExcludedList, file_object
    file_object = open("progression_data.txt","w")
    if len(ProgressList) != 0:
        file_object.write("Progress - "+str(ProgressList)+'\n')

    if len(MTrailerList) != 0:
        file_object.write('Progress (module trailer) - '+str(MTrailerList)+'\n')

    if len(RetrieverList) != 0:
        file_object.write('Module retriever - '+str(RetrieverList)+'\n')

    if len(ExcludedList) != 0:
        file_object.write('Excluded - '+str(ExcludedList)+'\n')
    file_object.close()


    file_object = open("progression_data.txt","r") 
    print(file_object.read())

    
def grading():  # This function hold the grading system
    
    global credit_defer,total,credit_fail,credit_pass, ProgressList, MTrailerList, RetrieverList,ExcludedList
    if credit_pass == 120:
        print("Progress\n") 
        ProgressList.append([credit_pass,credit_defer,credit_fail])
        
    elif credit_pass == 100:
        print("Progress (module trailer)\n")
        MTrailerList.append([credit_pass,credit_defer,credit_fail])
    
    elif credit_pass == 80:
        print("Module retriever\n")
        RetrieverList.append([credit_pass,credit_defer,credit_fail])
        
    elif credit_pass == 60:
        print("Module retriever\n")
        RetrieverList.append([credit_pass,credit_defer,credit_fail])
        
    elif credit_pass == 40 and credit_fail != 80:
        print("Module retriever\n")
        RetrieverList.append([credit_pass,credit_defer,credit_fail])
        
    elif credit_pass == 40 and credit_fail == 80:
        print("Exclude\n")
        ExcludedList.append([credit_pass,credit_defer,credit_fail])
        
    elif credit_pass == 20 and credit_fail <= 60:
        print("Module retriever\n")
        RetrieverList.append([credit_pass,credit_defer,credit_fail])
        
    elif credit_pass == 20 and credit_fail >= 80:
        print("Exclude\n")
        ExcludedList.append([credit_pass,credit_defer,credit_fail])
        
    elif credit_pass == 0 and credit_fail <= 60:
        print("Module retriever\n")
        RetrieverList.append([credit_pass,credit_defer,credit_fail])
        
    elif credit_pass == 0 and credit_fail >= 80:
        print("Exclude\n")
        ExcludedList.append([credit_pass,credit_defer,credit_fail])
    
        

def asking_inputs():  # This function ask the Student ID's and pass marks from the user

    global credit_defer, credit_fail,credit_pass,total
    while True:
        while True:     # Input the credit pass
            try:
                print("")
                credit_pass = int(input("Please enter your credits at pass: "))
                if credit_pass not in credit_range:
                    print("Out of range.")
                    continue
                else:
                    break
            except ValueError:
                print("Integer required")

        while True:     # Input the defer credit 
            try:    
                credit_defer = int(input("Please enter your credit at defer: "))
                if credit_defer not in credit_range:
                    print("Out of range.")
                    continue
                else:
                    break
            except ValueError:
                print("Integer required")

        while True:     # Input the fail credit 
            try:
                credit_fail = int(input("Please enter your credit at fail: "))
                if credit_fail not in credit_range:
                    print("Out of range.")
                    continue
                else:
                    break
            except ValueError:
                print("Integer required")

        total = credit_pass + credit_defer + credit_fail

        if total == 120:
            grading()
            break
        else:
            print("Total Incorrect ")
            continue
        

def ending():    #This function controls wether the user wants to continue the program or stop the program and print the dictionary part 
    while True:
        try:
            print("")
            print("Would you like to enter another set of data? ")
            ans=str(input("Enter 'y' for yes or 'q' to quit and view results:"))
            if ans =="y":
                asking_inputs()
                continue
            
            elif ans == "q":
                histogram()
                break
            else:
                print("Invalid Input")
                continue
        except:
            print("Inalid Input.")
            continue
asking_inputs()
ending()

# References
# 1.Lecture materials
# 2.w3schools Python: https://www.w3schools.com/python/
