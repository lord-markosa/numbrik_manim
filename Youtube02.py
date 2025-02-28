from manim import *


class ExponentialEquation(Scene):
    def construct(self):
        # Title
        title = Text('Can you solve it?').to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Equations
        eq1 = MathTex("2^{x+1} + 3^{y+1} = 43").shift(2*UP)
        eq2 = MathTex("3\cdot2^x + 2\cdot3^y = 42").next_to(eq1,
                                                            DOWN, buff=0.5)

        self.play(Write(eq1))
        self.play(Write(eq2))
        self.wait(1)

        # Replace equation 1 with simplified equation
        simpEq1 = MathTex("2\cdot2^x + 3\cdot3^y = 43").move_to(eq1)
#         step2 = MathTex(r"6x + 4y = 84").next_to(step1, DOWN, buff=0.5)

        self.play(ReplacementTransform(eq1, simpEq1))
        self.wait(1)

        # Replace exponential terms with linear terms

        newEq1 = MathTex("2X + 3Y = 43").move_to(simpEq1)
        newEq2 = MathTex("3X + 2Y = 42").move_to(eq2)

        self.play(ReplacementTransform(simpEq1, newEq1))
        self.play(ReplacementTransform(eq2, newEq2))
        self.wait(1)

        # add equations

        step1 = MathTex(r"5X + 5Y = 85").next_to(newEq2, DOWN, buff=0.5)
        step2 = MathTex(r"X+Y = 17").move_to(step1)

        self.play(Write(step1))
        self.wait(1)
        self.play(ReplacementTransform(step1, step2))
        self.wait(1)

        # subtract equations

        step3 = MathTex(r"-X+Y = 1").next_to(step2, DOWN, buff=0.5)

        self.play(Write(step3))
        self.wait(1)

        # add both the equation to get the value of Y

        step4 = MathTex(r"2Y = 18").next_to(step3, DOWN, buff=0.5)
        step5 = MathTex(r"Y = 9").move_to(step4)
        step6 = MathTex(r"X = 8").next_to(step5, DOWN, buff=0.5)
        self.play(Write(step4))

        self.wait(1)
        self.play(ReplacementTransform(step4, step5))
        self.wait(1)
        self.play(Write(step6))
        self.wait(1)

        step7 = MathTex(r"3^y = 9 \implies y = 2").move_to(step5)
        step8 = MathTex(r"2^x = 8 \implies x = 3").move_to(step6)

        self.play(ReplacementTransform(step5, step7))
        self.wait(1)
        self.play(ReplacementTransform(step6, step8))
        self.wait(1)
