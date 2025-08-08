from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # PART 1
        question = (
            VGroup(
                MathTex(
                    "\\text{One of the factors of }x^4+4\\text{ is:}",
                    color=GREY_N800,
                ),
            )
            .arrange(DOWN)
            .to_edge(UP)
        )

        self.play(FadeIn(question, shift=UP))
        self.wait(2)

        step1 = MathTex(
            "x^2 + 4",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(question, DOWN, buff=0.75)

        step2 = MathTex(
            "(x+2i)(x-2i),\\ i = \\sqrt{-1}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step1, DOWN, buff=0.5)

        self.play(FadeIn(step1))
        self.wait(1)
        self.play(FadeIn(step2))
        self.wait(1)
        self.play(FadeOut(step1, step2))
        self.wait(1)

        step3 = MathTex(
            "x^4 + 4",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(question, DOWN, buff=0.75)

        step4 = MathTex(
            "x^4 + 4",
            "+4x^2",
            "- 4x^2",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step3, 0)

        self.play(FadeIn(step3))
        self.wait(1)
        self.play(Transform(step3, step4[0]), FadeIn(step4[1:]))
        self.wait(1)

        step5 = MathTex(
            "(x^2 + 2)^2",
            "- (2x)^2",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step4, DOWN, buff=0.5)

        solidHighlight(self, step4[0:2])
        self.play(FadeIn(step5[0]))
        self.wait(1)
        solidHighlight(self, step4[2])
        self.play(FadeIn(step5[1]))
        self.wait(1)

        step6 = MathTex(
            "(x^2 - 2x + 2)",
            "(x^2 + 2x + 2)",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step5, DOWN, buff=0.5)

        self.play(FadeIn(step6))
        self.wait(1)

        solidHighlight(self, step6[1])

        self.wait(4)


class Options(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        options = (
            VGroup(
                MathTex("A) \\ x^2 + 2", color=GREY_N800),
                MathTex("B) \\ x^2 - 2", color=GREY_N800),
                MathTex("C) \\ x^2 + 2x + 2", color=GREY_N800),
                MathTex("D) \\ \\text{None of these}", color=GREY_N800),
            )
            .arrange(DOWN, buff=0.5, aligned_edge=LEFT)
            .to_edge(UP)
        )

        self.play(FadeIn(options))
        self.wait(5)

        self.wait(1)
        self.play(Create(SurroundingRectangle(options[2], corner_radius=0.1, buff=0.1)))
        self.wait(4)
