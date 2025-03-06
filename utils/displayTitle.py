from manim import *
from utils.constants import NUMBRIK_COLOR, TITLE_TEXT_POSITION


def displayTitle(self, title):
    # Title
    title = Text(title, color=NUMBRIK_COLOR).scale(
        1.2).move_to(TITLE_TEXT_POSITION)
    self.play(Write(title))
    self.wait(0.5)
    self.play(FadeOut(title), run_time=0.5)
    self.wait(1)
