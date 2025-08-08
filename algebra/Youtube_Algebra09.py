from manim import *
from utils import *


class SynDiv(Scene):
    def construct(self):
        ## SCENE 1

        exp = (
            MathTex(
                "(",
                "2",
                "x^3",
                "+ 3",
                "x^2",
                "-4",
                "x",
                "+5",
                ")",
                "\\div",
                "(x",
                "+",
                "2",
                ")",
            )
            .to_edge(UP)
            .scale(0.8)
        )

        self.play(Write(exp))

        # Step 1: Write the dividend and divisor

        divisor = MathTex(r"x+2").to_edge(LEFT).shift(UP)
        dividend = MathTex(r"\overline{\smash{\big)} 2x^3 + 3x^2 - 4x + 5}").next_to(
            divisor, RIGHT
        )
        quotient = MathTex("2x^2", "-x", "-2").next_to(dividend, UP)

        self.play(Write(divisor), Write(dividend))
        self.wait(1)

        minus = MathTex("-")

        # Step 2: Write the first subtraction step

        first_subtraction = MathTex(r"\underline{2x^3 +4x^2}", color=YELLOW).next_to(
            dividend[0][2], DOWN, aligned_edge=LEFT
        )
        first_remainder = MathTex("-", "x^2 -4x").next_to(
            first_subtraction[0][3], DOWN, aligned_edge=LEFT
        )
        self.play(dividend[0][2].animate.set_color(YELLOW))
        self.wait(0.5)
        self.wait(1)
        self.play(Write(quotient[0]))

        self.play(Write(first_subtraction), run_time=1.5)
        self.play(Write(minus.copy().next_to(first_subtraction, LEFT)))
        self.wait(1)
        self.play(Write(first_remainder))
        self.wait(1)

        # Step 3: Write the second subtraction step
        second_subtraction = MathTex(r"\underline{-x^2 -2x ", color=YELLOW).next_to(
            first_remainder, DOWN, aligned_edge=LEFT
        )
        second_remainder = MathTex("-2", "x + 5").next_to(
            second_subtraction[0][3], DOWN, aligned_edge=LEFT, buff=0.5
        )

        self.play(first_remainder[0].animate.set_color(YELLOW))
        self.wait(0.5)
        self.play(Write(quotient[1]))
        self.wait(1)
        self.play(Write(second_subtraction), run_time=1.5)
        self.play(Write(minus.copy().next_to(second_subtraction, LEFT)))
        self.wait(1)
        self.play(Write(second_remainder))
        self.wait(1)

        # Step 4: Write the third subtraction step

        third_subtraction = MathTex(r"\underline{-2x -4}", color=YELLOW).next_to(
            second_remainder, DOWN, aligned_edge=LEFT
        )
        third_remainder = MathTex("9").next_to(
            third_subtraction[0][4], DOWN, aligned_edge=LEFT
        )

        self.play(second_remainder[0].animate.set_color(YELLOW))
        self.wait(0.5)
        self.play(Write(quotient[2]))
        self.wait(1)
        self.play(Write(third_subtraction), run_time=1.5)
        self.play(Write(minus.copy().next_to(third_subtraction, LEFT)))
        self.wait(1)
        self.play(Write(third_remainder))
        self.wait(1)

        synthDiv = (
            Table(
                [
                    ["2", "2", "3", "-4", "5"],
                    ["-", " ", "4", "-2", "-4"],
                    [" ", "2", "-1", "-2", "9"],
                ]
            )
            .scale(0.6)
            .to_edge(RIGHT)
        )

        synthDiv.get_vertical_lines()[0].set_color(NUMBRIK_COLOR)
        synthDiv.get_horizontal_lines()[0].set_color(NUMBRIK_COLOR)
        synthDiv.get_entries((1, 1)).set_color(GREEN_N100)

        self.play(
            Create(synthDiv.get_rows()[0]),
            Create(synthDiv.get_horizontal_lines()),
            Create(synthDiv.get_vertical_lines()),
            Write(
                synthDiv.get_entries(
                    (2, 1),
                )
            ),
        )

        self.wait(1)

        arrow_ = Arrow(exp[13], synthDiv.get_entries((1, 1)))
        self.play(Create(arrow_))
        self.play(FadeOut(arrow_))

        self.wait(1)

        for i in range(4):
            arrow = Arrow(exp[2 * i + 1], synthDiv.get_entries((1, i + 2)))
            self.play(exp[2 * i + 1].animate.set_color(YELLOW))
            self.play(Create(arrow))
            self.play(synthDiv.get_entries((1, i + 2)).animate.set_color(YELLOW))
            self.play(FadeOut(arrow))

        self.wait(1)

        # First entry
        arrow1 = Arrow(synthDiv.get_entries((1, 2)), synthDiv.get_entries((3, 2)))
        self.play(Create(arrow1))
        self.play(Write(synthDiv.get_entries((3, 2))))
        self.play(FadeOut(arrow1))

        for i in range(3):
            arrow1 = Arrow(
                synthDiv.get_entries((1, 1)), synthDiv.get_entries((3, i + 2))
            )
            arrow2 = Arrow(
                synthDiv.get_entries((3, i + 2)), synthDiv.get_entries((2, i + 3))
            )
            self.play(Create(arrow1))
            self.play(Create(arrow2))
            self.play(Write(synthDiv.get_entries((2, i + 3))))
            self.wait(1)
            self.play(FadeOut(arrow1), FadeOut(arrow2))
            self.play(Write(synthDiv.get_entries((3, i + 3))))
            self.wait(1)

        self.wait(1)

        exp = MathTex(
            "\\text{quotient }=",
            "2",
            "x^2",
            "-",
            "x",
            "-2",
        ).next_to(synthDiv, DOWN, buff=0.75, aligned_edge=RIGHT)

        self.play(Write(exp[0]))

        for i in range(3):
            arrow1 = Arrow(synthDiv.get_entries((3, 2 + i)), exp[2 * i + 1])
            self.play(Create(arrow1))
            self.play(Write(exp[2 * i + 1]))
            if i != 2:
                self.play(Write(exp[2 * i + 2]))
            self.play(FadeOut(arrow1))

        self.wait(1)

        self.play(synthDiv.get_entries((3, 5)).animate.set_color(RED))
        self.play(
            Write(
                MathTex("\\text{remainder }= 9").next_to(
                    exp, DOWN, buff=0.25, aligned_edge=LEFT
                )
            )
        )

        self.wait(4)

        clearScreen(self)

        ## SCENE 2

        exp = (
            MathTex(
                "(",
                "2",
                "x^4",
                "+5",
                "x^3",
                "+7",
                "x^2",
                "+16",
                "x",
                "+15",
                ")",
                "\\div",
                "(2x",
                "+",
                "3",
                ")",
            )
            .to_edge(UP)
            .scale(0.8)
        )

        self.play(Write(exp))

        synthDiv = Table(
            [
                ["3/2", "2", "5", "7", "16", "15"],
                ["-", " ", "3", "3", "6", "15"],
                [" ", "2", "2", "4", "10", "0"],
            ]
        ).scale(0.6)

        synthDiv.get_vertical_lines()[0].set_color(NUMBRIK_COLOR)
        synthDiv.get_horizontal_lines()[0].set_color(NUMBRIK_COLOR)
        synthDiv.get_entries((1, 1)).set_color(GREEN_N100)

        self.play(
            Create(synthDiv.get_rows()[0]),
            Create(synthDiv.get_horizontal_lines()),
            Create(synthDiv.get_vertical_lines()),
            Write(
                synthDiv.get_entries(
                    (2, 1),
                )
            ),
        )

        self.wait(1)

        arrow_ = Arrow(exp[13], synthDiv.get_entries((1, 1)))
        self.play(Create(arrow_))
        self.play(FadeOut(arrow_))

        self.wait(1)

        for i in range(5):
            arrow = Arrow(exp[2 * i + 1], synthDiv.get_entries((1, i + 2)))
            self.play(exp[2 * i + 1].animate.set_color(YELLOW))
            self.play(Create(arrow))
            self.play(synthDiv.get_entries((1, i + 2)).animate.set_color(YELLOW))
            self.play(FadeOut(arrow))

        # First entry
        arrow1 = Arrow(synthDiv.get_entries((1, 2)), synthDiv.get_entries((3, 2)))
        self.play(Create(arrow1))
        self.play(Write(synthDiv.get_entries((3, 2))))
        self.play(FadeOut(arrow1))

        self.wait(1)

        for i in range(4):
            arrow1 = Arrow(
                synthDiv.get_entries((1, 1)), synthDiv.get_entries((3, i + 2))
            )
            arrow2 = Arrow(
                synthDiv.get_entries((3, i + 2)), synthDiv.get_entries((2, i + 3))
            )
            self.play(Create(arrow1))
            self.play(Create(arrow2))
            self.play(Write(synthDiv.get_entries((2, i + 3))))
            self.wait(1)
            self.play(FadeOut(arrow1), FadeOut(arrow2))
            self.play(Write(synthDiv.get_entries((3, i + 3))))
            self.wait(1)

        self.wait(1)

        exp2 = MathTex(
            "\\text{quotient }=",
            "2",
            "x^3",
            "+ 2",
            "x^2",
            "+ 4",
            "x",
            "+ 10",
        ).next_to(synthDiv, DOWN, buff=0.75, aligned_edge=RIGHT)

        exp3 = MathTex(
            "\\text{actual quotient }=",
            "x^3",
            "+",
            "x^2",
            "+ 2",
            "x",
            "+ 5",
        ).next_to(synthDiv, DOWN, buff=0.75, aligned_edge=RIGHT)

        self.play(Write(exp2[0]))

        for i in range(4):
            arrow1 = Arrow(synthDiv.get_entries((3, 2 + i)), exp2[2 * i + 1])
            self.play(Create(arrow1))
            self.play(Write(exp2[2 * i + 1]))
            if i != 3:
                self.play(Write(exp2[2 * i + 2]))
            self.play(FadeOut(arrow1))

        self.wait(1)

        self.play(synthDiv.get_entries((3, 6)).animate.set_color(RED))

        self.play(Transform(exp2, exp3))

        self.play(
            Write(
                MathTex("\\text{remainder }= 0").next_to(
                    exp2, DOWN, buff=0.25, aligned_edge=LEFT
                )
            )
        )

        self.wait(4)
