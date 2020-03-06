"""
Program: doctor.py
Author: Ken
Conducts an interactive session of nondirective psychotherapy.
"""

from breezypythongui import EasyFrame
import random

class Doctor(EasyFrame):
    
    def __init__(self):
        EasyFrame.__init__(self, title = "Doctor")
        self.statusField = self.addTextField(row = 3, column = 1, text = "Good morning, I hope you are well today.", state = "readonly")
        self.replyField = self.addtextField(row = 3, column = 1, text = "")
        hedges = ("Please tell me more.",
          "Many of my patients tell me the same thing.",
          "Please coninue.")
        qualifiers = ("Why do you say that ",
              "You seem to think that ",
              "Can you explain why ")

        replacements = {"I":"you", "me":"you", "my":"your",
                "we":"you", "us":"you", "mine":"yours"} 

    def reply(sentence):
        """Implements two different reply strategies."""
        probability = random.randint(1, 4)
        if probability == 1:
            return random.choice(hedges)
        else:
            return random.choice(qualifiers) + changePerson(sentence)

    def changePerson(sentence):
        """Replaces first person pronouns with second person
        pronouns."""
        words = sentence.split()
        replyWords = []
        for word in words:
            replyWords.append(replacements.get(word, word))
            return " ".join(replyWords) 

def main():
    """Handles the interaction between patient and doctor."""
    print("Good morning, I hope you are well today.")
    print("What can I do for you?")
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        print(reply(sentence))

# The entry point for program execution
if __name__ == "__main__":
    main()

