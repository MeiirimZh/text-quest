import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from chapters.chapter_default import ChapterDefault
from utils import move, take, use, talk


class Chapter2(ChapterDefault):
    def __init__(self, game_state_manager, current_scene, inventory):
        super().__init__(game_state_manager)

        self.chapter_name = "chapter_2"

        self.game_scenario = {
            "Home 2": {"text": "You're at home 2",
                     "choices": [{"text": "Go to forest", "action": lambda: move(self, "Forest 2")},
                                 {"text": "Stay at home", "action": lambda: move(self, "Home 2")}]},
            "Forest 2": {"text": "You're in forest 2",
                       "choices": [{"text": "Go to deep forest", "action": lambda: use(self, "Mysterious scroll", lambda: move(self, "Deep Forest 2"))},
                                   {"text": "Go back", "action": lambda: move(self, "Home")},
                                   {"text": "Take a mysterious scroll", "action": lambda: take(self, "Mysterious scroll")}]},
            "Deep Forest 2": {"text": "You're in deep forest 2. Suddenly you notice a person there.",
                            "choices": [{"text": '"Hello?"', "action": lambda: talk(self, "Hello")},
                                        {"text": "Go back", "action": lambda: move(self, "Forest")}]},
            "Hello 2": {"text": 'Stranger: "Hello stranger 2! I am a wizard, that can teleport people!"',
                      "choices": [{"text": '"Teleport me to my home"', "action": lambda: move(self, "Home")},
                                  {"text": '"Teleport me to forest"', "action": lambda: move(self, "Forest")}]}
        }

        self.current_scene = current_scene
        self.inventory = inventory

    def run(self):
        self.print_header()
        self.read_keys()
        self.print_footer()

    def return_current_scene(self):
        return self.current_scene
