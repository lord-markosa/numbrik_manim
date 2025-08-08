from manim import *
from utils import *


class Polynomials(Scene):
    def construct(self):
        shots = [
            self.intro,
            self.numberOfTerms,
            self.degreeOfPolynomial,
            self.operations,
            self.multiplication,
            self.longDivision,
            self.noteOnDivision,
            self.remainderTheorem,
            self.factorTheorem,
            self.remainderTheoremEx,
            self.factorTheoremEx,
        ]

        for shot in shots:
            shot()
            clearScreen(self)

    def intro(self):
        displayTitle(self, "Polynomials")
        animateTextSeq(
            self,
            [
                MathTex(
                    "\\text{Polynomial } =",
                    "\\text{ poly }",
                    "+",
                    "\\text{nomial}",
                    color=NUMBRIK_COLOR,
                ),
                Text('poly means "many"').scale(0.7),
                Text('nomial means "names" (here terms)').scale(0.7),
                MathTex("3x^3+2x^2+5x-7"),
            ],
        )

    def numberOfTerms(self):
        header = Text("Types of Polynomials", color=NUMBRIK_COLOR).to_edge(UP)
        table = MobjectTable(
            [
                [MathTex("3x^2"), Text("Monomial").scale(0.7)],
                [MathTex("2x + 5"), Text("Binomial").scale(0.7)],
                [MathTex("x^2 - 4x + 7"), Text("Trinomial").scale(0.7)],
                [MathTex("x^3 + 2x^2 - x + 6"), Text("Polynomial").scale(0.7)],
            ],
            line_config={
                "stroke_opacity": 0,
            },
        ).next_to(header, DOWN)

        self.play(Write(header))
        self.wait(1)

        for i in range(4):
            self.play(Create(table.get_rows()[i]))
            self.wait(2)

        self.wait(2)

    def degreeOfPolynomial(self):
        header = Text("Degree of a Polynomial", color=NUMBRIK_COLOR).to_edge(UP)
        table = (
            MobjectTable(
                [
                    [
                        MathTex("5x^4", "+ 2x^3 - x + 7").set_color_by_tex(
                            "5x^4", GREEN
                        ),
                        MathTex("4"),
                        MathTex("5"),
                    ],
                    [
                        MathTex("x^3", "+ 3x^2 - 5").set_color_by_tex("x^3", GREEN),
                        MathTex("3"),
                        MathTex("1"),
                    ],
                    [
                        MathTex("4x^2", "+ 2x").set_color_by_tex("4x^2", GREEN),
                        MathTex("2"),
                        MathTex("4"),
                    ],
                    [MathTex("5", color=GREEN), MathTex("0"), MathTex("5")],
                    [
                        MathTex("7x^2y^3", "+ 6xy + 5").set_color_by_tex(
                            "7x^2y^3", GREEN
                        ),
                        MathTex("2+3 = 5"),
                        MathTex("7"),
                    ],
                ],
                col_labels=[
                    Text("Expression").scale(0.7),
                    Text("Degree").scale(0.7),
                    Text("Leading Coeff").scale(0.7),
                ],
                line_config={
                    "stroke_opacity": 0,
                },
            )
            .scale(0.8)
            .next_to(header, DOWN)
        )

        self.play(Write(header))
        self.wait(1)

        self.play(Create(table.get_rows()[0]))
        for i in range(5):
            self.play(Create(table.get_rows()[i + 1]), run_time=1.5)
            self.wait(2)

    #
    # self.wait(2)

    #
    def operations(self):
        displayTitle(self, "Operations on Polynomials")

        seq = animateTextSeq(
            self,
            [
                MathTex("(x^2 + 2x) + (3x^2 - x + 5)"),
                MathTex("(1+3)x^2 + (2-1)x + 5"),
                MathTex("4x^2 + x + 5"),
                Text("NOTE: here we operate on the cofficients").scale(0.7),
                Text("of terms with same power of the variables").scale(0.7),
            ],
        )

        self.play(FadeOut(*seq))

        animateTextSeq(
            self,
            [
                MathTex("(x^2 + 2x) - (3x^2 - x + 5)"),
                MathTex("(1-3)x^2 + (2-(-1))x - 5"),
                MathTex("-2x^2 + 3x - 5"),
            ],
        )

    def remainderTheorem(self):
        displayTitle(self, "Remainder Theorem")
        animateTextSeq(
            self,
            [
                MathTex(
                    "\\text{Remainder when } P(x) \\text{ is divided by } (x-a) = P(a)",
                    color=NUMBRIK_COLOR,
                ),
                Text("Proof:"),
                MathTex(
                    "\\text{Let } g(x) \\text{ be the quotient when } P(x) \\text { is divided by } (x-a)"
                ),
                MathTex("P(x) = g(x)(x-a) + R", color=GREEN),
                MathTex(
                    "\\text{where R is the constant remainder as } (x-a) \\text{ is linear}"
                ),
                MathTex("P(x=a) = g(x=a)(a-a) + R"),
                MathTex("\\implies P(a) = R", color=NUMBRIK_COLOR),
            ],
        )

    def factorTheorem(self):
        displayTitle(self, "Factor Theorem")
        animateTextSeq(
            self,
            [
                MathTex(
                    r"(x-a) \text{ is a factor of } P(x) \text{ iff } P(a) = 0",
                    color=NUMBRIK_COLOR,
                ),
                Text("Proof:"),
                MathTex("\\text{Using Remainder theorem}"),
                MathTex("P(x) = g(x)(x-a) + R", color=GREEN),
                MathTex("\\text{if } (x-a) \\text{ is a factor then R = 0} "),
                MathTex("P(x=a) = g(x=a)(a-a) + 0"),
                MathTex("\\implies P(a) = 0", color=NUMBRIK_COLOR),
            ],
        )

    def multiplication(self):
        displayTitle(self, "Polynomial Multiplication")

        poly1 = MathTex("x^2+2x+3").to_edge(UP).shift(DOWN)
        poly2 = MathTex(r"\underline{x^2+4x+5}").next_to(
            poly1, DOWN, aligned_edge=RIGHT
        )
        part1 = MathTex("5x^2", "+ 10x", "+ 15").next_to(
            poly2, DOWN, aligned_edge=RIGHT
        )
        part2 = MathTex("4x^3", "+ 8x^2", "+ 12x").next_to(
            part1[1], DOWN, aligned_edge=RIGHT
        )
        part3 = MathTex("x^4+2x^3+3x^2").next_to(part2[1], DOWN, aligned_edge=RIGHT)

        self.play(Write(poly1), Write(poly2))
        self.wait(1)
        self.play(Write(part1))
        self.wait(1)
        self.play(Write(part2))
        self.wait(1)
        self.play(Write(part3))
        self.wait(1)
        self.play(
            Write(
                MathTex("\\overline{x^4 + 6x^3 + 15x^2 + 22x + 15}").next_to(
                    part3[0], DOWN, aligned_edge=LEFT
                )
            )
        )
        self.wait(1)

    def longDivision(self):
        displayTitle(self, "Polynomial Division")
        # Step 1: Write the dividend and divisor

        divisor = MathTex(r"x+5").to_corner(UL).shift(DOWN)
        dividend = MathTex(
            r"\overline{\smash{\big)} 2x^4 + 3x^3 + 2x^2 + x + 1}"
        ).next_to(divisor, RIGHT)
        quotient = MathTex("2x^3", "-7x^2", "+37x", "-184").next_to(dividend, UP)

        self.play(Write(divisor), Write(dividend))
        self.wait(1)

        minus = MathTex("-")

        # Step 2: Write the first subtraction step

        firstMultiplication = MathTex(r"2x^3(x+5)").to_edge(RIGHT).shift(UP)
        firstMultiplication_ = MathTex(r"2x^4 + 10x^3", color=YELLOW).next_to(
            firstMultiplication, DOWN
        )
        first_subtraction = MathTex(r"\underline{2x^4 + 10x^3}", color=YELLOW).next_to(
            dividend, DOWN, aligned_edge=LEFT
        )
        first_remainder = MathTex("-7", "x^3 + 2x^2").next_to(
            first_subtraction[0][3], DOWN, aligned_edge=LEFT
        )
        self.play(dividend[0][2].animate.set_color(YELLOW))
        self.wait(0.5)
        self.play(Write(firstMultiplication))
        self.play(Write(firstMultiplication_))
        self.wait(1)
        self.play(Write(quotient[0]))

        self.play(Write(first_subtraction), run_time=1.5)
        self.play(Write(minus.copy().next_to(first_subtraction, LEFT)))
        self.wait(1)
        self.play(Write(first_remainder))
        self.wait(1)

        # Step 3: Write the second subtraction step
        secondMultiplication = MathTex(r"-7x^2(x+5)").to_edge(RIGHT).shift(UP)
        secondMultiplication_ = MathTex(r"-7x^3 -35x^2", color=YELLOW).next_to(
            secondMultiplication, DOWN
        )
        second_subtraction = MathTex(
            r"\underline{-7x^3 - 35x^2 ", color=YELLOW
        ).next_to(first_remainder, DOWN, aligned_edge=LEFT)
        second_remainder = MathTex("37", "x^2 + x").next_to(
            second_subtraction[0][5], DOWN, aligned_edge=LEFT
        )

        self.play(first_remainder[0].animate.set_color(YELLOW))
        self.wait(0.5)
        self.play(Write(quotient[1]))
        self.play(FadeOut(firstMultiplication, firstMultiplication_))
        self.play(Write(secondMultiplication))
        self.play(Write(secondMultiplication_))
        self.wait(1)
        self.play(Write(second_subtraction), run_time=1.5)
        self.play(Write(minus.copy().next_to(second_subtraction, LEFT)))
        self.wait(1)
        self.play(Write(second_remainder))
        self.wait(1)

        # Step 4: Write the third subtraction step

        thirdMultiplication = MathTex(r"37x(x+5)").to_edge(RIGHT).shift(UP)
        thirdMultiplication_ = MathTex(r"37x^2 + 185x", color=YELLOW).next_to(
            thirdMultiplication, DOWN
        )
        third_subtraction = MathTex(r"\underline{37x^2 + 185x}", color=YELLOW).next_to(
            second_remainder, DOWN, aligned_edge=LEFT
        )
        third_remainder = MathTex("-184", "x + 1").next_to(
            third_subtraction[0][4], DOWN, aligned_edge=LEFT
        )

        self.play(second_remainder[0].animate.set_color(YELLOW))
        self.wait(0.5)
        self.play(Write(quotient[2]))
        self.play(FadeOut(secondMultiplication, secondMultiplication_))
        self.play(Write(thirdMultiplication))
        self.play(Write(thirdMultiplication_))
        self.wait(1)
        self.play(Write(third_subtraction), run_time=1.5)
        self.play(Write(minus.copy().next_to(third_subtraction, LEFT)))
        self.wait(1)
        self.play(Write(third_remainder))
        self.wait(1)

        # Step 5: Write the final subtraction step

        finalMultiplication = MathTex(r"-184(x+5)").to_edge(RIGHT).shift(UP)
        finalMultiplication_ = MathTex(r"-184x - 920", color=YELLOW).next_to(
            finalMultiplication, DOWN
        )
        final_subtraction = MathTex(r"\underline{-184x - 920}", color=YELLOW).next_to(
            third_remainder, DOWN, aligned_edge=LEFT
        )
        final_remainder = MathTex(r"921").next_to(
            final_subtraction[0][6], DOWN, aligned_edge=LEFT
        )

        self.play(third_remainder[0].animate.set_color(YELLOW))
        self.wait(0.5)
        self.play(Write(quotient[3]))
        self.play(FadeOut(thirdMultiplication, thirdMultiplication_))
        self.play(Write(finalMultiplication))
        self.play(Write(finalMultiplication_))
        self.wait(1)
        self.play(Write(final_subtraction), run_time=1.5)
        self.wait(1)
        self.play(Write(final_remainder))
        self.wait(1)

    def noteOnDivision(self):
        animateTextSeq(
            self,
            [
                Text("The degree of remainder polynomial", color=NUMBRIK_COLOR).scale(
                    0.7
                ),
                Text(
                    "is always one less than that of divisor polynomial",
                    color=NUMBRIK_COLOR,
                ).scale(0.7),
                Text("In the previous example:").scale(0.5),
                MathTex("\\text{divisor } = x+5 \\Rightarrow \\text{ deg } = 1"),
                MathTex(
                    "\\text{remainder } = 921 \\Rightarrow \\text{ deg } = 0 \\  (= 1 - 1)"
                ),
            ],
        )

    def remainderTheoremEx(self):
        animateTextSeq(
            self,
            [
                MathTex(
                    "f(x) = x^4 - 2x^3 + x - 5, \\text{ find remainder when divided by } x-2"
                ),
                Text("Using remainder theorem:"),
                MathTex("\\text{Remainder }= f(2)"),
                MathTex("f(2) = 2^4 - 2\\cdot2^3 + 2 - 5"),
                MathTex("\\implies \\text{ Remainder }= -3"),
            ],
        )

    def factorTheoremEx(self):
        animateTextSeq(
            self,
            [
                MathTex(
                    "x^3 - 3x^2 - x + 3,\\text{ check if } x-1 \\text{ is a factor}"
                ),
                MathTex("\\text{Let's calculate } f(1)"),
                MathTex("f(1) = 1^3 - 3\\cdot1^2 - 1 + 3 = 0"),
                MathTex(
                    "\\text{Hence using Factor theorem } f(1) \\text{ is a factor}"
                ),
            ],
        )
