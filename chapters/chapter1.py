import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from chapters.chapter_default import ChapterDefault
from utils import move, take, use, talk


class Chapter1(ChapterDefault):
    def __init__(self, game_state_manager, current_scene):
        super().__init__(game_state_manager)

        self.chapter_name = "chapter_1"

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
                                  {"text": '"Teleport me to forest"', "action": lambda: move(self, "Forest")},
                                  {"text": '"Teleport me to home 2"', "action": lambda: self.next_chapter()}]}
        }

        self.current_scene = current_scene

    def run(self):
        self.print_header()
        self.read_keys()
        self.print_footer()

    def return_current_scene(self):
        return self.current_scene
