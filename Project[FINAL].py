easy_question = ["_1_ khalifa is the tallest building in the world",
                  "The captial of australia in 2017 is _2_",
                 "In total there are _3_ Ocean",
                 "India got their independence in _4_"]
easyq_ans     = ["burgh","sydeny","7","1957"]

medium_question = ["Entomology is the science that studies _1_",
                   "Hitler party which came into power in 1933  is know as _2_ party.",
                   "In _3_, Germany declared  war on Russia and France ",
                   "India has largest deposits of _4_ in the world."]
mediumq_ans     = ["insects","nazi","1914","mica"]

hard_question = ["A total of _1_ lok Sabha seats belong to Rajasthan",
                "India's first atomic reactior was _2_ ",
                 "the total number of red blood cell in a normal human body is _3_ trillion",
                 "Bone marrow produces _4_ million red blood cells every second"]
hardq_ans     = ["25","aspara","30","2"]
blanks = ['_1_','_2_','_3_','_4_']



def intro():
    """Ask the name of the player  using input fumction and prints greetin
    Input :
     takes the name of the player
  behaviour:
     takes the input of the player then prints the greetings to player
     prints about the quiz in the next two line
return:none

"""

    name=input("Hello,what is your name?")

    print("Hello "+ name)
    print("Welcome To my Quiz")
    print("You will be asked 4 general knowledge questions")
    print("where you will need to fill the blanks ")

def endquiz():
    ''' This function is in the end of ask_question Behaviour to congrats the user for their completion of the  quiz
    return:none
 '''
    print('Congratulations!! you have succesfully completed the quiz')



def ask_level_diff():
    """
    Input:
      level number selected by the user
    behaviour:
     Takes the level   given by the user  and then uses ask_question function to launch the game
     according to the difficulty given by the user
     return:none

    """
    level = input("Now please Type a number between 1-3 to select your level (1 being the easiest and 3 being the hardest)   ")
    if level == "1":
        print("You have selected easy level ")
        ask_question(easy_question,easyq_ans,blanks)
    elif level == "2":
        print("you have selected medium difficulty")
        ask_question(medium_question,mediumq_ans,blanks)
    elif level =="3":
        print("You have selected hard difficulty")
        ask_question(hard_question,hardq_ans,blanks)

def anscheck(ans,number,quiz,blanks):
    print(quiz[number])
    ans_by_user= input('What is '+blanks[number])
    attempt=1
    max_attempt=4
    while ans_by_user != ans:
        attempt =attempt+1
        ans_by_user=input("You got the answer wrong why dont you try again")

        if max_attempt == attempt:
            print('Looks like you are not able to answer the question dont worry we will show you the answer')
            print(quiz[number].replace(blanks[number],ans))
            break
    while ans_by_user == ans:
        print('Looks like you got the answer right')
        print(quiz[number].replace(blanks[number],ans))
        
        break

""""
input :
 Takes ans_by_user as input
behaviour:
 uses the ans_by_user variable to cross check it with ans
 to ensure it matches and the uses of the while loop to   to limit the number  of attempts user can use
 The use of the replace string to   replace the blanks with the correct answer and  the correct answer can beeen seen by the user
 Blank is used so that the program can figure out what to replace in the question

"""



"""User_ans takes the answer of the user  while the ans check the output congrats the player for gettings the right answer if the ans is right  """
def ask_question(quiz, ans,blanks):
    """
    input:
         user_ans to obtain the answer from the user
    behaviour:
        The program uses  for loop in the quiz to print the individual  element  the quiz in a new line
        the program uses for loop to  take a range from 0-3 which  then uses to get the answer  of the quiz and  is put in the anscheck function to  check it with user ans

    """
    

    for blanks_no in range(0, len(blanks)):
        anscheck(ans[blanks_no],blanks_no,quiz,blanks)






intro()
ask_level_diff()
