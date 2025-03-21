from manim import *
from utils import *


class AlgebraicOperations(Scene):
    def construct(self):
        displayTitle(self, "Algebraic Operations")

        # Rules
        lines = animateTextSeq(
            self,
            [
                Text("Keep in mind"),
                Text("Group similar terms together").scale(0.6),
                Text("Then perform operations (+, -, x, ...)").scale(0.6),
                MathTex(
                    "2x^2y", "+", "3xy", "+", "1", "+", "5x^2y", "+", "2xy", "+", "4"
                ),
            ],
        )

        self.wait(0.5)

        self.play(
            lines[-1][0].animate.set_color(YELLOW),
            lines[-1][6].animate.set_color(YELLOW),
        )
        self.play(
            lines[-1][2].animate.set_color(RED), lines[-1][8].animate.set_color(RED)
        )
        self.play(
            lines[-1][4].animate.set_color(GREEN),
            lines[-1][10].animate.set_color(GREEN),
        )

        clearScreen(self)

        eqn1 = MathTex("2x", "+", "5", "+", "3").move_to(TITLE_TEXT_POSITION + UP)

        self.play(Write(eqn1), run_time=1.5)

        self.play(eqn1[0].animate.set_color(RED))
        self.play(eqn1[2:].animate.set_color(GREEN))

        eqn2 = MathTex("2x", "+", "8").next_to(eqn1, DOWN, buff=0.5)
        eqn2[0].set_color(RED)
        eqn2[2].set_color(GREEN)

        self.play(TransformFromCopy(eqn1[0], eqn2[0]))
        self.play(TransformFromCopy(eqn1[1], eqn2[1]))
        self.play(TransformFromCopy(eqn1[2:], eqn2[2]))

        self.wait(2)

        eqn3 = MathTex("2x", "+", "5", "+", "3x", "+", "2").next_to(
            eqn2, DOWN, buff=0.5
        )
        self.play(Write(eqn3), run_time=1.5)
        self.play(eqn3[0].animate.set_color(RED), eqn3[4].animate.set_color(RED))
        self.play(eqn3[2].animate.set_color(GREEN), eqn3[6].animate.set_color(GREEN))

        self.wait(2)

        eqn3_ = MathTex("2x", "+", "3x", "+", "5", "+", "2").next_to(
            eqn2, DOWN, buff=0.5
        )
        eqn3_[0].set_color(RED)
        eqn3_[2].set_color(RED)
        eqn3_[4].set_color(GREEN)
        eqn3_[6].set_color(GREEN)
        self.play(Transform(eqn3, eqn3_))

        eqn4 = MathTex("(2+3)x", "+", "5+2").next_to(eqn3_, DOWN, buff=0.5)
        eqn4[0].set_color(RED)
        eqn4[2].set_color(GREEN)

        self.play(TransformFromCopy(eqn3[0:3], eqn4[0]))
        self.play(TransformFromCopy(eqn3[3], eqn4[1]))
        self.play(TransformFromCopy(eqn3[4:], eqn4[2]))

        eqn5 = MathTex("5x", "+", "7").next_to(eqn4, DOWN, buff=0.5)
        eqn5[0].set_color(RED)
        eqn5[2].set_color(GREEN)

        self.play(TransformFromCopy(eqn4, eqn5), run_time=1.5)

        clearScreen(self)

        # Multiply
        animateTextSeq(
            self,
            [
                MathTex(r"3 \times (2x+5)"),
                MathTex(r"3 \cdot (2x+5)"),
                MathTex(r"3 \cdot 2x + 3 \cdot 5"),
                MathTex("6x + 15"),
            ],
        )

        clearScreen(self)

        animateTextSeq(
            self,
            [
                MathTex(r"3x \times (2x+5)"),
                MathTex(r"3x \cdot (2x+5)"),
                MathTex(r"3x \cdot 2x + 3x \cdot 5"),
                MathTex(r"3 \cdot 2 \cdot x \cdot x + 3 \cdot 5 \cdot x"),
                MathTex("6x^2 + 15x"),
            ],
        )

        clearScreen(self)

        # divide
        animateTextSeq(
            self,
            [
                MathTex(r" \frac{2x^2y+4xy}{2x}"),
                MathTex(r"\frac{2x^2y}{2x} + \frac{4xy}{2x}"),
                MathTex(r"xy +2y"),
            ],
        )

        clearScreen(self)

        # last problem

        eqn6 = MathTex(r" \frac{3x^2y + 6xy + 9x^2y + 3y^2x + 18}{3xy}").move_to(
            TITLE_TEXT_POSITION + 2 * UP
        )
        eqn6[0][0:4].set_color(GREEN)
        eqn6[0][9:13].set_color(GREEN)

        eqn7 = MathTex(r"\frac{12x^2y + 6xy + 3y^2x + 18}{3xy}").next_to(
            eqn6, DOWN, buff=0.5
        )

        eqn8 = MathTex(
            r"\frac{12x^2y}{3xy} + \frac{6xy}{3xy} + \frac{3y^2x}{3xy} + \frac{18}{3xy}"
        ).next_to(eqn7, DOWN, buff=0.5)

        eqn9 = MathTex(r"4x + 2 + y + \frac{6}{xy}").next_to(eqn8, DOWN, buff=0.5)

        self.play(Write(eqn6), run_time=2)
        self.wait(0.5)
        self.play(Write(eqn7), run_time=2)
        self.wait(0.5)
        self.play(Write(eqn8), run_time=2)
        self.wait(0.5)
        self.play(Write(eqn9), run_time=2)

        clearScreen(self)
