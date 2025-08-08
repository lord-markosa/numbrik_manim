from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        # Equation

        eq0 = MathTex(
            r"y^{dy} = x^{dx}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        self.play(FadeIn(eq0))
        self.wait(1)

        eq = MathTex(
            r"\ln y^{dy}",
            "=",
            r"\ln x^{dx}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(eq0, DOWN, buff=0.5)

        self.play(FadeIn(eq))
        self.wait(1)

        highlight1 = BackgroundRectangle(
            eq[0][3:], buff=0.07, corner_radius=0.12, color=YELLOW, fill_opacity=1
        )

        highlight2 = BackgroundRectangle(
            eq[2][3:], buff=0.1, corner_radius=0.12, color=YELLOW, fill_opacity=1
        )

        highlight1.z_index = -10
        highlight2.z_index = -10

        self.play(Create(highlight1), Create(highlight2))
        self.wait(1)
        self.play(highlight1.animate.set_opacity(0), highlight2.animate.set_opacity(0))
        self.wait(1)

        eq_ = MathTex(
            r"dy \ln y",
            "=",
            r"dx \ln x",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(eq, 0)

        self.play(
            Transform(eq[0][3:], eq_[0][0:2]),
            Transform(eq[2][3:], eq_[2][0:2]),
            Transform(eq[0][0:3], eq_[0][2:]),
            Transform(eq[2][0:3], eq_[2][2:]),
        )
        self.wait(1)

        # Integrate both sides
        eq_int = MathTex(
            r"\int",
            r"\ln y",
            r"\, dy",
            "=",
            r"\int",
            r"\ln x",
            r"\, dx",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(eq_, DOWN, buff=0.5)

        self.play(
            FadeIn(eq_int[3]),
            TransformFromCopy(eq_[0][0:2], eq_int[2]),
            TransformFromCopy(eq_[2][0:2], eq_int[6]),
            TransformFromCopy(eq_[0][2:], eq_int[1]),
            TransformFromCopy(eq_[2][2:], eq_int[5]),
        )

        self.play(Write(eq_int[0]), Write(eq_int[4]))
        self.wait(2)

        final_eq = MathTex(
            r"y \ln y - y = x \ln x - x + C",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(eq_int, DOWN, buff=0.5)

        box = SurroundingRectangle(final_eq, corner_radius=0.2, buff=0.2)
        self.play(Write(final_eq))
        self.play(Create(box))

        self.wait(4)


class IntegrationByParts(Scene):
    def construct(self):
        # Step 1: Show the product rule
        step1 = MathTex(
            r"\frac{d}{dx}(uv) = u \frac{dv}{dx} + v \frac{du}{dx}",
            color=GREY_N500,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        self.play(FadeIn(step1))
        self.wait(1)

        # Step 2: Integrate both sides
        step2 = MathTex(
            r"\int \frac{d}{dx}(uv) \, dx = \int u \, dv + \int v \, du",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step1, DOWN, buff=0.75)

        self.play(FadeIn(step2))
        self.wait(1)

        # Step 3: Use integral of derivative = original function
        step3 = MathTex(
            r"uv",
            "=",
            r"\int u \, dv",
            "+",
            r"\int v \, du",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step2, DOWN, buff=0.5)

        self.play(FadeIn(step3))
        self.wait(1)

        # Step 4: Rearranging terms
        step4 = MathTex(
            r"\int u \, dv",
            "=",
            r"uv",
            "-",
            r"\int v \, du",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step3, 0, buff=0.5)

        box = SurroundingRectangle(step4, corner_radius=0.2, buff=0.2)

        self.play(
            Transform(step3[0], step4[2]),
            Transform(step3[2], step4[1]),
            Transform(step3[2], step4[0]),
            Transform(step3[4], step4[4]),
            Transform(step3[1], step4[1]),
            Transform(step3[3], step4[3]),
        )
        self.wait(1)
        self.play(Create(box), step4.animate.set_color(GREY_N500))
        self.wait(4)


class LogarithmicRule(Scene):
    def construct(self):
        eq = MathTex(
            r"\log{m^n} = n\log{m}",
            color=GREY_N800,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        self.play(FadeIn(eq))
        box = SurroundingRectangle(eq, corner_radius=0.2, buff=0.2)
        self.play(Create(box))
        self.wait(4)


class IntegrateLn(Scene):
    def construct(self):
        eq = MathTex(
            r"\int \ln x \, dx",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        self.play(FadeIn(eq))
        self.wait(1)

        step1 = MathTex(
            r"\text{Let } u = \ln x \Rightarrow du = \frac{1}{x}dx",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(eq, DOWN, buff=0.5)

        self.play(FadeIn(step1))
        self.wait(1)

        step2 = MathTex(
            r"\text{Let } dv = dx \Rightarrow v = x",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step1, DOWN, buff=0.5)

        self.play(FadeIn(step2))
        self.wait(1)

        formula = MathTex(
            r"\int \ln x \, dx = x\ln x - \int x \cdot \frac{1}{x} \, dx",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step2, DOWN, buff=0.5)

        self.play(FadeIn(formula))
        self.wait(1)

        final = MathTex(
            r"\int \ln x \, dx = x\ln x - x",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(formula, DOWN, buff=0.5)

        box = SurroundingRectangle(final, corner_radius=0.2, buff=0.2)

        self.play(FadeIn(final))
        self.play(Create(box), final.animate.set_color(GREY_N500))
        self.wait(4)
