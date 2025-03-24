from manim import *


# Constants

TITLE_TEXT_POSITION = ORIGIN + UP
NUMBRIK_COLOR = ManimColor("#1099FF")


# Utility Functions


def displayTitle(self, title):
    # Title
    title = Text(title, color=NUMBRIK_COLOR).scale(1.2).move_to(TITLE_TEXT_POSITION)
    self.play(Write(title))
    self.wait(0.5)
    self.play(FadeOut(title), run_time=0.5)
    self.wait(1)


def animateTextSeq(
    self,
    lines,
    shift_val=0,
    next_reference=0,
    wait_time=1,
    iterative_callback=None,
    line_buffer=0.5,
):
    if len(lines) > 5:
        lines[0].move_to(TITLE_TEXT_POSITION + 2 * UP)
    elif len(lines) >= 3:
        lines[0].move_to(TITLE_TEXT_POSITION + UP)
    else:
        lines[0].move_to(TITLE_TEXT_POSITION)

    lines[0].shift(shift_val)

    if next_reference != 0:
        lines[0].next_to(next_reference, DOWN, buff=0.75)

    for i, line in enumerate(lines):
        if i > 0:
            line.next_to(lines[i - 1], DOWN, buff=line_buffer)
        self.play(Write(line), run_time=2 if len(line) > 10 else 1.5)
        self.wait(wait_time)
        iterative_callback(lines[i]) if iterative_callback is not None else None

    return lines


def clearScreen(self, wait_time=4):
    self.wait(wait_time)
    self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
