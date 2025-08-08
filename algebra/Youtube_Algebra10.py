from manim import *
from utils import *


class Exponents(Scene):
    def construct(self):
        shots = [self.intro, self.rules, self.radicals, self.graphs, self.problem]

        for shot in shots:
            shot()
            clearScreen(self)

    def intro(self):
        displayTitle(self, "Exponents")

        animateTextSeq(
            self,
            [
                MathTex(r"a^n = a \, \times \, a \, \times \, \dots \, (n \ times)"),
                MathTex(r"a^{\frac{1}{2}} = \sqrt{a}"),
                MathTex(r"a^{\frac{1}{3}} = \sqrt[3]{a}"),
            ],
        )

    def rules(self):
        animateTextSeq(
            self,
            [
                MathTex("a^x \\cdot a^y = a^{x+y}"),
                MathTex("(a^x)^y = a^{xy}"),
                MathTex("a^{-1} =  \\dfrac{1}{a}"),
            ],
        )

        clearScreen(self)

        animateTextSeq(
            self,
            [
                MathTex("a^0 = 1"),
                MathTex("1^n = 1"),
            ],
        )

        clearScreen(self)

        animateTextSeq(
            self,
            [
                MathTex("(ab)^n = a^n \\cdot b^n"),
                Text("Distributive Law", font_size=30),
            ],
        )

        clearScreen(self)

        animateTextSeq(
            self,
            [
                MathTex("\\frac{a^x}{a^y}"),
                MathTex("= a^x \\cdot (a^{y})^{-1}"),
                MathTex("= a^{x + (-y)}"),
                MathTex("= a^{x - y}"),
            ],
        )

        clearScreen(self)

        animateTextSeq(
            self,
            [
                MathTex("\\frac{a^2 \cdot a^{\\frac{1}{2}}}{a^3}"),
                MathTex("= a^{2 + \\frac{1}{2} - 3}"),
                MathTex("= a^{-\\frac{1}{2}}"),
            ],
        )

    def radicals(self):
        animateTextSeq(self, [MathTex("a^{\\frac{m}{n}} = \, \sqrt[n]{a^m}")])
        clearScreen(self)
        animateTextSeq(
            self,
            [
                MathTex("27^{\\frac{2}{3}}"),
                MathTex("= (27^{\\frac{1}{3}})^2"),
                MathTex("= 3^2"),
                MathTex("= 9"),
            ],
        )

    def graphs(self):
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-1, 9],
            x_length=10,
            y_length=7,
            axis_config={"include_numbers": True},
        )

        graph = axes.plot(lambda x: 2**x, x_range=[-3.5, 3], color=NUMBRIK_COLOR)
        label = MathTex("y = 2^x", color=NUMBRIK_COLOR).next_to(graph, RIGHT)

        graph2 = axes.plot(lambda x: 2 ** (-x), x_range=[-3, 3.5], color=RED_A)
        label2 = MathTex(
            "y = \\left(\\frac{1}{2}\\right)^x = 2^{-x}", color=RED_A
        ).next_to(graph2, LEFT)

        self.play(Create(axes), Create(graph), Write(label))
        self.wait(2)
        self.play(Create(graph2), Create(label2))

    def problem(self):
        animateTextSeq(self, [MathTex("\\text{Solve:}"), MathTex("2^x = x+1")])
        clearScreen(self)

        axes = Axes(
            x_range=[-5, 5],
            y_range=[-1, 10],
            x_length=8,
            y_length=6,
            axis_config={"include_numbers": True},
        )

        exp_graph = axes.plot(lambda x: 2**x, x_range=[-3.5, 3], color=GREEN)
        exp_label = MathTex("y = 2^x", color=GREEN).next_to(exp_graph, UP + RIGHT)

        line_graph = axes.plot(lambda x: x + 1, x_range=[-3.5, 3], color=RED)
        line_label = MathTex("y = x + 1", color=RED).next_to(line_graph, UP + RIGHT)

        point_a = Dot(axes.coords_to_point(0, 1), color=NUMBRIK_COLOR)

        point_b = Dot(axes.coords_to_point(1, 2), color=NUMBRIK_COLOR)

        self.play(Create(axes))
        self.play(Create(exp_graph), Write(exp_label))
        self.play(Create(line_graph), Write(line_label))
        self.wait(1)
        self.play(Create(point_a))
        self.play(Create(point_b))
        self.wait(3)
