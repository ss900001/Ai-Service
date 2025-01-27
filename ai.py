import json
import os
import subprocess
import requests
import urllib.parse
import webbrowser
import re
import os
import time

data_folder = 'data'
qa_file = os.path.join(data_folder, 'ai-con.json')
services_file = os.path.join(data_folder, 'services.json')


def initialize_files():
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    if not os.path.exists(qa_file):
        with open(qa_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps({}, indent=4))
    if not os.path.exists(services_file):
        with open(services_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps({}, indent=4))


def load_qa():
    try:
        with open(qa_file, 'r', encoding='utf-8') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}


def load_services():
    try:
        with open(services_file, 'r', encoding='utf-8') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}


def save_qa(data):
    with open(qa_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4))


def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # For Linux
        os.system('clear')

def execute_command(command):
    try:
        
        result = subprocess.run(["which", "msfvenom"], capture_output=True, text=True)
        if result.returncode != 0:
            return "Error: msfvenom is not installed or not found in the system path."


        if '>' in command:
            parts = command.split('>')
            cmd = parts[0].strip()
            output_file = parts[1].strip()


            output_dir = os.path.dirname(output_file)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)


            with open(output_file, 'wb') as f:
                result = subprocess.run(cmd, shell=True, stdout=f, stderr=subprocess.PIPE, text=True)
                if result.returncode == 0:
                    return f"Payload successfully created: {output_file}"
                else:
                    return f"Error: {result.stderr}"
        else:

            result = subprocess.run(command, shell=True, text=True, capture_output=True)
            return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"

    except Exception as e:
        return f"Failed to execute the command. Error: {e}"





def open_learning_module():
    html_file_path = os.path.join(data_folder, 'learning.html')  
    if os.path.exists(html_file_path):
        webbrowser.open(f'file://{os.path.abspath(html_file_path)}')
        print(f"Opening learning module: {html_file_path}")
    else:
        print("Error: Learning module file not found.")




def spy_mode():
    print("""
    SPY MODE ACTIVATED 
    ========================
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡀⠀⠀⢀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣤⣤⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⣿⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⣀⣠⠀⣶⣤⣄⣉⣉⣉⣉⣠⣤⣶⠀⣄⣀⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⣶⣾⣿⣿⣿⣿⣦⣄⣉⣙⣛⣛⣛⣛⣋⣉⣠⣴⣿⣿⣿⣿⣷⣶⠀⠀⠀
    ⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠛⠻⠿⠿⠿⠿⠿⠿⠿⠟⠛⠛⠛⠉⠉⠁⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣆⠀⠀⠀⢠⡄⠀⠀⠀⣰⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢀⣠⣶⣾⣿⡆⠸⣿⣶⣶⣾⣿⣿⣷⣶⣶⣿⠇⢰⣿⣷⣶⣄⡀⠀⠀⠀
    ⠀⠀⠺⠿⣿⣿⣿⣿⣿⣄⠙⢿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣿⣿⣿⣿⣿⠿⠗⠀⠀
    ⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣷⡄⠈⠙⠛⠛⠋⠁⢠⣾⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣀⣤⣬⣿⣿⣿⣇⠐⣿⣿⣿⣿⠂⣸⣿⣿⣿⣥⣤⣀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠘⠻⠿⠿⢿⣿⣿⣿⣧⠈⠿⠿⠁⣼⣿⣿⣿⡿⠿⠿⠟⠃⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⠀⣶⣦⠀⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    This mode allows you to search for a username or email across social media and web platforms.
          🔐Search by email has been disabled as it is not permitted for legal reasons.⚠️
                                       you can use username
    """)

    api_key = "API Key"  

    while True:
        choice = input("\nWould you like to search by 'username' or 'email' (or type 'exit' to leave): ").strip().lower()

        if choice == 'exit':
            print("Exiting spy mode... Returning to service mode.")
            break

        if choice == 'username':
            username = input("Enter the username to search for: ").strip()
            username_variations = [
                username.replace(" ", "_"),
                username.replace(" ", "."),
                username.replace(" ", ""),
                username.lower(),
                username.upper(),
                username.title(),
                username.replace(" ", "").lower(),
            ]

            social_media_platforms = {
                "Facebook": "https://www.facebook.com/",
                "Instagram": "https://www.instagram.com/",
                "Twitter": "https://www.twitter.com/",
                "LinkedIn": "https://www.linkedin.com/in/",
                "YouTube": "https://www.youtube.com/@",
                "GitHub": "https://github.com/",
                "TikTok": "https://www.tiktok.com/@",
                "Reddit": "https://www.reddit.com/user/",
                "Pinterest": "https://www.pinterest.com/",
                "Medium": "https://medium.com/@",
            }

            print(f"\nSearching for username '{username}'...\n")
            for variation in username_variations:
                print(f"\nChecking variation: '{variation}'")
                for platform, base_url in social_media_platforms.items():
                    url = base_url + variation
                    try:
                        response = requests.get(url, timeout=5)
                        if response.status_code == 200:
                            print(f"✅ Found on {platform}: {url}")
                        else:
                            print(f"❌ Not found on {platform}: {url}")
                    except requests.exceptions.RequestException:
                        print(f"❌ Not found on {platform}: {url}")
            print("\nUsername search complete! 🚀\n")

        elif choice == 'email':
            email = input("Enter the email address to search for: ").strip()
            params = {
                "api_key": api_key,
                "email": email,
            }
            try:
                response = requests.get("https://api.hunter.io/v2/email-verifier", params=params)
                if response.status_code == 200:
                    data = response.json()
                    if data.get("data"):
                        print("\n✅ Email information found:")
                        for key, value in data["data"].items():
                            print(f" - {key}: {value}")
                    else:
                        print("❌ No information found for this email.")
                else:
                    print(f"Error: {response.status_code} - {response.json().get('errors', 'Unknown error')}")
            except Exception as e:
                print(f"An error occurred: {e}")
            print("\nEmail search complete! 🚀\n")
        else:
            print("Invalid choice. Please choose 'username' or 'email'.")

