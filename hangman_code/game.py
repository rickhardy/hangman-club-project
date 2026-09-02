from enum import IntEnum
"Defines the class self that holds details of the game and "
"provides game specific functions"


class Game:

        class Game_status(IntEnum):  
        # in game_status_function
                NEW_GAME = 0
                IN_PLAY = 1
                WON = 2
                LOST = 3

        def __init__(
                self,
                word: str,
                used_letters: list[str] | None = None,
                letters_remaining: list[str] | None = None, 
                accepted_letters: list[str] | None = None,
                status: Game_status | None = None,
                    ) -> None:
        
                self.word = self.set_word (word)
                self.accepted_letters = self.set_accepted_letters(accepted_letters)
                self.used_letters = self.set_used_letters(used_letters)
                self.letters_remaining = self.set_letters_remaining(letters_remaining)
                self.status = self.set_status(status)




# FOR EVERY SINGLE ATTRIBUTE, THERE IS A GET AND A SET

        def get_word(self):
                return self.word
        
        def set_word(self,word):
                # This function takes an input of a list and returns a list
                if word.isalpha():
                        return (word)
                else:
                        raise TypeError (f"Non alphabetic characters in word: {self.accepted_letters}")
                
 
        def get_used_letters(self, used_letters):
                if used_letters == None:
                        used_letters = [] 
                else: 
                        used_letters = used_letters
                return used_letters       
        
        def set_used_letters(self,used_letters):
                        used_letters = [] if used_letters is None else used_letters
                        return used_letters

        
        def get_status(self):
                return self.status
                
        def set_status(self, status):

                if status == None:  
                        status = self.Game_status.NEW_GAME
                elif isinstance(status, self.Game_status):
                        if self.calculate_unsucessful_attempts() > 10:
                                self.status = self.Game_status.LOST
                        elif self.is_word_guessed():
                                self.status = self.Game_status.WON
                        else:
                                # self.status = status # No change
                                None # so no action
                else:
                        raise TypeError(f"{status!r} is not a valid Game_status")

                return status
        
        def is_word_guessed():
                return False

        def set_accepted_letters(self,accepted_letters):
                        accepted_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if accepted_letters is None else accepted_letters
                        
                        if accepted_letters.isalpha():
                                return (accepted_letters)
                        else:
                                raise TypeError (f"Non alphabetic characters in word: {accepted_letters}")

                        
        def set_letters_remaining(self,letters_remaining):
                        letters_remaining = self.accepted_letters if letters_remaining is None else letters_remaining
                        return letters_remaining

        def get_letters_remaining(self):
                return self.letters_remaining


                        
        def get_attempts_remaining(self):
                return self.attempts_remaining

        def set_attempts_remaining(self,attempts_remaining):
                if isinstance(attempts_remaining, int):
                        if attempts_remaining >= 0:
                                self.attempts_remaining = attempts_remaining
                                return self.attempts_remaining
                        else:
                                return 0
                else:
                        raise TypeError

        def make_guess (self, letter):
                print ('calculating guess')
                self.used_letters.append(letter)
                if letter in self.word:
                        print ('yes') 

                else:
                        print ('no')
                        
                self.set_status        
                self.calculate_display_option ()


        def calculate_unsucessful_attempts(self):
                unsuccessful_attempts = 0
                for used_letter in self.used_letters:
                        if used_letter not in self.word:
                                unsuccessful_attempts += 1 
                return unsuccessful_attempts      

        def calculate_display_option (self):
                display_option = (1 << self.calculate_unsucessful_attempts()) - 1  
                return display_option

        def calculate_word_template():
                None

        def to_dict(self):
                return {
                        "word": self.word,
                        "used_letters": self.used_letters,
                        "letters_remaining": self.letters_remaining,
                        "display_option": self.calculate_display_option(),
                        "status": self.status.name,
                        "accepted_letters": self.accepted_letters
                }





