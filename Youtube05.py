from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        radius = 3
        A = LEFT * radius
        B = RIGHT * radius
        diameter = Line(A, B, color=BLACK)
        semicircle = ArcBetweenPoints(B, A, angle=PI, color=BLACK)

        # Point C moving on arc from 60 to 10 degrees
        arc_tracker = ValueTracker(135)

        def get_c():
            angle_rad = arc_tracker.get_value() * DEGREES
            return radius * np.array([np.cos(angle_rad), np.sin(angle_rad), 0])

        triangle_arc = always_redraw(
            lambda: Polygon(
                A, B, get_c(), fill_color=YELLOW, fill_opacity=1, color=BLACK
            )
        )

        radius_marker = Arrow(
            (A + B) / 2 + DOWN * 0.4,
            A + DOWN * 0.4,
            color=BLACK,
            stroke_width=4,
            buff=0,
        ).set_z_index(-20)

        radius_label = Text(
            "R", font="Comic Sans MS", font_size=28, color=NUMBRIK_COLOR
        ).next_to(radius_marker, 0, buff=0.2)

        radius_label_background = BackgroundRectangle(
            radius_label, color=WHITE, buff=0.1, fill_opacity=1
        ).set_z_index(-10)

        ## PART 1: Problem Introduction

        self.play(Create(semicircle), Create(diameter))
        self.play(Create(triangle_arc))
        self.wait(1)
        self.play(FadeIn(radius_label, radius_label_background), run_time=0.5)
        self.play(GrowArrow(radius_marker), run_time=0.5)
        self.wait(1)

        self.play(arc_tracker.animate.set_value(45), run_time=3, rate_func=smooth)
        clearScreen(self, 4)

        # Equal area triangle animation
        base_p1 = LEFT * 3
        base_p2 = RIGHT * 3
        height = 3
        tracker = ValueTracker(-2)

        def top_point():
            return np.array([tracker.get_value(), height, 0])

        area_triangle = always_redraw(
            lambda: Polygon(
                base_p1,
                base_p2,
                top_point(),
                fill_color=YELLOW,
                fill_opacity=1,
                color=BLACK,
            )
        )

        locus_p3 = DashedLine(
            base_p1 + UP * height + LEFT * 0.25,
            base_p2 + UP * height + RIGHT * 0.25,
            color=BLACK,
        )

        height_marker = DoubleArrow(
            base_p2 + 0.5 * RIGHT,
            base_p2 + 0.5 * RIGHT + UP * height,
            color=BLACK,
            stroke_width=4,
            buff=0,
        ).set_z_index(-20)

        height_label = Text(
            "H", font="Comic Sans MS", font_size=28, color=NUMBRIK_COLOR
        ).next_to(height_marker, 0)

        height_label_background = BackgroundRectangle(
            height_label, color=WHITE, buff=0.1, fill_opacity=1
        ).set_z_index(-10)

        base_marker = DoubleArrow(
            base_p1 + 0.4 * DOWN,
            base_p2 + 0.4 * DOWN,
            color=BLACK,
            stroke_width=4,
            buff=0,
        ).set_z_index(-20)

        base_label = Text(
            "B", font="Comic Sans MS", font_size=28, color=NUMBRIK_COLOR
        ).next_to(base_marker, 0)

        base_label_background = BackgroundRectangle(
            base_label, color=WHITE, buff=0.1, fill_opacity=1
        ).set_z_index(-10)

        # Part 2: Demonstrate equal area triangles on the same base

        self.play(FadeIn(area_triangle))
        self.play(Create(locus_p3))
        self.wait(1)

        self.play(FadeIn(height_label, height_label_background), run_time=0.5)
        self.play(GrowArrow(height_marker), run_time=0.5)
        self.play(FadeIn(base_label, base_label_background), run_time=0.5)
        self.play(GrowArrow(base_marker), run_time=0.5)
        self.wait(1)

        self.play(tracker.animate.set_value(2), run_time=3, rate_func=smooth)

        clearScreen(self, 4)

        ## Part 3: Demonstration of maximum area triangle

        self.play(Create(semicircle), Create(diameter))
        self.play(Create(triangle_arc))
        self.play(FadeIn(radius_label, radius_label_background), run_time=0.5)
        self.play(GrowArrow(radius_marker), run_time=0.5)
        self.wait(1)

        self.play(Create(locus_p3))
        self.play(arc_tracker.animate.set_value(90), run_time=2, rate_func=smooth)

        # Change height label to R
        height_label = Text(
            "R", font="Comic Sans MS", font_size=28, color=NUMBRIK_COLOR
        ).next_to(height_marker, 0)

        self.play(FadeIn(height_label, height_label_background), run_time=0.5)
        self.play(GrowArrow(height_marker), run_time=0.5)

        clearScreen(self, 4)

        # Part 4: Main solution (AM >= GM)

        arc_tracker.set_value(75)
        triangle_arc_new = Polygon(
            A, B, get_c(), fill_color=YELLOW, fill_opacity=0.5, color=BLACK
        )

        self.play(Create(semicircle), Create(diameter))
        self.play(Create(triangle_arc_new))
        self.play(FadeIn(radius_label, radius_label_background), run_time=0.5)
        self.play(GrowArrow(radius_marker), run_time=0.5)
        self.wait(1)

        line1 = Line(get_c(), A)
        line2 = Line(get_c(), B)
        right_angle = RightAngle(line1, line2, length=0.3, quadrant=(1, 1), color=BLACK)

        self.play(Create(right_angle))

        label_a = Text(
            "A", font="Comic Sans MS", font_size=28, color=NUMBRIK_COLOR
        ).next_to((get_c() + B) / 2, RIGHT, buff=0.3)

        label_b = Text(
            "B", font="Comic Sans MS", font_size=28, color=NUMBRIK_COLOR
        ).next_to((get_c() + A) / 2, LEFT, buff=0.4)

        self.play(FadeIn(label_a, label_b))

        self.wait(4)


