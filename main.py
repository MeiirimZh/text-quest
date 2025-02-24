from data import Data
from chapters.chapter1 import Chapter1
from chapters.chapter2 import Chapter2


class Game:
    def __init__(self):
        self.data = Data()
        self.current_chapter = self.data.load()["current_chapter"]
        self.chapter_1_scene = self.data.load()["chapter_1_scene"]
        self.chapter_2_scene = self.data.load()["chapter_2_scene"]
        
        self.game_state_manager = GameStateManager(self.current_chapter)
        self.chapter1 = Chapter1(self.game_state_manager, self.chapter_1_scene)
        self.chapter2 = Chapter2(self.game_state_manager, self.chapter_2_scene)

        self.chapters = {"Chapter 1": self.chapter1, "Chapter 2": self.chapter2}

    def run(self):
        while True:
            self.chapters[self.game_state_manager.get_state()].run()


class GameStateManager:
    def __init__(self, current_state):
        self.current_state = current_state

    def get_state(self):
        return self.current_state
    
    def set_state(self, state):
        self.current_state = state


if __name__ == "__main__":
    game = Game()
    game.run()
