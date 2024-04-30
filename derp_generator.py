import os
from colorama import Fore, Style, init

def banner():
    init(autoreset=True)
    print(Fore.BLUE + Style.BRIGHT + """
                ⣀⣤⣴⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀      ⣠⡤⣤⣄⣾⣿⣿⣿⣿⣿⣿⣷⣠⣀⣄⡀⠀⠀⠀⠀ 
⠀⠀       ⠙⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣬⡿⠀⠀⠀⠀ 
⠀      ⠀    ⣼⠟⢿⣿⣿⣿⣿⣿⣿⡿⠘⣷⣄⠀⠀⠀⠀⠀ 
     ⣰⠛⠛⣿⢠⣿⠋⠀⠀⢹⠻⣿⣿⡿⢻⠁⠀⠈⢿⣦⠀⠀⠀⠀ 
     ⢈⣵⡾⠋⣿⣯⠀⠀⢀⣼⣷⣿⣿⣶⣷⡀⠀⠀⢸⣿⣀⣀⠀⠀ 
     ⢾⣿⣀⠀⠘⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⠿⣿⡁⠀⠀⠀ 
      ⠈⠙⠛⠿⠿⠿⢿⣿⡿⣿⣿⡿⢿⣿⣿⣿⣿⣷⣄⠀⠘⢷⣆⠀⠀ 
         ⠀⠀⢠⣿⠏⠀⣿⡏⠀⣼⣿⠛⢿⣿⣿⣆⠀⠀⣿⡇⡀ 
       ⠀⠀  ⣾⡟⠀⠀⣿⣇⠀⢿⣿⡀⠈⣿⡌⠻⠷⠾⠿⣻⠁ 
⠀      ⣠⣶⠟⠫⣤⠀⠀⢸⣿⠀⣸⣿⢇⡤⢼⣧⠀⠀⠀⢀⣿⠀  
     ⣾⡏⠀⡀⣠⡟⠀⠀⢀⣿⣾⠟⠁⣿⡄⠀⠻⣷⣤⣤⡾⠋⠀  
    ⠀⠙⠷⠾⠁⠻⣧⣀⣤⣾⣿⠋⠀⠀⢸⣧⠀⠀⠀⠉⠁⠀⠀⠀  
⠀⠀⠀        ⠈⠉⠉⠹⣿⣄⠀⠀⣸⡿⠀⠀⠀⠀⠀⠀⠀   
⠀⠀⠀⠀     ⠀⠀ ⠀ ⠀⠙⠛⠿⠟⠛⠁⠀               
""")
    print(Fore.MAGENTA + Style.BRIGHT + "                         Derp Generator                                  ")
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "                           By d1r7b46                                    \n" + Style.RESET_ALL)
    print("-" * 45)

if __name__ == "__main__":
    banner()

def generate_emails(domain):
    # Check if domain contains a dot
    if '.' not in domain:
        raise ValueError("Invalid domain name. Please provide a valid domain name.")

    # Read common usernames from file
    with open('common_usernames.txt', 'r') as file:
        common_usernames = file.read().splitlines()

    # Check if additional usernames file exists
    additional_usernames = []
    if os.path.exists('additional_usernames.txt'):
        with open('additional_usernames.txt', 'r') as file:
            additional_usernames = file.read().splitlines()

    # Generate email addresses
    emails = [username + '@' + domain for username in common_usernames]

    # Ask if users have been added to additional_users.txt
    add_additional = input("Have users been added to additional_usernames.txt? (y/n): ").lower()
    if add_additional == 'y':
        with open('additional_usernames.txt', 'r') as file:
            additional_usernames.extend(file.read().splitlines())
        emails.extend(username.strip() + '@' + domain for username in additional_usernames)
    elif add_additional != 'n':
        print("Invalid input. Assuming 'n'.")

    return emails

if __name__ == "__main__":
    domain = input("Enter the domain name: ")
    try:
        emails = generate_emails(domain)
        # Create a filename based on the domain
        filename = domain.split('.')[0] + "_unvalidated.txt"
        # Check if file already exists
        if os.path.exists(filename):
            raise FileExistsError(f"File {filename} already exists.")
        with open(filename, 'w') as output_file:
            for email in emails:
                output_file.write(email + '\n')
        print(f"\nGenerated emails are saved in {filename}")
    except ValueError as e:
        print(e)
    except FileExistsError as e:
        print(e)
