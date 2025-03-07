from manim import *


def clearScreen(self):
    self.wait(4)
    self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
