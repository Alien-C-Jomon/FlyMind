import sys, os, pathlib
sys.path.append("repo")
import utils as utl
import pandas as pd

print("--- FlyMind Neural Analysis ---")
df_spike = utl.load_exps(["./results/flymind_comparison/sugar_run.parquet", "./results/flymind_comparison/control_run.parquet"])
df_rate, df_rate_std = utl.get_rate(df_spike, t_run=0.5, n_run=2)
print("Total responding neurons in Sugar:", df_rate["sugar_run"].dropna().count())
print("Total responding neurons in Control:", df_rate["control_run"].dropna().count())

print("Initializing 3D Ursina Behavioral World...")
from ursina import *
app = Ursina()
window.title = "FlyMind: Sweet vs Bitter Decision World"
window.color = color.black

ground = Entity(model="plane", scale=(30, 1, 30), color=color.dark_gray)
sugar_zone = Entity(model="cube", scale=(4, 2, 4), position=(0, 1, 10), color=color.lime)
control_zone = Entity(model="cube", scale=(4, 2, 4), position=(0, 1, -10), color=color.red)

fly = Entity(model="sphere", color=color.yellow, scale=(1.5, 1, 2), position=(0, 1, 0))
text_status = Text(text="FlyMind Brain Active: Ready (Press S for Sugar, C for Control)", position=(-0.8, 0.45), scale=1.2, color=color.cyan)

active_stimulus = "sugar"

def update():
    global active_stimulus
    if held_keys["s"]:
        active_stimulus = "sugar"
        text_status.text = "Brain State: SUGAR TASTED - Feed Zone!"
        fly.color = color.lime
    if held_keys["c"]:
        active_stimulus = "control"
        text_status.text = "Brain State: CONTROL/BITTER - / Fleeing!"
        fly.color = color.red
        
    if active_stimulus == "sugar":
        fly.z += 3 * time.dt
        if fly.z > 10: fly.z = 10
    else:
        fly.z -= 3 * time.dt
        if fly.z < -10: fly.z = -10

def input(key):
    if key == "escape":
        application.quit()

print("3D Ursina World ready!")
app.run()
