from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        # Define radius of outer (quarter) circle
        R = 6

        newOrigin = ORIGIN + 3 * DOWN + 3 * LEFT

        # Create quarter circle (arc from 0 to 90 degrees)
        quarter_circle = Arc(
            radius=R, start_angle=0, angle=PI / 2, arc_center=newOrigin, color=GREY_N400
        )

        # Create the straight edges (x-axis and y-axis legs)
        leg_x = Line(newOrigin, newOrigin + RIGHT * R, color=GREY_N400)
        leg_y = Line(newOrigin, newOrigin + UP * R, color=GREY_N400)

        # Fill the quarter circle area
        shaded_area = Sector(
            R, color=YELLOW, stroke_color=GREY_N400, fill_opacity=1
        ).shift(3 * DOWN + 3 * LEFT)

        # Inner circle: touches the vertical side (y-axis leg)
        # We'll place its center somewhere along the quarter circle's x-axis

        r_small = 1.5  # radius of inner circle
        inner_center = newOrigin + RIGHT * r_small + UP * (r_small + 0.5)
        inner_circle = Circle(
            radius=r_small, color=WHITE, stroke_color=GREY_N400, fill_opacity=1
        ).move_to(inner_center)

        # Tangent half-chord line:
        # Draw a line from somewhere on quarter arc to the x-axis that is tangent to inner circle

        # Let's define it geometrically:
        # Pick point A on the arc at 60 degrees
        theta = PI / 3  # 60 degrees
        arc_point = newOrigin + R * np.array([np.cos(theta), np.sin(theta), 0])
        bottom_point = newOrigin + 2 * r_small * RIGHT  # Point on top of inner circle

        # Draw a chord from arc_point to a point on x-axis such that it is tangent
        # We'll just draw a line from arc_point to the tangent point for simplicity
        tangent_line = Line(arc_point, bottom_point, color=GREY_N400)

        length_label = (
            Text("12", font_size=32, font="Comic Sans MS", color=NUMBRIK_COLOR)
            .next_to(tangent_line, RIGHT, buff=0.2)
            .shift(UP * 0.5)
        )

        self.play(
            FadeIn(shaded_area), Create(quarter_circle), Create(leg_x), Create(leg_y)
        )
        self.wait(1)
        self.play(Create(inner_circle))
        self.wait(1)
        self.play(Create(tangent_line), FadeIn(length_label, shift=0.25 * LEFT))
        self.wait(2)

        # Solution

        outerRadiusMarker = Arrow(
            newOrigin + 0.5 * LEFT,
            newOrigin + R * UP + 0.5 * LEFT,
            color=NUMBRIK_COLOR,
            stroke_width=4,
            buff=0,
        )

        outerRadiusLabel = Text(
            "R", font="Comic Sans MS", font_size=32, color=NUMBRIK_COLOR
        ).next_to(outerRadiusMarker, LEFT, buff=0.1)

        innerRadiusMarker = Arrow(
            inner_center,
            inner_center + r_small * RIGHT,
            color=NUMBRIK_COLOR,
            stroke_width=4,
            buff=0,
        )

        innerRadiusLabel = Text(
            "r", font="Comic Sans MS", font_size=32, color=NUMBRIK_COLOR
        ).next_to(innerRadiusMarker, UP, buff=0.05)

        self.play(GrowArrow(innerRadiusMarker), GrowArrow(outerRadiusMarker))
        self.play(FadeIn(innerRadiusLabel, outerRadiusLabel))
        self.wait(2)

        labelO = Text(
            "O", font_size=32, font="Comic Sans MS", color=NUMBRIK_COLOR
        ).next_to(newOrigin, DOWN, buff=0.2)
        labelA = Text(
            "A", font_size=32, font="Comic Sans MS", color=NUMBRIK_COLOR
        ).next_to(arc_point, UP, buff=0.3)
        labelB = Text(
            "B", font_size=32, font="Comic Sans MS", color=NUMBRIK_COLOR
        ).next_to(bottom_point, DOWN, buff=0.2)

        lineOA = DashedLine(newOrigin, arc_point, color=GREY_N400)

        self.play(
            Create(lineOA),
            FadeIn(labelA, shift=0.25 * DOWN),
            FadeIn(labelO, labelB, shift=0.25 * UP),
        )

        self.wait(4)


class Statements(Scene):
    def construct(self):
        step1 = MathTex(
            "Area",
            "= \\frac{\\pi R^2}{4} - \\pi r^2",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        step2 = MathTex(
            "= \\frac{\\pi}{4}(R^2 - 4r^2)",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step1[1], DOWN, buff=0.5, aligned_edge=LEFT)

        self.play(FadeIn(step1))
        self.wait(1)
        self.play(FadeIn(step2))

        clearScreen(self, 1)

        step3 = MathTex(
            "\\text{In } \\triangle OAB",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        step4 = MathTex(
            "OA^2 = OB^2 + AB^2",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step3, DOWN, buff=0.5)

        step5 = MathTex(
            "R^2 = (2r)^2 + 12^2",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step4, DOWN, buff=0.5)

        step6 = MathTex(
            "\\Rightarrow R^2 - 4r^2 = 12^2",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step5, DOWN, buff=0.5)

        self.play(FadeIn(step3))
        self.wait(1)
        self.play(FadeIn(step4))
        self.wait(1)
        self.play(FadeIn(step5))
        self.wait(1)
        self.play(FadeIn(step6))

        clearScreen(self, 1)

        step7 = MathTex(
            "Area ",
            "= \\frac{\\pi}{4}(R^2 - 4r^2)",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        step8 = MathTex(
            "= \\frac{\\pi}{4}(12^2)",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step7[1], DOWN, buff=0.5, aligned_edge=LEFT)

        step9 = MathTex(
            "= 36\\pi",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step8, DOWN, buff=0.5, aligned_edge=LEFT)

        self.play(FadeIn(step7))
        self.wait(1)
        self.play(FadeIn(step8))
        self.wait(1)
        self.play(FadeIn(step9))
        self.wait(1)

        self.wait(4)
