from manim import *
from utils import *
import numpy as np


def getAxis(x_range=[-5, 5, 1], y_range=[-5, 5, 1], x_length=6, y_length=6):
    return Axes(
        x_range=x_range,
        y_range=y_range,
        x_length=x_length,
        y_length=y_length,
        tips=True,
        axis_config={
            "include_ticks": False,
            "include_numbers": False,
            "color": GRAY_D,
            "font_size": 24,
            "tip_shape": StealthTip,
        },
    )


def getLabel(self, text, animate=True, color=YELLOW):
    text = MathTex(text, color=GREY_N500)
    bg = SurroundingRectangle(text, corner_radius=0.1, buff=0.2, color=color)
    if animate:
        self.play(FadeIn(text), Create(bg))
    return VGroup(text, bg)


class Parabola(Scene):
    def construct(self):
        axes = getAxis(x_range=[-4, 4, 1], y_range=[-1, 9, 1], y_length=5.8).to_edge(UP)
        label = getLabel(self, "y = x^2")

        self.play(
            LaggedStart(label.animate.to_edge(DOWN), Create(axes), lag_ratio=0.6),
            run_time=2,
        )

        parabola = axes.plot(
            lambda x: x**2,
            x_range=[-2.8, 2.8],
            color=NUMBRIK_COLOR,
        )

        self.play(Create(parabola))
        self.wait(4)


class Ellipse(Scene):
    def construct(self):
        axes = getAxis(x_range=[-4, 4, 1], y_range=[-4, 4, 1], y_length=5).to_edge(UP)
        label = getLabel(
            self, "\\left(\\frac{x}{a}\\right)^2 + \\left(\\frac{y}{b}\\right)^2 = 1"
        )

        self.play(
            LaggedStart(label.animate.to_edge(DOWN), Create(axes), lag_ratio=0.6),
            run_time=2,
        )

        ellipse = axes.plot_parametric_curve(
            lambda t: np.array([3 * np.cos(t), 2 * np.sin(t), 0]),
            t_range=[0, 2 * np.pi],
            color=NUMBRIK_COLOR,
        )

        self.play(Create(ellipse))
        self.wait(4)


class Hyperbola(Scene):
    def construct(self):
        axes = getAxis(y_range=[-5.5, 5.5, 1], y_length=5.8).to_edge(UP)
        label = getLabel(self, "xy = 1")

        self.play(
            LaggedStart(label.animate.to_edge(DOWN), Create(axes), lag_ratio=0.6),
            run_time=2,
        )

        # Right branch
        hyperbola_right = axes.plot(
            lambda x: 1 / x,
            x_range=[0.2, 4.5],
            color=NUMBRIK_COLOR,
        )

        # Left branch
        hyperbola_left = axes.plot(
            lambda x: 1 / x,
            x_range=[-4.5, -0.2],
            color=NUMBRIK_COLOR,
        )

        hyperbola = VGroup(hyperbola_right, hyperbola_left)

        self.play(Create(hyperbola))
        self.wait(4)


class Circle(Scene):
    def construct(self):
        axes = getAxis(
            x_range=[-4, 4, 1], y_range=[-4, 4, 1], x_length=5.8, y_length=5.8
        ).to_edge(UP)
        label = getLabel(self, "x^2 + y^2 = 9")

        self.play(
            LaggedStart(label.animate.to_edge(DOWN), Create(axes), lag_ratio=0.6),
            run_time=2,
        )

        circle = axes.plot_parametric_curve(
            lambda t: np.array([2.7 * np.cos(t), 2.7 * np.sin(t), 0]),
            t_range=[0, 2 * np.pi],
            color=NUMBRIK_COLOR,
        )

        self.play(Create(circle))
        self.wait(4)


## NOT NEEDED ##

# class Sin(Scene):
#     def construct(self):
#         axes = getAxis(x_range=[-1, 8, 1], y_range=[-3, 3, 1], x_length=10, y_length=5)

#         sinCurve1 = axes.plot(
#             lambda x: 1.5 * np.sin(x),
#             x_range=[-0.5, 2.2 * np.pi],
#             color=NUMBRIK_COLOR,
#         )

#         sinCurve2 = axes.plot(
#             lambda x: 1.5 * np.sin(2 * x),
#             x_range=[-0.5, 2.2 * np.pi],
#             color=NUMBRIK_COLOR,
#         )

