from manim import *
from utils import *


class Take1(Scene):
    def construct(self):
        r1 = 2
        r2 = 1.5
        r3 = 2.5

        startAngle = PI / 2
        theta = ValueTracker(0)
        phi = np.arctan(r2 / r1)
        ref = ORIGIN + RIGHT

        lineA = always_redraw(
            lambda: Line(
                ref,
                ref
                + r1 * np.sin(startAngle + theta.get_value()) * UP
                + r1 * np.cos(startAngle + theta.get_value()) * RIGHT,
                color=GREY_N400,
            )
        )

        arcA = always_redraw(
            lambda: Arc(
                radius=r1,
                start_angle=startAngle,
                angle=theta.get_value(),
                arc_center=ref,
                stroke_color=[GREY_N100, GREY_N500],
                stroke_width=6,
            )
        )

        arcB = always_redraw(
            lambda: Arc(
                radius=r3,
                start_angle=startAngle + phi,
                arc_center=ref,
                angle=theta.get_value() - 2 * PI,
                stroke_color=[GREY_N200, GREY_N800],
                stroke_width=6,
            )
        )

        lineB = always_redraw(
            lambda: Line(
                ref
                + r1 * np.sin(startAngle + theta.get_value()) * UP
                + r1 * np.cos(startAngle + theta.get_value()) * RIGHT,
                ref
                + r3 * np.sin(startAngle + phi + theta.get_value()) * UP
                + r3 * np.cos(startAngle + phi + theta.get_value()) * RIGHT,
                color=GREY_N400,
            )
        )

        innerCircle = Circle(
            r1,
            color=PURPLE_A,
            fill_opacity=1,
            stroke_width=0,
            arc_center=ref,
            z_index=-1,
        )

        ring = Annulus(r1, r3, 1, 0, ORANGE_N100, arc_center=ref, z_index=-1)

        outerCircle = Circle(
            r3,
            color=GREEN_N50,
            fill_opacity=1,
            stroke_width=0,
            arc_center=ref,
            z_index=-1,
        )

        eqn0 = nMath(
            "\\pi a^2",
            "\\; + \\;",
            "Ring",
            "\\; = \\;",
            "\\pi c^2",
            color=GREY_N800,
        ).to_edge(LEFT)
        eqn0.rotate(startAngle, OUT, eqn0.get_center())

        eqn = nMath(
            "\\pi a^2",
            "\\;+\\;",
            "\\pi b^2",
            "\\;=\\;",
            "\\pi c^2",
            color=GREY_N800,
        ).to_edge(LEFT)
        eqn.rotate(startAngle, OUT, eqn.get_center())

        eqn2 = (
            nMath(
                "a^2",
                "+",
                "b^2",
                "=",
                "c^2",
                color=GREY_N800,
            )
            .rotate(startAngle)
            .next_to(eqn, RIGHT, buff=1)
        )

        hgl = solidHighlight(self, [eqn0[0], eqn0[2], eqn0[4]], buff=0.2, animate=False)
        hgl2 = solidHighlight(self, [eqn[0], eqn[2], eqn[4]], buff=0.2, animate=False)

        hgl[0].set_color(PURPLE_A)
        hgl[1].set_color(ORANGE_N100).shift(LEFT * 0.1)
        hgl[2].set_color(GREEN_N50)

        hgl2[0].set_color(PURPLE_A)
        hgl2[1].set_color(YELLOW_N50)
        hgl2[2].set_color(GREEN_N50)

        lineC = Line(ref, lineB.get_end(), color=GREY_N400)

        labelA = nMath("a").rotate(startAngle).next_to(lineA, RIGHT)
        labelC = (
            nMath("c")
            .rotate(startAngle)
            .next_to(lineC, DOWN + LEFT, buff=-0.75)
            .shift(0.2 * LEFT + 0.2 * UP)
        )

        rtAngle = always_redraw(
            lambda: getRightAngle(
                ref
                + r3 * np.sin(startAngle + phi + theta.get_value()) * UP
                + r3 * np.cos(startAngle + phi + theta.get_value()) * RIGHT,
                ref
                + r1 * np.sin(startAngle + theta.get_value()) * UP
                + r1 * np.cos(startAngle + theta.get_value()) * RIGHT,
                ref,
                color=GREY_N400,
                length=0.3,
            )
        )

        marker1 = DashedLine(
            lineB.get_end(), lineB.get_end() + UP * 1.2, color=GREY_N100
        )
        marker2 = DashedLine(
            lineB.get_start(), lineB.get_start() + UP * 1.2, color=GREY_N100
        )
        labelB = lengthMarkerV2(lineB.get_end(), lineB.get_start(), "b", UP)
        labelB[2].rotate(startAngle).shift(UP * 0.4)

        self.add(arcA)
        self.play(Create(lineA))
        self.play(theta.animate.set_value(2 * PI), run_time=4)
        self.play(LaggedStart(Create(lineB), Create(rtAngle), lag_ratio=0.5))
        self.add(arcB)
        self.play(theta.animate.set_value(4 * PI), run_time=4)
        self.play(Create(lineC))
        self.play(
            LaggedStart(
                FadeIn(labelA),
                FadeIn(labelC),
                AnimationGroup(Create(marker1), Create(marker2)),
                FadeIn(labelB),
                lag_ratio=0.5,
            )
        )
        self.wait(1)
        self.play(FadeOut(labelA, labelB, labelC, marker1, marker2, lineC))
        self.play(FadeIn(innerCircle), run_time=2)
        self.play(FadeIn(eqn0[0], hgl[0]))
        self.play(FadeOut(innerCircle))
        self.play(FadeIn(ring), run_time=2)
        self.play(FadeIn(eqn0[1:3], hgl[1]))
        self.play(FadeOut(ring))
        self.play(FadeIn(outerCircle), run_time=2)
        self.play(FadeIn(eqn0[3:5], hgl[2]))
        self.play(FadeOut(outerCircle))

        alpha = ValueTracker(PI)
        tempLineB = always_redraw(
            lambda: Line(
                lineB.get_start(),
                lineB.get_start()
                + r2 * np.cos(alpha.get_value()) * RIGHT
                + r2 * np.sin(alpha.get_value()) * UP,
                color=GREY_N400,
            )
        )
        tempCircleB = circleB = always_redraw(
            lambda: Arc(
                radius=r2,
                arc_center=lineB.get_start(),
                start_angle=PI,
                angle=alpha.get_value() - PI,
                stroke_width=6,
                stroke_color=[GREY_N100, GREY_N400],
                sheen_direction=UP,
            )
        )
        self.add(tempLineB, tempCircleB)
        self.remove(lineB)

        circleB = always_redraw(
            lambda: Circle(
                radius=r2,
                arc_center=ref
                + r1 * np.sin(startAngle + theta.get_value()) * UP
                + r1 * np.cos(startAngle + theta.get_value()) * RIGHT,
                stroke_width=6,
                stroke_color=[GREY_N100, GREY_N400],
                sheen_direction=UP,
            )
        )

        area2 = always_redraw(
            lambda: Sector(
                radius=r2,
                arc_center=ref
                + r1 * np.sin(startAngle + theta.get_value()) * UP
                + r1 * np.cos(startAngle + theta.get_value()) * RIGHT,
                start_angle=startAngle + PI / 2 - 4 * PI,
                angle=theta.get_value() - 4 * PI,
                color=YELLOW,
                fill_opacity=0.7,
            )
        )

        disclaimer = (
            nText("Both are Area swept by rod B", color=GREY_N400)
            .to_edge(RIGHT)
            .rotate(PI / 2)
            .next_to(eqn, RIGHT, buff=1)
            .scale(0.9)
        )

        self.play(alpha.animate.set_value(3 * PI), run_time=4)
        self.add(circleB, lineB)
        self.remove(tempCircleB, tempLineB)

        rod_points = 40

        def T(t):
            return np.array([r1 * np.cos(t), r1 * np.sin(t), 0.0])

        # Tangent unit vector
        def u(t):
            return np.array([-np.sin(t), np.cos(t), 0.0])

        for i in range(rod_points):
            alpha = i / (rod_points - 1)  # param along the rod from 0 to 1

            def point_func(alpha=alpha):
                t = startAngle + theta.get_value()
                return ref + T(t) + alpha * r2 * u(t)

            trace = TracedPath(
                point_func, stroke_color=ORANGE, stroke_width=4, stroke_opacity=0.5
            )
            self.add(trace)

        self.add(circleB, area2)
        self.play(theta.animate.set_value(6 * PI), run_time=10)
        self.play(Write(disclaimer))
        self.wait(1)
        self.play(FadeOut(disclaimer), run_time=0.5)

        self.play(
            TransformMatchingTex(eqn0, eqn),
            Transform(hgl[0], hgl2[0]),
            Transform(hgl[1], hgl2[1]),
            Transform(hgl[2], hgl2[2]),
        )
        self.play(fadeInTex(eqn2))
        highlight(self, eqn2, buff=0.2, color=RED_N100, unhighlight=False)

        self.wait(1)


