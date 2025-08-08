# find the area of this circular ring

from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        # Draw a shaded circular ring (annulus)
        outer_circle = Circle(
            radius=3, color=YELLOW, stroke_color=BLACK, fill_opacity=1
        )
        inner_radius = ValueTracker(0.1)
        inner_circle = always_redraw(
            lambda: Circle(
                radius=inner_radius.get_value(),
                color=WHITE,
                fill_opacity=1,
                stroke_color=BLACK,
            )
        )
        # ring = Difference(
        #     outer_circle.copy().set_fill(BLUE, 0.5),
        #     inner_circle.copy().set_fill(BLACK, 1),
        # )
        # self.play(FadeIn(ring))

        self.play(Create(outer_circle), rate_functions=smooth)
        self.wait(1)

        self.add(inner_circle)
        self.play(
            inner_radius.animate.set_value(1.75), run_time=0.75, rate_func=rush_from
        )
        self.play(
            inner_radius.animate.set_value(1.5), run_time=0.25, rate_func=rush_from
        )
        self.wait(1)

        # Draw a chord of the outer circle that is tangent to the inner circle
        # For simplicity, draw a horizontal chord at y = 1 (tangent to inner circle with radius 1)
        x = np.sqrt(outer_circle.radius**2 - inner_radius.get_value() ** 2)
        chord_end_1 = ([-x, inner_radius.get_value(), 0],)
        chord_end_2 = ([x, inner_radius.get_value(), 0],)
        chord = Line(
            chord_end_1,
            chord_end_2,
            color=BLACK,
        )
        self.play(Create(chord))

        label_chord = Text(
            "30", font="Segoe UI Symbol", font_size=28, color=BLACK
        ).next_to(chord, UP, buff=0.2)

        self.play(FadeIn(label_chord))
        self.wait(2)

        # Solution

        outerRadiusMarker = Arrow(
            ORIGIN,
            ORIGIN + DOWN * 3 / 2**0.5 + LEFT * 3 / 2**0.5,
            color=NUMBRIK_COLOR,
            stroke_width=4,
            buff=0,
        )

        outerRadiusLabel = (
            MathTex(
                "R_1", tex_template=TexFontTemplates.comic_sans, color=NUMBRIK_COLOR
            )
            .next_to(0.8 * LEFT + 0.3 * DOWN, 0)
            .scale(0.8)
        )

        innerRadiusMarker = Arrow(
            ORIGIN,
            ORIGIN + DOWN * 1.5 / 2**0.5 + RIGHT * 1.5 / 2**0.5,
            color=NUMBRIK_COLOR,
            stroke_width=4,
            buff=0,
        )

        innerRadiusLabel = (
            MathTex(
                "R_2", tex_template=TexFontTemplates.comic_sans, color=NUMBRIK_COLOR
            )
            .next_to(0.8 * RIGHT + 0.3 * DOWN, 0)
            .scale(0.8)
        )

        self.play(GrowArrow(innerRadiusMarker), GrowArrow(outerRadiusMarker))
        self.play(FadeIn(innerRadiusLabel, outerRadiusLabel))

        self.wait(2)

        self.play(
            FadeOut(
                innerRadiusLabel, innerRadiusMarker, outerRadiusLabel, outerRadiusMarker
            )
        )

        dashedInnerRadius = DashedLine(ORIGIN, ORIGIN + UP * 1.5, color=NUMBRIK_COLOR)
        dashedOuterRadius = DashedLine(
            ORIGIN, ORIGIN + 1.5 * UP + LEFT * x, color=NUMBRIK_COLOR
        )

        right_angle = RightAngle(
            dashedInnerRadius, chord, length=0.3, quadrant=(-1, -1), color=NUMBRIK_COLOR
        )

        self.play(Create(dashedInnerRadius), Create(dashedOuterRadius))
        self.wait(1)
        self.play(Create(right_angle))
        self.wait(1)

        innerRadiusLabel.next_to(dashedInnerRadius, RIGHT, buff=0.2)
        outerRadiusLabel.next_to(LEFT + UP * 0.2, 0)

        self.play(FadeIn(innerRadiusLabel, outerRadiusLabel))

        label_chord2 = (
            MathTex("15", tex_template=TexFontTemplates.comic_sans, color=NUMBRIK_COLOR)
            .next_to(UP * 1.8 + LEFT * x / 2, 0)
            .scale(0.8)
        )

        self.wait(2)

        self.play(FadeOut(label_chord))
        self.play(FadeIn(label_chord2))

        self.wait(4)


class Statements(Scene):
    def construct(self):
        step1 = MathTex(
            "Area = \\pi (R_1^2 - R_2^2)",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        step2 = MathTex(
            "R_1^2 - R_2^2 = 15^2",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step1, DOWN, buff=0.5)

        step3 = MathTex(
            "\\Rightarrow Area = \\pi\\cdot15^2 = 225\\pi",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step2, DOWN, buff=0.5)

        self.play(FadeIn(step1, shift=0.4 * UP))
        self.wait(1)
        self.play(FadeIn(step2, shift=0.4 * UP))
        self.wait(1)
        self.play(FadeIn(step3, shift=0.4 * UP))

        self.wait(4)