#         line1 = DashedLine(axes.c2p(0, 1.5), axes.c2p(6.5, 1.5), color=GREY_B)
#         line2 = DashedLine(axes.c2p(0, -1.5), axes.c2p(6.5, -1.5), color=GREY_B)

#         labels = VGroup()

#         for x in range(1, 3):
#             if x == 0:
#                 continue
#             label = (
#                 nMath(str(x) if x != 1 else "" + "\\pi")
#                 .scale(0.5)
#                 .move_to(axes.c2p(x * np.pi, 0))
#                 .shift(0.4 * DOWN)
#             )
#             mark = Line(
#                 axes.c2p(x * np.pi, 0) + 0.1 * UP,
#                 axes.c2p(x * np.pi, 0) + 0.1 * DOWN,
#                 color=GREY_D,
#             )
#             labels.add(label, mark)

#         for y in [-1, 1]:
#             if y == 0:
#                 continue
#             label = nMath(str(y)).scale(0.5).move_to(axes.c2p(0, y * 1.5) + 0.3 * LEFT)
#             labels.add(label)

#         self.play(Create(axes))
#         self.play(Create(sinCurve1), run_time=2)
#         self.play(Create(line1), Create(line2), FadeIn(labels))
#         self.wait(1)

#         newLabels = VGroup()
#         for x in [1, 3]:
#             if x == 0:
#                 continue
#             label = (
#                 nMath("\\frac{ " + (str(x) if x != 1 else "") + "\\pi}{2}")
#                 .scale(0.5)
#                 .move_to(axes.c2p(x * np.pi / 2, 0))
#                 .shift(0.5 * DOWN)
#             )
#             mark = Line(
#                 axes.c2p(x * np.pi / 2, 0) + 0.1 * UP,
#                 axes.c2p(x * np.pi / 2, 0) + 0.1 * DOWN,
#                 color=GREY_D,
#             )
#             newLabels.add(label, mark)

#         self.play(Transform(sinCurve1, sinCurve2))
#         self.play(FadeIn(newLabels))

#         self.play(
#             VGroup(sinCurve1, axes, labels, newLabels, line1, line2).animate.scale(1.4)
#         )
#         self.wait(1)


## NOT NEEDED ##
# class SinSync(Scene):
#     def construct(self):
#         t = ValueTracker(0)
#         axes = getAxis(x_range=[-1, 8, 1], y_range=[-3, 3, 1], x_length=10, y_length=5)

#         sinCurve1 = axes.plot(
#             lambda x: 1.5 * np.sin(2 * x),
#             x_range=[-0.5, 2.2 * np.pi],
#             color=NUMBRIK_COLOR,
#         )

#         line1 = DashedLine(axes.c2p(0, 1.5), axes.c2p(6.5, 1.5), color=GREY_B)
#         line2 = DashedLine(axes.c2p(0, -1.5), axes.c2p(6.5, -1.5), color=GREY_B)

#         labels = VGroup()

#         for x in range(1, 3):
#             if x == 0:
#                 continue
#             label = (
#                 nMath(str(x) if x != 1 else "" + "\\pi")
#                 .scale(0.5)
#                 .move_to(axes.c2p(x * np.pi, 0))
#                 .shift(0.4 * DOWN)
#             )
#             mark = Line(
#                 axes.c2p(x * np.pi, 0) + 0.1 * UP,
#                 axes.c2p(x * np.pi, 0) + 0.1 * DOWN,
#                 color=GREY_D,
#             )
#             labels.add(label, mark)

#         for y in [-1, 1]:
#             if y == 0:
#                 continue
#             label = nMath(str(y)).scale(0.5).move_to(axes.c2p(0, y * 1.5) + 0.3 * LEFT)
#             labels.add(label)

#         for x in [1, 3]:
#             if x == 0:
#                 continue
#             label = (
#                 nMath("\\frac{ " + (str(x) if x != 1 else "") + "\\pi}{2}")
#                 .scale(0.5)
#                 .move_to(axes.c2p(x * np.pi / 2, 0))
#                 .shift(0.5 * DOWN)
#             )
#             mark = Line(
#                 axes.c2p(x * np.pi / 2, 0) + 0.1 * UP,
#                 axes.c2p(x * np.pi / 2, 0) + 0.1 * DOWN,
#                 color=GREY_D,
#             )
#             labels.add(label, mark)

#         grp = VGroup(sinCurve1, axes, labels, line1, line2).scale(1.4)

