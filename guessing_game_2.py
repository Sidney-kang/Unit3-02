#Created by : Sidney Kang
#Created on : 5 Oct. 2017
#Created for : ICS3UR
# Daily Assignment - Unit3-01
# This program shows how to use an if statement

import ui

from numpy import random

def check_number_touch_up_inside(sender):
    #This checks the number of students entered versus the constant (25 stuents)
    
    #input
    number_enteredt = int(view['input_of_number_textbox'].text)
    # Random number guess
    number_to_guess = random.randint(1,10)
    
    #process
    if number_entered == number_to_guess:
         #output
       view['check_answer_label'].text = "You guessed the number!!!"
    else:
       view['check_answer_label'].text = "Sorry, number is " + str(number_to_guess)
       
view = ui.load_view()
view.present('sheet')
