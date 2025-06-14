from manim import *
from utils import *

class Trash(Scene):
    def construct(self):

        # long division trash
        # # Create each part of the long division
        # divisor = MathTex("x+4").shift(LEFT * 2)
        # dividend = MathTex(r"x^2+2x+3").next_to(divisor, RIGHT, buff=0.5)
        # division_line = MathTex(r"\overline{\phantom{x^2+2x+3}}").next_to(
        #     dividend, DOWN, buff=0.1
        # )
        # subtraction = MathTex(r"-~(x^2-2x)").next_to(
        #     division_line, DOWN, aligned_edge=LEFT
        # )
        # remainder1 = MathTex(r"0+4x+3").next_to(subtraction, DOWN, aligned_edge=LEFT)
        # subtraction2 = MathTex(r"-~(4x-8)").next_to(remainder1, DOWN, aligned_edge=LEFT)
        # remainder2 = MathTex(r"0+11").next_to(subtraction2, DOWN, aligned_edge=LEFT)

        # # Group all parts together
        # long_division = VGroup(
        #     divisor,
        #     dividend,
        #     division_line,
        #     subtraction,
        #     remainder1,
        #     subtraction2,
        #     remainder2,
        # )

        # # Animate the long division
        # self.play(Write(long_division))
        # self.wait(2)
        # self.play(FadeOut(long_division))

        # header = Text("Polynomial Long Division").to_edge(UP)
        # dividend = MathTex("2x^4 + 3x^3 + 2x^2 + x + 1").scale(1.2)
        # divisor = MathTex("x + 5").scale(1.2).next_to(dividend, DOWN)

        # self.play(Write(header))
        # self.play(Write(dividend))
        # self.play(Write(divisor))

        # quotient = MathTex("2x^3 - 7x^2 + 37x - 184").next_to(divisor, DOWN)
        # remainder = MathTex("Remainder = 921").next_to(quotient, DOWN)

        # self.wait(1)
        # self.play(Write(quotient))
        # self.play(Write(remainder))
        # self.wait(2)
        # self.play(FadeOut(dividend, divisor, quotient, remainder, header))

        # self.play(
        #     Write(
        #         MathTex(
        #             r"\begin{array}{r}2x^3-7x^2+37x-184\phantom{)}\\x+5{\overline{\smash{\big)}\,2x^4 + 3x^3 + 2x^2 + x + 1\phantom{)}}}\\\underline{-~\phantom{(}(2x^4+10x^3) \ \ \ \ \ \ \ \ \ \ \ \ \ \phantom{-b)}}\\-7x^3+2x^2\ \ \ \ \ \ \ \ \ \ \ \phantom{)}\\ \underline{-~\phantom{()}(-7x^3-35x^2) \ \ \ \ \ \ \ \ \ \ }\\ 37x^2+x \ \ \ \ \ \phantom{)}\\ \underline{-~\phantom{()}(37x^2+185x)} \\ -184x+1\phantom{)} \\ \underline{-~\phantom{()}(-184x-920)} \\ 921\phantom{)}\end{array}",
        #         )
        #     ),
        #     run_time=6,
        # )
