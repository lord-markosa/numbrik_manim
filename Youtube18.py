from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        stroke_color = GREY_N800
        base = 6
        height = 5
        radius = base * height / (base + height)
        theta = np.arctan(height / base)

        A = ORIGIN + 2.5 * DOWN + LEFT * 3
        B = A + RIGHT * base
        C = A + height * UP

        labelA = nText("A").move_to(A + 0.4 * DOWN + 0.4 * LEFT)
        labelB = nText("B").move_to(B + 0.4 * DOWN + 0.4 * RIGHT)
        labelC = nText("C").move_to(C + 0.4 * UP + 0.4 * LEFT)

        arc_center = A + radius * RIGHT + radius * UP

        triangle = Polygon(A, B, C, color=stroke_color)
        semi = Sector(
            radius=radius,
            start_angle=PI - theta,
            angle=PI,
            arc_center=arc_center,
            color=YELLOW,
            fill_opacity=1,
            stroke_width=DEFAULT_STROKE_WIDTH,
            stroke_color=stroke_color,
        )

        labelHeight = lengthMarker(A + 0.4 * LEFT, C + 0.4 * LEFT, label="5")
        labelBase = lengthMarker(A + 0.4 * DOWN, B + 0.4 * DOWN, label="6")

        rightAngle1 = RightAngle(Line(A, B), Line(A, C), length=0.3, color=stroke_color)

        labelArea = nText("Area = ?").move_to(arc_center + UP + 2 * RIGHT)
        areaArrow = CurvedArrow(
            labelArea.get_left() + 0.5 * LEFT,
            arc_center + DOWN + 0.5 * LEFT,
            color=GREY_N400,
        )
        labelAreaHighlight = SurroundingRectangle(
            labelArea, corner_radius=0.1, buff=0.2, color=RED_N100
        )

        self.play(
            LaggedStart(
                Create(triangle),
                Create(rightAngle1),
                FadeIn(labelA, labelB, labelC, scale=1.2),
                lag_ratio=0.6,
            )
        )
        self.wait(1)
        self.play(Create(semi))
        self.wait(1)
        self.play(FadeIn(labelHeight[1], labelHeight[2]))
        self.play(GrowArrow(labelHeight[0]))
        self.wait(1)
        self.play(FadeIn(labelBase[1], labelBase[2]))
        self.play(GrowArrow(labelBase[0]))
        self.wait(1)
        self.play(fadeInTex(labelArea), Create(areaArrow), Create(labelAreaHighlight))
        self.wait(4)
        self.play(FadeOut(labelArea, areaArrow, labelAreaHighlight))
        self.wait(1)

        # SOLUTION

        proj1 = A + radius * UP
        proj2 = A + radius * RIGHT

        radius1 = DashedLine(proj1, arc_center, color=stroke_color)
        radius2 = DashedLine(proj2, arc_center, color=stroke_color)

        rightAngle2 = RightAngle(
            Line(proj1, arc_center), Line(proj1, C), length=0.3, color=stroke_color
        )
        rightAngle3 = RightAngle(
            Line(proj2, B), Line(proj2, arc_center), length=0.3, color=stroke_color
        )

        radiusLabel = nText("R").move_to(radius2.get_center() + 0.4 * LEFT).scale(1.1)

        tempPolygon = Polygon(proj2, arc_center, B, color=RED_N100, stroke_width=7)
        tempPolygon2 = Polygon(A, C, B, color=RED_N100, stroke_width=7)

        self.play(LaggedStart(Create(radius1), Create(radius2), lag_ratio=0.8))
        self.play(Create(rightAngle2), Create(rightAngle3))
        self.wait(1)
        self.play(FadeIn(radiusLabel))
        self.wait(1)
        self.play(Create(tempPolygon), run_time=1)
        self.wait(1)
        self.play(Uncreate(tempPolygon))
        self.wait(1)
        self.play(Create(tempPolygon2))
        self.wait(1)
        self.play(Uncreate(tempPolygon2))
        self.wait(1)

        highlight1 = SurroundingRectangle(
            labelHeight[1], corner_radius=0.1, buff=0.15, color=RED_N100
        )
        highlight2 = SurroundingRectangle(
            radiusLabel, corner_radius=0.1, buff=0.15, color=RED_N100
        )

        self.play(Create(highlight1), Create(highlight2))
        self.wait(1)
        self.play(Uncreate(highlight1), Uncreate(highlight2))
        self.wait(1)

        labelBase2 = lengthMarker(
            arc_center + 0.3 * UP, B + (radius + 0.3) * UP, label="6-R"
        )
        labelBase2Marker = DashedLine(B, B + (radius + 0.5) * UP, color=GREY_N400)

        self.play(
            Create(labelBase2Marker),
            FadeIn(labelBase2[1], labelBase2[2]),
        )
        self.play(GrowArrow(labelBase2[0]))

        highlight3 = SurroundingRectangle(
            labelBase2[1], corner_radius=0.1, buff=0.15, color=RED_N100
        )
        highlight4 = SurroundingRectangle(
            labelBase[1], corner_radius=0.1, buff=0.15, color=RED_N100
        )

        self.play(Create(highlight3), Create(highlight4))
        self.wait(1)
        self.play(Uncreate(highlight3), Uncreate(highlight4))
        self.wait(1)

        self.wait(1)

        self.wait(4)


class Statements(Scene):
    def construct(self):
        step1 = nMath("\\text{Using }\\triangle \\text{ similarity:}").to_edge(UP)
        step2 = nMath("\\frac{R}{5} = ", "\\frac{6-R}{6}").next_to(
            step1, DOWN, buff=0.5
        )
        step3 = nMath("11R = 30").next_to(step2, DOWN, buff=0.5)
        step4 = nMath("R = \\frac{30}{11}").next_to(step3, DOWN, buff=0.5)
        self.play(fadeInTex(step1))
        self.wait(1)
        self.play(fadeInTex(step2[0]))
        self.wait(1)
        self.play(fadeInTex(step2[1]))
        self.wait(1)
        self.play(fadeInTex(step3))
        self.wait(1)
        self.play(fadeInTex(step4))

        step5 = nMath("Area ", "= \\frac{\\pi R^2}{2} = \\frac{450\\pi}{121}").next_to(
            step4, DOWN, buff=0.75
        )
        self.play(fadeInTex(step5))
        highlight(self, step5, buff=0.2, wait_time=4)


class Thumnnail(Scene):
    def construct(self):
        stroke_width = 6
        stroke_color = GREY_N800
        base = 6
        height = 5
        radius = base * height / (base + height)
        theta = np.arctan(height / base)

        A = ORIGIN + 2.5 * DOWN + LEFT * 3
        B = A + RIGHT * base
        C = A + height * UP

        arc_center = A + radius * RIGHT + radius * UP

        triangle = Polygon(A, B, C, color=stroke_color, stroke_width=stroke_width)
        semi = Sector(
            radius=radius,
            start_angle=PI - theta,
            angle=PI,
            arc_center=arc_center,
            color=NUMBRIK_COLOR_50,
            fill_opacity=1,
            stroke_width=stroke_width,
            stroke_color=stroke_color,
        )

        labelHeight = lengthMarker(A + 0.4 * LEFT, C + 0.4 * LEFT, label="5")
        labelBase = lengthMarker(A + 0.4 * DOWN, B + 0.4 * DOWN, label="6")

        rightAngle1 = RightAngle(Line(A, B), Line(A, C), length=0.3, color=stroke_color)

        self.add(triangle, semi, rightAngle1)

        self.wait(10)
