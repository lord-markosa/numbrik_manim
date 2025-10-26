from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        a = 2

        center = ORIGIN + DOWN * a / 2
        circle = Sector(
            radius=a,
            arc_center=center,
            stroke_color=GREY_N400,
            fill_opacity=1,
        )

        triangle = Polygon(
            center + UP * a + RIGHT * a,
            center + UP * a,
            center + RIGHT * a,
            color=YELLOW,
            fill_opacity=1,
            stroke_color=GREY_N400,
            stroke_width=0,
        )

        A, B, C = triangle.get_vertices()

        line1 = Line(A, B, color=GREY_N400)
        line2 = Line(A, C, color=GREY_N400)

        arc1 = Arc(
            a,
            start_angle=PI / 2,
            angle=-PI / 2,
            arc_center=center,
            color=GREY_N400,
            z_index=0.001,
        )

        area = Intersection(
            circle,
            triangle,
            color=WHITE,
            fill_opacity=1,
            stroke_color=WHITE,
            z_index=0,
        )

        grp1 = VGroup(triangle, area, arc1, line1, line2)

        area2 = grp1.copy().rotate(PI, UP + LEFT, center + a / 2 * UP + a / 2 * RIGHT)

        side = lengthMarkerV2(
            a * UP + a * RIGHT,
            a * UP + a * LEFT,
            "2a",
            0.5 * UP,
        )

        self.add(grp1, area2)
        self.wait(1)
        self.play(Rotate(area2, PI / 2, IN, center + UP * a), run_time=2)

        rotation_axis = DashedLine(RIGHT * 1.5 * a, LEFT * 1.5 * a, color=GREY_N400)

        tmpGrp = VGroup(grp1, area2)
        self.play(tmpGrp.animate.shift(UP * a / 2), run_time=1.5)
        self.play(Create(rotation_axis), run_time=1.5)
        self.play(
            Rotate(
                tmpGrp.copy(),
                PI,
                rotation_axis.get_unit_vector(),
                ORIGIN,
            ),
            run_time=2,
        )
        self.wait(1)

        self.play(GrowArrow(side[0]), GrowArrow(side[1]), FadeIn(side[2]))
        squareFinal = Square(2 * a, color=ORANGE, fill_opacity=0.5, z_index=0.02)
        self.play(FadeIn(squareFinal))
        self.wait(0.5)
        self.play(FadeOut(squareFinal))

        circle = Circle(a, color=NUMBRIK_COLOR_50, fill_opacity=0.5, z_index=0.02)
        self.play(FadeIn(circle))
        self.wait(0.5)
        self.play(FadeOut(circle))

        self.wait(10)


class Intro(Scene):
    def construct(self):
        a = 4

        square1 = Square(a).set_color_by_gradient([BLUE, WHITE]).set_stroke(GREY_N400)

        self.play(Create(square1))

        side = lengthMarkerV2(
            a / 2 * DOWN + a / 2 * RIGHT, a / 2 * UP + a / 2 * RIGHT, "a", 0.5 * RIGHT
        )

        self.play(GrowArrow(side[0]), GrowArrow(side[1]), FadeIn(side[2]))
        self.wait(1)

        theta = ValueTracker(0)

        arc1 = always_redraw(
            lambda: Arc(
                radius=a,
                arc_center=square1.get_corner(DL),
                start_angle=PI / 2,
                angle=-theta.get_value(),
                color=GREY_N400,
            )
        )
        radius1 = always_redraw(
            lambda: Line(
                square1.get_corner(DL),
                square1.get_corner(DL)
                + a * np.sin(-theta.get_value() + PI / 2) * UP
                + a * np.cos(-theta.get_value() + PI / 2) * RIGHT,
                color=YELLOW,
            )
        )

        alpha = ValueTracker(0)

        arc2 = always_redraw(
            lambda: Arc(
                radius=a,
                arc_center=square1.get_corner(UR),
                start_angle=PI,
                angle=alpha.get_value(),
                color=GREY_N400,
            )
        )
        radius2 = always_redraw(
            lambda: Line(
                square1.get_corner(UR),
                square1.get_corner(UR)
                + a * np.sin(alpha.get_value() + PI) * UP
                + a * np.cos(alpha.get_value() + PI) * RIGHT,
                color=YELLOW,
            )
        )

        self.add(
            arc1,
            arc2,
        )

        self.play(Create(radius1))
        self.play(theta.animate.set_value(PI / 2), run_time=2)
        self.play(LaggedStart(FadeOut(radius1), Create(radius2), lag_ratio=0.5))
        self.play(alpha.animate.set_value(PI / 2), run_time=2)
        self.play(FadeOut(radius2))
        self.wait(5)


class HighlightArea(Scene):
    def construct(self):
        a = 4

        center = ORIGIN + DOWN * a / 2 + LEFT * a / 2

        circle = Sector(
            radius=a,
            arc_center=center,
            stroke_color=GREY_N400,
            fill_opacity=1,
        )

        triangle = Polygon(
            -center,
            center + UP * a,
            center + RIGHT * a,
            color=YELLOW,
            fill_opacity=1,
            stroke_color=GREY_N400,
            stroke_width=0,
            z_index=1,
        )

        arc1 = Arc(
            a,
            start_angle=PI / 2,
            angle=-PI / 2,
            arc_center=center,
            color=GREY_N400,
            z_index=10,
        )

        displaySquare = Square(a, color=GREY_N400, z_index=10)

        # color is set to white to hide any unwanted extra line
        area = Intersection(
            circle,
            triangle,
            color=WHITE,
            fill_opacity=1,
            stroke_color=WHITE,
            z_index=5,
        )

        grp1 = VGroup(
            triangle,
            area,
            arc1,
        )

        area2 = grp1.copy().rotate(PI, UP + LEFT, ORIGIN)

        side = lengthMarkerV2(
            a / 2 * DOWN + a / 2 * RIGHT, a / 2 * UP + a / 2 * RIGHT, "a", 0.5 * RIGHT
        )

        self.add(displaySquare, grp1, area2, side)

        self.play(FadeIn(grp1[0], area2[0]))
        self.wait(1)
        self.play(FadeOut(side))
        self.play(
            VGroup(grp1, area2, displaySquare).animate.scale(0.5).shift(RIGHT * a / 4)
        )

        self.wait(10)


class Statements(Scene):
    def construct(self):
        stmt2 = nMath("2 \\times Area", "=", "(2a)^2", "-", "\\pi a^2").to_edge(UP)
        stmt3 = nMath("Area", "=", "\\left(2-\\frac{\\pi}{2}\\right)a^2").next_to(
            stmt2, DOWN, buff=0.5
        )
        self.play(FadeIn(stmt2[0]))
        self.wait(0.5)
        self.play(FadeIn(stmt2[1:3]))
        self.wait(0.5)
        self.play(FadeIn(stmt2[3:]))
        self.wait(1)
        self.play(fadeInTex(stmt3))

        self.wait(10)
