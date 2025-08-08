from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        question = MathTex(
            "f\\left(x - f(y)\\right) = f\\left(f(y)\\right) + xf(y) + f(x) - 1",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        question2 = MathTex(
            "\\text{Find } f:\\mathbb{R}\\to\\mathbb{R} \\quad \\forall \\, x, y \\in \\mathbb{R}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(question, DOWN, buff=0.6)

        self.play(FadeIn(question, question2, shift=0.7 * UP))

        self.wait(1)

        highlight(self, question, buff=0.2, wait_time=2)

        self.play(FadeOut(question2))

        step1 = MathTex(
            "\\text{Let } f(y) = x \\quad x, y \\in \\mathbb{R}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(question, DOWN, buff=0.75)

        step2 = MathTex(
            "f(0) = f(x) + x^2 + f(x) - 1",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step1, DOWN, buff=0.5)

        step3 = MathTex(
            "f(x) = \\frac{f(0)+1}{2} - \\frac{x^2}{2}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step2, DOWN, buff=0.5)

        step4 = MathTex(
            "f(x) = 1 - \\frac{x^2}{2}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step3, DOWN, buff=0.5)

        self.play(FadeIn(step1))
        self.wait(1)

        self.play(FadeIn(step2))
        self.wait(1)

        self.play(FadeIn(step3))
        highlight(self, step3, buff=0.2, wait_time=2)

        self.play(FadeIn(step4))
        highlight(self, step4, 0.2, 4)

        self.wait(4)


class Extras(Scene):
    def construct(self):
        e1 = MathTex(
            "x = y",
            color=NUMBRIK_COLOR,
        tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        e2 = MathTex(
            "x = f(y)",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(e1, 0)

        self.play(FadeIn(e1))
        self.wait(1)
        self.play(Transform(e1, e2))

        clearScreen(self, 4)

        e3 = MathTex(
            "\\text{for }x=0\\text{ we get:}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        e4 = MathTex(
            "f(0) = \\frac{f(0)+1}{2} - 0",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(e3, DOWN, buff=0.5)

        e5 = MathTex(
            "f(0) = 1",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(e4, DOWN, buff=0.5)

        self.play(FadeIn(e3))
        self.wait(1)
        self.play(FadeIn(e4))
        self.wait(1)
        self.play(FadeIn(e5))
        highlight(self, e5, buff=0.2, wait_time=4)

        self.wait(4)