def get_wireless_interface():
    try:

        output = subprocess.check_output("iw dev", shell=True, text=True)
        for line in output.splitlines():
            if line.strip().startswith("Interface"):
                interface = line.split()[1]
                return interface
    except Exception as e:
        print(f"Error while detecting wireless interface: {e}")
        return None


def monitor_mode():
    interface = get_wireless_interface()
    if not interface:
        print("No wireless interface found.")
        return

    print(f"Enabling Monitor Mode on interface: {interface}...")
    commands = [
        f"sudo ifconfig {interface} down",
        f"sudo iwconfig {interface} mode monitor",
        f"sudo ifconfig {interface} up",
        f"sudo airmon-ng check kill",
    ]

    for command in commands:
        print(f"Executing: {command}")
        output = subprocess.run(command, shell=True, text=True, capture_output=True)
        if output.returncode != 0:
            print(f"Error executing command: {command}\n{output.stderr}")
        else:
            print(f"Success: {command}")

def service_mode():
    services = load_services()
    print(""" 
              /\___/\ (( 
              \@_@'/  )) 
              {_:Y:.}_// 
Meawoo----------{_}^-'{_}---------- ❤️ ‍☀️ ‍💚
             /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$    /$$  
                    /$$__  $$ /$$$_  $$ /$$$_  $$ /$$$_  $$ /$$$_  $$ /$$$$  
  /$$$$$$$ /$$$$$$$| $$  \ $$| $$$$\ $$| $$$$\ $$| $$$$\ $$| $$$$\ $$|_  $$  
 /$$_____//$$_____/|  $$$$$$$| $$ $$ $$| $$ $$ $$| $$ $$ $$| $$ $$ $$  | $$  
|  $$$$$$|  $$$$$$  \____  $$| $$\ $$$$| $$\ $$$$| $$\ $$$$| $$\ $$$$  | $$  
 \____  $$\____  $$ /$$  \ $$| $$ \ $$$| $$ \ $$$| $$ \ $$$| $$ \ $$$  | $$  
 /$$$$$$$//$$$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$/ /$$$$$$
|_______/|_______/  \______/  \______/  \______/  \______/  \______/ |______ 

 Ai Service  version.1.0.0.0                                          
 Youtube channel Link https://www.youtube.com/@ss9oooo1/
    """)
    print("Enter Service Name😈 Or Type 'exit' to quit.")

    while True:
        print("\nPlease choose an option:")
        print("Type (show) to show  command  you can exute here or type 2 ✨")
        print("2. Show Option      (Show all available services working with AI. 🤖 )")
        choice = input("Please Entert The Number🤔 : ").strip()

        if choice == 'exit':
            print("Exiting service mode 🤕")
            break

        if choice == '2':  
            print("Service ss900001 selected!")
            while True:
                print("\nSelect an option for ss900001:")
                print("1. Activate Spy Mode         (Search and discover public information about any person on the web! 🔍 )")
                print("2. Learning Mode             (Discover the best ethical hacking tools for mastering cybersecurity! 🛡️ 💡)")
                print("3. Enable Monitor Mode       (with AI-powered service in just 1 second! 🚀)")
                print("4. Restart Networking        (Resolve network issues by restarting your networking service for a fresh connection! 🔄)")
                print("5. Fix Apache Permissions    ( Resolve issues with your Apache2 service by correcting permissions for smooth operation! 🛠️)")
                print("6. Go back to main menu")
                
                spy_choice = input("Please Entert The Number🤔 :  ").strip()

                if spy_choice == '1':
                    print("Activating Spy Mode...")
                    spy_mode()  
                elif spy_choice == '2':
                    print("Opening Learning Mode...")
                    open_learning_module()  
                elif spy_choice == '3':
                    print("Enabling Monitor Mode...")
                    
                    interface = get_wireless_interface()
                    if not interface:
                        print("No wireless interface found.")
                    else:
                        print(f"Enabling Monitor Mode on interface: {interface}...")
                        commands = [
                            f"sudo ifconfig {interface} down",
                            f"sudo iwconfig {interface} mode monitor",
                            f"sudo ifconfig {interface} up",
                            f"sudo airmon-ng check kill",
                        ]

                        for command in commands:
                            print(f"Executing: {command}")
                            output = subprocess.run(command, shell=True, text=True, capture_output=True)
                            if output.returncode != 0:
                                print(f"Error executing command: {command}\n{output.stderr}")
                            else:
                                print(f"Success: {command}")
                    
                elif spy_choice == '4':
                    
                    print("Restarting Networking...")
                    network_restart_command = services.get("network_restart")
                    if network_restart_command:
                        print(f"Executing: {network_restart_command}")
                        output = execute_command(network_restart_command)  
                        print(output)
                    
                elif spy_choice == '5':
                        print("Fixing Apache Permissions...")  
                        apache_fix_command = services.get("service apache2 fix")
                        if apache_fix_command:
                           print(f"Executing: {apache_fix_command}")
                           output = execute_command(apache_fix_command) 
                           print(output)
                        else:
                           print("Service 'service apache2 fix' not found in services.")
                elif spy_choice == '6':
                    print("Returning to the main menu...")
                    break  # Exit to main menu
                else:
                    print("Invalid choice. Please try again.")
            continue  

        if choice == "show":
            print("Available services:")
            for key, command in services.items():
                print(f"- {key}: {command}")
            continue

        if choice in services:
            command = services[choice]
            if "LHOST=" in command and "LPORT=" in command:
                lhost = input("Enter LHOST (IP Address): ").strip()
                lport = input("Enter LPORT (Port): ").strip()
                command = command.replace("YOUR_IP", lhost).replace("YOUR_PORT", lport)

            print(f"Executing command for service '{choice}': {command}")
            output = execute_command(command)
            print(output)
        else:
            print(f"Service '{choice}' not found.")










