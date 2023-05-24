import os
from colorama import Fore, Style
from bypass_vip import BypassVip
from autocomplete import AutoComplete


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    bypass = BypassVip()
    autocomplete = AutoComplete()
    bypass.print_header()

    try:
        while True:
            print(
                f"{Fore.GREEN}[1] Enter a single URL\n[2] Enter multiple URLs from a file\n[3] View Support Sites\n[4] View History\n[0] Exit{Style.RESET_ALL}")
            choice = autocomplete.get_user_input(
                f"\nEnter your choice: ")

            if choice == '1':
                url = autocomplete.get_user_input(f"\nEnter the URL: ")
                autocomplete.save_history(url)
                response = bypass.post_url(url)

                if response.status_code == 200:
                    bypass.print_result(response.json())
                else:
                    bypass.print_error("Error, please try again later")

            elif choice == '2':
                file_path = autocomplete.get_user_input(
                    f"\nEnter the file path: ")
                try:
                    with open(file_path, 'r') as file:
                        file_urls = file.read().splitlines()

                    for url in file_urls:
                        autocomplete.save_history(url)
                        response = bypass.post_url(url)

                        if response.status_code == 200:
                            bypass.print_result(response.json())
                        else:
                            bypass.print_error("Error, please try again later")
                except FileNotFoundError:
                    bypass.print_error("File not found. Please try again.")

            elif choice == '3':
                bypass.print_supported_websites()

            elif choice == '4':
                autocomplete.show_history()

            elif choice == '0':
                print(f"{Fore.GREEN}Exiting...{Style.RESET_ALL}")
                break

            else:
                print(
                    f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"{Fore.RED}\nInterrupted by user. Exiting...{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