class Statements(Scene):
    def construct(self):
        step1 = MathTex(
            "Area = \\frac{1}{2}BH = Constant",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        step2 = MathTex(
            "Max\\ Area = \\frac{1}{2}(2R)(R) = R^2",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        self.play(FadeIn(step1))
        clearScreen(self, 1)

        self.play(FadeIn(step2))
        clearScreen(self, 1)

        step3 = MathTex(
            "Arithmetic\\ Mean = \\frac{a_1 + a_2 + ... + a_n}{n}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        step4 = MathTex(
            "Geometric\\ Mean = \\sqrt[n]{a_1 \\cdot a_2 \\cdot ... \\cdot a_n}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step3, DOWN, buff=0.5)

        step5 = Text("AM-GM Inequality").next_to(step4, DOWN, buff=1).scale(0.95)

        finalStep = MathTex(
            "\\frac{a_1 + a_2 + ... + a_n}{n} \\geq \\sqrt[n]{a_1 \\cdot a_2 \\cdot ... \\cdot a_n}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step5, DOWN, buff=0.85)

        preq = MathTex(
            "where \\ a_1, a_2, ..., a_n \\in \\mathbb{R}^{+}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(finalStep, DOWN, buff=0.5)

        self.play(FadeIn(step3))
        self.wait(1)
        self.play(FadeIn(step4))
        self.wait(1)
        self.play(FadeIn(step5))
        self.wait(1)
        self.play(
            FadeIn(
                BackgroundRectangle(
                    step5,
                    color=RED_N100,
                    corner_radius=0.2,
                    buff=0.2,
                    fill_opacity=1,
                ).set_z_index(-10)
            )
        )
        self.wait(1)
        self.play(FadeIn(finalStep))
        self.wait(1)
        self.play(FadeIn(preq))

        clearScreen(self, 4)

        step6 = MathTex(
            "Let \\ a_1 = A^2, a_2 = B^2, n = 2",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        step7 = MathTex(
            "\\frac{A^2 + B^2}{2} \\geq \\sqrt{A^2B^2}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step6, DOWN, buff=0.5)

        step8 = MathTex(
            "\\Rightarrow \\frac{4R^2}{2} \\geq \\sqrt{A^2B^2}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step7, DOWN, buff=0.5)

        step8_ = MathTex(
            "\\Rightarrow AB \\leq 2R^2",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step8, DOWN, buff=0.5)

        step9 = MathTex(
            "Area  = \\frac{1}{2}AB \\leq R^2",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step8_, DOWN, buff=0.5)

        self.play(FadeIn(step6))
        self.wait(1)
        self.play(FadeIn(step7))
        self.wait(1)
        self.play(FadeIn(step8))
        self.wait(1)
        self.play(FadeIn(step8_))
        self.wait(1)
        self.play(FadeIn(step9))
        clearScreen(self, 4)

        extra1 = MathTex(
            "A^2 + B^2 = (2R)^2 = 4R^2",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        extra1_ = MathTex(
            "\\text{Using Pythagoras Th.}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(extra1, DOWN, buff=0.5)

        extra2 = MathTex(
            "Area = \\frac{1}{2}AB",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        extra3 = MathTex(
            "Max\\ Area = R^2",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        self.play(FadeIn(extra1))
        self.wait(1)
        self.play(FadeIn(extra1_))
        clearScreen(self, 2)
        self.play(FadeIn(extra2))
        clearScreen(self, 2)
        self.play(FadeIn(extra3))
        clearScreen(self, 2)
