from manim import *
from utils import *


class SolveOption(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # # PART 1
        # question = (
        #     VGroup(
        #         MathTex(
        #             "\\text{If } \\alpha, \\beta \\text{ are the roots of the equation}",
        #             color=BLACK,
        #         ),
        #         MathTex(
        #             "ax^2 + bx + c = 0. \\text{ Find: }",
        #             "\\frac{\\beta}{a\\alpha+b} + \\frac{\\alpha}{a\\beta+b}",
        #             color=BLACK,
        #         ),
        #     )
        #     .arrange(DOWN, aligned_edge=LEFT, center=False)
        #     .scale(0.8)
        #     .to_corner(UP + LEFT)
        # )

        # self.play(FadeIn(question, shift=UP))
        # self.wait(1)

        # highlight = SurroundingRectangle(
        #     question[1][1][2:6], buff=0.1, corner_radius=0.1
        # )

        # self.play(Create(highlight))
        # self.wait(1)

        # # Expand RHS

        # step1 = (
        #     MathTex(
        #         "a\\alpha + b",
        #         color=NUMBRIK_COLOR,
        #         tex_template=TexFontTemplates.comic_sans,
        #     )
        #     .scale(0.8)
        #     .next_to(question, DOWN, buff=1)
        # )

        # step2 = (
        #     MathTex(
        #         "\\alpha(a\\alpha + b)",
        #         color=NUMBRIK_COLOR,
        #         tex_template=TexFontTemplates.comic_sans,
        #     )
        #     .scale(0.8)
        #     .next_to(question, DOWN, buff=1)
        # )

        # step3 = (
        #     MathTex(
        #         "a\\alpha^2 + b\\alpha",
        #         color=NUMBRIK_COLOR,
        #         tex_template=TexFontTemplates.comic_sans,
        #     )
        #     .scale(0.8)
        #     .next_to(question, DOWN, buff=1)
        # )

        # pointer = CurvedArrow(
        #     start_point=question[1][0][4].get_bottom() + 0.2 * DOWN,
        #     end_point=step3.get_left() + 0.2 * LEFT + 0.1 * DOWN,
        #     stroke_width=3,
        #     color=YELLOW,
        # )

        # step4 = (
        #     MathTex(
        #         "=-c",
        #         color=NUMBRIK_COLOR,
        #         tex_template=TexFontTemplates.comic_sans,
        #     )
        #     .scale(0.8)
        #     .next_to(step3, RIGHT, buff=0.2, aligned_edge=DOWN)
        # )

        # step5 = (
        #     MathTex(
        #         "\\Rightarrow a\\alpha + b = -\\frac{c}{\\alpha}",
        #         color=NUMBRIK_COLOR,
        #         tex_template=TexFontTemplates.comic_sans,
        #     )
        #     .scale(0.8)
        #     .next_to(step3, DOWN, buff=0.5)
        #     .shift(0.2 * RIGHT)
        # )

        # self.play(FadeIn(step1, shift=0.4 * UP))
        # self.play(FadeOut(highlight))
        # self.wait(1)

        # self.play(Transform(step1, step2))
        # self.wait(1)
        # self.play(Transform(step1, step3))
        # self.wait(1)
        # self.play(Create(pointer))
        # self.play(FadeIn(step4))
        # self.wait(1)
        # self.play(FadeIn(step5, shift=UP))
        # self.wait(1)
        # self.play(FadeOut(step1, step4, step5, pointer))
        # self.wait(1)

        # step6 = (
        #     MathTex(
        #         "\\frac{\\beta}{a\\alpha+b} + \\frac{\\alpha}{a\\beta+b} = ",
        #         "\\frac{\\beta}{-c/\\alpha}",
        #         "+",
        #         "\\frac{\\alpha}{-c/\\beta}",
        #         color=NUMBRIK_COLOR,
        #         tex_template=TexFontTemplates.comic_sans,
        #     )
        #     .scale(0.8)
        #     .next_to(question, DOWN, buff=1)
        #     .shift(0.2 * RIGHT)
        # )

        # step7 = (
        #     MathTex(
        #         "-\\frac{\\alpha\\beta}{c}",
        #         "-\\frac{\\alpha\\beta}{c}",
        #         color=NUMBRIK_COLOR,
        #         tex_template=TexFontTemplates.comic_sans,
        #     )
        #     .scale(0.8)
        #     .next_to(step6[1], 0, aligned_edge=DOWN + LEFT)
        #     .shift(0.2 * RIGHT)
        # )

        # step8 = (
        #     MathTex(
        #         "-2\\frac{\\alpha\\beta}{c}",
        #         color=NUMBRIK_COLOR,
        #         tex_template=TexFontTemplates.comic_sans,
        #     )
        #     .scale(0.8)
        #     .next_to(step6[1], 0, aligned_edge=DOWN + LEFT)
        #     .shift(0.2 * RIGHT)
        # )

        # step9 = (
        #     MathTex(
        #         "-2\\frac{c/a}{c}",
        #         color=NUMBRIK_COLOR,
        #         tex_template=TexFontTemplates.comic_sans,
        #     )
        #     .scale(0.8)
        #     .next_to(step6[1], 0, aligned_edge=DOWN + LEFT)
        #     .shift(0.2 * RIGHT)
        # )

        # step10 = (
        #     MathTex(
        #         "-\\frac{2}{a}",
        #         color=NUMBRIK_COLOR,
        #         tex_template=TexFontTemplates.comic_sans,
        #     )
        #     .scale(0.8)
        #     .next_to(step6[1], 0, aligned_edge=DOWN + LEFT)
        #     .shift(0.2 * RIGHT)
        # )

        # self.play(FadeIn(step6[0], shift=0.5 * UP))
        # self.play(FadeIn(step6[1:]))
        # self.wait(1)
        # self.play(FadeOut(step6[2]), Transform(step6[1], step7[0]), Transform(step6[3], step7[1]))
        # self.wait(1)
        # self.play(Transform(step6[1:], step8))
        # self.wait(1)
        # self.play(Transform(step6[1:], step9))
        # self.wait(1)
        # self.play(Transform(step6[1:], step10))
        # self.wait(1)

        # self.play(FadeIn(step4))

        # step4 = (
        #     MathTex(
        #         "2+10+12 = 24",
        #         color=NUMBRIK_COLOR,
        #         tex_template=TexFontTemplates.comic_sans,
        #     )
        #     .scale(0.8)
        #     .next_to(step1, DOWN, buff=0.5)
        # )

        # Options
        options = (
            VGroup(
                MathTex("A) \\ -\\frac{1}{a}", color=BLACK),
                MathTex("B) \\ -\\frac{2}{c}", color=BLACK),
                MathTex("C) \\ -\\frac{2}{b}", color=BLACK),
                MathTex("D) \\ -\\frac{2}{a}", color=BLACK),
            )
            .arrange(DOWN, aligned_edge=LEFT, center=False)
            .scale(0.8)
            .to_corner(UL)
        )

        self.play(FadeIn(options))
        self.wait(2)

        self.play(Create(SurroundingRectangle(options[3], corner_radius=0.1, buff=0.1)))
        self.wait(2)

        # self.play(options.animate.to_edge(DOWN))

        # self.play(FadeOut(step1, step4))
        # self.wait(1)

        # self.play(
        #     Create(
        #         SurroundingRectangle(
        #             question[1][0][5:], color=YELLOW,
        #         )
        #     )
        # )

        # step5 = (
        #     MathTex(
        #         "x=1",
        #         color=NUMBRIK_COLOR,
        #         tex_template=TexFontTemplates.comic_sans,
        #     )
        #     .scale(0.8)
        #     .next_to(question, DOWN, buff=0.75)
        # )

        # step6 = (
        #     MathTex(
        #         "a(1)^2 + b(1) + c = 2(1+2)(1+3)",
        #         color=NUMBRIK_COLOR,
        #         tex_template=TexFontTemplates.comic_sans,
        #     )
        #     .scale(0.8)
        #     .next_to(step5, DOWN, buff=0.5)
        # )

        # step7 = (
        #     MathTex(
        #         "a + b + c = 24",
        #         color=NUMBRIK_COLOR,
        #         tex_template=TexFontTemplates.comic_sans,
        #     )
        #     .scale(0.8)
        #     .next_to(step6, DOWN, buff=0.5)
        # )

        # self.play(FadeIn(step5))
        # self.wait(1)
        # self.play(FadeIn(step6))
        # self.wait(1)
        # self.play(FadeIn(step7))

        # # # Highlight correct option
        # # box = SurroundingRectangle(options[2], color=GREEN, buff=0.1)
        # # self.play(Create(box))
        # # self.wait(2)

        # # # Final confirmation
        # # answer = Text("Correct Answer: C) 24", color=GREEN).scale(0.7).to_edge(DOWN)
        # # self.play(Write(answer))

        # self.play(
        #     Create(
        #         SurroundingRectangle(
        #             options[2], buff=0.1, color=NUMBRIK_COLOR, corner_radius=0.1
        #         )
        #     )
        # )

        self.wait(4)
