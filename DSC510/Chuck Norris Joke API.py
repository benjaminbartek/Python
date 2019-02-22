#// File: Week 10 Assignment.py
#// Name: Benjamin Bartek
#// Date: February 16, 2019
#// Course: DSC 510 - Introduction to Programming
#// Desc: This program is a simple API program that retrieves random Chuck Norris jokes from https://api.chucknorris.io/jokes/random
#//       The program allows the user to make a new request until they enter input to make the program quit.
#// Usage: The program 1) displays a welcome message 2) retrieves and displays a random Chuck Norris joke, then
#//        3) prompts the user to either a) request a new Chuck Norris joke or b) quit the program. This is achieved
#//        primarily through an API, functions, and loops.

#Imports
import requests, json

#Globals
#Class color allows some code for bolding. Could add actual color if getting fancy.
class color:
   bold = '\033[1m'
   end = '\033[0m'

#URL variable for retrieving joke from API. Headers variable prevents caching.
url = "https://api.chucknorris.io/jokes/random"
headers = {'cache-control':'no-cache'}

#Function Definitions
#Welcome displays a welcome message
def Welcome():
    welcome_msg = (color.bold + 'Welcome To The Random Chuck Norris Joke Retriever!' + color.end)
    print(welcome_msg.center(117))

#Quit displays a final message and ends the program.
def Quit():
    quit_msg = (color.bold + 'Best be on your way before Chuck Norris\'s boot meets your face. GOOD BYE!' + color.end)
    print('\n\n')
    print(quit_msg.center(117))

#Get_Joke makes the actual API request via reponse_raw, then turns it into a dictionary and prints with formatting.
def Get_Joke():
    response_raw = requests.get(url, headers=headers) #API request
    response_string = str(response_raw.text) #json.dumps did not work for me but this code did
    response_dict = json.loads(response_string) #JSON dictionary

    check_out = 'Check out this Chuck Norris Joke!'
    borders = ('-'*100) #borders

    print('\n') #Any separate new line commands exist on a separate line because they throw centering off
    print(check_out.center(112)) #centered msg before the joke
    print(borders.center(117)) #centered top border
    print(response_dict['value']) #uncentered joke - in Jupyter the text wraps around & centering looks bad
    print(borders.center(117)) #centered bottom border
    print('\n\nWant to save this joke for later? Copy the source URL below.')
    print(color.bold + 'SOURCE: ' + color.end, (response_dict['url']))

#Main program function runs the functions, with a loop for retrieving more jokes
def main():
    Welcome()
    while True:
        Get_Joke()
        New_Joke = input('\n\nWould you like another Chuck Norris joke? Type Y to continue or N to quit: ')
        if New_Joke.startswith('y') or New_Joke.startswith('Y'):
            continue
        elif New_Joke.startswith('n') or New_Joke.startswith('N'):
            Quit()
            break
        else:
            print('\n\nError: invalid input. Here\'s another joke for the road. If you want to quit, try again after the new joke.')

#Main Program
main()
