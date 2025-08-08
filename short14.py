from manim import *
from utils import *
import numpy as np


class ConstantInscribedAngle(Scene):
    def construct(self):
        radius = 2.5
        theme_black = GREY_N800

        # Fixed base points A and B on circle (chord)
        A = np.array(
            [-radius * np.sin(30 * DEGREES), -radius * np.cos(30 * DEGREES), 0]
        )
        B = np.array([radius * np.sin(30 * DEGREES), -radius * np.cos(30 * DEGREES), 0])

        labelA = (
            MathTex("A", tex_template=TexFontTemplates.comic_sans, color=NUMBRIK_COLOR)
            .scale(0.7)
            .next_to(A, DOWN + 0.5 * LEFT, buff=0.1)
        )

        labelB = (
            MathTex("B", tex_template=TexFontTemplates.comic_sans, color=NUMBRIK_COLOR)
            .scale(0.7)
            .next_to(B, DOWN + 0.5 * RIGHT, buff=0.1)
        )

        # Draw the circle
        circle = Circle(radius=radius, color=theme_black).move_to(ORIGIN)

        # Create ValueTracker to control the vertex angle position
        angle_tracker = ValueTracker(PI / 2)

        # Get moving point C on the arc such that angle ACB = 30°
        def get_point_C():
            angle = angle_tracker.get_value()
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            return np.array([x, y, 0])

        # Define always-updating point C
        dotO = Dot(ORIGIN, color=theme_black, radius=0.05)
        dotO.z_index = 10

        labelO = (
            MathTex("O", tex_template=TexFontTemplates.comic_sans, color=NUMBRIK_COLOR)
            .scale(0.7)
            .next_to(ORIGIN, UP, buff=0.2)
        )

        # Triangle sides
        lineAC = always_redraw(lambda: Line(A, get_point_C(), color=theme_black))
        lineBC = always_redraw(lambda: Line(B, get_point_C(), color=theme_black))
        base = Line(A, B, color=theme_black)

        # Angle marker at C
        angle_arc = always_redraw(
            lambda: Angle(
                lineAC,
                lineBC,
                quadrant=(-1, -1),
                radius=0.6,
                other_angle=False,
                color=theme_black,
            )
        )

        # Find projection of O onto AB
        AB = B - A
        AB_unit = AB / np.linalg.norm(AB)
        OA = ORIGIN - A
        proj_length = np.dot(OA, AB_unit)
        P = A + proj_length * AB_unit

        def getVectorCP():
            C = get_point_C()
            CP = P - C
            CP_unit = CP / np.linalg.norm(CP)
            return CP_unit

        labelC = always_redraw(
            lambda: MathTex(
                "C", tex_template=TexFontTemplates.comic_sans, color=NUMBRIK_COLOR
            )
            .scale(0.7)
            .move_to(get_point_C() - 0.4 * getVectorCP())
        )

        # Angle label
        angle_label = always_redraw(
            lambda: MathTex(
                "30^{\\circ}",
                tex_template=TexFontTemplates.comic_sans,
                color=NUMBRIK_COLOR,
            )
            .scale(0.6)
            .move_to(get_point_C() + 1.1 * getVectorCP())
        )

        # Base label and marker
        base_label = (
            MathTex("12", tex_template=TexFontTemplates.comic_sans, color=NUMBRIK_COLOR)
            .scale(0.7)
            .next_to(base, DOWN, buff=0.5)
        )

        base_label_background = BackgroundRectangle(
            base_label, color=WHITE, buff=0.1, fill_opacity=1
        ).set_z_index(-10)

        base_marker = DoubleArrow(
            A + 0.7 * DOWN,
            B + 0.7 * DOWN,
            color=NUMBRIK_COLOR,
            stroke_width=4,
            buff=0,
        ).set_z_index(-20)

        self.play(Create(base))
        self.play(FadeIn(base_label, base_label_background, labelA, labelB))
        self.play(GrowArrow(base_marker))
        self.play(Create(lineAC), Create(lineBC))
        self.play(FadeIn(labelC))
        self.play(Create(angle_arc), FadeIn(angle_label))
        self.wait(2)

        self.play(Create(circle), Create(dotO), FadeIn(labelO))
        self.wait(1)

        # self.play(FadeOut(angle_label))

        # Animate the point moving along the arc to show angle stays the same
        self.play(
            angle_tracker.animate.set_value(30 * DEGREES),
            run_time=2,
            rate_func=smooth,
        )

        self.wait(0.25)

        self.play(
            angle_tracker.animate.set_value(150 * DEGREES),
            run_time=4,
            rate_func=smooth,
        )

        self.wait(0.25)

        self.play(
            angle_tracker.animate.set_value(90 * DEGREES),
            run_time=2,
            rate_func=smooth,
        )

        # self.play(FadeIn(angle_label))

        # self.play(angle_tracker.animate.set_value(PI / 2), run_time=3, rate_func=smooth)
        self.wait(1)

        # Draw lines OA and OB from the center to points A and B
        O = ORIGIN
        lineOA = DashedLine(O, A, color=theme_black, dashed_ratio=0.8)
        lineOB = DashedLine(O, B, color=theme_black, dashed_ratio=0.8)
        self.play(Create(lineOA), Create(lineOB))
        self.wait(1)

        angle2 = Angle(
            lineOA,
            lineOB,
            # quadrant=(-1, -1),
            radius=0.6,
            other_angle=False,
            color=theme_black,
        )

        angle2Label = (
            MathTex(
                "60^{\\circ}",
                tex_template=TexFontTemplates.comic_sans,
                color=NUMBRIK_COLOR,
            )
            .scale(0.6)
            .next_to(angle2, DOWN, buff=0.15)
        )

        self.play(Create(angle2), FadeIn(angle2Label))
        self.wait(1)

        # perpendicular = DashedLine(O, proj_point, color=NUMBRIK_COLOR)

        # rtAngle = RightAngle(
        #     Line(A, B), perpendicular, length=0.3, quadrant=(1, -1), color=NUMBRIK_COLOR
        # )

        # self.play(FadeOut(angle2Label))
        # self.play(Create(perpendicular))
        # self.play(Create(rtAngle))

        triangle_area = Polygon(
            ORIGIN, A, B, color=YELLOW_N50, fill_opacity=1, stroke_width=0
        )
        triangle_area.z_index = -10
        self.play(FadeIn(triangle_area))

        self.wait(4)


