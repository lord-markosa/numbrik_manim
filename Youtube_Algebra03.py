from manim import *
from utils.displayTitle import displayTitle
from utils.animateTextSeq import animateTextSeq
from utils.clearScreen import clearScreen


class Equations(Scene):
    def construct(self):
        # Title
        displayTitle(self, "Algebraic Equations")

        animateTextSeq(self, [MathTex("3x + 2"),
                              MathTex(r"3 \cdot 1 + 2 = 5"),
                              MathTex(r"3 \cdot 2 + 2 = 8"),
                              MathTex(r"3 \cdot \frac{2}{3} + 2 = 4"),
                              Text("When is this expression equal to 14?").scale(.6)])

        clearScreen(self)

        # Equation: 3x + 2 = 14
        animateTextSeq(self, [MathTex("3x + 2 = 14"),
                              MathTex("3x + 2 - 2 = 14 - 2"),
                              MathTex("3x = 12"),
                              MathTex("\\frac{3x}{3} = \\frac{12}{3}"),
                              MathTex("x = 4")])

        clearScreen(self)

        # Second Equation
        animateTextSeq(self, [MathTex("3x + 2 = x + 6"),
                              MathTex("3x + 2 - 2 = x + 6 - 2"),
                              MathTex("3x = x + 4"),
                              MathTex("3x - x = x + 4 - x"),
                              MathTex("2x = 4"),
                              MathTex("\\frac{2x}{2} = \\frac{4}{2}"),
                              MathTex("x = 2")])

        clearScreen(self)

        # Calculate faster
        animateTextSeq(self, [Text("Speed up using these").scale(.8),
                              Text("Move terms directly to the other side").scale(.6),
                              MathTex(r"+ \leftrightarrow -"),
                              MathTex(r"\times \leftrightarrow \div")])

        clearScreen(self)

        animateTextSeq(self, [MathTex("4(3x + 2) = 4x + 16"),
                              MathTex(
                                  "(3x + 2)} = \\frac{4x + 16}{4}"),
                              MathTex("3x + 2 = x + 4"),
                              MathTex("3x = x + 4 - 2")])

        clearScreen(self)

        animateTextSeq(self, [MathTex("3x = x + 2"),
                              MathTex("3x - x = 2"),
                              MathTex("2x = 2"),
                              MathTex(r"x = \frac{2}{2} = 1")])

        clearScreen(self)

        # Wrap up
        animateTextSeq(self, [Text("And that’s how we solve an equation!").scale(.6),
                              MathTex("5x - 3 = 2x + 9")])

        clearScreen(self)
