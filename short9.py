from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # PART 1
        question = MathTex(
            "\\sqrt{x}^{\\sqrt{x}^{\\sqrt{x}^{^{\\ ...^{\\ \\infty}}}}}",
            "=",
            "\\frac{1}{3}",
            color=BLACK,
        ).to_edge(UP)

        self.play(FadeIn(question, shift=UP))
        self.wait(2)

        highlight1 = BackgroundRectangle(
            question[0],
            buff=0.1,
            corner_radius=0.2,
            color=YELLOW_N50,
        )

        highlight11 = SurroundingRectangle(question[2], corner_radius=0.1, buff=0.1)

        highlight2 = BackgroundRectangle(
            question[0][3:],
            buff=0.05,
            corner_radius=0.12,
            color=YELLOW_N50,
        )

        highlight1.set_z_index(-10)
        highlight2.set_z_index(-10)

        self.play(Create(highlight1))
        self.wait(1)
        self.play(Create(highlight11))
        self.wait(1)
        self.play(Transform(highlight1, highlight2))
        self.wait(1)

        step1 = MathTex(
            "\\sqrt{x}^{\\frac{1}{3}} = \\frac{1}{3}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(question, DOWN, buff=0.75)

        step2 = MathTex(
            "x^{\\frac{1}{2}\\cdot\\frac{1}{3}}",
            "=",
            "\\frac{1}{3}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step1, DOWN, buff=0.5)

        step3 = MathTex(
            "x^{\\frac{1}{6}}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step2[0], 0, aligned_edge=RIGHT)

        step4 = MathTex(
            "x = \\frac{1}{3^6}",
            "= \\frac{1}{729}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step2, DOWN, buff=0.5)

        self.play(FadeIn(step1))
        self.wait(1)
        self.play(highlight1.animate.set_opacity(0), FadeOut(highlight11))
        self.wait(1)
        self.play(FadeIn(step2))
        self.wait(1)
        self.play(Transform(step2[0][0], step3[0]), Transform(step2[0][1:], step3[1:]))
        self.wait(1)
        self.play(FadeIn(step4[0]))
        self.play(FadeIn(step4[1]))

        self.wait(4)


class Options(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        options = (
            VGroup(
                VGroup(
                    MathTex("A) \\ \\frac{1}{27}", color=BLACK),
                    MathTex("B) \\ \\frac{1}{81}", color=BLACK),
                ).arrange(RIGHT, buff=1),
                VGroup(
                    MathTex("C) \\ \\frac{1}{243}", color=BLACK),
                    MathTex("D) \\ \\frac{1}{729}", color=BLACK),
                ).arrange(RIGHT, buff=1),
            )
            .arrange(DOWN, center=False, buff=0.5)
            .to_edge(UP)
        )

        self.play(FadeIn(options))
        self.wait(5)

        self.wait(1)
        self.play(Create(SurroundingRectangle(options[1][1], corner_radius=0.1, buff=0.1)))
        self.wait(4)
