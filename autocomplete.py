import os
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
from colorama import Fore, Style


class AutoComplete:
    def __init__(self):
        self.create_folder()
        self.history_path = os.path.join('./bin', 'history.dat')
        self.history = FileHistory(self.history_path)
        self.completer = WordCompleter(self.load_history(), ignore_case=True)

    def create_folder(self):
        try:
            os.mkdir('./bin')
        except FileExistsError:
            pass

    def load_history(self):
        try:
            with open(self.history_path, 'r') as file:
                return file.read().splitlines()
        except FileNotFoundError:
            return []

    def save_history(self, url):
        with open(self.history_path, 'a') as file:
            file.write(f'{url}\n')
        self.completer = WordCompleter(self.load_history(), ignore_case=True)

    def show_history(self):
        print(f"\n{Fore.GREEN}History:{Style.RESET_ALL}")
        for url in self.load_history():
            print(f"{Fore.YELLOW}{url}{Style.RESET_ALL}")
        print()

    def get_user_input(self, prompt_message):
        return prompt(prompt_message,
                      history=self.history,
                      auto_suggest=AutoSuggestFromHistory(),
                      )
