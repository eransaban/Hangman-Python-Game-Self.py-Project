import os # load module to clear screan
import time   # import module to count time 
clear = lambda: os.system("cls") # create Clear Screen Varible

old_letters = []   # Keep letters Guessed
letter_guessed_lower = [] # uses for function guessed letters
MAX_TRIES = 6  # number of tries
num_of_tries = 1   # every wrong guess will add a number to this count
win = False   #check win status
secret_word = []  # keep secret word




def check_win(secret_word, old_letters_guessed):
    """This function will check if the user guessed the secret word.
    :param secret_word: the chosen word for the game.
    :param old_letters_guessed: the list that contain old guessed words.
    :type secret: str
    :type old_letters_guessed: list
    :return: True or False
    :rtype: Boolean
    """

    word = list(secret_word)
	
    for i in word:
        if i not in old_letters_guessed:
            return False
			
    return True
	
def show_hidden_word(secret_word, old_letters_guessed):
    """ This function will mask the secret word and reveal only guessed letters.
    :param secret_word: the chosen word for the game
    :param old_letters_guessed: the list that contain old guessed words
    :type secret: str
    :type old_letters_guessed: list
    :return: the masked secret word
    :rtype: str
    """

    new_secret = []
    word = list(secret_word)
		
    for i in word:
        if i in old_letters_guessed:
            new_secret.append(i)
        else:
            new_secret.append("_")


    return(" ".join(new_secret))
	
def check_valid_input(letter_guessed, old_letters_guessed):
    """ This function will check the letters the user is typing and decide if it's valid or not."
    :param letter_guessed: the letter the user type
    :param old_letters_guessed: the list that contain old guessed words
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True or False
    :rtype: Boolean
    """
    
    letter_guessed_lower = []
    global old_letters
    sum_of_letters = len(letter_guessed)
    letter_guessed_lower = letter_guessed.lower()

    if sum_of_letters == 1 and letter_guessed_lower.isalpha() == True:
        if letter_guessed_lower in old_letters_guessed:
            return False
        else:
            return True
    elif sum_of_letters == 1 and letter_guessed_lower.isalpha() == False:
        return False
    elif sum_of_letters > 1 and letter_guessed_lower.isalpha() == True:
        return False
    elif sum_of_letters > 1 and letter_guessed_lower.isalpha() == False:	
        return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """ This function will check the letter typed by the user, after it was validated, and than shows where it belong in the game."
    :param letter_guessed: the letter the user type
    :param old_letters_guessed: the list that contain old guessed words
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True or False
    :rtype: Boolean
    """

    global old_letters
    check = check_valid_input(letter_guessed, old_letters_guessed)
    if check == False:
        old_letters_guessed.sort()
        print("X")
        print(" -> ".join(old_letters_guessed).strip())
        return False
    elif check == True:
        if letter_guessed in old_letters_guessed:
            old_letters_guessed.sort()
            print("X")
            print(" -> ".join(old_letters_guessed).strip())
            return False
        else:
            old_letters_guessed.append(letter_guessed)
            return True


def choose_word(file_path, index):
    """ This function will read the file specified and choose a word from it based on the number we wil choose."
    :param file_path: path for our file with a list of words
    :param index: the number the player has choosen to pick a word from
    :type file_path: str
    :type index: list
    :return: the word that was choosen
    :rtype: str
    """

    list_words =open(file_path, "r")
    words = list_words.read().split()
    word_only_once = [] 

    for word in words:
        if word in word_only_once:
            continue
        else:
            word_only_once.append(word)

    unique_word_sum = len(word_only_once)
    
    index_number = index % unique_word_sum

    result = words[index_number-1]
    list_words.close()
	
    return result
	
	
	
def print_hangman(num_of_tries):
    """ This function will print the hangman phothos based on user guesses."
    :param num_of_tries: a varible that represent the status of the player and hoe many tries are left.
    :type num_of_tries: int
    :return: photo that will hangman mode
    :rtype: dict
    """
	
    return(hangman_photos[num_of_tries])
    
hangman_photos = {

1 : ("""     x-------x
"""),

2 : ("""     x-------x
    |
    |
    |
    |
    |
"""),

3 : ("""     x-------x
    |       |
    |       0
    |
    |
    | 
"""),	


4 : ("""    x-------x
    |       |
    |       0
    |       |
    |
    | """), 
	
	
5 : ("""     x-------x
    |       |
    |       0
    |      /|\\
    |
    | 
"""),

	
6 : ("""     x-------x
    |       |
    |       0
    |      /|\\
    |      /
    | """) ,

7 : ("""
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |	""") 
	
}
	
def reset_game():
    """ after a new game is choosen, this func clear old game data and create blank varibals"""
    global old_letters
    global letter_guessed_lower
    global MAX_TRIES
    global num_of_tries
    global win
    global secret_word
    old_letters = []
    letter_guessed_lower = []
    MAX_TRIES = 6
    num_of_tries = 1
    win = False
    
   



	
	
