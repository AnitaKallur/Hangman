import random
word_list = ['apple', 'banana', 'orange', 'mango', 'pear', 'strawberry', 'watermelon', 'grapes', 'blueberry', 'pineapple', 'cherry', 'cranberry', 'durian', 'fig', 'guava', 'kiwifruit', 'lychee', 'papaya', 'pomegranate']
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word) 
        self.num_letters = len(set(self.word))
        self.num_lives = 5
        self.list_letters = []  
        print(f'The mistery word has {len(self.word)} characters')
        print(self.word_guessed)
        self.hangman_drawing = {
        0: '''
            +---+
            |   |
                |
                |
                |
                |
        ===========''', 
        1: '''
            +---+
            |   |
            O   |
                |
                |
                |
        ===========''',
        2: '''
            +---+
            |   |
            O   |
            |   |
                |
                |
        ===========''',
        3: '''
            +---+
            |   |
            O   |
           /|   |
                |
                |
        ===========''',
        4: '''
            +---+
            |   |
            O   |
           /|\  |
                |
                |
        ===========''',
        5: '''
             +---+
            |   |
            O   |
           /|\  |
           /    |
                |
        ===========''',
        6: '''
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
        ==========='''}
        
    pass
       

    def check_lives(self, num_lives):
        self.num_lives = num_lives
        if self.num_lives == 5:
            print(self.hangman_drawing[0])
        elif self.num_lives == 4:
            self.hangman_drawing[2]
        elif self.num_lives == 3:
            self.hangman_drawing[3]
        elif self.num_lives == 2:
            self.hangman_drawing[4]
        elif self.num_lives == 1:
            self.hangman_drawing[5]
        elif self.num_lives == 0:
            self.hangman_drawing[6]
        print(self.hangman_drawing[5-self.num_lives])

       
    def check_letter(self, letter):
        
        self.letter = letter
        if letter in self.word:     
            for i in range(len(self.word)):
                if self.letter == self.word[i]:
                    self.word_guessed[i] = letter
            self.num_letters -= 1
            print(self.word_guessed)
        
        else:
            self.num_lives -= 1
            self.check_lives(self.num_lives)
            print(self.num_lives)

        self.list_letters.append(letter) 
                
       
    def ask_letter(self):
        while True:
            letter = input('Enter a single character: ').lower()
            if letter in self.list_letters:
                print(f"{letter}) was already tried")
            elif len(letter) > 1:
                print('Please enter just one character')     
            else:
                break
       
        self.check_letter(letter)
    

def play_game(word_list):
    word_list
    
    while True:
        game.ask_letter()
        if game.num_lives == 0:
            print(f"You lost! The word was {game.word}")
            break    
        elif game.num_letters == 0:
            print(f"Congratulations! You WON!")
            break                    

if __name__ == '__main__':
    #word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon', 'grapes', 'blueberry', 'pineapple', 'cherry', 'cranberry', 'durian', 'fig', 'guava', 'kiwifruit', 'lychee', 'papaya', 'pomegranate']
    game = Hangman(word_list)
    play_game(word_list)
     
# %%