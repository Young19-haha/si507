from random import randrange

## CONSTANTS ##

##Art by Hayley Jane Wakenshaw - https://www.asciiart.eu/animals/dogs
DOG_LEFT = """
   __
o-''|\_____/)
 \_/|_)     )
    \  __  /
    (_/ (_/ 
"""

DOG_RIGHT = """
        __
(\_____/|''-o
(     (_|\_/
 \  __   / 
  \_) \_) 
"""

##Art by Joan Stark - https://www.asciiart.eu/animals/cats
CAT_LEFT = """
 /\    /    
(' )  (
 (  \  )
 |(__)/
"""

CAT_RIGHT = """
\    /\\
 )  ( ')
(  /  )
 \(__)|
"""

class Pet:
    '''A Tamagotchi pet!
    Attributes
    ----------
    name : string
        The pet's name
    sound : string
        The pet's sound
    '''
    max_boredom = 6
    max_hunger = 10
    leaves_hungry = 16
    leaves_bored = 12

    ascii_art_left = ""
    ascii_art_right = ""

    # TODO: Add attribute "sound"
    def __init__(self, name, sound):
        self.name = name
        self.hunger = randrange(self.max_hunger)
        self.boredom = randrange(self.max_boredom)
        self.sound = sound

    def mood(self):
        '''Get the mood of a pet. A pet can be happy, hungry or bored,
        depending on wether it was fed or has played enough.

        Parameters
        ----------
        none

        Returns
        -------
        str
            The mood of the pet
        '''

        if self.hunger <= self.max_hunger and self.boredom <= self.max_boredom:
            return "happy"
        elif self.hunger > self.max_hunger:
            return "hungry"
        else:
            return "bored"

    def status(self):
        '''Get the status of a pet to know it's name, how it feels and what it wants.

        Parameters
        ----------
        none

        Returns
        -------
        str
            The name, mood and wants of the pet.
        '''

        state = "I'm " + self.name + '. '
        state += 'I feel ' + self.mood() + '. '
        if self.mood() == 'hungry':
            state += 'Please feed me.'
        if self.mood() == 'bored':
            state += 'You can play with me.'
        return state

    def do_command(self, resp):
        '''Calls the appropriate methods of a pet based on command "resp" given by player.

        Parameters
        ----------
        resp : string
            The command to be issued to the pet.

        Returns
        -------
        none
        '''

        if resp == "speak":
            print(self.speak())
        elif resp == "play":
            self.play()
        elif resp == "feed":
            self.feed()
        elif resp == "wait":
            print("Nothing to do...")
        else:
            print("Please provide a valid command.")

    def has_left(self):
        '''Returns True if a pet has left the game due to hunger or boredom, otherwise False.

        Parameters
        ----------
        none

        Returns
        -------
        bool
            If a pet has left
        '''
        return self.hunger > self.leaves_hungry or self.boredom > self.leaves_bored

    def clock_tick(self): #TODO
        #TODO: implement function and add docstring
        # pass
        """Add 2 to the pet's hunger and boredom

        Parameters
        ----------
        none

        Returns
        -------
        int
            max_hunger and max_boredom
        """
        self.hunger += 2
        self.boredom += 2
        return self.hunger, self.boredom

    def speak(self): #TODO
        #TODO: implement function and add docstring
        # pass
        """Print "I say: " and then the pet's unique sound.

        Parameters
        ----------
        none

        Returns
        -------
        none
        """
        return f"I say: {self.sound}"

    def feed(self): #TODO
        #TODO: implement function and add docstring
        # pass
        """The pet's hunger is decreased by 5.

        Parameters
        ----------
        none

        Returns
        -------
        none
        """

        self.hunger -= 5
        if self.hunger < 0:
            self.hunger = 0
        return 

    def play(self, limit_guess = 3): #TODO
        #TODO: implement function and add docstring
        # pass
        """The user tries to guess which way the pet will look up
        to 3 times. If guess correctly, the play is done and 
        pet's boredom is decreased by 5.

        Parameters
        ----------
        none

        Returns
        -------
        none
        """

        num_guess = 0
        pet_look_direction = ['left', 'right']
        while num_guess < limit_guess:
            my_guess = input('Does the pet look left or right?\n')
            if my_guess in pet_look_direction:
                rand_index = randrange(2)
                if my_guess == pet_look_direction[rand_index]:
                    print('Correct!')
                    self.boredom -= 5
                    if self.boredom < 0:
                        self.boredom = 0
                    break
                else:
                    print(f"I look to the {pet_look_direction[rand_index]}. Try again.")
                    if rand_index == 0:
                        print(self.ascii_art_left)
                    else:
                        print(self.ascii_art_right)
                num_guess += 1
            else:
                print("Please provide a valid command.\n")


