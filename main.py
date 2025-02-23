import keyboard
import os
import time

from utils import move, take, use, talk


class Game:
    def __init__(self):
        self.game_scenario = {
            "Home": {"text": "You're at home",
                     "choices": [{"text": "Go to forest", "action": lambda: move(self, "Forest")},
                                 {"text": "Stay at home", "action": lambda: move(self, "Home")}]},
            "Forest": {"text": "You're in forest",
                       "choices": [{"text": "Go to deep forest", "action": lambda: use(self, "Mysterious scroll", lambda: move(self, "Deep Forest"))},
                                   {"text": "Go back", "action": lambda: move(self, "Home")},
                                   {"text": "Take a mysterious scroll", "action": lambda: take(self, "Mysterious scroll")}]},
            "Deep Forest": {"text": "You're in deep forest. Suddenly you notice a person there.",
                            "choices": [{"text": '"Hello?"', "action": lambda: talk(self, "Hello")},
                                        {"text": "Go back", "action": lambda: move(self, "Forest")}]},
            "Hello": {"text": 'Stranger: "Hello stranger! I am a wizard, that can teleport people!"',
                      "choices": [{"text": '"Teleport me to my home"', "action": lambda: move(self, "Home")},
                                  {"text": '"Teleport me to forest"', "action": lambda: move(self, "Forest")}]}
        }



        self.current_scene = "Home"
        self.current_choice = 0

        self.message = ""

        self.inventory = []

    def run(self):
        while True:
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

            key = keyboard.read_key()

            if key == "up":
                self.current_choice = max(0, self.current_choice - 1)
            if key == "down":
                self.current_choice = min(len(self.game_scenario[self.current_scene]["choices"]) - 1,
                                          self.current_choice + 1)
            if key == "enter":
                action = self.game_scenario[self.current_scene]["choices"][self.current_choice]["action"]
                action()

            time.sleep(.15)

            if self.message:
                print(self.message)

                key = keyboard.read_key()

                self.message = ""

            os.system("cls")


if __name__ == "__main__":
    game = Game()
    game.run()
