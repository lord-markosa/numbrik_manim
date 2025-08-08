from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # PART 1
        question = (
            VGroup(
                MathTex(
                    "\\text{Find the number of real roots of}",
                    color=BLACK,
                ),
                MathTex(
                    "(x^2 + 3x)^2",
                    "-",
                    "(x^2 + 3x)",
                    "- 6 = 0",
                    color=BLACK,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, center=False)
            .scale(0.7)
            .to_corner(UP + LEFT)
        )

        highlight1 = BackgroundRectangle(
            question[1][0][1:6],
            buff=0.1,
            corner_radius=0.1,
            color=YELLOW_N50,
        )

        highlight2 = BackgroundRectangle(
            question[1][2][1:6],
            buff=0.1,
            corner_radius=0.1,
            color=YELLOW_N50,
        )

        self.play(FadeIn(question, shift=UP))
        self.wait(1)

        step1 = (
            MathTex(
                "y = ",
                "x^2 + 3x",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(question, DOWN, buff=0.5)
        )

        step2 = (
            MathTex(
                "(x^2 + 3x)^2 - (x^2 + 3x) - 6 = 0",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step1, DOWN, buff=0.25)
        )

        step3 = (
            MathTex(
                "\\Rightarrow y^2 - y - 6 = 0",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step2, DOWN, buff=0.25)
        )

        step4 = (
            MathTex(
                "\\Rightarrow (y-3)(y+2) = 0",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step3, DOWN, buff=0.25)
        )

        step5 = (
            MathTex(
                "(x^2 + 3x - 3)",
                "(x^2 + 3x + 2)",
                "= 0",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step4, DOWN, buff=0.25)
        )

        highlight1.z_index = -10
        highlight2.z_index = -10

        self.play(Create(highlight1), Create(highlight2))
        self.wait(1)

        self.play(FadeIn(step1[1]))
        self.wait(1)
        self.play(highlight1.animate.set_opacity(0), highlight2.animate.set_opacity(0))
        self.wait(1)
        self.play(FadeIn(step1[0]))
        self.wait(1)
        self.play(FadeIn(step2))
        self.wait(1)
        self.play(FadeIn(step3))
        self.wait(1)
        self.play(FadeIn(step4))
        self.wait(1)
        self.play(FadeIn(step5))
        self.wait(1)

        self.play(FadeOut(step1, step2, step3, step4))
        self.play(step5.animate.next_to(step1, 0))

        def solveEqIndependently(eqn1, eqn2, result, ref):
            step7 = (
                MathTex(
                    eqn1,
                    color=NUMBRIK_COLOR,
                    tex_template=TexFontTemplates.comic_sans,
                )
                .scale(0.7)
                .next_to(ref, DOWN, buff=0.25)
            )

            step8 = (
                MathTex(
                    eqn2,
                    color=NUMBRIK_COLOR,
                    tex_template=TexFontTemplates.comic_sans,
                )
                .scale(0.7)
                .next_to(step7, DOWN, buff=0.25)
            )

            step9 = (
                MathTex(
                    result,
                    color=NUMBRIK_COLOR,
                    tex_template=TexFontTemplates.comic_sans,
                )
                .scale(0.7)
                .next_to(step8, DOWN, buff=0.25)
            )

            self.wait(1)
            self.play(FadeIn(step7))
            self.wait(1)
            self.play(FadeIn(step8))
            self.wait(1)
            self.play(FadeIn(step9))
            self.wait(1)
            self.play(FadeOut(step7, step8, step9))
            self.wait(1)

        solveEqIndependently(
            "D = (3)^2 - 4(-3)", "= 21 > 0", "2 \\text{ roots!}", step5[0]
        )
        solveEqIndependently(
            "D = (3)^2 - 4(2)", "= 1 > 0", "2 \\text{ roots!}", step5[1]
        )

        stepFinal = (
            MathTex(
                "4 \\text{ roots!}",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step5, DOWN, buff=0.25)
        )

        self.play(Write(stepFinal))
        self.wait(1)
        self.play(FadeOut(step5, stepFinal))
        self.wait(1)


class Options(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        options = (
            VGroup(
                MathTex("A) \\ 1", color=BLACK),
                MathTex("B) \\ 2", color=BLACK),
                MathTex("C) \\ 3", color=BLACK),
                MathTex("D) \\ 4", color=BLACK),
            )
            .arrange(DOWN, center=False, buff=0.25)
            .scale(0.7)
            .to_corner(UL)
        )

        self.play(FadeIn(options))
        self.wait(30)

        self.play(Create(SurroundingRectangle(options[3], corner_radius=0.1, buff=0.1)))
        self.wait(4)

class Options(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        options = (
            VGroup(
                MathTex("A) \\ 2", color=BLACK),
                MathTex("B) \\ 4", color=BLACK),
                MathTex("C) \\ 6", color=BLACK),
                MathTex("D) \\ 8", color=BLACK),
            )
            .arrange(DOWN, center=False, buff=0.25)
            .scale(0.7)
            .to_corner(UL)
        )

        self.play(FadeIn(options))
        self.wait(30)

        self.play(Create(SurroundingRectangle(options[1], corner_radius=0.1, buff=0.1)))
        self.wait(4)
