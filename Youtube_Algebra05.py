from manim import *


class CompletingTheSquare(Scene):
    def construct(self):
        eq1 = MathTex("x^2 + 6x + 5 = 0")
        eq2 = MathTex("x^2 + 6x + 9 - 9 + 5 = 0").shift(DOWN)
        eq3 = MathTex("(x+3)^2 - 4 = 0").shift(2 * DOWN)
        eq4 = MathTex("(x+3)^2 = 4").shift(3 * DOWN)
        eq5 = MathTex("x+3 = \\pm 2").shift(4 * DOWN)
        eq6 = MathTex("x = -3 \\pm 2").shift(5 * DOWN)
        eq7 = MathTex("x = -1, -5").shift(6 * DOWN)

        self.play(Write(eq1))
        self.wait(1)
        self.play(Transform(eq1, eq2))
        self.wait(1)
        self.play(Transform(eq1, eq3))
        self.wait(1)
        self.play(Transform(eq1, eq4))
        self.wait(1)
        self.play(Transform(eq1, eq5))
        self.wait(1)
        self.play(Transform(eq1, eq6))
        self.wait(1)
        self.play(Transform(eq1, eq7))
        self.wait(2)
