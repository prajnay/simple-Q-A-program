easy_question = ["_1_ khalifa is the tallest building in the world","The captial of australia in 2017 is _2_",
                 "In total there are _3_ Ocean","India got their independence in _4_"]
easyq_ans     = ["burgh","sydeny","7","1957"]

medium_question = ["Entomology is the science that studies _1_","Hitler party which came into power in 1933  is know as _2_ party."
                   ,"In _3_, Germany declared  war on Russia and France ","India has largest deposits of _4_ in the world."]
medium_ans     = ["insects","nazi","1914","mica"]

hard_question = ["A total of _1_ lok Sabha seats belong to Rajasthan",
                "India's first atomic reactior was _2_ ",
                 "the total number of red blood cell in a normal human body is _3_ trillion",
                 "Bone marrow produces _4_ million red blood cells every second"]
hard_ans     = ["25","aspara","30","2"]


# takes  the name and explain quiz#
def intro():
    name=input("Hello,what is your name?")
    print("Hello "+ name)
    print("Welcome To my Quiz")
    print("You will be asked 4 general knowledge questions")
    print("where you will need to fill the blanks ")
   
def endquiz():
    print('Congratulations!! you have succesfully completed the quiz')
    

 #Ask the questions and limits the number of the attempt#   
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
        


        
def easy_diff():
    print("Here is your first question please do not right answer in caps  and when asked number of   something please write the integer value")
    print(easy_question[0])
    user_ans1=input("what is _1_ ")
    attempt=1
    max_attempt=4
    while user_ans1 != easyq_ans[0]:
        attempt= attempt+1
        user_ans1=input('Wrong answer try again ')
        if max_attempt == attempt:
            print("you got the question wrong the quiz will restart")
            easy_diff()
                        
                    

    print(easy_question[1])
    user_ans2=input('What is_2_?')
    attempt1=1
    max_attempt1=4
    while user_ans2 != easyq_ans[1]:
        attempt1= attempt1+1
        user_ans2=input('Wrong answer try again ')
        if max_attempt1 == attempt1:
            print("you got the question wrong the quiz will restart")
            easy_diff()

   
        

    print(easy_question[2])
    user_ans3=input('what is _3_')
    attempt2=1
    max_attempt2=4
    while user_ans3 != easyq_ans[2]:
        attempt2= attempt2+1
        user_ans3=input('Wrong answer try again ')
        if max_attempt2 == attempt2:
            print("you got the question wrong the quiz will restart")
            easy_diff()


    print(easy_question[3])
    attempt3=1
    max_attempt3=4
    user_ans4=input('what is _4_')
    while user_ans4 != easyq_ans[3]:
        attempt3= attempt3+1
        user_ans4=input('Wrong answer try again ')
        if max_attempt3 == attempt3:
            print("you got the question wrong the quiz will restart")
            easy_diff()

    print(endquiz())

def medium_diff():
    print('Here is your first question please do not right answer in caps  and when asked number of something please write the integer value')
    print(medium_question[0])
    user_ans1=input('what is _1_?')
    attempt=1
    max_attempt=4
    while user_ans1 != medium_ans[0]:
        attempt= attempt+1
        user_ans1=input('Wrong answer try again ')
        if max_attempt == attempt:
            print("you got the question wrong the quiz will restart")
            medium_diff()

    print(medium_question[1])
    user_ans2=input('What is _2_')
    attempt1=1
    max_attempt1=4
    while user_ans2 != medium_ans[1]:
        attempt1= attempt1+1
        user_ans2=input('Wrong answer try again ')
        if max_attempt1 == attempt1:
            print("you got the question wrong the quiz will restart")
            medium_diff()

    print(medium_question[2])
    user_ans3=input('What is _3_?')
    attempt2=1
    max_attempt2=4
    while user_ans3 != medium_ans[2]:
        attempt2= attempt2+1
        user_ans3=input('Wrong answer try again ')
        if max_attempt2 == attempt2:
            print("you got the question wrong the quiz will restart")
            medium_diff()
    print(medium_question[3])
    user_ans4=input('What is _4_?')
    attempt3=1
    max_attempt3=4
    while user_ans4 != medium_ans[3]:
        attempt3= attempt3+1
        user_ans4=input('Wrong answer try again ')
        if max_attempt3 == attempt3:
            print("you got the question wrong the quiz will restart")
            medium_diff()
    print(endquiz())
     
def hard_diff():
    print('Here is your first question please do not right answer in caps  and when asked number of something please write the integer value')
    print(hard_question[0])
    user_ans1=input('what is _1_?')
    attempt=1
    max_attempt=4
    while user_ans1 != hard_ans[0]:
        attempt= attempt+1
        user_ans1=input('Wrong answer try again ')
        if max_attempt == attempt:
            print("you got the question wrong the quiz will restart")
            hard_diff()




    print(hard_question[1])
    user_ans2=input('What is _2_')
    attempt1=1
    max_attempt1=4
    while user_ans2 != hard_ans[1]:
        attempt1= attempt1+1
        user_ans2=input('Wrong answer try again ')
        if max_attempt1 == attempt1:
            print("you got the question wrong the quiz will restart")
            hard_diff()


    print(hard_question[2])
    user_ans3=input('What is _3_')
    attempt2=1
    max_attempt2=4
    while user_ans3 != hard_ans[2]:
        attempt2= attempt2+1
        user_ans3=input('Wrong answer try again ')
        if max_attempt2 == attempt2:
            print("you got the question wrong the quiz will restart")
            hard_diff()

    print(hard_question[3])
    user_ans4=input('What is _4_')
    attempt3=1
    max_attempt3=4
    while user_ans4 != hard_ans[3]:
        attempt3= attempt3+1
        user_ans4=input('Wrong answer try again ')
        if max_attempt3 == attempt3:
            print("you got the question wrong the quiz will restart")
            hard_diff()
       
     
    print(endquiz())


intro()
ask_level_diff()
