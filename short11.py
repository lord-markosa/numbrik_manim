from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # PART 1
        question = (
            VGroup(
                MathTex(
                    "N =",
                    "1^1\\cdot2^2\\cdot3^3\\cdot...\\cdot29^{29}\\cdot30^{30}",
                    color=BLACK,
                ),
                MathTex(
                    "\\frac{N}{125^k}",
                    ",\\ k \\in  \\text{Integers, find max k}",
                    color=BLACK,
                ),
            )
            .arrange(DOWN, buff=0.75)
            .scale(0.7)
            .to_edge(UP)
        )

        self.play(FadeIn(question, shift=UP))
        self.wait(2)

        highlight0 = SurroundingRectangle(question[0][1], corner_radius=0.1, buff=0.1)

        self.play(Create(highlight0))
        self.wait(1)
        self.play(FadeOut(highlight0))
        self.wait(1)

        step0 = (
            MathTex(
                "\\frac{N}{5^{3k}}",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(question[1][0], 0)
        )

        self.play(Transform(question[1][0], step0))
        self.wait(1)

        highlight01 = SurroundingRectangle(question[1][0], corner_radius=0.1, buff=0.1)

        self.play(Create(highlight01))
        self.wait(1)
        self.play(FadeOut(highlight01))
        self.wait(1)

        step1 = (
            MathTex(
                "\\text{Maximum power of 5 in N = ?}",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(question, DOWN, buff=0.75)
        )

        self.play(FadeIn(step1))
        self.wait(1)

        step2 = (
            MathTex(
                "5^5 ...\\ 10^{10} ...\\ 15^{15} ...\\ ...\\ 30^{30}",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step1, DOWN, buff=0.5)
        )

        self.play(FadeIn(step2))
        self.wait(1)

        step3 = (
            MathTex(
                "15^{15} = (3\\cdot5)^{15} = 3^{15}\\cdot5^{15}",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step2, DOWN, buff=0.5)
        )

        self.play(FadeIn(step3))
        self.wait(1)
        self.play(FadeOut(step3))

        step4 = (
            MathTex(
                "5^5 ...\\ 5^{10}...\\ 5^{15} ...\\ ...\\ 5^{30}",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step2, DOWN, buff=0.5)
        )

        self.play(FadeIn(step4))
        self.wait(1)

        step5 = (
            MathTex(
                "5+10 + ...\\ ",
                "2\\cdot25",
                "+30",
                "=130",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step4, DOWN, buff=0.5)
            .shift(RIGHT * 0.5)
        )

        self.play(FadeIn(step5[0:3]))
        self.wait(1)

        highlight2 = BackgroundRectangle(
            step5[1], color=YELLOW, corner_radius=0.1, buff=0.1
        )
        highlight2.z_index = -10

        self.play(Create(highlight2))
        self.wait(1)

        self.play(highlight2.animate.set_opacity(0))

        self.play(step5.animate.shift(LEFT * 0.5))
        # self.play(FadeIn(step5[3]))
        # self.wait(1)

        step6 = (
            MathTex(
                "130 - 3k \\ge 0 \\Rightarrow k \\le 43",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step5, DOWN, buff=0.5)
        )

        self.play(FadeIn(step6))
        self.wait(1)

        self.wait(4)


class Options(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        options = (
            VGroup(
                MathTex("A) \\ 27", color=BLACK),
                MathTex("B) \\ 35", color=BLACK),
                MathTex("C) \\ 43", color=BLACK),
                MathTex("D) \\ 48", color=BLACK),
            )
            .arrange(DOWN, center=False, buff=0.25, aligned_edge=LEFT)
            .scale(0.7)
            .to_edge(UP)
        )

        self.play(FadeIn(options))
        self.wait(5)

        self.wait(1)
        self.play(Create(SurroundingRectangle(options[2], corner_radius=0.1, buff=0.1)))
        self.wait(4)
