from manim import *
from utils import *


class thankyouScene(Scene):
    def construct(self):
        expression = (
            Text("Like, Subscribe and Share!", color=ManimColor("#1099FF"))
            .scale(1.2)
            .move_to(ORIGIN + UP)
        )
        self.play(Write(expression), run_time=2)
        self.wait(4)


class temp(Scene):
    def construct(self):
        animateTextSeq(
            self, [MathTex("(a+b)^2 = a^2 + 2ab + b^2", color=NUMBRIK_COLOR).scale(1.2)]
        )
