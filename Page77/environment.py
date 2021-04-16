import tkinter as tk
from tkinter import Button
import time
import numpy as numpy
from PIL import ImageTk, Image

PhotoImage = ImageTk.PhotoImage
UNIT = 100 # 픽셀 수
HEIGHT = 5 # 그리드월드 세로
WIDTH = 5 # 그리드월드 가로
TRANSITION_PROB = 1
POSSIBLE_ACTIONS = [0, 1, 2, 3] # 좌, 우, 상, 하
ACTIONS = [(-1,0), (1,0), (0,-1), (0,1)] # 좌표로 나타낸 행동
REWARDS = []

class GraphicDisplay(tk.Tk):
    def __init__(self, agent):
        super(GraphicDisplay, self).__init__()
        self.title('Policy Iteration')
        self.geometry('{0}x{1}'.format(HEIGHT * UNIT, HEIGHT * UNIT + 50))
        self.texts = []
        self.arrows = []
        self.env = Env()
        self.agent = agent
        self.evaluation_count = 0
        self.improvement_count = 0
        self.is_moving = 0
        (self.up, self.down, self.left, self.right), self.shapes = self.load_images()
        self.canvas = self._build_canvas()
        self.text_reward(2, 2, "R : 1.0")
        self.text_reward(1, 2, "R : -1.0")
        self.text_reward(2, 1, "R : -1.0")