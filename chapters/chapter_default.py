import keyboard
import time
import os

from data import Data


class ChapterDefault:
    def __init__(self, game_state_manager):
        self.game_state_manager = game_state_manager

        self.data = Data()

        self.current_choice = 0

        self.message = ""

        self.inventory = []

    def print_header(self):
        print(self.game_scenario[self.current_scene]["text"])
        if self.inventory:
            print(f'Inventory: {", ".join(self.inventory)}\n')
        else:
            print('Inventory: empty\n')

        for choice in self.game_scenario[self.current_scene]["choices"]:
            if choice["text"] == self.game_scenario[self.current_scene]["choices"][self.current_choice]["text"]:
                print(f"> {choice["text"]}")
            else:
                print(choice["text"])

    def read_keys(self):
        key = keyboard.read_key()

        if key == "up":
            self.current_choice = max(0, self.current_choice - 1)
        if key == "down":
            self.current_choice = min(len(self.game_scenario[self.current_scene]["choices"]) - 1,
                                      self.current_choice + 1)
        if key == "enter":
            action = self.game_scenario[self.current_scene]["choices"][self.current_choice]["action"]
            action()
        if key == "s":
            save = self.data.load()
            save["current_chapter"] = self.game_state_manager.get_state()
            save[self.chapter_name+"_scene"] = self.current_scene
            self.data.save(save)

        time.sleep(.15)
    
    def print_footer(self):
        if self.message:
                print(self.message)

                key = keyboard.read_key()

                self.message = ""

        os.system("cls")

    def next_chapter(self):
        chapter_name = self.chapter_name.split("_")
        self.game_state_manager.set_state(f"{chapter_name[0].capitalize()} {int(chapter_name[1])+1}")
