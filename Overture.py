from manim import *
from constants import NUMBRIK_COLOR, TITLE_TEXT_POSITION


class Overture(Scene):
    def construct(self):
        # Opening text
        title_text = Text("Numbrik", color=NUMBRIK_COLOR).scale(
            1.5).move_to(TITLE_TEXT_POSITION)

        # Initialize DOTS
        dot = Circle(fill_opacity=1,
                     radius=0.125, stroke_width=0)

        dots = VGroup(*[dot.copy() for _ in range(3)]
                      ).arrange(RIGHT).next_to(title_text, DOWN, buff=0.4)

        dot_colors = [RED, YELLOW, GREEN]

        for dot, color in zip(dots, dot_colors):
            dot.set_fill(color)

        # Animations
        self.wait(0.5)
        self.play(Write(title_text), run_time=1.75)
        self.wait(0.5)

        for dot in dots:
            self.play(FadeIn(dot), run_time=0.5)

        # Closure
        self.play(FadeOut(title_text), FadeOut(dots))
        self.wait(0.5)
