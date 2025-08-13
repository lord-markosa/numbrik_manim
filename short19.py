from manim import *
from utils import *


class Problem(Scene):
    def construct(self):
        themeColor = GREY_N500

        question = VGroup(
            MathTex(
                "\\text{Find the maximum value of}",
                color=GREY_N800,
            ),
            MathTex("2^{sin^2{x}} + 2^{cos^2{x}}", color=GREY_N800).scale(1.1),
        ).arrange(DOWN)

        self.play(FadeIn(question, shift=UP))
        self.wait(10)


class Statements(Scene):
    def construct(self):
        statement_groups = [
            [
                "\\text{Let }Y = 2^{sin^2{x}}",
                "2^{sin^2{x}} + 2^{1-sin^2{x}}",
                "\\Rightarrow 2^{sin^2{x}} + \\frac{2}{2^{sin^2{x}}}",
                "\\Rightarrow Y + \\frac{2}{Y}",
            ],
            [
                "\\frac{Y + \\frac{2}{Y}}{2} \\ge \\sqrt{Y\\cdot\\frac{2}{Y}}",
                "\\Rightarrow Y+\\frac{2}{Y} \\ge 2\\sqrt{2}",
            ],
        ]

        for statements in statement_groups:
            prev = 0
            for stmt in statements:
                mathStmt = nMath(stmt)
                if prev == 0:
                    mathStmt.to_edge(UP)
                else:
                    mathStmt.next_to(prev, DOWN, buff=0.5)
                self.play(FadeIn(mathStmt))
                prev = mathStmt
                self.wait(1)
            clearScreen(self)


class Options(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        options = (
            VGroup(
                MathTex("A) \\ 2\\sqrt{2}", color=BLACK),
                MathTex("B) \\ \\sqrt{2}", color=BLACK),
                MathTex("C) \\ 4\\sqrt{2}", color=BLACK),
                MathTex("D) \\ 2", color=BLACK),
            )
            .arrange(DOWN, center=False, buff=0.25, aligned_edge=LEFT)
            .to_edge(UP)
        )

        self.play(FadeIn(options))
        self.wait(5)

        self.wait(1)
        self.play(Create(SurroundingRectangle(options[0], corner_radius=0.1, buff=0.1)))
        self.wait(4)
