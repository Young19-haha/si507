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


    def __init__(self, name, sound, age=0):
        self.name = name
        self.hunger = randrange(self.max_hunger)
        self.boredom = randrange(self.max_boredom)
        self.sound = sound
        self.age = age

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
            state += 'Please feed me. '
        if self.mood() == 'bored':
            state += 'You can play with me. '
        return state + f"I'm {self.age} years old now." 

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
        elif resp == "adopt":
            self.adopt()
        elif resp == "list":
            self.list_name()
        elif resp == "choose":
            self.choose()
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

    def clock_tick(self): 
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
        self.age += 2
        return self.hunger, self.boredom, self.age

    def speak(self):
        """Print "I say: " and then the pet's unique sound.

        Parameters
        ----------
        none

        Returns
        -------
        none
        """
        return f"I say: {self.sound}"

    def feed(self):
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
    
    def adopt(self):
        """The player adds an additional pet to game.
        Parameters
        ----------
        none
        
        Returns
        -------
        none
        """
        main()

    def list_name(self):
        """The names of all pets are listed.
        Parameters
        ----------
        name_list: list
            the list of all pets
        
        Returns
        -------
        none
        """
        for name in pet_dict.keys():
            print(name)
        

    def choose(self):
        """List names. Ask player to provide a valid name. 
        Go back to standaed menu.
        
        Parameters
        ----------
        none
        
        Returns
        -------
        none
        """
        self.list_name()
        while True:
            name = input("Please provide a valid name.\n")
            if name in pet_dict.keys():
                break
         
        if pet_dict[name]['type'].lower() == 'cat':
            p = Cat(name, pet_dict[name]['sound'], pet_dict[name]['meow_count'], pet_dict[name]['age'])
        if pet_dict[name]['type'].lower() == 'dog':
            p = Dog(name, pet_dict[name]['sound'], pet_dict[name]['age'])
        if pet_dict[name]['type'].lower() == 'poddle':
            p = Poodle(name, pet_dict[name]['sound'], pet_dict[name]['age'])

        while True:
            while not p.has_left():
                print()
                print(p.status())
                if p.age > 18:
                    print(f"{p.name} has left.\nProgram terminates.")
                    break

                command = input("What should I do?\n")
                p.do_command(command)
                p.clock_tick()
                update_pet_dict_age(p.age, p.name, pet_dict)

            print("Your pet has left.")
            pet_dict.pop(p.name)

            if not list(pet_dict.keys()):
                option = input("Do you want play it again or quit?\n")
                if option == "again":
                    main()
                elif option == "quit":
                    print("Byebye~")

        

#######################################################################
#---------- Part 2: Inheritance - subclasses
#######################################################################

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

    def clock_tick(self):
        self.hunger += 2
        self.boredom += 2
        self.age += 2
        return self.hunger, self.boredom, self.age
        

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
        return f"I say: {self.sound} arrrf!"


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

    def __init__(self, name, sound, meow_count, age = 0):
        super().__init__(name, sound)
        self.meow_count = meow_count
        self.age = age

    def clock_tick(self):
        self.hunger += 2
        self.boredom += 2
        self.age += 3
        return self.hunger, self.boredom, self.age

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

    def clock_tick(self):
        self.hunger += 2
        self.boredom += 2
        self.age += 2.5
        return self.hunger, self.boredom, self.age

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

def check_name_is_unique(name, pet_dict):
    """Check whether names in the list is unique
    
    Parameters
    ----------
    name: str
        new name
    name_list: dict
        the dict of all pet
        
    Returns
    -------
    none
    """
    while True:
        name_list = []
        for key in pet_dict:
            name_list.append(key)
        if name not in name_list:
            break 
        else:
            print("Please provide a valid name.\n")
            name = get_name()

def build_pet_dict(resp, name, sound, age, meow_count=0):
    if resp == 'cat':
        pet_dict[name] = {"type":resp, "sound":sound, 
        "age": age, "meow_count": meow_count}
    else:
        pet_dict[name] = {"type":resp, "sound":sound,
        "age": age}

def update_pet_dict_age(age, name, pet_dict):
    pet_dict[name]['age'] = age


pet_dict = {}

def main():
    """Play loop

    Parameters
    ----------
    none

    Returns
    -------
    none
    """
    while True:

        p = None

        while p == None:
            resp_pet_type = input("What kind of pet would you like to adopt?\n")

            if resp_pet_type.lower() == 'cat':
                name = get_name()
                check_name_is_unique(name, pet_dict.keys())
                sound = get_sound()
                meow_count = get_meow_count()
                p = Cat(name, sound, meow_count)
                build_pet_dict(resp_pet_type, name, sound, p.age, meow_count)
            elif resp_pet_type.lower() == 'dog':
                name = get_name()
                check_name_is_unique(name, pet_dict.keys())
                sound = get_sound()
                p = Dog(name, sound)
                build_pet_dict(resp_pet_type, name, sound, p.age)
            elif resp_pet_type.lower() == 'poodle':
                name = get_name()
                check_name_is_unique(name, pet_dict.keys())
                sound = get_sound()
                p = Poodle(name, sound)
                build_pet_dict(resp_pet_type, name, sound, p.age)
            else:
                print("We only have Cats, Dogs and Poodles.")  

        while not p.has_left():
            print()
            print(p.status())
            if p.age > 18:
                print(f"{p.name} has left.\nProgram terminates.")
                break
           
            command = input("What should I do?\n")
            p.do_command(command)
            p.clock_tick()
            update_pet_dict_age(p.age, p.name, pet_dict)
            

        print("Your pet has left.")
        pet_dict.pop(p.name)

        if not list(pet_dict.keys()):
            option = input("Do you want play it again or quit?\n")
            if option == "again":
                main()
            elif option == "quit":
                print("Byebye~")
                break
            break
        
        
        


if __name__ == "__main__":
    main()