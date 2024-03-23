# Pseudocode
# 1. Install pyfiglet and colorama module
    # pip install pyfiglet
    # pip install colorama

# 2. Import pyfiglet (for fonts) and colorama (for color and style)
# 3. From pyfiglet import figlet and from colorama import foreground and style
import pyfiglet
from pyfiglet import Figlet
import colorama
from colorama import Fore, Style

# 4. Ask for name (input)
name = input("Enter your name: ")

# 5. Ask for dream job (input)
dream_job = input("Enter your dream job: ")

# 6. Ask when to expect to graduate (in years)
expected_graduation = input("When do you expect to graduate? (enter number of years only): ")

# 7. Display name, dream job, and message in a fancy way
figlet = Figlet(font = '3d-ascii')
result = (f"{name}, YOU WILL BE AN AMAZING {dream_job} IN {expected_graduation} YEARS! AIM HIGH AND REACH THAT DREAM!")
print(f"\n{Fore.CYAN}{Style.BRIGHT}{figlet.renderText(result)}")