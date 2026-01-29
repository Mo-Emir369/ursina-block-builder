from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from pathlib import Path

from world import World
from save_system import save_world, load_world
from blocks import BLOCK_ORDER
from ui import HUD
from pause_menu import PauseMenu


app = Ursina()

window.title = "Ursina Block Builder"
window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = True

player = FirstPersonController()
player.cursor.visible = True

Sky()

# Sounds
place_sfx = Audio('assets/sounds/place.wav', autoplay=False)
break_sfx = Audio('assets/sounds/break.wav', autoplay=False)

# World + HUD
world = World()
hud = HUD()

WORLD_PATH = Path("worlds/world.json")

def do_save():
    save_world(WORLD_PATH, world.to_save_data())
    print("Saved")

def do_load():
    data = load_world(WORLD_PATH)
    world.load_from_data(data)
    print("Loaded")

pause = PauseMenu(player=player, on_save=do_save, on_load=do_load)

# Starter ground
for z in range(20):
    for x in range(20):
        world.add_block((x, 0, z), "grass")

# Load if exists
data = load_world(WORLD_PATH)
if data:
    world.load_from_data(data)

selected_idx = 0
reach = 6  # build/break distance

def get_target():
    # Ignore player + UI hotbar
    return raycast(
        camera.world_position,
        camera.forward,
        distance=reach,
        ignore=[player, hud.hotbar]
    )

def input(key):
    global selected_idx

    # Toggle pause menu
    if key == 'escape':
        if pause.enabled:
            pause.hide()
        else:
            pause.show()
        return

    # Save / Load even while paused
    if key == 'f5':
        do_save()
        return

    if key == 'f9':
        do_load()
        return

    # If paused, block gameplay input
    if pause.enabled:
        return

    # Scroll selection
    if key in ('scroll up', 'scroll down'):
        if key == 'scroll up':
            selected_idx = (selected_idx + 1) % hud.n
        else:
            selected_idx = (selected_idx - 1) % hud.n
        hud.set_selected(selected_idx)
        return

    # Number selection 1..9
    if key.isdigit():
        n = int(key)
        if 1 <= n <= hud.n:
            selected_idx = n - 1
            hud.set_selected(selected_idx)
        return

    # Place / Break
    hit = get_target()
    if hit and hit.hit:
        if key == 'left mouse down':
            place_pos = hit.entity.position + hit.normal
            if world.add_block(place_pos, BLOCK_ORDER[selected_idx]):
                place_sfx.play()

        elif key == 'right mouse down':
            if world.remove_block(hit.entity.position):
                break_sfx.play()

app.run()
