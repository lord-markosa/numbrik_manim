from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        R = 1.75

        stroke_color = GREY_N800

        O = ORIGIN + 1.5 * UP
        A = O + LEFT * R
        B = O + RIGHT * R
        C = O + DOWN * np.sqrt(3) * R

        # Draw circles
        circleA = Circle(
            radius=R, color=stroke_color, fill_color=WHITE, fill_opacity=1
        ).move_to(A)
        circleB = Circle(
            radius=R, color=stroke_color, fill_color=WHITE, fill_opacity=1
        ).move_to(B)
        circleC = Circle(
            radius=R, color=stroke_color, fill_color=WHITE, fill_opacity=1
        ).move_to(C)

        # Draw triangle between centers
        region = getTriangularRegion(A, B, C)

        AB = DashedLine(A, B, color=stroke_color)
        BC = DashedLine(B, C, color=stroke_color)
        CA = DashedLine(C, A, color=stroke_color)

        sectorA = Sector(
            radius=R,
            arc_center=A,
            start_angle=-PI / 3,
            angle=PI / 3,
            color=GREEN_N50,
            fill_opacity=1,
            stroke_width=DEFAULT_STROKE_WIDTH,
            stroke_color=stroke_color,
        )

        sectorB = Sector(
            radius=R,
            arc_center=B,
            start_angle=PI,
            angle=PI / 3,
            color=GREEN_N50,
            fill_opacity=1,
            stroke_width=DEFAULT_STROKE_WIDTH,
            stroke_color=stroke_color,
        )

        sectorC = Sector(
            radius=R,
            arc_center=C,
            start_angle=PI / 3,
            angle=PI / 3,
            color=GREEN_N50,
            fill_opacity=1,
            stroke_width=DEFAULT_STROKE_WIDTH,
            stroke_color=stroke_color,
        )

        sectorD = Sector(
            radius=R,
            arc_center=C,
            start_angle=0,
            angle=PI / 3,
            color=GREEN_N50,
            fill_opacity=1,
            stroke_width=DEFAULT_STROKE_WIDTH,
            stroke_color=stroke_color,
        )

        sectorE = Sector(
            radius=R,
            arc_center=C,
            start_angle=2 * PI / 3,
            angle=PI / 3,
            color=GREEN_N50,
            fill_opacity=1,
            stroke_width=DEFAULT_STROKE_WIDTH,
            stroke_color=stroke_color,
        )

        radius = Arrow(B, B + R * np.cos(PI / 4), color=stroke_color, z_index=5, buff=0)
        radiusLabel = nText("R").move_to(radius.get_center() + 0.3 * (DOWN + RIGHT))

        self.play(
            LaggedStart(
                Create(circleA), Create(circleB), Create(circleC), lag_ratio=0.4
            )
        )
        self.play(GrowArrow(radius), FadeIn(radiusLabel))
        self.wait(1)
        self.play(FadeIn(region))
        self.wait(1)
        self.play(Create(AB), Create(BC), Create(CA))
        self.wait(2)
        self.play(FadeIn(sectorA, sectorB, sectorC))
        self.play(
            Uncreate(circleA),
            Uncreate(circleB),
            Uncreate(circleC),
            Transform(AB, Line(A, B, color=GREY_N800)),
            Transform(BC, Line(B, C, color=GREY_N800)),
            Transform(CA, Line(C, A, color=GREY_N800)),
            FadeOut(radiusLabel, radius),
        )
        self.wait(2)
        self.play(
            ClockwiseTransform(sectorB, sectorD),
            CounterclockwiseTransform(sectorA, sectorE),
        )
        self.wait(1)

        self.wait(4)


class Statements(Scene):
    def construct(self):
        question = MathTex(
            "\\text{Calculate the highlighted area.}", color=BLACK
        ).to_edge(UP)
        self.play(FadeIn(question, scale=1.2))
        clearScreen(self, 4)

        step1 = nMath("Ar(eq.\\triangle - semicircle)").to_edge(UP)
        step2 = nMath("\\frac{\\sqrt{3}}{4}(2R)^2 - \\frac{\\pi R^2}{2}").next_to(
            step1, DOWN, buff=0.5
        )
        step3 = nMath("\\left( \\sqrt{3} - \\frac{\\pi}{2} \\right)R^2").next_to(
            step2, DOWN, buff=0.5
        )

        self.play(fadeInTex(step1))
        self.wait(1)
        self.play(fadeInTex(step2))
        self.wait(1)
        self.play(fadeInTex(step3))
        highlight(self, step3, buff=0.2, wait_time=4)
