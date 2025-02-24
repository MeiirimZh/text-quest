import json


class Data:
    def __init__(self):
        self.path = "data.json"

    def save(self, data):
        with open(self.path, "w") as file:
            json.dump(data, file, indent=2)

    def load(self):
        try:
            with open(self.path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            self.save({"current_chapter": "Chapter 1",
                       "chapter_1_scene": "Home",
                       "chapter_2_scene": "Home 2",
                       "inventory": []})
            return {"current_chapter": "Chapter 1", "chapter_1_scene": "Home", "chapter_2_scene": "Home 2", "inventory": []}
