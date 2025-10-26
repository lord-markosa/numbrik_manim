from manim import *
from utils import *


class Template(Scene):
    def construct(self):
        axis = getAxis(x_length=12, y_length=7, color=GREY_N50)

        a = 3.5
        b = 2

        line1 = Line(ORIGIN, ORIGIN + a * RIGHT, color=GREY_N200)
        line2 = Line(
            ORIGIN + a * RIGHT, ORIGIN + a * RIGHT + b * RIGHT, color=GREY_N200
        )

        lengthMarker1 = lengthMarkerV3(
            ORIGIN, line1.get_end(), "a", DOWN * 0.5, tip_length=0.15, scale=0.8
        )
        lengthMarker2 = lengthMarkerV3(
            line2.get_start(),
            line2.get_end(),
            "b",
            DOWN * 0.5,
            tip_length=0.15,
            scale=0.8,
        )

        alpha = ValueTracker(0)
        midPoint = Dot(ORIGIN + (a + b) / 2 * RIGHT, color=ORANGE_N400)

        def getPosition(dist, angle):
            return dist * np.cos(angle) * RIGHT + dist * np.sin(angle) * UP

        tempRadius = always_redraw(
            lambda: Line(
                ORIGIN + (a + b) / 2 * RIGHT,
                ORIGIN
                + (a + b) / 2 * RIGHT
                + getPosition((a + b) / 2, alpha.get_value()),
                color=YELLOW,
            )
        )

        # self.add(tempRadius)
        # self.play(alpha.animate.set_value(PI), run_time=1.5)

        self.play(
            LaggedStart(
                Create(axis),
                Create(line1),
                FadeIn(lengthMarker1),
                FadeIn(Dot(a * RIGHT, color=GREY_N500)),
                Create(line2),
                FadeIn(lengthMarker2),
                FadeIn(Dot((a + b) * RIGHT, color=GREY_N200)),
                FadeIn(midPoint),
                Create(tempRadius),
                lag_ratio=0.4,
            )
        )

        # self.play(LaggedStart(FadeIn(midPoint), Create(tempRadius), lag_ratio=0.4))
        # self.add(tempRadius)

        # self.add(tempArc2, tempRadius2, EllipseTrace)

        self.play(
            alpha.animate.set_value(PI),
            run_time=1.5,
            # rate_func=there_and_back_with_pause,
        )
        self.play(
            LaggedStart(
                FadeOut(tempRadius),
                FadeOut(lengthMarker1, lengthMarker2),
                lag_ratio=0.3,
            )
        )

        self.wait(5)


class Main(Scene):
    def construct(self):
        a = 3.5
        b = 2
        theta = ValueTracker(0)

        axis = getAxis(x_length=12, y_length=7, color=GREY_N50)
        lineB = Line(
            ORIGIN + a * RIGHT, ORIGIN + a * RIGHT + b * RIGHT, color=GREY_N200
        )

        dotB = Dot((a + b) * RIGHT, color=GREY_N200)

        def getPosition(dist, angle):
            return dist * np.cos(angle) * RIGHT + dist * np.sin(angle) * UP

        mainRadius = always_redraw(
            lambda: Line(
                ORIGIN, getPosition((a + b) / 2, theta.get_value()), color=GREY_N200
            )
        )
        mainArc1 = always_redraw(
            lambda: Arc(
                (a + b) / 2, start_angle=0, angle=theta.get_value(), color=ORANGE_N50
            )
        )

        dot1 = always_redraw(
            lambda: Dot(getPosition((a + b) / 2, theta.get_value()), color=ORANGE_N400)
        )

        mainRadius2 = always_redraw(
            lambda: Line(
                getPosition((a + b) / 2, theta.get_value()),
                getPosition((a + b) / 2, theta.get_value())
                + getPosition((a - b) / 2, -theta.get_value()),
                color=GREY_N200,
            )
        )
        mainArc2 = always_redraw(
            lambda: Arc(
                (a - b) / 2,
                start_angle=0,
                arc_center=getPosition((a + b) / 2, theta.get_value()),
                angle=-theta.get_value(),
                color=GREEN_N100,
            )
        )

        dot2 = always_redraw(
            lambda: Dot(
                getPosition((a + b) / 2, theta.get_value())
                + getPosition((a - b) / 2, -theta.get_value()),
                color=GREY_N500,
            ),
        )

        path = TracedPath(
            lambda: getPosition((a + b) / 2, theta.get_value())
            + getPosition((a - b) / 2, -theta.get_value()),
            stroke_width=6,
            stroke_color=NUMBRIK_COLOR,
        )

        lengthMarker1 = lengthMarkerV3(
            ORIGIN,
            a * RIGHT,
            "a",
            DOWN * 0.3,
            tip_length=0.15,
            scale=0.8,
            color=GREY_N200,
            centerDist=0.2,
        )
        lengthMarker2 = lengthMarkerV3(
            b * UP, ORIGIN, "b", LEFT * 0.3, tip_length=0.15, scale=0.8, color=GREY_N200
        )

        self.add(
            axis,
            lineB,
            dotB,
            mainRadius,
            mainArc1,
            mainRadius2,
            path,
            mainArc2,
            dot1,
            dot2,
        )

        self.play(theta.animate.set_value(2 * PI), run_time=10.01)
        self.wait(1)
        self.play(Rotate(VGroup(lineB, dotB), PI / 2, OUT, a * RIGHT))
        self.play(
            LaggedStart(
                VGroup(lineB, dotB).animate.shift(LEFT * a),
                FadeIn(lengthMarker1, lengthMarker2),
                lag_ratio=0.4,
            )
        )
        self.wait(10)


class Statements(Scene):
    def construct(self):
        stmt = nMath("\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1")
        self.play(fadeInTex(stmt))
        self.wait(10)