#######################################################################
#---------- Part 2: Inheritance - subclasses
#######################################################################

# TODO: Implement the Dog, Cat and Poodle subclasses and add docstrings
class Dog(Pet):
    """Subclass of Pet
    Attributes
    ----------
    name: str
        The dog's name
    sound: str
        The dog's sound
    """

    ascii_art_left = DOG_LEFT
    ascii_art_right = DOG_RIGHT

    def play(self, limit_guess = 3):
        """The user tries to guess which way the pet will look up
        to 3 times. If guess correctly, the play is done and 
        pet's boredom is decreased by 5.

        Parameters
        ----------
        none

        Returns
        -------
        none
        """
        super().play()
        
    def speak(self):
        """Print "I say: " and Dog sound

        Parameters
        ----------
        none

        Returns
        -------
        none
        """
        return super().speak() + " arrrf!"


class Cat(Pet):
    """Subclass of Pet
    Attributes
    ----------
    name: str
        The name of cat
    sound: str
        The sound of cat
    meow_count: int
        The number of sound
    """

    ascii_art_left = CAT_LEFT
    ascii_art_right = CAT_RIGHT 

    def __init__(self, name, sound, meow_count):
        super().__init__(name, sound)
        self.meow_count = meow_count


    def speak(self):
        """Print "I say: " and repeated count of sound

        Parameters
        ----------
        none

        Returns
        -------
        none
        """
        return f"I say: {self.sound * int(self.meow_count)}"

    def play(self):
        """Cats have 5 attempts while playing. Guess which way
         the cat will look. If guess correctly, the play is done and
          pet's boredom is decreased by 5.

        Parameters
        ----------
        limit_guess: int
            default limit guess 5 times

        Returns
        -------
        none
        """
        super().play(5)


class Poodle(Dog):
    """Subclass of Dog
    Attibutes
    ---------
    name: str
        The name of Poodle
    sound: str
        The sound of Poodle
    """

    def dance(self):
        """Return "Dancing in circles like poodles do!"

        Parameters
        ----------
        none

        Returns
        -------
        str: sentence saying "Dancing in circles like poodles do!"
        """
        dance = "Dancing in circles like poodles do!"
        return dance
    
    def speak(self):
        """First print the dance method and then the speak method from the superclass.

        Parameters
        ----------
        none

        Returns
        -------
        none
        """
        return self.dance() + super().speak()


def get_name():
    '''Asks the player which name a pet should have.

    Parameters
    ----------
    none

    Returns
    -------
    none
    '''
    return input("How do you want to name your pet?\n")
def get_sound():
    '''Asks the player what sound a pet should make

    Parameters
    ----------
    none

    Returns
    -------
    none
    '''
    return input("What does your pet say?\n")
def get_meow_count():
    '''Asks the player how often a cat should make a sound.

    Parameters
    ----------
    none

    Returns
    -------
    none
    '''
    while True:
        resp = input("How often does your Cat make a sound?\n")
        if resp.isnumeric():
            return int(resp)

p = None

while p == None:
    resp_pet_type = input("What kind of pet would you like to adopt?\n")

    # TODO: Instantiate either a cat, dog or poodle depending on the input
    # given by the player (case insenstive) and assign it to the variable p.
    # If the player does not provide valid input, print: 
    # "We only have Cats, Dogs and Poodles.". Continue the loop till
    # the player provides a vaild pet.
    if resp_pet_type.lower() == 'cat':
        name = get_name()
        sound = get_sound()
        meow_count = get_meow_count()
        p = Cat(name, sound, meow_count)
    elif resp_pet_type.lower() == 'dog':
        name = get_name()
        sound = get_sound()
        p = Dog(name, sound)
    elif resp_pet_type.lower() == 'poodle':
        name = get_name()
        sound = get_sound()
        p = Poodle(name, sound)
    else:
        print("We only have Cats, Dogs and Poodles.")  

while not p.has_left():
    print()
    print(p.status())

    command = input("What should I do?\n")
    p.do_command(command)
    p.clock_tick()

print("Your pet has left.")