def start_game():
    """ This function will start the game and print logo and number of trues."
    :param num_of_tries: a varible that represent the status of the player and hoe many tries are left.
    :type num_of_tries: int
    :return: logo of game
    :rtype: str
    """

    
    HANGMAN_ASCII_ART = """
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/ """


    print (HANGMAN_ASCII_ART, "\n", "You Have", MAX_TRIES ,"Tries", "\n", "Good Luck !!!")
	

def the_end():
    """ Print The End Logo	"""

    end = """
  _______ _            ______           _ 
 |__   __| |          |  ____|         | |
    | |  | |__   ___  | |__   _ __   __| |
    | |  | '_ \ / _ \ |  __| | '_ \ / _` |
    | |  | | | |  __/ | |____| | | | (_| |
    |_|  |_| |_|\___| |______|_| |_|\__,_|"""
    print(end)
    

def win_game():
    """ Print You Win Logo	"""
    win = """ ______      __     __          __          ___             ______
 \ \ \ \     \ \   / /          \ \        / (_)           / / / /
  \ \ \ \     \ \_/ /__  _   _   \ \  /\  / / _ _ __      / / / / 
   \ \ \ \     \   / _ \| | | |   \ \/  \/ / | | '_ \    / / / /  
    \ \ \ \     | | (_) | |_| |    \  /\  /  | | | | |  / / / /   
     \_\_\_\    |_|\___/ \__,_|     \/  \/   |_|_| |_| /_/_/_/    
                                                                  
                                                                  """
    print(win)


def lose():
    """ Print You Lose Logo	"""
    lose = """
      ______ __     __           _                     ______     
     / / / / \ \   / /          | |                    \ \ \ \    
    / / / /   \ \_/ /__  _   _  | |     ___  ___  ___   \ \ \ \   
   / / / /     \   / _ \| | | | | |    / _ \/ __|/ _ \   \ \ \ \  
  / / / /       | | (_) | |_| | | |___| (_) \__ \  __/    \ \ \ \ 
 /_/_/_/        |_|\___/ \__,_| |______\___/|___/\___|     \_\_\_\
                                                                  
                                                                  """
    print(lose)							  

def main(): 
    """ This is the main function it will will run through the game and call functions when needed """
    global old_letters
    global letter_guessed_lower
    global MAX_TRIES
    global num_of_tries
    global win
    global secret_word
    start_game()  # print the hangman logo
	
    file_path = input("Enter file path:")     #ask for the file location
    index = int(input("Enter Index:"))     #choose a number to choose a word from from the file

    secret_word = choose_word(file_path, index) #save secret word to varbibale
    sword = list(secret_word) #for checking guess with right letters.

    print("\n \n", show_hidden_word(secret_word, old_letters)) #print hidden secret word 

    print("\n \n \n" "Let's Start !" "\n \n \n" )  #let's start
    print(print_hangman(num_of_tries),"\n")  #print intial hangman mode


    while win != True:    #loop to check til var become true and stop
        if num_of_tries == 7:  # you this var get to 7, game over
            lose() # print lose logo
            again = input("Do You Want To play Again ?(type yes or no):") #ask if you want to play again
            if again == "yes":   # type yes to restart the game
                num_of_tries = 1   #set varible to 1 
                reset_game() #run func to clear varibles
                main() #start main func again
            else:   #if typed anything else include no  end's game
                clear()  #clear screen
                the_end()  # the end logo
                time.sleep(3) # wait 3 seconds
                os._exit(1) # close console
        letter_guessed = input("Guess a Letter: ")     #save letter input to var
        guess = try_update_letter_guessed(letter_guessed, old_letters) #run try func to check if letter is ok
        if guess == True:     #if true run this actions
            if letter_guessed in sword:   #if letter in secret word
                print(show_hidden_word(secret_word, old_letters))  #print hidden word with letter revealed
                win = check_win(secret_word, old_letters)   #check if player won by running check win
                if win == True:  #if player win
                    clear()  #clear screen
                    win_game()   #print win logo 
            else:   #if not
                clear()   #clear screan
                guess = try_update_letter_guessed(letter_guessed, old_letters) #recheck letter, so the var will have the X and letter list with arrow
                print(guess)  #print var
                num_of_tries = num_of_tries + 1  #add 1 to the var number count 
                print(print_hangman(num_of_tries)) #print hangman status based on guess number
        else: #if not
            clear() #clear screan
            guess = try_update_letter_guessed(letter_guessed, old_letters) #recheck letter, so the var will have the X and letter list with arrow
            print(guess) #print var
            num_of_tries = num_of_tries + 1 #add 1 to the var number count 
            print(print_hangman(num_of_tries)) #print hangman status based on guess number
	
    if win == True: # when loop end and player win = true
        again = input("Do You Want To play Again ? (type yes or no):")  #ask if player wnat to play again
        if again == "yes":  #if eq yes 
            num_of_tries = 1  #reset game with the folowing
            reset_game()
            main()
        else:  #if not  shows the end counting and quiting
            clear()
            the_end()
            time.sleep(3)
            os._exit(1)
		
	


if __name__ == "__main__": 
    main() 