#         pointer1 = always_redraw(
#             lambda: Dot(
#                 axes.c2p(t.get_value(), 1.5 * np.sin(2 * t.get_value())),
#                 radius=0.1,
#                 color=RED_N100,
#             )
#         )

#         self.add(grp, pointer1)
#         self.wait(1)
#         self.play(t.animate.set_value(PI / 4), run_time=5)
#         self.wait(1)
#         self.play(t.animate.set_value(PI / 2), run_time=5)
#         self.wait(1)
#         self.play(t.animate.set_value(3 * PI / 4), run_time=5)
#         self.wait(3)
#         self.play(t.animate.set_value(PI), run_time=5)
#         self.wait(1)
#         self.play(t.animate.set_value(3 * PI / 2), run_time=10)
#         self.wait(1)
#         self.play(t.animate.set_value(7 * PI / 4), run_time=5)
#         self.wait(3)
#         self.play(t.animate.set_value(2 * PI), run_time=5)
#         self.wait(4)


class FourPetal(Scene):
    def construct(self):
        axes = getAxis()
        label = MathTex("\\left(x^2 + y^2\\right)^{\\frac{3}{2}} = 2xy", color=BLACK)

        self.play(Write(label), run_time=2)
        self.wait(1)
        arrow = Arrow(LEFT * 2, ORIGIN, color=GREY_N500)
        self.play(
            label.animate.to_edge(LEFT),
            FadeIn(VGroup(axes)),
            VGroup(axes).animate.to_edge(RIGHT),
            GrowArrow(arrow),
        )
        fourPetal = axes.plot_parametric_curve(
            lambda t: np.array(
                [5 * np.sin(2 * t) * np.cos(t), 5 * np.sin(2 * t) * np.sin(t), 0]
            ),
            t_range=[0, 2 * np.pi],
            color=NUMBRIK_COLOR,
        )

        self.play(Create(fourPetal), run_time=4)

        self.wait(4)


