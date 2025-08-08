from manim import *
from utils import *


class EquationsTheory(Scene):
    def construct(self):
        shots = [
            # self.intro,
            self.coeffRootsRelation,
            # self.complexNumbers,
            # self.fundamentalTheoremOfAlgebra,
            # self.conjugateTheory,
            # self.repeatedRootTheory,
        ]

        for shot in shots:
            shot()
            clearScreen(self)

    def intro(self):
        displayTitle(self, "Theory of Equations")
        animateTextSeq(
            self,
            [
                Text("Disclaimer", color=ORANGE),
                Text(
                    "You would require some prior knowledge explained in", font_size=32
                ),
                Text(
                    "Polynomial and Quadratic Equations' video",
                    font_size=32,
                    color=GREEN_N100,
                ),
                Text("Factor & remainder theorem", font_size=32),
                Text(
                    "Perfect square approach to solve quadratic equation", font_size=32
                ),
            ],
            wait_time=0.2,
            line_buffer=0.3,
        )

    def complexNumbers(self):
        animateTextSeq(
            self,
            [
                MathTex("\\text{Consider } x^2 + 1 = 0"),
                MathTex("x = \\pm\\sqrt{-1}"),
                MathTex(
                    "\\text{We define: } i = \\sqrt{-1}",
                    color=NUMBRIK_COLOR,
                ),
                MathTex("x = \\pm i"),
                Text("where i is an imaginary number", font_size=30),
            ],
        )

        clearScreen(self)

        lines = animateTextSeq(
            self,
            [
                MathTex("\\text{Consider } x^2 + 2x + 3 = 0"),
                MathTex("(x+1)^2 + 2 = 0"),
                MathTex("x = -1\\pm\\sqrt{2}i"),
                MathTex("\\text{now, }-1\\pm\\sqrt{2}i \\text{ is a complex number}"),
                MathTex(
                    "z = a+ib\\text{ where }z \\in \\mathbb{C}\\ \\& \\ a, b \\in \\mathbb{R}",
                    color=GREEN_N100,
                ),
            ],
        )

        self.play(Create(SurroundingRectangle(lines[-1], buff=0.25)))

        clearScreen(self)

        plane = (
            ComplexPlane(
                x_range=(-4, 4, 1),
                y_range=(-4, 4, 1),
            )
            .add_coordinates()
            .scale(0.8)
        )

        dot1 = Dot(plane.n2p(-1 + np.sqrt(2) * 1j), color=RED)
        dot2 = Dot(plane.n2p(-1 - np.sqrt(2) * 1j), color=RED)
        label1 = MathTex("-1+\\sqrt{2}i").next_to(dot1, LEFT).scale(0.7)
        label2 = MathTex("-1-\\sqrt{2}i").next_to(dot2, LEFT).scale(0.7)

        self.play(
            Create(plane),
            Create(
                plane.get_axis_labels(
                    x_label=MathTex("Re(z)").scale(0.5),
                    y_label=MathTex("Img(z)").scale(0.5),
                )
            ),
        )
        self.wait(1)
        self.play(
            Create(dot1), Create(dot2), Write(label1), Write(label2), run_time=1.25
        )

        clearScreen(self)

        animateTextSeq(
            self,
            [
                Text("Conjugate of Complex number:", font_size=36, color=NUMBRIK_COLOR),
                MathTex("\\overline{a+ib} = a-ib \\text{ where } a,b \\in \\mathbb{R}"),
                MathTex("\\overline{2+3i} = 2-3i"),
            ],
        )

    def fundamentalTheoremOfAlgebra(self):
        lines = animateTextSeq(
            self,
            [
                Text("Fundamental Theorem of Algebra", color=NUMBRIK_COLOR),
                MathTex(
                    "p(x) = a_nx^n + a_{n-1}x^{n-1} + a_{n-2}x^{n-2} + a_{n-3}x^{n-3} + ... + a_0"
                ),
                MathTex("\\text{has atleast 1 root in Complex Number }"),
                MathTex("\\text{given }deg(f) \\geq 1"),
                MathTex(
                    "p(h) = 0 \\text{ for some } h \\in \\mathbb{C}",
                    color=GREEN_N100,
                ),
            ],
            wait_time=0.2,
        )

        self.play(Create(SurroundingRectangle(lines[-1], buff=0.25)))

        clearScreen(self)

        lines = animateTextSeq(
            self,
            [
                MathTex(
                    "\\text{Every equation of }n^{th}\\text{ degree has }n\\text{ roots.}",
                    color=NUMBRIK_COLOR,
                ),
                MathTex(
                    "p(x) = a_nx^n + a_{n-1}x^{n-1} + a_{n-2}x^{n-2} + a_{n-3}x^{n-3} + ... + a_0"
                ),
                Text(
                    "Using fundamental theorem of Algebra, this has atleast 1 root. We can write",
                    font_size=30,
                ),
                MathTex("p(x) = (x-\\alpha_1)p_1(x) \\text{ where } deg(p_1) = n-1"),
                Text("Repeating the same n times we get", font_size=30),
                MathTex(
                    "p(x) = (x-\\alpha_1)(x-\\alpha_2)...(x-\\alpha_n)p_n,\\text{ where }deg(p_n) = 0",
                    color=GREEN_N100,
                ),
            ],
            wait_time=0.2,
        )

        clearScreen(self)

        animateTextSeq(
            self,
            [
                MathTex("\\text{Find the roots of}"),
                MathTex("x^3+8x^2+19x+12=0"),
            ],
            wait_time=0.2,
        )

    def coeffRootsRelation(self):
        # lines = animateTextSeq(
        #     self,
        #     [
        #         MathTex("ax^2+bx+c = 0"),
        #         MathTex("x^2+\\frac{b}{a}x+\\frac{c}{a} = 0"),
        #         MathTex(
        #             "\\text{Let the roots be }\\alpha\\text{, }\\beta\\text{, we can write:}",
        #         ).scale(0.8),
        #         MathTex("(x-\\alpha)(x-\\beta) = 0"),
        #         MathTex("x^2-(\\alpha+\\beta)x+\\alpha\\cdot\\beta"),
        #         MathTex(
        #             "\\implies -\\frac{b}{a} = \\alpha + \\beta, \\quad \\frac{c}{a} = \\alpha\\cdot\\beta",
        #             color=GREEN_N100,
        #         ),
        #     ],
        # )

        # self.play(Create(SurroundingRectangle(lines[-1], buff=0.25)))
        # clearScreen(self)

        lines = animateTextSeq(
            self,
            [
                MathTex("ax^3+bx^2+cx+d = 0"),
                MathTex("x^3+\\frac{b}{a}x^2+\\frac{c}{a}x+\\frac{d}{a} = 0"),
                MathTex(
                    "\\text{Let the roots be }\\alpha\\text{, }\\beta\\text{, }\\gamma\\text{, we can write:}",
                ).scale(0.8),
                MathTex("(x-\\alpha)(x-\\beta)(x-\\gamma) = 0"),
                MathTex(
                    "x^3-(\\alpha+\\beta+\\gamma)x^2+(\\alpha\\cdot\\beta+\\beta\\cdot\\gamma+\\gamma\\cdot\\alpha)x - \\alpha\\cdot\\beta\\cdot\\gamma = 0"
                ),
                MathTex(
                    "\\implies -\\frac{b}{a} = \\alpha + \\beta + \\gamma, \\quad \\frac{c}{a} = \\alpha\\cdot\\beta+\\beta\\cdot\\gamma+\\gamma\\cdot\\alpha, \\quad -\\frac{d}{a}=\\alpha\\cdot\\beta\\cdot\\gamma",
                    color=GREEN_N100,
                ).scale(0.9),
            ],
        )

        self.play(Create(SurroundingRectangle(lines[-1], buff=0.25)))

        clearScreen(self)

        # lines = animateTextSeq(
        #     self,
        #     [
        #         MathTex(
        #             "p(x) = a_nx^n + a_{n-1}x^{n-1} + a_{n-2}x^{n-2} + a_{n-3}x^{n-3} + ... + a_0"
        #         ),
        #         MathTex(
        #             "-\\frac{a_{n-1}}{a_n} = \\text{ sum of roots}", color=GREEN_N100
        #         ),
        #         MathTex(
        #             "\\frac{a_{n-2}}{a_n} = \\text{ sum of roots taken 2 at a time}",
        #             color=GREEN_N100,
        #         ),
        #         Text("so on...", font_size=32),
        #         MathTex(
        #             "(-1)^n\\frac{a_0}{a_n} = \\text{ product of roots}",
        #             color=GREEN_N100,
        #         ),
        #     ],
        #     shift_val=UP,
        # )

        # clearScreen(self)

        # self.play(
        #     Write(
        #         MathTex(
        #             "\\text{Form an equation with roots }1, 2, 3, 4 \\text{ and leading coefficient 1.}"
        #         ).move_to(TITLE_TEXT_POSITION)
        #     )
        # )

        # clearScreen(self)

        # animateTextSeq(
        #     self,
        #     [
        #         MathTex(
        #             "\\text{Find the condition which must be satisfied by the coefficients of}"
        #         ),
        #         MathTex(
        #             "x^3-px^2+qx-r=0 \\text{  when 2 of its roots }\\alpha, \\beta"
        #         ),
        #         MathTex("\\text{satisfies }\\alpha+\\beta = 0"),
        #     ],
        #     wait_time=0.2,
        # )

    def conjugateTheory(self):
        lines = animateTextSeq(
            self,
            [
                Text(
                    "In equation with Real coefficients,",
                    font_size=36,
                    color=NUMBRIK_COLOR,
                ),
                Text(
                    "Complex Root occurs in Conjugate Pairs",
                    font_size=36,
                    color=NUMBRIK_COLOR,
                ),
            ],
            line_buffer=0.2,
            wait_time=0.2,
            shift_val=2 * UP,
        )

        animateTextSeq(
            self,
            [
                MathTex("\\text{If }\\alpha+i\\beta \\text{ is a root of:}"),
                MathTex(
                    "p(x) = a_nx^n + a_{n-1}x^{n-1} + a_{n-2}x^{n-2} + a_{n-3}x^{n-3} + ... + a_0"
                ),
                MathTex("\\text{then }\\alpha-i\\beta \\text{ is also a root of }p(x)"),
            ],
            next_reference=lines[-1],
        )

        clearScreen(self)

        animateTextSeq(
            self,
            [
                MathTex("\\text{Solve the equation } x^4 + 4x^3 + 6x^2 + 4x + 5 = 0"),
                MathTex("\\text{Given one root is } i"),
            ],
            wait_time=0.2,
        )

    def repeatedRootTheory(self):
        lines = animateTextSeq(
            self,
            [
                MathTex(
                    "\\text{If }\\alpha \\text{ is a repeated root of } p(x)",
                    color=NUMBRIK_COLOR,
                ),
                MathTex(
                    "\\text{then } p'(\\alpha) = 0",
                    color=NUMBRIK_COLOR,
                ),
            ],
            line_buffer=0.2,
            wait_time=0.2,
            shift_val=2 * UP,
        )

        animateTextSeq(
            self,
            [
                MathTex("p(x) = (x-\\alpha)^mq(x)"),
                MathTex(
                    "\\Rightarrow p'(x) = m(x-\\alpha)^{m-1}q(x) + (x-\\alpha)^mq'(x)"
                ),
                MathTex(
                    "\\Rightarrow p'(x) = (x-\\alpha)^{m-1}(mq(x) + (x-\\alpha)q'(x))"
                ),
                MathTex("\\text{For } m > 1,\\ p'(\\alpha) = 0"),
            ],
            next_reference=lines[-1],
        )

        clearScreen(self)

        animateTextSeq(
            self,
            [
                MathTex(
                    "\\text{Show that } p(x) = x^3 + px + q \\text{ has a repeated root if}"
                ),
                MathTex("4p^3+27q^2=0"),
            ],
            wait_time=0.2,
        )
