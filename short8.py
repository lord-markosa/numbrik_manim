from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # PART 1
        question = (
            VGroup(
                MathTex(
                    "\\text{Side of a cube is decreased by } 20\\%",
                    color=BLACK,
                ),
                MathTex(
                    "\\text{\\% decrease in Surface Area } = \\ ?",
                    color=BLACK,
                ),
            )
            .arrange(DOWN)
            .scale(0.7)
            .to_edge(UP)
        )

        self.play(FadeIn(question, shift=UP))
        self.wait(2)

        step1 = (
            MathTex(
                "SA \\propto a^2",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(question, DOWN, buff=0.75)
        )

        step2 = (
            MathTex(
                "a_{new} = 0.8a",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step1, DOWN, buff=0.25)
        )

        step3 = (
            MathTex(
                "a_{new}^{2} = (0.8a)^2 = 0.64a^2",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step2, DOWN, buff=0.25)
        )

        step4 = (
            MathTex(
                "SA_{new} = 0.64 \\times SA",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step3, DOWN, buff=0.25)
        )

        finalStep = (
            MathTex(
                "decrease",
                "= (1-0.64)\\times100",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step4, DOWN, buff=0.25)
        )

        finalStep2 = (
            MathTex(
                "= 36\\%",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(finalStep[1], DOWN, aligned_edge=LEFT)
        )

        self.play(FadeIn(step1))
        self.wait(1)
        self.play(FadeIn(step2))
        self.wait(1)
        self.play(FadeIn(step3))
        self.wait(1)
        self.play(FadeIn(step4))
        self.wait(1)
        self.play(FadeIn(finalStep))
        self.play(FadeIn(finalStep2))

        self.wait(4)


class Options(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        options = (
            VGroup(
                MathTex("A) \\ 16\\%", color=BLACK),
                MathTex("B) \\ 36\\%", color=BLACK),
                MathTex("C) \\ 64\\%", color=BLACK),
                MathTex("D) \\ 20\\%", color=BLACK),
            )
            .arrange(DOWN, center=False, buff=0.25)
            .scale(0.7)
            .to_edge(UP)
        )

        self.play(FadeIn(options))
        self.wait(5)

        self.wait(1)
        self.play(Create(SurroundingRectangle(options[1], corner_radius=0.1, buff=0.1)))
        self.wait(4)
