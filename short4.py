from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # PART 1
        question = (
            VGroup(
                MathTex(
                    "\\text{Find a, b if }",
                    "x^2+1",
                    "\\text{ is a factor of}",
                    color=BLACK,
                ),
                MathTex(
                    "x^4+x^3+8x^2+ax+b",
                    color=BLACK,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, center=False)
            .scale(0.8)
            .to_corner(UP + LEFT)
        )

        self.play(FadeIn(question, shift=UP))
        self.wait(2)

        highlight1 = SurroundingRectangle(question[1], buff=0.1, corner_radius=0.1)
        self.play(Create(highlight1))
        self.wait(1)

        step1 = (
            MathTex(
                r"\begin{array}{r}Q(x)\quad \quad \quad \quad \phantom{)}\\x^2+1{\overline{\smash{\big)}\,x^4+x^3+8x^2+ax+b\phantom{)}}}\\\underline{-~\phantom{(}\ \ Q(x)(x^2+1)\phantom{-b)}}\\R(x)\ \ \ \ \ \ \ \ \ \ \end{array}",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(question, DOWN, aligned_edge=LEFT, buff=1)
        )

        step2 = (
            MathTex(
                "R(x) = 0 \\ \\text{ for all }  x",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(step1, DOWN, buff=0.5, aligned_edge=LEFT)
        )

        highlight = SurroundingRectangle(question[0][1], buff=0.1, corner_radius=0.1)

        self.play(FadeIn(step1, shift=UP * 0.2))
        self.wait(1)
        self.play(Write(step2))
        self.wait(1)
        self.play(FadeOut(highlight1))
        self.wait(2)
        self.play(FadeOut(step1, step2))
        self.wait(1)
        self.play(Create(highlight))

        step3 = (
            MathTex(
                "x^2+1 = (x+i)(x-i) \\text{ where } i = \\sqrt{-1}",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(question, DOWN, buff=1, aligned_edge=LEFT)
        )

        step4 = (
            MathTex(
                "x = i",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(step3, DOWN, buff=0.5, aligned_edge=LEFT)
        )

        pointer = CurvedArrow(
            end_point=question[1].get_bottom() + 0.2 * DOWN,
            start_point=step4.get_right() + 0.2 * RIGHT,
            stroke_width=3,
            color=YELLOW,
        )

        step5 = (
            MathTex(
                "i^4+i^3+8i^2+ai+b = 0",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(question, DOWN, buff=1, aligned_edge=LEFT)
        )

        step6 = (
            MathTex(
                "\\Rightarrow (a-1)i+b-7 = 0",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(step5, DOWN, buff=0.5, aligned_edge=LEFT)
        )

        step7 = (
            MathTex(
                "\\Rightarrow a = 1, b = 7",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(step6, DOWN, buff=0.5, aligned_edge=LEFT)
        )

        self.play(FadeIn(step3, shift=0.2 * UP))
        self.wait(1)
        self.play(Write(step4))
        self.play(step3.animate.set_color(NUMBRIK_COLOR_50))
        self.play(FadeIn(pointer))
        self.wait(1)
        self.play(FadeOut(step3, step4, pointer))
        self.wait(1)
        self.play(FadeIn(step5))
        self.wait(1)
        self.play(Write(step6))
        self.wait(1)
        self.play(Write(step7))
        self.wait(4)


class Options(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        options = (
            VGroup(
                MathTex("A) \\ a = 1, b = 7", color=BLACK),
                MathTex("B) \\ a = 2, b = 6", color=BLACK),
                MathTex("C) \\ a = 7, b = 1", color=BLACK),
                MathTex("D) \\ a = 6, b = 2", color=BLACK),
            )
            .arrange(DOWN, aligned_edge=LEFT, center=False, buff=0.5)
            .scale(0.8)
            .to_corner(UL)
        )

        self.play(FadeIn(options))
        self.wait(30)

        self.play(Create(SurroundingRectangle(options[0], corner_radius=0.1, buff=0.1)))
        self.wait(4)
