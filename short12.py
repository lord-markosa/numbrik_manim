from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # PART 1
        question = (
            VGroup(
                MathTex(
                    "\\text{Given }",
                    "x-4y = 9",
                    color=BLACK,
                ),
                MathTex(
                    "\\text{Find the value of }",
                    "\\frac{5^x}{625^y}",
                    color=BLACK,
                ),
            )
            .arrange(DOWN, center=False, buff=0.25, aligned_edge=LEFT)
            .to_edge(UP)
        )

        self.play(FadeIn(question, shift=UP))
        self.wait(2)

        highlight01 = SurroundingRectangle(question[0][1], corner_radius=0.1, buff=0.1)

        self.play(Create(highlight01))
        self.wait(1)
        self.play(FadeOut(highlight01))
        self.wait

        highlight0 = SurroundingRectangle(question[1][1], corner_radius=0.1, buff=0.1)

        self.play(Create(highlight0))
        self.wait(1)
        self.play(FadeOut(highlight0))
        self.wait(1)

        step1 = MathTex(
            "625 = 25^2 = 5^4",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(question, DOWN, buff=0.75)

        self.play(FadeIn(step1))
        self.wait(1)
        self.play(FadeOut(step1))

        step2 = MathTex(
            "\\frac{5^x}{625^y}",
            "= \\frac{5^x}{5^{4y}}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(question, DOWN, buff=0.75)

        self.play(FadeIn(step2))
        self.wait(1)

        step3 = MathTex(
            "= 5^{x-4y}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step2, DOWN, buff=0.5)

        self.play(FadeIn(step3))
        self.wait(1)

        highlight2 = BackgroundRectangle(
            step3[0][2:], color=YELLOW, corner_radius=0.1, buff=0.1
        )
        highlight2.z_index = -10

        self.play(Create(highlight2))
        self.wait(1)

        highlight3 = BackgroundRectangle(
            question[0][1], color=YELLOW, corner_radius=0.1, buff=0.1
        )
        highlight3.z_index = -10

        self.play(Create(highlight3))
        self.wait(1)

        step4 = MathTex(
            "= 5^9",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step3, DOWN, buff=0.5)

        self.play(FadeIn(step4))

        self.wait(4)


class Options(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        options = (
            VGroup(
                MathTex("A) \\ 125^{-1}", color=BLACK),
                MathTex("B) \\ 25^9", color=BLACK),
                MathTex("C) \\ 5^9", color=BLACK),
                MathTex("D) \\ \\text{Cannot be determined}", color=BLACK),
            )
            .arrange(DOWN, center=False, buff=0.25, aligned_edge=LEFT)
            .to_edge(UP)
        )

        self.play(FadeIn(options))
        self.wait(5)

        self.wait(1)
        self.play(Create(SurroundingRectangle(options[2], corner_radius=0.1, buff=0.1)))
        self.wait(4)
