from manim import *
from utils import *


class NestedSemicircles(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Points A, B, and midpoint C
        A = LEFT * 2
        B = RIGHT * 2
        C = ORIGIN  # Midpoint of AB

        # Draw segment AB and midpoint
        segment = Line(A, B, color=BLACK)

        label_a = Text("A", font_size=24, color=BLACK).next_to(A, DOWN)
        label_b = Text("B", font_size=24, color=BLACK).next_to(B, DOWN)
        label_c = Text("C", font_size=24, color=BLACK).next_to(C, DOWN)

        label_bc = MathTex("12", font_size=30, color=BLACK).next_to((B + C) / 2, DOWN)

        # Semicircle on AB (radius 2, center C)
        semi_ab = Arc(radius=2, start_angle=0, angle=PI, arc_center=C, color=BLACK)

        # Semicircle on AC (radius 1, center A + RIGHT)
        semi_ac = Arc(
            radius=1, start_angle=0, angle=PI, arc_center=A + RIGHT, color=BLACK
        )

        # Semicircle on CB (radius 1, center C + RIGHT)
        semi_cb = Arc(
            radius=1, start_angle=0, angle=PI, arc_center=C + RIGHT, color=BLACK
        )

        r = 4 / 6

        # Construct outer circle that touches all 3 semicircles
        center = UP * (2 - r)  # Empirical value; adjust for precision
        dot_n = Dot(center, radius=0.05, color=BLACK)

        radius = DashedLine(center, center + RIGHT * r, color=BLACK)

        label_radius = Text("r", font_size=24, color=RED_N100).next_to(
            radius, UP, buff=0.1
        )

        inner_circle = Circle(radius=r, color=BLACK).move_to(center)

        grp = VGroup(
            segment,
            label_a,
            label_b,
            label_c,
            label_bc,
            semi_ab,
            semi_ac,
            semi_cb,
            inner_circle,
            dot_n,
            radius,
            label_radius,
        )

        question = (
            VGroup(
                MathTex(
                    "\\text{Given C is the mid-point of AB,}",
                    color=BLACK,
                ),
                MathTex(
                    "r = \\ ?",
                    color=BLACK,
                ),
            )
            .arrange(DOWN, center=False)
            .scale(0.7)
            .to_edge(UP)
        )

        self.play(FadeIn(grp, question))
        self.wait(2)

        P = (A + C) / 2

        label_n = Text(
            "N", font="Comic Sans MS", color=NUMBRIK_COLOR, font_size=20
        ).next_to(center, LEFT + UP, buff=0.1)
        dot_p = Dot(P, radius=0.05, color=BLACK)
        label_p = Text(
            "P", font="Comic Sans MS", color=NUMBRIK_COLOR, font_size=22
        ).next_to(dot_p, DOWN)

        self.play(Write(label_p), Create(dot_p))
        self.wait(1)
        self.play(Write(label_n))
        self.wait(1)

        line_np = Line(center, P, color=NUMBRIK_COLOR)
        line_nc = Line(center, C, color=NUMBRIK_COLOR)

        self.play(Create(line_nc), Create(line_np))
        self.wait(1)

        def highlight(obj1, obj2):
            self.play(
                obj1.animate.set_color(NUMBRIK_COLOR_50),
                obj2.animate.set_color(NUMBRIK_COLOR_50),
            )
            self.wait(0.5)
            self.play(obj1.animate.set_color(BLACK), obj2.animate.set_color(BLACK))

        # triangle NPC is a right angled triangle
        # NP = r + 6
        #

        highlight(semi_ac, inner_circle)
        self.wait(1)
        line_temp = DashedLine(center, center + UP * r, color=NUMBRIK_COLOR)
        self.play(Create(line_temp), run_time=0.3)
        highlight(semi_ab, inner_circle)
        self.play(FadeOut(line_temp))
        self.wait(1)

        step1 = (
            MathTex(
                "NP^2 = CN^2 + PC^2",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(grp, DOWN, buff=1)
        )

        step2 = (
            MathTex(
                "(r+6)^2 = (12-r)^2 + 6^2",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step1, DOWN, buff=0.25)
        )

        step_final = (
            MathTex(
                "\\Rightarrow r = 4",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step2, DOWN, buff=0.25)
        )

        self.play(FadeIn(step1))
        self.wait(1)
        self.play(FadeIn(step2))
        self.wait(1)
        self.play(FadeIn(step_final))

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
            .arrange(DOWN, buff=0.25)
            .scale(0.7)
        )

        self.play(FadeIn(options))
        self.wait(30)

        self.play(Create(SurroundingRectangle(options[1], corner_radius=0.1, buff=0.1)))
        self.wait(4)


class Extend(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        _step1 = (
            MathTex(
                "\\text{In }\\Delta NPC \\ (\\angle C = 90^\\circ)",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .to_edge(UP)
        )

        _step2 = (
            MathTex(
                "NP = r + 6",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(_step1, DOWN, buff=0.25)
        )

        _step3 = (
            MathTex(
                "CN = 12 - r",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(_step2, DOWN, buff=0.25)
        )

        _step4 = (
            MathTex(
                "PC = 6",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(_step3, DOWN, buff=0.25)
        )

        self.play(FadeIn(_step1))
        self.wait(1)
        self.play(FadeIn(_step2))
        self.wait(1)
        self.play(FadeIn(_step3))
        self.wait(1)
        self.play(FadeIn(_step4))
        self.wait(1)

        self.play(FadeOut(_step1, _step2, _step3, _step4))

        step1 = (
            MathTex(
                "NP^2 = CN^2 + PC^2",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .to_edge(UP)
        )

        step2 = (
            MathTex(
                "(r+6)^2 = (12-r)^2 + 6^2",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step1, DOWN, buff=0.25)
        )

        step_final = (
            MathTex(
                "\\Rightarrow r = 4",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step2, DOWN, buff=0.25)
        )

        self.play(FadeIn(step1))
        self.wait(1)
        self.play(FadeIn(step2))
        self.wait(1)
        self.play(FadeIn(step_final))

