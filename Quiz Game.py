while True:

    introduction = input("Welcome to Jouti's Quiz Game, are you ready ? (yes/no) ").lower()
    score = 0


    if introduction == "yes":
        print("Okay, let's go! ")



    print( """
        RULES : 
    ---------------------------
        The quiz has 5 questions.
    There are 3 possible answers per question but only one is correct.
        To submit your answer, be sure to put only the letter of the desired answer.
    Each correct answer is worth 1 point.
        Have fun :) 
    ---------------------------
       """
       )

    start_game = input("Rules understood? (yes/no) ").lower()

    if start_game == "yes":
        print("Super, let's start then by the first question : ")
    else:
        print("Try to read it again it's very easy ;) ")

    qst_1 = input("""
              Who was elected President of the United States in 2017 ?
              --------------------------------------------------------
    A - Donald Trump
    B - Barack Obama
    C - George Bush

    Your answer : 
        """
              ).upper()

    if qst_1 == "A":
        print("Next question")
        score += 1
    elif qst_1 == "B":
        print("Next question")
        score += 0
    elif qst_1 == "C":
        print("Next question")
        score += 0

    qst_2 = input("""
                What is the national language of Canada? ")
                -------------------------------------------
    A - English
    B - Dutch
    C - French
    
        """
              ).upper()

    if qst_2 == "A":
        print("Next question")
        score += 0
    elif qst_2 == "B":
        print("Next question")
        score += 1
    elif qst_2 == "C":
        print("Next question")
        score += 0

    qst_3 = input("""
               What native country is Brazil? 
               ------------------------------
    A - South American
    B - North American
    C - West American
    
        """
              ).upper()

    if qst_3 == "A":
        print("Next question")
        score += 0
    elif qst_3 == "B":
        print("Next question")
        score += 1
    elif qst_3 == "C":
        print("Next question")
        score += 0

    qst_4 = input("""
               Saudi Arabia is the biggest producer of?
               ----------------------------------------
    A - Oil
    B - Coal
    C - Coffee
        
        """
                  ).upper()

    if qst_4 == "A":
        print("Last question")
        score += 1
    elif qst_4 == "B":
        print("Last question")
        score += 0
    elif qst_4 == "C":
        print("Last question")
        score += 0

    qst_5 = input("""
            Which religion believes in One God and the Last Prophet Muhammad (PBUH)? 
            ------------------------------------------------------------------------
    A - Islam
    B - Hinduism
    C - Buddism
        
        """
                  ).upper()

    if qst_5 == "A":
        print("")
        score += 1
    elif qst_5 == "B":
        print("")
        score += 0
    elif qst_5 == "C":
        print("")
        score += 0

    print("The game is Over !")

    if score < 3:
        print("Your final score is : ", score, ", you can do better :( ")
    else:
        print("Your final score is : ", score, ", well done :) ")

    play_again = input("Do you want to play again? (Yes/no)  ").lower()
    if play_again != "yes":
        break
