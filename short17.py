from manim import *
from utils import *


class QuarterCircleWithSemicircles(Scene):
    def construct(self):
        themeColor = GREY_N500

        question = (
            MathTex(
                "\\text{Which of the following is true?}",
                color=BLACK,
            )
            .scale(0.8)
            .arrange(DOWN)
            .to_edge(UP)
        )

        self.play(FadeIn(question, shift=UP))

        R = 4  # Radius of the main quarter circle

        O = ORIGIN + 2 * DOWN + R / 2 * LEFT
        A = O + RIGHT * R
        B = O + UP * R

        # Draw quarter circle
        quarter_sector = Sector(
            radius=R,
            start_angle=0,
            angle=PI / 2,
            color=YELLOW,
            fill_opacity=1,
            stroke_width=DEFAULT_STROKE_WIDTH,
            stroke_color=themeColor,
            arc_center=O,
            z_index=-10,
        )

        radius1 = Line(O, A, color=themeColor)
        radius2 = Line(O, B, color=themeColor)

        self.play(Create(quarter_sector), Create(radius1), Create(radius2))

        # Semicircle on OA (horizontal)
        semi1 = Sector(
            radius=R / 2,
            angle=PI,
            arc_center=(O + A) / 2,
            color=themeColor,
            fill_color=WHITE,
            fill_opacity=1,
            stroke_width=DEFAULT_STROKE_WIDTH,
            stroke_color=themeColor,
        )

        # Semicircle on OB (vertical)
        semi2 = Sector(
            radius=R / 2,
            angle=PI,
            arc_center=(O + B) / 2,
            start_angle=-PI / 2,
            color=themeColor,
            fill_color=WHITE,
            fill_opacity=1,
            stroke_width=DEFAULT_STROKE_WIDTH,
            stroke_color=themeColor,
        )

        # Approximate the overlapping region using two filled circles and their intersection
        # Centered at midpoint of OA
        circle1 = Circle(radius=R / 2).move_to(O + RIGHT * R / 2)

        # Centered at midpoint of OB
        circle2 = Circle(radius=R / 2).move_to(
            O + UP * R / 2,
        )

        shaded_region = Intersection(
            circle1,
            circle2,
            color=YELLOW,
            fill_opacity=1,
            stroke_color=themeColor,
        )

        self.play(
            LaggedStart(
                Create(semi1), Create(semi2), Create(shaded_region), lag_ratio=0.2
            )
        )
        label1 = nMath("A_1").move_to(O + 2.5 * R / 4 * (UP + RIGHT))
        label2 = nMath("A_2").move_to(O + R / 4 * (UP + RIGHT))
        self.play(FadeIn(label1, label2))
        self.wait(4)

        area1 = Sector(
            radius=R,
            start_angle=0,
            angle=PI / 2,
            color=NUMBRIK_COLOR,
            fill_opacity=0.75,
            stroke_width=DEFAULT_STROKE_WIDTH,
            stroke_color=GREY_N400,
            arc_center=O,
            z_index=10,
        )

        area2 = Sector(
            radius=R / 2,
            angle=PI,
            arc_center=(O + A) / 2,
            color=themeColor,
            fill_color=NUMBRIK_COLOR,
            fill_opacity=0.75,
            stroke_width=DEFAULT_STROKE_WIDTH,
            stroke_color=GREY_N400,
            z_index=10,
        )

        area3 = Sector(
            radius=R / 2,
            angle=PI,
            arc_center=(O + B) / 2,
            start_angle=-PI / 2,
            color=themeColor,
            fill_color=NUMBRIK_COLOR,
            fill_opacity=0.75,
            stroke_width=DEFAULT_STROKE_WIDTH,
            stroke_color=GREY_N400,
            z_index=10,
        )

        area4 = Intersection(
            circle1,
            circle2,
            color=NUMBRIK_COLOR,
            fill_opacity=0.75,
            stroke_color=GREY_N400,
            z_index=10,
        )

        self.play(FadeIn(area1))
        self.wait(1)
        self.play(FadeOut(area1))
        self.wait(1)
        self.play(FadeIn(area2))
        self.wait(1)
        self.play(FadeOut(area2))
        self.wait(1)
        self.play(FadeIn(area3))
        self.wait(1)
        self.play(FadeOut(area3))
        self.wait(1)
        self.play(FadeIn(area4))
        self.wait(1)
        self.play(FadeOut(area4))
        self.wait(4)


class Statements(Scene):
    def construct(self):
        statement_groups = [
            [
                r"A_1 = A_L - 2A_S + A_2",
                r"A_1 = \frac{\pi R^2}{4} - 2\frac{\pi\left(\frac{R}{2}\right)^2}{2} + A_2",
                r"A_1 = \frac{\pi R^2}{4} - \frac{\pi R^2}{4} + A_2",
                r"\Rightarrow A_1 = A_2",
            ],
        ]

        for statements in statement_groups:
            prev = 0
            for stmt in statements:
                mathStmt = nMath(stmt)
                if prev == 0:
                    mathStmt.to_edge(UP)
                else:
                    mathStmt.next_to(prev, DOWN, buff=0.5)
                self.play(FadeIn(mathStmt))
                prev = mathStmt
                self.wait(1)
            clearScreen(self)


class Options(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        options = (
            VGroup(
                MathTex("A) \\ A_1 > A_2", color=BLACK),
                MathTex("B) \\ A_1 < A_2", color=BLACK),
                MathTex("C) \\ A_1 = A_2", color=BLACK),
                MathTex("D) \\ \\text{Cannot be compared}", color=BLACK),
            )
            .arrange(DOWN, center=False, buff=0.25, aligned_edge=LEFT)
            .to_edge(UP)
        )

        self.play(FadeIn(options))
        self.wait(5)

        self.wait(1)
        self.play(Create(SurroundingRectangle(options[2], corner_radius=0.1, buff=0.1)))
        self.wait(4)