# class Solve(Scene):
#     def construct(self):
#         r1 = 2
#         r2 = 1.5
#         r3 = 2.5
#         circleA = Circle(
#             r1,
#             stroke_color=[GREY_N100, GREY_N500],
#             stroke_width=6,
#         )
#         circleC = Circle(
#             r3,
#             color=BLACK,
#             stroke_color=[GREY_N200, GREY_N800],
#             stroke_width=6,
#         )

#         phi = np.arctan(r2 / r1)

#         theta = ValueTracker(0)
#         startAngle = PI / 2

#         lineA = always_redraw(
#             lambda: Line(
#                 ORIGIN,
#                 r1 * np.sin(startAngle + theta.get_value()) * UP
#                 + r1 * np.cos(startAngle + theta.get_value()) * RIGHT,
#                 color=GREY_N400,
#             )
#         )

#         lineB = always_redraw(
#             lambda: Line(
#                 r1 * np.sin(startAngle + theta.get_value()) * UP
#                 + r1 * np.cos(startAngle + theta.get_value()) * RIGHT,
#                 r3 * np.sin(startAngle + phi + theta.get_value()) * UP
#                 + r3 * np.cos(startAngle + phi + theta.get_value()) * RIGHT,
#                 color=GREY_N400,
#             )
#         )

