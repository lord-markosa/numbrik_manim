from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # PART 1
        question = (
            VGroup(
                MathTex(
                    "\\text{Find the value of }a+b+c",
                    color=BLACK,
                ),
                MathTex(
                    "\\text{where }ax^2 + bx + c = 2(x+2)(x+3)",
                    color=BLACK,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, center=False)
            .scale(0.8)
            .to_corner(UP + LEFT)
        )

        self.play(FadeIn(question, shift=UP))
        self.wait(1)

        # Expand RHS

        step1 = (
            MathTex(
                "2(x+2)(x+3)",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(question, DOWN, buff=1)
        )

        step2 = (
            MathTex(
                "2(x^2+5x+6)",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(step1, 0)
        )

        step3 = (
            MathTex(
                "2x^2+10x+12",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(step1, 0)
        )

        step4 = (
            MathTex(
                "2+10+12 = 24",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(step1, DOWN, buff=0.5)
        )

        # # Options
        options = (
            VGroup(
                MathTex("A) \\  20", color=BLACK),
                MathTex("B) \\  22", color=BLACK),
                MathTex("C) \\  24", color=BLACK),
                MathTex("D) \\  26", color=BLACK),
            )
            .arrange(DOWN, aligned_edge=LEFT, center=False)
            .scale(0.8)
            .next_to(question, DOWN, buff=0.75, aligned_edge=LEFT)
        )

        self.play(FadeIn(options, shift=DOWN))
        self.wait(1)

        self.play(options.animate.to_edge(DOWN))
        self.play(FadeIn(step1, shift=UP))
        self.wait(1)
        self.play(Transform(step1, step2))
        self.wait(1)
        self.play(Transform(step1, step3))
        self.wait(1)
        self.play(FadeIn(step4))
        self.wait(1)

        self.play(FadeOut(step1, step4))
        self.wait(1)

        self.play(
            Create(
                SurroundingRectangle(
                    question[1][0][5:], color=YELLOW, buff=0.1, corner_radius=0.1
                )
            )
        )

        step5 = (
            MathTex(
                "x=1",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(question, DOWN, buff=0.75)
        )

        step6 = (
            MathTex(
                "a(1)^2 + b(1) + c = 2(1+2)(1+3)",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(step5, DOWN, buff=0.5)
        )

        step7 = (
            MathTex(
                "a + b + c = 24",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(step6, DOWN, buff=0.5)
        )

        self.play(FadeIn(step5))
        self.wait(1)
        self.play(FadeIn(step6))
        self.wait(1)
        self.play(FadeIn(step7))

        # # Highlight correct option
        # box = SurroundingRectangle(options[2], color=GREEN, buff=0.1)
        # self.play(Create(box))
        # self.wait(2)

        # # Final confirmation
        # answer = Text("Correct Answer: C) 24", color=GREEN).scale(0.7).to_edge(DOWN)
        # self.play(Write(answer))

        self.play(
            Create(
                SurroundingRectangle(
                    options[2], buff=0.1, color=NUMBRIK_COLOR, corner_radius=0.1
                )
            )
        )

        self.wait(4)