def search_wikipedia(question):
    search_url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch={question}"
    response = requests.get(search_url)

    if response.status_code == 200:
        data = response.json()
        search_results = data.get('query', {}).get('search', [])

        if search_results:
            title = search_results[0]['title']
            extract_url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&explaintext=&titles={title}"
            extract_response = requests.get(extract_url)

            if extract_response.status_code == 200:
                extract_data = extract_response.json()
                page = next(iter(extract_data['query']['pages'].values()))
                full_content = page.get('extract', "No content found.")

                
                summary = full_content[:500] + "..." if len(full_content) > 500 else full_content

                
                result = f"""
                
🌐 Search Result for Your Query
========================================
Title: {title}

📖Summary:

{summary}

🔗  more: [Explore full article on Wikipedia](https://en.wikipedia.org/wiki/{title.replace(' ', '_')})
========================================
                """
                return result.strip()
            else:
                return "Failed to retrieve article content."
        else:
            return "No relevant Wikipedia article found."
    else:
        return "Failed to search Wikipedia."

def search_youtube(query):

    encoded_query = urllib.parse.quote(query)
    youtube_url = f"https://www.youtube.com/results?search_query={encoded_query}"
    return f"Here are some YouTube search results for your question:\n{youtube_url}"

def main():
    initialize_files()
    while True:

        print("Welcome to the AI System! 🤖✨ We're here to make your experience smarter, faster, and more exciting. 🚀😊 You can:")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("1. Ask a Question – Get instant answers to anything you’re curious about! 💡❓")
        print("2. Activate service ss900001 - Unlock smart features tailored just for you! 🚀⚙️")
        print("Type 'exit' to quit.")

        try:
            choice = input("Please Enter the Number🤔 :  ").strip()

            if choice == 'exit':
                print("Goodbye🤨")
                break

            if choice == '1':
                print("\nI can provide information from the web to help you out! 🌐📚")
                print("However, I’m not advanced enough to have deep conversations just yet. 😊\n")

                while True:

                    question = input("Ask a question: ").strip().lower()

                    if question == 'exit':
                        print("Goodbye🤨")
                        break  
                    

                    if question == 'clear':
                        os.system('clear' if os.name == 'posix' else 'cls')
                        continue


                    answer = load_qa().get(question, None)
                    if answer:
                        print(f"Answer from database: {answer}")
                    else:

                        print("Searching ......⌛️")
                        wiki_result = search_wikipedia(question)
                        print(wiki_result)

                        print("Searching YouTube ⌛️...")
                        youtube_result = search_youtube(question)
                        print(youtube_result)


                    ask_another = input("\nDo you want to ask another question? (y/n): ").strip().lower()
                    if ask_another != 'y':
                        print("Returning to the main menu...\n")
                        break  

            elif choice == '2':

                service_mode()

            else:
                print("Invalid choice. Please enter 1 or 2.")

        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")






if __name__ == "__main__":
    main()