class Statements(Scene):
    def construct(self):
        question = MathTex(
            "\\text{The circumradius (R) is:}",
            color=GREY_N800,
        ).to_edge(UP)

        self.play(FadeIn(question, shift=0.5 * UP))
        self.wait(4)
        self.play(FadeOut(question))
        self.wait(1)

        step1 = MathTex(
            "\\angle AOB = 2\\angle ACB = 60^\\circ",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        step2 = MathTex(
            "R = AO = BO",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step1, DOWN, buff=0.5)

        step3 = MathTex(
            "\\Rightarrow \\Delta AOB \\text{ is equilateral}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step2, DOWN, buff=0.5)

        step4 = MathTex(
            "R = AB = 12",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step3, DOWN, buff=0.7)

        self.play(FadeIn(step1, shift=0.5 * UP))
        self.wait(1)
        self.play(FadeIn(step2))
        self.wait(1)
        self.play(FadeIn(step3))
        self.wait(1)
        self.play(FadeIn(step4))
        highlight(self, step4, buff=0.2, wait_time=4)


class Options(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        options = (
            VGroup(
                VGroup(
                    MathTex("A) \\ 6", color=BLACK),
                    MathTex("C) \\ 12", color=BLACK),
                ).arrange(DOWN, buff=0.25, aligned_edge=LEFT),
                VGroup(
                    MathTex("B) \\ 6\\sqrt{3}", color=BLACK),
                    MathTex("D) \\ 12\\sqrt{3}", color=BLACK),
                ).arrange(DOWN, buff=0.25, aligned_edge=LEFT),
            )
            .arrange(RIGHT, buff=2)
            .to_edge(UP)
        )

        self.play(FadeIn(options))
        self.wait(5)

        self.wait(1)
        self.play(
            Create(SurroundingRectangle(options[0][1], corner_radius=0.1, buff=0.1))
        )
        self.wait(4)
