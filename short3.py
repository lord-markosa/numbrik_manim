from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # PART 1
        question = (
            VGroup(
                MathTex(
                    "\\text{If } \\alpha, \\beta \\text{ are the roots of the equation}",
                    color=BLACK,
                ),
                MathTex(
                    "ax^2 + bx + c = 0. \\text{ Find the equation}",
                    "",
                    color=BLACK,
                ),
                MathTex(
                    "\\text{whose roots are }",
                    "1/\\alpha \\text{ and } 1/\\beta }",
                    "",
                    color=BLACK,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, center=False)
            .scale(0.8)
            .to_corner(UP + LEFT)
        )

        self.play(FadeIn(question, shift=UP))
        self.wait(1)

        highlight = SurroundingRectangle(
            question[1][0][0:11], buff=0.1, corner_radius=0.1
        )

        self.play(Create(highlight))
        self.wait(1)

        # Expand RHS

        step1 = (
            MathTex(
                "\\alpha + \\beta = -\\frac{b}{a}",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(question, DOWN, buff=0.75)
            .to_edge(LEFT)
        )

        step2 = (
            MathTex(
                "\\alpha\\beta  = \\frac{c}{a}",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(step1, RIGHT, buff=0.75, aligned_edge=DOWN + UP)
        )

        step3 = (
            MathTex(
                "\\frac{1}{\\alpha} + \\frac{1}{\\beta} = ",
                "\\frac{\\alpha + \\beta}{\\alpha\\beta} =",
                "\\frac{-b/a}{c/a}",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(step1, DOWN, buff=0.5)
            .to_edge(LEFT)
        )

        step32 = (
            MathTex(
                "-\\frac{b}{c}",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(step3[2], 0, aligned_edge=LEFT + UP)
        )

        step4 = (
            MathTex(
                "\\frac{1}{\\alpha\\beta} =",
                "\\frac{1}{c/a}",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(step3[1], RIGHT)
            .shift(LEFT * 0.4)
        )

        step42 = (
            MathTex(
                "\\frac{a}{c}",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(step4[1], 0, aligned_edge=LEFT + DOWN)
        )

        group1 = VGroup(step3[0], step3[2], step4)

        step5 = (
            MathTex(
                "\\Rightarrow x^2 - \\left(-\\frac{b}{c}\\right)x + \\frac{a}{c} = 0",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(group1, 0)
            .to_edge(LEFT)
        )

        self.play(FadeIn(step1, shift=0.4 * UP))
        self.play(FadeIn(step2, shift=0.4 * UP))
        self.play(FadeOut(highlight))
        self.wait(1)
        self.play(Write(step3))
        self.wait(1)
        self.play(Transform(step3[2], step32))
        self.play(FadeOut(step3[1]))
        self.play(step3[2].animate.shift(1.5 * LEFT))
        self.wait(1)
        self.play(Write(step4))
        self.wait(1)
        self.play(Transform(step4[1], step42))

        self.play(FadeOut(step1, step2))
        self.play(group1.animate.shift(1.2 * UP))
        self.play(Write(step5))

        self.wait(1)

        self.play(FadeOut(group1, step5))

        highlight2 = SurroundingRectangle(question[2][1], buff=0.1, corner_radius=0.1)

        self.wait(1)
        self.play(Create(highlight2))
        self.wait(1)

        step6 = (
            MathTex(
                "y =",
                "\\frac{1}{x}",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(question, DOWN, buff=1)
            .to_edge(LEFT)
        )

        step7 = (
            MathTex(
                "\\Rightarrow x = \\frac{1}{y}",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(step6, RIGHT, buff=0.5)
        )

        step8 = (
            MathTex(
                "a\\left(\\frac{1}{y}\\right)^2 + b\\left(\\frac{1}{y}\\right) + c = 0",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(step6, DOWN, buff=0.5)
            .to_edge(LEFT)
        )

        step9 = (
            MathTex(
                "a + by + cy^2 = 0",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(step8, 0, aligned_edge=LEFT + UP)
        )

        step10 = (
            MathTex(
                "a + bx + cx^2 = 0",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(step8, 0, aligned_edge=LEFT + UP)
        )

        self.play(FadeIn(step6[1]))
        self.wait(0.5)
        self.play(Write(step6[0]))
        self.wait(1)
        self.play(Write(step7))

        self.play(FadeOut(highlight2))
        self.wait(1)

        self.play(Write(step8))
        self.wait(1)
        self.play(Transform(step8, step9))
        self.wait(1)
        self.play(Transform(step8, step10))

        self.wait(4)


class Options(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        options = (
            VGroup(
                MathTex("A) \\ cx^2 + ax + b = 0", color=BLACK),
                MathTex("B) \\ ax^2 + cx + b = 0", color=BLACK),
                MathTex("C) \\ cx^2 + bx + a = 0", color=BLACK),
                MathTex("D) \\ bx^2 + cx + a = 0", color=BLACK),
            )
            .arrange(DOWN, aligned_edge=LEFT, center=False, buff=0.5)
            .scale(0.8)
            .to_corner(UL)
        )

        self.play(FadeIn(options))
        self.wait(30)

        self.play(Create(SurroundingRectangle(options[2], corner_radius=0.1, buff=0.1)))
        self.wait(4)