class ConicSections3D(ThreeDScene):
    def construct(self):
        # Set up axes
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-3, 3, 1],
            axis_config={"include_numbers": False, "color": GREY_N800},
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        self.play(FadeIn(axes))

        # Create a cone (double cone for all conics)
        cone1 = Surface(
            lambda u, v: np.array([v * np.cos(u), v * np.sin(u), v]),
            u_range=[0, TAU],
            v_range=[0, 3],
            resolution=(100, 100),
            fill_opacity=0.3,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )

        cone2 = Surface(
            lambda u, v: np.array([v * np.cos(u), v * np.sin(u), -v]),
            u_range=[0, TAU],
            v_range=[0, 3],
            resolution=(100, 100),
            fill_opacity=0.3,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )

        self.play(Create(cone1), Create(cone2))
        self.wait(1)

        # CIRCLE: plane perpendicular to axis
        circle_plane = Surface(
            lambda u, v: np.array([u, v, 1.5]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.7,
            resolution=(100, 100),
            checkerboard_colors=[YELLOW, YELLOW],
        )
        self.play(Create(circle_plane))
        self.wait(2)

        # ELLIPSE: tilted plane cutting both sides
        ellipse_plane = Surface(
            lambda u, v: np.array([u, v, 1 + 0.5 * u]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.7,
            resolution=(100, 100),
            checkerboard_colors=[YELLOW, YELLOW],
        )
        self.play(Transform(circle_plane, ellipse_plane))
        self.wait(1)

        # PARABOLA: plane parallel to a cone side
        parabola_plane = Surface(
            lambda u, v: np.array([u, v, 0.7 * u + 0.5]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.7,
            resolution=(100, 100),
            checkerboard_colors=[YELLOW, YELLOW],
        )
        self.play(Transform(circle_plane, parabola_plane))
        self.wait(1)

        # HYPERBOLA: steep tilted plane cutting both cones
        hyperbola_plane = Surface(
            lambda u, v: np.array([u, v, 2 * u]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.7,
            resolution=(100, 100),
            checkerboard_colors=[YELLOW, YELLOW],
        )
        self.play(Transform(circle_plane, hyperbola_plane))
        self.wait(1)

        self.wait(2)


class ConicsStatements(Scene):
    def construct(self):
        generalEqn = MathTex(
            "Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0", color=BLACK
        ).to_edge(UP)
        versus = Text("V/S", color=GREY_N800).next_to(generalEqn, DOWN, buff=0.6)
        ourEquation = MathTex(
            "\\left(x^2+y^2\\right)^{\\frac{3}{2}} = 2xy", color=BLACK
        ).next_to(versus, DOWN, buff=0.6)
        self.play(fadeInTex(generalEqn), run_time=3)
        self.wait(2)
        self.play(FadeIn(versus))
        self.play(fadeInTex(ourEquation))

        clearScreen(self, 4)

        conic1 = Text("Circle", color=GREY_N500)
        conic2 = Text("Ellipse", color=GREY_N500)
        conic3 = Text("Parabola", color=GREY_N500)
        conic4 = Text("Hyperbola", color=GREY_N500)

        self.play(Write(conic1), run_time=2)
        self.wait(1)
        self.play(Transform(conic1, conic2))
        self.wait(1)
        self.play(Transform(conic1, conic3))
        self.wait(1)
        self.play(Transform(conic1, conic4))
        self.wait(1)


class PolarIntro(Scene):
    def construct(self):
        axes = getAxis(x_range=[-6, 6, 1], y_range=[-6, 6, 1], x_length=7, y_length=7)
        pole = Dot(axes.get_center(), radius=0.1, color=GREY_N800)
        poleLabel = getLabel(self, "\\text{Pole}", animate=False, color=YELLOW).move_to(
            ORIGIN + 2 * DOWN + 2 * LEFT
        )

        arrow = Arrow(
            poleLabel.get_corner(UP + RIGHT), axes.get_origin(), color=GREY_N400
        )

        polarAxisLabel = getLabel(
            self, "\\text{Polar Axis}", animate=False, color=YELLOW
        ).move_to(ORIGIN + 2 * DOWN + 4.5 * RIGHT)

        # Create a curved arrow from the polar axis label to the axis, centered in the first quadrant
        arrow2 = CurvedArrow(
            polarAxisLabel.get_left() + 0.2 * LEFT,
            axes.c2p(3, 0) + 0.2 * DOWN,
            angle=-PI / 3,
            color=GREY_N400,
            arc_center=axes.c2p(2, 2),
        )

        radialLine = Arrow(
            axes.get_origin(),
            axes.c2p(4, 4),
            color=GREY_N800,
            tip_length=0.3,
            stroke_width=3,
            buff=0,
        )

        point = Dot(axes.c2p(4, 4), radius=0.05, color=GREY_N500)

        angle = Angle(
            Line(axes.c2p(0, 0), axes.c2p(2, 0)),
            radialLine,
            color=GREY_N400,
            radius=0.7,
        )

        label2 = nMath("(r, \\theta)").next_to(point, RIGHT)

        label3 = nMath("r").move_to(axes.c2p(2.1, 2.1) + 0.25 * UP + 0.25 * LEFT)

        label4 = nMath("\\theta").move_to(axes.c2p(1.7, 0.7))

        label5 = MathTex("x = r \\cos{\\theta}", color=BLACK).move_to(
            2.5 * LEFT + 2.5 * UP
        )
        label6 = MathTex("y = r \\sin{\\theta}", color=BLACK).next_to(
            label5, DOWN, buff=0.25
        )

        perpendicular = DashedLine(point, axes.c2p(4, 0), color=GREY_N500)
        base = DashedLine(point, axes.c2p(0, 4), color=GREY_N500)

        self.play(Create(axes))
        self.wait(1)
        self.play(
            LaggedStart(
                Create(pole), FadeIn(poleLabel), GrowArrow(arrow), lag_ratio=0.5
            )
        )

        self.wait(1)
        self.play(LaggedStart(FadeIn(polarAxisLabel), Create(arrow2)))

        self.wait(1)
        self.play(Create(point))
        self.play(Create(radialLine))
        self.play(Create(angle))
        self.play(FadeIn(label2))
        self.wait(1)
        self.play(FadeIn(label3, label4))
        self.wait(1)
        self.play(Create(perpendicular), Create(base))
        self.wait(1)
        self.play(fadeInTex(label5), fadeInTex(label6))
        self.play(
            Create(
                SurroundingRectangle(
                    VGroup(label5, label6), buff=0.2, corner_radius=0.12
                )
            )
        )

        self.wait(4)


class ConvertToPolar(Scene):
    def construct(self):
        eq1 = MathTex("x = r \\cos{\\theta}", color=BLACK).to_edge(UP)
        eq2 = MathTex("y = r \\sin{\\theta}", color=BLACK).next_to(eq1, DOWN, buff=0.5)

        eqn = MathTex(
            "\\left(x^2 + y^2\\right)^{\\frac{3}{2}} = 2xy", color=BLACK
        ).next_to(eq2, DOWN, buff=0.75)

        step1 = nMath(
            "\\left(r^2\\sin^2{\\theta} + r^2\\cos^2{\\theta}\\right)^{\\frac{3}{2}} = 2r \\sin{\\theta} \\cdot r \\cos{\\theta}"
        ).next_to(eqn, DOWN, buff=0.75)

        step2 = nMath("r = \\sin{2\\theta}").next_to(step1, DOWN, buff=0.5)

        self.play(fadeInTex(eq1), fadeInTex(eq2))
        self.wait(1)
        self.play(FadeIn(eqn, scale=1.2))
        self.wait(1)
        self.play(FadeIn(step1))
        self.wait(1)
        self.play(FadeIn(step2))
        highlight(self, step2, buff=0.2, wait_time=4)


class PolarEqn(Scene):
    def construct(self):
        step2 = getLabel(self, "r = \\sin{2\\theta}", color=RED)
        self.wait(1)
        self.play(step2.animate.to_corner(UP + LEFT))
        self.wait(4)


class Quote(Scene):
    def construct(self):
        quote = Tex(
            "Pure mathematics is, in its way, \\\\the poetry of logical ideas.",
            color=BLACK,
        )
        quoteBy = (
            Text("Albert Einstein", color=NUMBRIK_COLOR)
            .next_to(quote, DOWN, buff=0.5)
            .scale(0.7)
        )

        VGroup(quote, quoteBy).move_to(ORIGIN)

        self.play(fadeInTex(quote))
        self.play(FadeIn(quoteBy, shift=0.25 * UP))
        self.wait(4)


class FourPetalConstruction(Scene):
    def construct(self):
        ## ======= sin curve =======

        t = ValueTracker(PI / 4)

        axes1 = getAxis(x_range=[-1, 8, 1], y_range=[-2, 2, 1], x_length=6, y_length=5)

        sinCurve1 = axes1.plot(
            lambda x: 1.5 * np.sin(x),
            x_range=[-0.5, 2.2 * np.pi],
            color=NUMBRIK_COLOR,
        )

        sinCurve2 = axes1.plot(
            lambda x: 1.5 * np.sin(2 * x),
            x_range=[-0.5, 2.2 * np.pi],
            color=NUMBRIK_COLOR,
        )

        line1 = DashedLine(axes1.c2p(0, 1.5), axes1.c2p(6.5, 1.5), color=GREY_B)
        line2 = DashedLine(axes1.c2p(0, -1.5), axes1.c2p(6.5, -1.5), color=GREY_B)

        labels = VGroup()

        for x in range(1, 3):
            if x == 0:
                continue
            label = (
                nMath(str(x) if x != 1 else "" + "\\pi")
                .scale(0.7)
                .move_to(axes1.c2p(x * np.pi, 0))
                .shift(0.4 * DOWN + 0.1 * RIGHT)
            )
            mark = Line(
                axes1.c2p(x * np.pi, 0) + 0.1 * UP,
                axes1.c2p(x * np.pi, 0) + 0.1 * DOWN,
                color=GREY_D,
            )
            labels.add(label, mark)

        for y in [-1, 1]:
            if y == 0:
                continue
            label = nMath(str(y)).scale(0.7).move_to(axes1.c2p(0, y * 1.5) + 0.3 * LEFT)
            labels.add(label)

        self.play(Create(axes1))
        self.play(Create(sinCurve1), run_time=2)
        self.play(Create(line1), Create(line2), FadeIn(labels))
        self.wait(1)

        newLabels = VGroup()
        for x in [1, 3]:
            if x == 0:
                continue
            label = (
                nMath("\\frac{ " + (str(x) if x != 1 else "") + "\\pi}{2}")
                .scale(0.7)
                .move_to(axes1.c2p(x * np.pi / 2, 0))
                .shift(0.5 * DOWN + 0.2 * LEFT)
            )
            mark = Line(
                axes1.c2p(x * np.pi / 2, 0) + 0.1 * UP,
                axes1.c2p(x * np.pi / 2, 0) + 0.1 * DOWN,
                color=GREY_D,
            )
            newLabels.add(label, mark)

        self.play(Transform(sinCurve1, sinCurve2))
        self.play(FadeIn(newLabels))
        self.wait(1)

        grp = VGroup(sinCurve1, axes1, labels, newLabels, line1, line2)

        self.play(grp.animate.to_edge(RIGHT))

        pointer1 = always_redraw(
            lambda: Dot(
                axes1.c2p(t.get_value(), 1.5 * np.sin(2 * t.get_value())),
                radius=0.1,
                color=RED_N100,
            )
        )

        radialDistance = always_redraw(
            lambda: Arrow(
                axes1.c2p(t.get_value(), 0),
                axes1.c2p(t.get_value(), 1.5 * np.sin(2 * t.get_value())),
                tip_length=0.2,
                stroke_width=3,
                color=GREY_C,
                buff=0,
            )
        )

        grp.add(pointer1, radialDistance)

        ## ======= r = sin2(theta) ========

        axes = getAxis(x_length=6, y_length=6).to_edge(LEFT)
        self.play(Create(axes))
        self.wait(1)

        pointer2 = always_redraw(
            lambda: Dot(
                axes.c2p(
                    4 * np.sin(2 * t.get_value()) * np.cos(t.get_value()),
                    4 * np.sin(2 * t.get_value()) * np.sin(t.get_value()),
                ),
                radius=0.1,
                color=RED_N100,
            )
        )

        radialLine = always_redraw(
            lambda: Arrow(
                axes.get_origin(),
                axes.c2p(
                    4 * np.sin(2 * t.get_value()) * np.cos(t.get_value()),
                    4 * np.sin(2 * t.get_value()) * np.sin(t.get_value()),
                ),
                color=GREY_C,
                buff=0,
                tip_length=0.2,
                stroke_width=3,
            )
        )
        self.play(
            LaggedStart(Create(pointer1), GrowArrow(radialDistance), lag_ratio=0.5)
        )
        self.play(TransformFromCopy(radialDistance, radialLine), Create(pointer2))

        angleMarker = always_redraw(
            lambda: DashedLine(
                axes.get_origin(),
                axes.c2p(
                    2 * np.abs(np.sin(2 * t.get_value())) * np.cos(t.get_value()),
                    2 * np.abs(np.sin(2 * t.get_value())) * np.sin(t.get_value()),
                ),
                color=GREY_C,
            )
        )

        angle = always_redraw(
            lambda: Arc(
                0.7, 0, t.get_value(), arc_center=axes.get_origin(), color=GREY_C
            )
        )

        self.play(Create(angle))

        ## adding all

        # self.add(
        #     axes,
        #     axes1,
        #     sinCurve1,
        #     labels,
        #     line1,
        #     line2,
        #     pointer2,
        #     trace,
        #     pointer1,
        #     radialLine,
        #     angleMarker,
        #     angle,
        # )
        self.wait(1)
        self.play(t.animate.set_value(PI / 8), run_time=1)
        self.wait(1)
        self.play(t.animate.set_value(0), run_time=1)
        self.wait(1)
        trace = TracedPath(
            pointer2.get_center,
            stroke_color=NUMBRIK_COLOR,
            stroke_width=DEFAULT_STROKE_WIDTH,
        )
        self.add(trace)
        self.play(t.animate.set_value(PI / 4), run_time=2)
        self.wait(1)
        self.play(t.animate.set_value(PI / 2), run_time=2)
        self.add(angleMarker)
        self.wait(1)
        self.play(t.animate.set_value(3 * PI / 4), run_time=2)
        self.wait(3)
        self.play(t.animate.set_value(PI), run_time=2)
        self.wait(1)
        self.play(t.animate.set_value(3 * PI / 2), run_time=4)
        self.wait(1)
        self.play(t.animate.set_value(7 * PI / 4), run_time=2)
        self.wait(3)
        self.play(t.animate.set_value(2 * PI), run_time=2)
        self.wait(2)

        self.play(FadeOut(grp), FadeOut(pointer2, angle))
        self.wait(4)


class Thumbnail(Scene):
    def construct(self):
        eqn = MathTex(
            "\\left(x^2 + y^2\\right)^{\\frac{3}{2}} = 2xy",
            tex_template=TexFontTemplates.chalkboard_se,
            color=VIOLET_N1000,
        ).scale(3)
        self.add(eqn)
        self.wait(10)
