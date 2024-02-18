# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.  
  
# Student ID: 20220218 | W1998814          # Date:  2023/04/20

# variables
credit_range = [0,20,40,60,80,100,120]
credit_pass=0
credit_defer=0
credit_fail=0

ans = 0
progress_count = 0
module_trailer_count = 0
module_retriever_count = 0
exclude_count = 0
total_outcomes = 0
file_object = 0

#lists
ProgressList = []
MTrailerList = []
RetrieverList = []
ExcludedList = []
student_ids = []
user_student_id = ''

#Dictionary
dictionary_list = {}



def dictionary():  # This method is used to print the data sets in the dictionary, using a for loop.
    print('')
    print("part 4: \n")
    print("-"*70)
    print(" "*30,"Dictionary")
    for x, y in dictionary_list.items():
        print(x, ":", y)
    print('')
    print("-"*70)

def grading():  # This function hold the grading system

    global credit_defer,total,credit_fail,credit_pass, ProgressList, MTrailerList, RetrieverList,ExcludedList
    if credit_pass == 120:
        print("Progress\n") 
        dictionary_list[user_student_id]=f"Progress - {credit_pass,credit_defer,credit_fail}"
        ProgressList.append([credit_pass, credit_defer, credit_fail])

    elif credit_pass == 100:
        print("Progress (module trailer)\n")
        dictionary_list[user_student_id] = f"Module trailer - {credit_pass, credit_defer, credit_fail}"
        MTrailerList.append([credit_pass, credit_defer, credit_fail])
    
    elif credit_pass == 80:
        print("Module retriever\n")
        dictionary_list[user_student_id] = f"Module retriever - {credit_pass, credit_defer, credit_fail}"
        RetrieverList.append([credit_pass, credit_defer, credit_fail])
        
    elif credit_pass == 60:
        print("Module retriever\n")
        dictionary_list[user_student_id] = f"Module retriever - {credit_pass, credit_defer, credit_fail}"
        RetrieverList.append([credit_pass, credit_defer, credit_fail])
        
    elif credit_pass == 40 and credit_fail != 80:
        print("Module retriever\n")
        dictionary_list[user_student_id] = f"Module retriever - {credit_pass, credit_defer, credit_fail}"
        RetrieverList.append([credit_pass, credit_defer, credit_fail])
        
    elif credit_pass == 40 and credit_fail == 80:
        print("Exclude\n")
        dictionary_list[user_student_id] = f"Exclude - {credit_pass, credit_defer, credit_fail}"
        ExcludedList.append([credit_pass, credit_defer, credit_fail])
        
    elif credit_pass == 20 and credit_fail <= 60:
        print("Module retriever\n")
        dictionary_list[user_student_id] = f"Module retriever - {credit_pass, credit_defer, credit_fail}"
        RetrieverList.append([credit_pass, credit_defer, credit_fail])
        
    elif credit_pass == 20 and credit_fail >= 80:
        print("Exclude\n")
        dictionary_list[user_student_id] = f"Exclude - {credit_pass, credit_defer, credit_fail}"
        ExcludedList.append([credit_pass, credit_defer, credit_fail])
        
    elif credit_pass == 0 and credit_fail <= 60:
        print("Module retriever\n")
        dictionary_list[user_student_id] = f"Module retriever - {credit_pass, credit_defer, credit_fail}"
        RetrieverList.append([credit_pass, credit_defer, credit_fail])
        
    elif credit_pass == 0 and credit_fail >= 80:
        print("Exclude\n")
        dictionary_list[user_student_id] = f"Exclude - {credit_pass, credit_defer, credit_fail}"
        ExcludedList.append([credit_pass, credit_defer, credit_fail])


def asking_inputs(): # This function ask the Student ID's and pass marks from the user

    global credit_defer,credit_fail,credit_pass,total,student_ids, user_student_id
    while True:
        while True:  #Input the student ID 
            try:
                user_student_id = str(input("Please enter your student ID : "))
                student_ids.append(user_student_id)
                check_clone_id = student_ids.count(user_student_id)
                if check_clone_id > 1:
                    print("You have already entered this student id, Please try a different ID!")
                    continue
                else:
                    break
            except ValueError:
                continue

        while True:  # Input the credit pass 
            try:
                #print("")
                credit_pass = int(input("Please enter your credits at pass: "))
                if credit_pass not in credit_range:
                    print("Out of range.")
                    continue
                else:
                    break
            except ValueError:
                print("Integer required")

        while True:  # Input the defer credit 
            try:    
                credit_defer = int(input("Please enter your credit at defer: "))
                if credit_defer not in credit_range:
                    print("Out of range.")
                    continue
                else:
                    break
            except ValueError:
                print("Integer required")

        while True:   # Input the fail credit 
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
            print("Incorrect Total, Try Again!")
            continue
        

def ending():    #This function controls wether the user wants to continue the program or stop the program and print the dictionary part 
    while(True):
            print("")
            print("Would you like to enter another set of data? ")
            ans=str(input("Enter 'y' for yes or 'q' to quit and view results:"))
            if ans =="y":
                asking_inputs()
                continue
            
            elif ans == "q":
                #histogram()
                dictionary()
                break
asking_inputs()
ending()

# References
# 1.Lecture materials
# 2.w3schools Python: https://www.w3schools.com/python/
