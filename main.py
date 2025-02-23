import keyboard
import os
import time


class Game:
    def __init__(self):
        self.game_scenario = {
            "Home": {"text": "You're at home",
                     "choices": [{"text": "Go to forest", "action": lambda: self.move("Forest")},
                                 {"text": "Stay at home", "action": lambda: self.move("Home")}]},
            "Forest": {"text": "You're in forest",
                       "choices": [{"text": "Go to deep forest", "action": lambda: self.use("Mysterious scroll", lambda: self.move("Deep Forest"))},
                                   {"text": "Go back", "action": lambda: self.move("Home")},
                                   {"text": "Take a mysterious scroll", "action": lambda: self.take("Mysterious scroll")}]},
            "Deep Forest": {"text": "You're in deep forest. Suddenly you notice a person there.",
                            "choices": [{"text": '"Hello?"', "action": lambda: self.talk("Hello")},
                                        {"text": "Go back", "action": lambda: self.move("Forest")}]},
            "Hello": {"text": 'Stranger: "Hello stranger! I am a wizard, that can teleport people!"',
                      "choices": [{"text": '"Teleport me to my home"', "action": lambda: self.move("Home")},
                                  {"text": '"Teleport me to forest"', "action": lambda: self.move("Forest")}]}
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

    def move(self, target):
        self.current_scene = target

    def take(self, item):
        self.inventory.append(item)
        del self.game_scenario[self.current_scene]["choices"][self.current_choice]
        self.current_choice = 0

    def use(self, item, action, remove_item=True):
        if item in self.inventory:
            action()
            if remove_item:
                self.inventory.remove(item)
        else:
            self.message = f"You need {item} to do it."

    def talk(self, dialogue):
        self.current_scene = dialogue


if __name__ == "__main__":
    game = Game()
    game.run()
