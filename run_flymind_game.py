from ursina import *
import time
import random

app = Ursina()
window.title = 'FlyMind Chemosensory Sandbox'
window.color = color.black

# Overhead camera view
camera.position = (0, 20, -14)
camera.rotation_x = 55

# Arena floor
ground = Entity(model='plane', scale=(30, 1, 30), color=color.dark_gray)

fly = Entity(model='cube', color=color.yellow, scale=(1, 0.8, 1.5), position=(0, 0.5, 0))

sugar_items = []
bitter_items = []

status_text = Text(text='Click buttons below to spawn Sugar (S) or Bitter (B)!', position=(-0.85, 0.45), scale=1.1, color=color.cyan)

def spawn_sugar():
    # Spawn random location around the arena
    pos = Vec3(random.uniform(-8, 8), 0.75, random.uniform(-8, 8))
    item = Entity(model='cube', color=color.lime, scale=(1.5, 1.5, 1.5), position=pos)
    sugar_items.append({'entity': item, 'time': time.time()})
    status_text.text = 'Sugar spawned! Fly approaching...'

def spawn_bitter():
    # Spawn random location around the arena
    pos = Vec3(random.uniform(-8, 8), 0.75, random.uniform(-8, 8))
    item = Entity(model='cube', color=color.red, scale=(1.5, 1.5, 1.5), position=pos)
    bitter_items.append({'entity': item, 'time': time.time()})
    status_text.text = 'BITTER SPAWNED! Fly fleeing!'

Button(text='Spawn Sugar (S)', color=color.lime, scale=(0.25, 0.08), position=(-0.6, -0.4), on_click=spawn_sugar)
Button(text='Spawn Bitter (B)', color=color.red, scale=(0.25, 0.08), position=(-0.3, -0.4), on_click=spawn_bitter)

def update():
    global sugar_items, bitter_items
    current_time = time.time()
    
    # 10-second decay timer cleanup
    for s in list(sugar_items):
        if current_time - s['time'] > 10:
            destroy(s['entity'])
            sugar_items.remove(s)
            
    for b in list(bitter_items):
        if current_time - b['time'] > 10:
            destroy(b['entity'])
            bitter_items.remove(b)
            
    # Fly AI: Bitter takes absolute priority (fleeing)
    fleeing = False
    for b in bitter_items:
        dist = distance(fly.position, b['entity'].position)
        if dist < 12:
            dir_away = (fly.position - b['entity'].position).normalized()
            fly.position += dir_away * 7 * time.dt
            fly.look_at(fly.position + dir_away)
            status_text.text = 'BITTER SENSED! Frantically fleeing!'
            fleeing = True
            break
            
    if not fleeing and sugar_items:
        closest = min(sugar_items, key=lambda s: distance(fly.position, s['entity'].position))
        dist = distance(fly.position, closest['entity'].position)
        if dist > 0.8:
            fly.look_at(closest['entity'].position)
            fly.position += fly.forward * 4 * time.dt
            status_text.text = 'Approaching Sugar reward...'
        else:
            status_text.text = 'Feasting on Sugar!'
    elif not fleeing and not sugar_items:
        status_text.text = 'Exploring arena... Press S or B to spawn stimuli'

def input(key):
    if key == 's':
        spawn_sugar()
    elif key == 'b':
        spawn_bitter()
    elif key == 'escape':
        application.quit()

app.run()
