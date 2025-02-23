def move(game, target):
        game.current_scene = target

def take(game, item):
    game.inventory.append(item)
    del game.game_scenario[game.current_scene]["choices"][game.current_choice]
    game.current_choice = 0

def use(game, item, action, remove_item=True):
    if item in game.inventory:
        action()
        if remove_item:
            game.inventory.remove(item)
    else:
        game.message = f"You need {item} to do it."

def talk(game, dialogue):
    game.current_scene = dialogue
