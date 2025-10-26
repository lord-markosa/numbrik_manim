from manim import *
from utils import *


class TriangleSimilarity(Scene):
    def construct(self):
        # Create a triangle ABC
        A = Dot([-3, -2, 0], color=RED)
        B = Dot([0, 3, 0], color=RED)
        C = Dot([3, -2, 0], color=RED)

        triangle = (
            Polygon(
                A.get_center(),
                B.get_center(),
                C.get_center(),
                stroke_color=[GREY_N200, GREY_N800],
                stroke_width=6,
                sheen_direction=RIGHT,
            )
            .move_to(ORIGIN)
            .shift(LEFT * 2)
        )

        A, B, C = triangle.get_vertices()

        A_label = nText("A").next_to(A, LEFT + DOWN, buff=0.2)
        B_label = nText("B").next_to(B, UP, buff=0.3)
        C_label = nText("C").next_to(C, RIGHT + DOWN, buff=0.2)

        line_ab_marks = createMidPointMarks(Line(A, B))
        line_bc_marks = createMidPointMarks(Line(B, C))

        D = (A + B) / 2
        E = (B + C) / 2
        DE = Line(
            D,
            E,
            color=GREY_N800,
            stroke_color=[GREY_N200, GREY_N800],
            stroke_width=6,
            sheen_direction=RIGHT,
        )
        D_label = nText("D").next_to(D, LEFT, buff=0.3)
        E_label = nText("E").next_to(E, RIGHT, buff=0.3)

        self.play(
            LaggedStart(
                Create(triangle),
                FadeIn(A_label, B_label, C_label, scale=1.1),
                Create(DE),
                FadeIn(D_label, E_label),
                FadeIn(line_ab_marks, line_bc_marks),
            )
        )

        stmt1 = nMath("DE \\parallel AC").shift(UP * 0.5).shift(3.5 * RIGHT)
        stmt2 = nMath("2\\cdot DE = AC").shift(DOWN * 0.5).shift(3.5 * RIGHT)

        self.play(fadeInTex(stmt1))
        self.wait(1)
        self.play(fadeInTex(stmt2))
        self.wait(10)


class ThalesTheorem(Scene):
    def construct(self):
        # Circle with center at origin
        circle = Circle(
            radius=3,
            stroke_color=[GREY_N200, GREY_N800],
            stroke_width=6,
            sheen_direction=RIGHT,
        )

        # Points A and C are endpoints of the diameter
        A = LEFT * 3
        C = RIGHT * 3
        A_label = nText("A").next_to(A, LEFT, buff=0.3)
        C_label = nText("C").next_to(C, RIGHT, buff=0.3)

        # Point B somewhere on the circle (upper half)
        theta = ValueTracker(PI / 3)
        getB = lambda: 3 * (
            np.sin(theta.get_value()) * UP + np.cos(theta.get_value()) * RIGHT
        )
        B_label = always_redraw(
            lambda: nText("B").move_to(
                getB()
                + 0.5
                * (np.sin(theta.get_value()) * UP + np.cos(theta.get_value()) * RIGHT)
            )
        )

        center = Dot(ORIGIN, color=GREY_N800)
        centerLabel = nText("O").next_to(ORIGIN, DOWN, buff=0.3)

        # Triangle ABC
        triangle = always_redraw(
            lambda: Polygon(
                A,
                getB(),
                C,
                stroke_color=[GREY_N200, GREY_N800],
                stroke_width=6,
                sheen_direction=RIGHT,
            )
        )

        # Highlight the right angle at B
        right_angle = always_redraw(
            lambda: getRightAngle(A, getB(), C, color=GREY_N200, length=0.4)
        )

        self.play(
            LaggedStart(
                Create(circle),
                AnimationGroup(Create(center), FadeIn(centerLabel, shif=UP)),
                Create(triangle),
                Create(right_angle),
                FadeIn(A_label, B_label, C_label),
            )
        )
        self.wait(1)
        self.play(theta.animate.set_value(5 * PI / 6), run_time=3)
        self.play(theta.animate.set_value(PI / 2), run_time=2.5)

        self.wait(3)
