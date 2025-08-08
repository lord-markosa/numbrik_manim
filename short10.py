from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # PART 1
        question = (
            VGroup(
                MathTex(
                    "\\alpha, \\beta \\text{ are the roots of }",
                    "x^2 - 6x + 10 = 0",
                    color=BLACK,
                ),
                MathTex(
                    "\\text{Find }",
                    "\\frac{a_{10} + 10b_8}{a_9}",
                    "\\text{ where } a_n = \\alpha^{n} - \\beta^{n}",
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
                "D = (-6)^2 - 4\\cdot10 = -4",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(question, DOWN, buff=0.75)
        )

        step2 = (
            MathTex(
                "x = a \\pm ib \\text{ where } i = \\sqrt{-1}",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step1, DOWN, buff=0.25)
        )

        step3 = (
            MathTex(
                "\\frac{\\alpha^{10} - \\beta^{10} + 10\\alpha^{8} - 10\\beta^{8}}{\\alpha^{9} - \\beta^{9} }",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(question, DOWN, buff=0.75)
        )

        step4 = (
            MathTex(
                "\\frac{\\alpha^{10} + 10\\alpha^{8} - \\beta^{10}  - 10\\beta^{8}}{\\alpha^{9} - \\beta^{9} }",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step3, 0)
        )

        highlight1 = SurroundingRectangle(question[1][1], corner_radius=0.1, buff=0.1)
        highlight2 = BackgroundRectangle(
            question[0][1], color=YELLOW, corner_radius=0.1, buff=0.1
        )
        highlight2.z_index = -10

        self.play(FadeIn(step1))
        self.wait(1)
        self.play(FadeIn(step2))
        self.wait(1)
        self.play(FadeOut(step1, step2))
        self.wait(1)
        self.play(Create(highlight1))
        self.wait(1)
        self.play(FadeIn(step3))
        self.play(FadeOut(highlight1))
        self.wait(1)
        self.play(Transform(step3[0][3:7], step4[0][8:12]), Transform(step3[0][7:12], step4[0][3:8]))
        self.wait(1)
        # self.play(FadeOut(step3), step4.animate.next_to(step3, 0))

        step5 = (
            MathTex(
                "\\frac{\\alpha^{8}(\\alpha^2 + 10) - \\beta^{8}(\\beta^2 + 10)}{\\alpha^{9} - \\beta^{9} }",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step3, DOWN, buff=0.25)
        )

        highlight3 = BackgroundRectangle(
            step5[0][3:8], color=YELLOW, corner_radius=0.1, buff=0.1
        )

        highlight3.z_index = -10

        highlight4 = BackgroundRectangle(
            step5[0][13:18], color=YELLOW, corner_radius=0.1, buff=0.1
        )

        highlight4.z_index = -10

        step5_explainer = (
            MathTex(
                "\\alpha^2 - 6\\alpha + 10 = 0",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(question, DOWN, buff=0.75)
        )

        step5_explainer2 = (
            MathTex(
                "\\Rightarrow \\alpha^2 + 10 = 6\\alpha",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step5_explainer, DOWN, buff=0.25)
        )

        step6 = (
            MathTex(
                "\\frac{\\alpha^{8}(6\\alpha) - \\beta^{8}(6\\beta)}{\\alpha^{9} - \\beta^{9}}",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step5, DOWN, buff=0.25)
        )

        step7 = (
            MathTex(
                "\\frac{6(\\alpha^{9} - \\beta^{9})}{\\alpha^{9} - \\beta^{9}}",
                "= 6",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step6, 0)
        )

        self.play(FadeIn(step5))
        self.wait(1)
        self.play(Create(highlight3), Create(highlight4))
        self.wait(1)
        self.play(Create(highlight2))
        self.wait(1)
        self.play(
            FadeOut(step3, step5),
            highlight3.animate.set_opacity(0),
            highlight4.animate.set_opacity(0),
        )
        self.play(FadeIn(step5_explainer))
        self.wait(1)
        self.play(FadeIn(step5_explainer2))
        self.wait(1)
        self.play(FadeOut(step5_explainer, step5_explainer2))
        self.play(
            FadeIn(step3, step5),
            highlight3.animate.set_opacity(1),
            highlight4.animate.set_opacity(1),
        )
        self.play(FadeIn(step6))
        self.wait(1)
        self.play(Transform(step6, step7[0]))
        self.wait(1)
        self.play(FadeIn(step7[1]))

        self.wait(4)


class Options(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        options = (
            VGroup(
                MathTex("A) \\ 1", color=BLACK),
                MathTex("B) \\ 6", color=BLACK),
                MathTex("C) \\ 3", color=BLACK),
                MathTex("D) \\ 12", color=BLACK),
            )
            .arrange(DOWN, center=False, buff=0.25, aligned_edge=LEFT)
            .scale(0.7)
            .to_edge(UP)
        )

        self.play(FadeIn(options))
        self.wait(5)

        self.wait(1)
        self.play(Create(SurroundingRectangle(options[1], corner_radius=0.1, buff=0.1)))
        self.wait(4)
