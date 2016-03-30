

#These are the quizes that the use will select

quizEasy = """The language that makes up the majority of the internets web pages,
    and creates the structure of a website is called ___1___, which stands for 
    ___2___. This is used to create images, texts and other elements that you
    see on a webpage. ___3___ is used to add style to the webpages including
    colors, font styles, font sizes and many other effects. CSS stands
    for ___4___."""

quizMedium = """In computer programming a ___1___ is a finite sequence of characters,
    including letters, numbers, symbols and punctuation marks. a ___2___ serves
    as a place holder for a ___1___. The ___2___ holds a value or string that
    we can reference later in order to save time. We can combine two strings
    by a process known as ___3___. For this,  we use the ___4___ sign like we 
    use in mathematics when combining two numbers"""

quizHard = """you create a ___1___ with the def keyword. A ___1___ operates on 
    inputs called ___2___ which are separated by commas and go between the
    ___3___ marks. The final product of a ___1___ is called an ___4___."""

#Answers will be stored as lists and referenced later
answers_1 = ["HTML", "Hypertext markup language", "CSS", "Cascading style sheet"]
answers_2 = ["string", "variable", "concatenation", "+"]
answers_3 = ["function", "parameters", "parenthesis", "output"]

blanks=["___1___", "___2___", "___3___", "___4___"]

#This will ask the user to select level 1 2 or 3

def game_setup():
    user_prompt=raw_input("Welcome to the Python Challenge! Please select level easy, medium, or hard.")
    
    while user_prompt not in ["easy", "medium", "hard"]:
        user_prompt = raw_input("Incorrect. Please enter level easy, medium, or hard.")
    
    if user_prompt == "easy":
        return quizEasy, answers_1
        
    if user_prompt == "medium":
        return quizMedium, answers_2
        
    if user_prompt == "hard":
        return quizHard, answers_3
        
    else:
        return ("Error. Please select level 1, 2, or 3.")




#this will check users answer and return a response
def answerCheck(user_input, correctAnswer):
    user_input = raw_input
    answers = game_setup(user_prompt)
    correctAnswer = answers[answerIndex]
    if user_input == correctAnswer:
        return "Correct"
    return "Incorrect. Please Try Again"

#this is the game code
def game_start():
    quiz, answers = game_setup()
    

    blanksIndex = 0 #answerindex not needed bc are same length as blank index
    

    while blanksIndex < len(blanks):
        
        for answer in answers:
            print quiz
            user_input = raw_input("What is the answer for "+ blanks[answers.index(answer)])
            while user_input != answer:
                user_input = raw_input("Incorrect, try again.")
            if user_input == answer:
                print "Good job! that answer is correct!"
                quiz = quiz.replace(blanks[blanksIndex], user_input)
                print quiz
                blanksIndex += 1

game_start()

