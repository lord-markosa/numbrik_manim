from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        # Equation

        eq0 = MathTex(
            "\\sqrt{\\underbrace{29\\cdot30\\cdot31\\cdot32} + 1}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        underbrace = eq0[0][13:19]
        underbrace.set_color(GREY_N400)

        self.play(FadeIn(eq0[0][0:13], eq0[0][19:]))
        self.wait(2)

        step1 = MathTex(
            "(a-3k)(a-k)(a+k)(a+3k)",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(eq0, DOWN, 1.5)

        arrow = Arrow(
            underbrace.get_center(),
            step1.get_center() + 0.3 * UP,
            color=GREY_N400,
        )

        self.play(Write(underbrace))
        self.wait(1)
        self.play(GrowArrow(arrow))
        self.play(FadeIn(step1))
        self.wait(1)

        step2 = MathTex(
            "\\text{where } a = \\frac{30+31}{2}, \\ k = \\frac{1}{2}",
            color=GREY_N400,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step1, DOWN, 0.5)

        self.play(FadeIn(step2))
        self.wait(2)

        highlight_ = SurroundingRectangle(step1, corner_radius=0.1, buff=0.2)
        self.play(Create(highlight_))
        self.play(FadeOut(eq0, step2, arrow, highlight_, step1))

        step3 = MathTex(
            "\\sqrt{(a-3k)(a-k)(a+k)(a+3k) + 1}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        self.play(
            FadeIn(step3[0]),
        )
        self.wait(1)

        step4 = MathTex(
            "\\sqrt{(a^2-k^2)(a^2-9k^2) + 1}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step3, DOWN, 0.5)

        step5 = MathTex(
            "\\sqrt{a^4 - 10a^2k^2 + 9k^4 + 1}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step4, DOWN, 0.5)

        self.play(FadeIn(step4))
        self.wait(1)
        self.play(FadeIn(step5))
        self.wait(1)

        self.play(FadeOut(step3, step4))
        self.play(step5.animate.to_edge(UP))
        self.wait(1)

        highlight_ = SurroundingRectangle(step5[0][12:], corner_radius=0.1, buff=0.1)
        self.play(Create(highlight_))

        self.wait(1)

        step7 = MathTex(
            "\\sqrt{a^4 - 10a^2k^2 + 25k^4}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step5, DOWN, 0.5)

        step8 = MathTex(
            "a^2 - 5k^2",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step7, DOWN, 0.5)

        self.wait(2)
        self.play(FadeOut(highlight_))
        self.play(FadeIn(step7))
        self.wait(1)
        self.play(FadeIn(step8))
        highlight_ = SurroundingRectangle(step8, corner_radius=0.1, buff=0.2)
        self.play(Create(highlight_), step8.animate.set_color(GREY_N400))

        self.play(FadeOut(highlight_, step7, step5))
        self.play(step8.animate.to_edge(UP))

        step9 = MathTex(
            "\\left(\\frac{30+31}{2}\\right)^2 - \\frac{5}{4}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step8, DOWN, 0.75)

        step10 = MathTex(
            "\\left(30.5^2 - 1.25)",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step9, DOWN, 0.5)

        step11 = MathTex(
            "929",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step10, DOWN, 0.6)

        self.play(FadeIn(step9))
        self.wait(1)
        self.play(FadeIn(step10))
        self.wait(1)
        self.play(FadeIn(step11))
        self.play(step11.animate.scale(1.1).set_color(GREY_N400))
        highlight_ = SurroundingRectangle(step11, corner_radius=0.1, buff=0.2)
        self.play(Create(highlight_))

        clearScreen(self, 4)

        step6 = MathTex(
            "9k^4 +1",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step5, DOWN, 0.5)

        step61 = (
            MathTex(
                "=\\frac{9}{16} + 1 \\quad \\because k = \\frac{1}{2}",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .next_to(step6, DOWN, 0.5, aligned_edge=LEFT)
            .shift(LEFT * 0.3)
        )

        step62 = MathTex(
            "=25k^4",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step61, DOWN, 0.5, aligned_edge=LEFT)

        self.play(FadeIn(step6))
        self.wait(1)
        self.play(FadeIn(step61))
        self.wait(1)
        self.play(FadeIn(step62))

        self.wait(10)