#         circleB = always_redraw(
#             lambda: Circle(
#                 radius=r2,
#                 arc_center=r1 * np.sin(startAngle + theta.get_value()) * UP
#                 + r1 * np.cos(startAngle + theta.get_value()) * RIGHT,
#                 stroke_width=6,
#                 stroke_color=[GREY_N100, GREY_N400],
#                 sheen_direction=UP,
#             )
#         )

#         area2 = always_redraw(
#             lambda: Sector(
#                 radius=r2,
#                 arc_center=r1 * np.sin(startAngle + theta.get_value()) * UP
#                 + r1 * np.cos(startAngle + theta.get_value()) * RIGHT,
#                 start_angle=startAngle + PI / 2,
#                 angle=theta.get_value(),
#                 color=YELLOW,
#                 fill_opacity=0.7,
#             )
#         )

#         def T(t):
#             return np.array([r1 * np.cos(t), r1 * np.sin(t), 0.0])

#         # Tangent unit vector
#         def u(t):
#             return np.array([-np.sin(t), np.cos(t), 0.0])

#         rod_points = 40
#         for i in range(rod_points):
#             alpha = i / (rod_points - 1)  # param along the rod from 0 to 1

#             def point_func(alpha=alpha):
#                 t = startAngle + theta.get_value()
#                 return T(t) + alpha * r2 * u(t)

#             trace = TracedPath(
#                 point_func, stroke_color=ORANGE, stroke_width=6, stroke_opacity=0.5
#             )
#             self.add(trace)

#         self.add(circleC, circleA, lineB, lineA, circleB, area2)
#         self.play(theta.animate.set_value(2 * PI), run_time=10)

#         self.wait(5)
