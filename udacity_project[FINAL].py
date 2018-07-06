easy_question = ["_1_ khalifa is the tallest building in the world","The captial of australia in 2017 is _2_",
                 "In total there are _3_ Ocean","India got their independence in _4_"]
easyq_ans     = ["burgh","sydeny","7","1957"]

medium_question = ["Entomology is the science that studies _1_","Hitler party which came into power in 1933  is know as _2_ party."
                   ,"In _3_, Germany declared  war on Russia and France ","India has largest deposits of _4_ in the world."]
mediumq_ans     = ["insects","nazi","1914","mica"]

hard_question = ["A total of _1_ lok Sabha seats belong to Rajasthan",
                "India's first atomic reactior was _2_ ",
                 "the total number of red blood cell in a normal human body is _3_ trillion",
                 "Bone marrow produces _4_ million red blood cells every second"]
hardq_ans     = ["25","aspara","30","2"]



def intro():
#Ask the name 
    name=input("Hello,what is your name?")
#Greets the player  and tell how many queston are the in the quiz
    print("Hello "+ name)
    print("Welcome To my Quiz")
    print("You will be asked 4 general knowledge questions")
    print("where you will need to fill the blanks ")
   
def endquiz():
    #Congrats the player for completing the quiz
    print('Congratulations!! you have succesfully completed the quiz')
    

 #This code ask the player what difficulty they want to choose   
def ask_level_diff():
    level = input("Now please Type a number between 1-3 to select your level (1 being the easiest and 3 being the hardest)   ")
    if level == "1":
        print("You have selected easy level ")
        easy_diff()
    elif level == "2":
        print("you have selected medium difficulty")
        medium_diff()
    elif level =="3":
        print("You have selected hard difficulty")
        hard_diff()
        
def anscheck(quiz_difficulty,ans,ans_by_user):
#Says the max amount of the attempt given to the user
    attempt = 1 
    max_attempt =4
#Use of the while loop to add attempt number  for every time the user getthe ans wrong  
    while ans_by_user!= ans:
        attempt=attempt+1
        ans_by_user=input("Wrong answer try again.")
#       if function to restart the quiz if users uses all of his or her attempts 
        if max_attempt == attempt:
            print('You got the question wrong the quiz will restar')
            quiz_difficulty
            

#user ans Takes the answer from  the user

            
def easy_diff():
    print("Here is your first question please do not right answer in caps  and when asked number of   something please write the integer value")
    print(easy_question[0])
    user_ans1=input("what is _1_ ")
    anscheck(easy_diff,easyq_ans[0],user_ans1)
                        
    print(easy_question[1])
    user_ans2=input('What is_2_?')
    anscheck(easy_diff,easyq_ans[1],user_ans2)

    print(easy_question[2])
    user_ans3=input('what is _3_')
    anscheck(easy_diff,easyq_ans[2],user_ans3)


    print(easy_question[3])
    user_ans4=input('what is _4_')
    anscheck(easy_diff,easyq_ans[3],user_ans4)

    print(endquiz())

def medium_diff():
    print('Here is your first question please do not right answer in caps  and when asked number of something please write the integer value')
    print(medium_question[0])
    user_ans1=input('what is _1_?')
    anscheck(medium_diff,mediumq_ans[0],user_ans1)

    print(medium_question[1])
    user_ans2=input('What is _2_')
    anscheck(medium_diff,mediumq_ans[1],user_ans2)

    print(medium_question[2])
    user_ans3=input('What is _3_?')
    anscheck(medium_diff,mediumq_ans[2],user_ans3)

    print(medium_question[3])
    user_ans4=input('What is _4_?')
    anscheck(medium_diff,mediumq_ans[3],user_ans4)
    
    print(endquiz())
     
def hard_diff():
    print('Here is your first question please do not right answer in caps  and when asked number of something please write the integer value')
    print(hard_question[0])
    user_ans1=input('what is _1_?')
    anscheck(hard_diff,hardq_ans[0],user_ans1)

    print(hard_question[1])
    user_ans2=input('What is _2_')
    anscheck(hard_diff,hardq_ans[1],user_ans2)

    print(hard_question[2])
    user_ans3=input('What is _3_')
    anscheck(hard_diff,hardq_ans[2],user_ans3)

    print(hard_question[3])
    user_ans4=input('What is _4_')
    anscheck(hard_diff,hardq_ans[3],user_ans4)
            
    print(endquiz())


intro()
ask_level_diff()
