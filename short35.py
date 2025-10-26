from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        r1 = 1
        r2 = 2
        r3 = np.sqrt(r1 * r1 + r2 * r2)

        startAngle = PI / 2
        theta = ValueTracker(0)
        phi = np.arctan(r2 / r1)
        shift = ValueTracker(0)
        getRef = lambda: ORIGIN + shift.get_value() * RIGHT

        lineA = always_redraw(
            lambda: Line(
                getRef(),
                getRef()
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
                arc_center=getRef(),
                stroke_color=[GREY_N100, GREY_N500],
                stroke_width=6,
            )
        )

        arcB = always_redraw(
            lambda: Arc(
                radius=r3,
                start_angle=startAngle + phi,
                arc_center=getRef(),
                angle=theta.get_value() - 2 * PI,
                stroke_color=[GREY_N200, GREY_N800],
                stroke_width=6,
            )
        )

        lineB = always_redraw(
            lambda: Line(
                getRef()
                + r1 * np.sin(startAngle + theta.get_value()) * UP
                + r1 * np.cos(startAngle + theta.get_value()) * RIGHT,
                getRef()
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
            arc_center=getRef(),
            z_index=-1,
        )

        ring = Annulus(r1, r3, 1, 0, ORANGE_N100, arc_center=getRef(), z_index=-1)

        outerCircle = Circle(
            r3,
            color=GREEN_N50,
            fill_opacity=1,
            stroke_width=0,
            arc_center=getRef(),
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

        lineC = Line(getRef(), lineB.get_end(), color=GREY_N400)

        labelA = nMath("a").rotate(startAngle).next_to(lineA, RIGHT)
        labelC = (
            nMath("c")
            .rotate(startAngle)
            .next_to(lineC, DOWN + LEFT, buff=-0.75)
            .shift(0.2 * LEFT + 0.2 * UP)
        )

        rtAngle = always_redraw(
            lambda: getRightAngle(
                getRef()
                + r3 * np.sin(startAngle + phi + theta.get_value()) * UP
                + r3 * np.cos(startAngle + phi + theta.get_value()) * RIGHT,
                getRef()
                + r1 * np.sin(startAngle + theta.get_value()) * UP
                + r1 * np.cos(startAngle + theta.get_value()) * RIGHT,
                getRef(),
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

        # self.add(arcA)
        # self.play(Create(lineA))
        # self.play(theta.animate.set_value(2 * PI), run_time=4)
        # self.play(LaggedStart(Create(lineB), Create(rtAngle), lag_ratio=0.5))
        # self.add(arcB)
        # self.play(theta.animate.set_value(4 * PI), run_time=4)
        # self.play(Create(lineC))
        # self.play(
        #     LaggedStart(
        #         FadeIn(labelA),
        #         FadeIn(labelC),
        #         AnimationGroup(Create(marker1), Create(marker2)),
        #         FadeIn(labelB),
        #         lag_ratio=0.5,
        #     )
        # )
        # self.wait(1)
        # self.play(FadeOut(labelA, labelB, labelC, marker1, marker2, lineC))
        # self.play(FadeIn(innerCircle), run_time=2)
        # self.play(FadeIn(eqn0[0], hgl[0]))
        # self.play(FadeOut(innerCircle))
        # self.play(FadeIn(ring), run_time=2)
        # self.play(FadeIn(eqn0[1:3], hgl[1]))
        # self.play(FadeOut(ring))
        # self.play(FadeIn(outerCircle), run_time=2)
        # self.play(FadeIn(eqn0[3:5], hgl[2]))
        # self.play(FadeOut(outerCircle))

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
                arc_center=getRef()
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
                arc_center=getRef()
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

        # self.play(alpha.animate.set_value(3 * PI), run_time=4)
        # self.add(circleB, lineB)
        # self.remove(tempCircleB, tempLineB)

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
                return getRef() + T(t) + alpha * r2 * u(t)

            trace = TracedPath(
                point_func, stroke_color=ORANGE, stroke_width=4, stroke_opacity=0.5
            )
            # self.add(trace)

        # self.add(circleB, area2)
        # self.play(theta.animate.set_value(6 * PI), run_time=10)
        # self.play(Write(disclaimer))
        # self.wait(1)
        # self.play(FadeOut(disclaimer), run_time=0.5)

        # self.play(
        #     TransformMatchingTex(eqn0, eqn),
        #     Transform(hgl[0], hgl2[0]),
        #     Transform(hgl[1], hgl2[1]),
        #     Transform(hgl[2], hgl2[2]),
        # )
        # self.play(fadeInTex(eqn2))
        # highlight(self, eqn2, buff=0.2, color=RED_N100, unhighlight=False)

        # self.wait(1)
        # self.wait(5)


class Take3(Scene):
    def construct(self):
        r1 = 1.5
        r2 = 2
        r3 = np.sqrt(r1 * r1 + r2 * r2)

        startAngle = PI / 6
        theta = ValueTracker(0)
        phi = np.arctan(r2 / r1)
        shift = ValueTracker(0)
        getRef = lambda: ORIGIN + shift.get_value() * RIGHT

        refLineA = DashedLine(
            getRef(),
            getRef() + r1 * np.sin(startAngle) * UP + r1 * np.cos(startAngle) * RIGHT,
            color=GREY_N100,
        )

        lineA = always_redraw(
            lambda: Line(
                getRef(),
                getRef()
                + r1 * np.sin(startAngle + theta.get_value()) * UP
                + r1 * np.cos(startAngle + theta.get_value()) * RIGHT,
                color=GREY_N100,
            )
        )

        arcA = always_redraw(
            lambda: Arc(
                radius=r1,
                start_angle=startAngle,
                angle=theta.get_value(),
                arc_center=getRef(),
                stroke_color=[GREY_N100, GREY_N500],
                stroke_width=6,
            )
        )

        arcB = always_redraw(
            lambda: Arc(
                radius=r3,
                start_angle=startAngle + phi,
                arc_center=getRef(),
                angle=theta.get_value(),
                stroke_color=[GREY_N200, GREY_N800],
                stroke_width=6,
            )
        )

        lineB = always_redraw(
            lambda: Line(
                getRef()
                + r1 * np.sin(startAngle + theta.get_value()) * UP
                + r1 * np.cos(startAngle + theta.get_value()) * RIGHT,
                getRef()
                + r3 * np.sin(startAngle + phi + theta.get_value()) * UP
                + r3 * np.cos(startAngle + phi + theta.get_value()) * RIGHT,
                color=GREY_N100,
            )
        )

        refLineB = DashedLine(
            getRef() + r1 * np.sin(startAngle) * UP + r1 * np.cos(startAngle) * RIGHT,
            getRef()
            + r3 * np.sin(startAngle + phi) * UP
            + r3 * np.cos(startAngle + phi) * RIGHT,
            color=GREY_N100,
        )

        rtAngle = always_redraw(
            lambda: getRightAngle(
                getRef()
                + r3 * np.sin(startAngle + phi + theta.get_value()) * UP
                + r3 * np.cos(startAngle + phi + theta.get_value()) * RIGHT,
                getRef()
                + r1 * np.sin(startAngle + theta.get_value()) * UP
                + r1 * np.cos(startAngle + theta.get_value()) * RIGHT,
                getRef(),
                color=GREY_N100,
                length=0.2,
            )
        )

        refRtAngle = always_redraw(
            lambda: getRightAngle(
                getRef()
                + r3 * np.sin(startAngle + phi) * UP
                + r3 * np.cos(startAngle + phi) * RIGHT,
                getRef()
                + r1 * np.sin(startAngle) * UP
                + r1 * np.cos(startAngle) * RIGHT,
                getRef(),
                color=GREY_N100,
                length=0.2,
            )
        )

        refInnerCircle = DashedVMobject(
            Circle(
                radius=r1,
                arc_center=getRef(),
                stroke_width=6,
                stroke_color=GREY_N100,
                z_index=-1,
            ),
            dashed_ratio=0.9,
        )
        refOuterCircle = DashedVMobject(
            Circle(
                radius=r3,
                arc_center=getRef(),
                stroke_width=6,
                stroke_color=GREY_N100,
                z_index=-1,
            ),
            dashed_ratio=0.8,
        )

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
                return getRef() + T(t) + alpha * r2 * u(t)

            trace = TracedPath(
                point_func,
                stroke_color=ORANGE,
                stroke_width=6,
                stroke_opacity=0.5,
                z_index=-1,
            )
            self.add(trace)

        # theta.set_value(2 * PI / 3)

        circleB = always_redraw(
            lambda: Circle(
                radius=r2,
                arc_center=getRef()
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
                arc_center=getRef()
                + r1 * np.sin(startAngle + theta.get_value()) * UP
                + r1 * np.cos(startAngle + theta.get_value()) * RIGHT,
                start_angle=startAngle + PI / 2,
                angle=theta.get_value(),
                color=YELLOW,
                fill_opacity=0.7,
            )
        )

        self.add(
            arcA,
            arcB,
            lineB,
            lineA,
            refLineA,
            refLineB,
            rtAngle,
            refRtAngle,
            refInnerCircle,
            refOuterCircle,
            # lengthMarker1,
            # refLengthMarker1,
            # refLengthMarker2,
            # lengthLabel,
            # angleMarker,
            # angleLabel,
            # circleB,
            # area2,
        )

        # ANIMATION HUB

        getTangentPoint = (
            lambda: r1 * np.cos(theta.get_value() + startAngle) * RIGHT
            + r1 * np.sin(theta.get_value() + startAngle) * UP
        )

        centerMarker1 = always_redraw(lambda: Dot(getTangentPoint(), color=RED_N100))
        centerMarker2 = always_redraw(
            lambda: Circle(radius=0.2, arc_center=getTangentPoint(), color=RED_N100)
        )

        centerMarker3 = Arrow(
            getTangentPoint() + 3 * RIGHT,
            getTangentPoint() + 0.2 * RIGHT,
            color=NUMBRIK_COLOR,
            stroke_width=12,
            tip_length=0.5,
        )

        centerMarker3.set_color_by_gradient(
            [NUMBRIK_COLOR_50, NUMBRIK_COLOR]
        ).set_sheen_direction(centerMarker3.get_unit_vector())

        self.play(
            FadeIn(centerMarker1), Create(centerMarker2), GrowArrow(centerMarker3)
        )

        alpha = ValueTracker(0)
        tempLineB = always_redraw(
            lambda: Line(
                lineB.get_start(),
                lineB.get_start()
                + r2 * np.cos(alpha.get_value() + startAngle + PI / 2) * RIGHT
                + r2 * np.sin(alpha.get_value() + startAngle + PI / 2) * UP,
                color=GREY_N100,
            )
        )
        tempCircleB = always_redraw(
            lambda: Arc(
                radius=r2,
                arc_center=lineB.get_start(),
                start_angle=startAngle + PI / 2,
                angle=alpha.get_value(),
                stroke_width=6,
                stroke_color=[GREY_N100, GREY_N400],
                sheen_direction=UP,
            )
        )
        self.play(FadeOut(centerMarker3))
        self.add(tempLineB, tempCircleB)
        self.remove(lineB)

        self.play(alpha.animate.set_value(2 * PI), run_time=3)

        self.wait(1)

        self.remove(tempLineB, tempCircleB)
        self.add(circleB, lineB, area2)

        self.play(theta.animate.set_value(2 * PI / 3), run_time=3)

        angleMarker = getAngle(
            refLineA.get_end(), getRef(), lineA.get_end(), color=GREY_N400
        )

        angleLabel = (
            nMath("120^\\circ", color=BLACK)
            .scale(0.9)
            .next_to(angleMarker, UP, buff=0.2)
            .shift(RIGHT * 0.1)
        )

        lengthMarker1 = DoubleArrow(
            refLineB.get_start() + T(startAngle) * 0.2,
            refLineB.get_end() + T(startAngle) * 0.2,
            color=GREY_N400,
            tip_length=0.28,
            buff=0,
        )

        lengthLabel = (
            nMath("12", color=BLACK)
            .scale(0.9)
            .next_to(lengthMarker1, RIGHT + UP, buff=-0.4)
            .rotate(startAngle)
            .shift(0.4 * DOWN + 0.2 * RIGHT)
        )

        refLengthMarker1 = DashedLine(
            refLineB.get_start(),
            refLineB.get_start() + T(startAngle) * 0.4,
            color=GREY_N100,
        )

        refLengthMarker2 = DashedLine(
            refLineB.get_end(),
            refLineB.get_end() + T(startAngle) * 0.4,
            color=GREY_N100,
        )

        angleMarker2 = getAngle(
            lineA.get_end() + refLineB.get_unit_vector(),
            lineA.get_end(),
            lineB.get_end(),
            color=GREY_N400,
        )

        angleLabel2 = (
            nMath("120^\\circ", color=BLACK)
            .scale(0.9)
            .next_to(angleMarker2, LEFT, buff=0.2)
            .shift(RIGHT * 0.1)
        )

        self.play(
            LaggedStart(Create(angleMarker), fadeInTex(angleLabel), lag_ratio=0.5)
        )
        self.play(
            LaggedStart(Create(angleMarker2), fadeInTex(angleLabel2), lag_ratio=0.5)
        )
        self.play(
            LaggedStart(
                AnimationGroup(
                    Create(refLengthMarker1),
                    Create(refLengthMarker2),
                ),
                GrowArrow(lengthMarker1),
                fadeInTex(lengthLabel),
                lag_ratio=0.5,
            ),
        )
        self.wait(2)

        # self.play(
        #     FadeOut(
        #         lengthMarker1,
        #         refLengthMarker1,
        #         refLengthMarker2,
        #         lengthLabel,
        #         angleMarker,
        #         angleLabel,
        #     )
        # )

        # self.wait(1)

        self.wait(10)


class Statements(Scene):
    def construct(self):
        stmt1 = nMath(
            "Area ", "= \\pi (12)^2 \\times \\frac{120^\\circ}{360^\\circ}"
        ).to_edge(UP)
        stmt2 = nMath("=48\\pi").next_to(stmt1[1], DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(fadeInTex(stmt1))
        self.wait(1)
        self.play(fadeInTex(stmt2))
        self.wait(4)
