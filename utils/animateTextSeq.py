from manim import *
from utils.constants import TITLE_TEXT_POSITION


def animateTextSeq(self, lines):
    if len(lines) > 5:
        lines[0].move_to(TITLE_TEXT_POSITION + 2*UP)
    else:
        lines[0].move_to(TITLE_TEXT_POSITION + UP)

    for i, line in enumerate(lines):
        if i > 0:
            line.next_to(lines[i-1], DOWN, buff=0.5)
        self.play(Write(line), run_time=2 if len(line) > 10 else 1.5)
        self.wait(2)

    return lines[-1]
