from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        f = 0.7
        x = 4 * f
        y = 9 * f
        r = 6 * f

        pr = np.sqrt(x**2 + r**2)
        qr = np.sqrt(y**2 + r**2)

        R = ORIGIN + 3.5 * LEFT + 2.5 * DOWN
        P = R + UP * pr
        Q = R + RIGHT * qr
        T = (x * Q + y * P) / (x + y)

        labelP = nText("P", font_size=40).next_to(P, UP + LEFT, buff=0.2)
        labelQ = nText("Q", font_size=40).next_to(Q, DOWN + RIGHT, buff=0.2)
        labelR = nText("R", font_size=40).next_to(R, DOWN + LEFT, buff=0.2)
        labelT = nText("T", font_size=40).next_to(T, UP + RIGHT, buff=0.2)

        triangle = Polygon(P, Q, R, stroke_color=GREY_N800)
        rightAngle1 = RightAngle(Line(R, Q), Line(R, P), color=GREY_N800, length=0.3)

        tempQuarterArc = Arc(
            radius=r,
            arc_center=R,
            stroke_color=GREY_N800,
            stroke_width=DEFAULT_STROKE_WIDTH,
            angle=PI / 2,
        )

        dotT = Dot(T, color=BLACK, radius=0.05)

        labelPT = nText("4", font_size=36).next_to(
            (P + T) / 2, UP + 0.1 * RIGHT, buff=0.2
        )
        labelQT = nText("9", font_size=36).next_to((Q + T) / 2, UP + RIGHT, buff=0.1)

        quarterCircle = Sector(
            radius=r,
            arc_center=R,
            stroke_color=GREY_N800,
            stroke_width=DEFAULT_STROKE_WIDTH,
            color=YELLOW,
            angle=PI / 2,
            z_index=-20,
        )

        radiusLine = DashedLine(R, T, color=GREY_N800)

        radiusLabel = nText("r", font_size=36).move_to(
            (R + T) / 2 + DOWN * 0.3 + RIGHT * 0.3
        )

        rightAngle = RightAngle(Line(T, P), Line(T, R), color=GREY_N800, length=0.4)

        labelPT2 = nText("x", font_size=36).next_to(
            (P + T) / 2, UP + 0.1 * RIGHT, buff=0.2
        )
        labelQT2 = nText("y", font_size=36).next_to((Q + T) / 2, UP + RIGHT, buff=0.1)

        regionPRT = getTriangularRegion(P, R, T, color=RED_N50)
        regionPRT.set_opacity(0)
        regionQRT = getTriangularRegion(Q, R, T, color=GREEN_N50)
        regionQRT.set_opacity(0)

        # triangle,
        self.play(
            LaggedStart(
                Create(triangle),
                AnimationGroup(
                    FadeIn(labelP, scale=1.2, shift=0.5 * DOWN),
                    FadeIn(labelQ, scale=1.2, shift=0.5 * UP),
                    FadeIn(labelR, scale=1.2, shift=0.5 * UP),
                    Create(rightAngle1),
                ),
                lag_ratio=0.7,
            )
        )
        self.wait(1)

        # quarterCircle,
        self.play(Create(tempQuarterArc))
        self.wait(1)

        # dotT,
        self.play(
            LaggedStart(
                Create(dotT),
                FadeIn(labelT, shift=0.5 * DOWN + 0.5 * LEFT, scale=1.2),
                lag_ratio=0.7,
            )
        )
        self.wait(1)

        self.play(
            LaggedStart(
                FadeIn(labelPT, scale=1.2, shift=0.5 * DOWN),
                FadeIn(labelQT, scale=1.2, shift=0.5 * DOWN),
                lag_ratio=0.7,
            )
        )
        self.wait(1)

        # highlight the area we need to find
        self.play(FadeIn(quarterCircle))
        self.wait(4)

        ## SOLUTION

        # radiusLine,
        self.play(LaggedStart(Create(radiusLine), FadeIn(radiusLabel), lag_ratio=0.5))
        self.wait(1)

        self.play(quarterCircle.animate.set_opacity(0))
        self.wait(1)

        self.play(
            ReplacementTransform(labelPT, labelPT2),
            ReplacementTransform(labelQT, labelQT2),
        )
        self.wait(1)

        self.play(
            LaggedStart(
                regionPRT.animate.set_opacity(0.7),
                regionQRT.animate.set_opacity(0.7),
                lag_ratio=0.8,
            )
        )
        self.wait(1)

        self.play(regionPRT.animate.set_opacity(0), regionQRT.animate.set_opacity(0))
        self.wait(1)

        # Show right triangle (radius perpendicular to the tangent)
        self.play(Create(rightAngle))
        self.wait(1)

        self.play(regionPRT.animate.set_opacity(0.7))
        self.wait(1)
        self.play(regionPRT.animate.set_opacity(0))

        self.play(regionQRT.animate.set_opacity(0.7))
        self.wait(1)
        self.play(regionQRT.animate.set_opacity(0))
        self.wait(1)

        hgl_triangle = Polygon(P, Q, R, stroke_color=RED_N100, stroke_width=6)
        self.play(FadeIn(hgl_triangle))
        self.wait(1)

        self.play(FadeOut(hgl_triangle))
        self.wait(1)

        self.play(quarterCircle.animate.set_opacity(1))

        self.wait(10)


class PythagorasTheorem(Scene):
    def construct(self):
        # Triangle vertices (right-angled triangle)
        f = 0.7
        b = 3 * f
        c = 4 * f
        A = ORIGIN + (c + b) / 2 * DOWN + (c + b) / 2 * LEFT + 3 * LEFT + 0.5 * UP
        B = A + b * RIGHT
        C = A + c * UP

        # Draw triangle ABC
        triangle = Polygon(A, B, C, stroke_color=BLACK, color=YELLOW, fill_opacity=1)

        self.play(Create(triangle))

        triangle2 = triangle.copy()
        self.play(triangle2.animate.rotate(PI / 2, IN, A).shift(UP * (b + c)))

        triangle3 = triangle2.copy()
        self.play(
            triangle3.animate.rotate(PI / 2, IN, triangle2.get_vertices()[0]).shift(
                RIGHT * (b + c)
            )
        )

        triangle4 = triangle3.copy()
        self.play(
            triangle4.animate.rotate(PI / 2, IN, triangle3.get_vertices()[0]).shift(
                DOWN * (b + c)
            )
        )

        P = B
        Q = triangle2.get_vertices()[1]
        R = triangle3.get_vertices()[1]
        S = triangle4.get_vertices()[1]

        square = Polygon(P, Q, R, S, color=RED_N50, fill_opacity=0.3, z_index=-19)
        self.play(FadeIn(square))

        lengthAB = lengthMarkerV2(A, B, "c", DOWN * 0.4)
        lengthAC = lengthMarkerV2(C, A, "b", LEFT * 0.4)

        length1 = lengthMarkerV2(
            triangle3.get_vertices()[0], triangle2.get_vertices()[0], "b+c", UP * 0.4
        )

        length2 = lengthMarkerV2(
            triangle4.get_vertices()[0], triangle3.get_vertices()[0], "b+c", RIGHT * 0.4
        )

        length2[2].shift(RIGHT * 0.3)

        areaSqLabel = (
            MathTex("a^2", color=BLACK).scale(1.3).move_to((P + Q + R + S) / 4)
        )

        self.play(
            LaggedStart(
                FadeIn(lengthAB),
                FadeIn(lengthAC),
                FadeIn(length1),
                FadeIn(length2),
                FadeIn(areaSqLabel),
                lag_ratio=0.5,
            )
        )

        self.wait(4)


class Statements(Scene):
    def construct(self):
        main1 = nMath("PR^2 = r^2 + x^2").to_edge(UP)

        main2 = nMath("QR^2 = r^2 + y^2").next_to(main1, DOWN, buff=0.5)

        main3 = nMath("PR^2 + QR^2 = 2r^2 + x^2 + y^2").next_to(main2, DOWN, buff=0.5)

        main4 = nMath("PQ^2 = 2r^2 + x^2 + y^2").next_to(main3, DOWN, buff=0.5)

        main5 = nMath("(x+y)^2 = 2r^2 + x^2 + y^2").next_to(main4, DOWN, buff=0.5)

        main6 = nMath("r^2  = xy").next_to(main5, DOWN, buff=0.5)

        main_final = nMath("r = \\sqrt{xy}").next_to(main6, DOWN, buff=0.5)

        self.play(fadeInTex(main1))
        self.wait(1)
        self.play(fadeInTex(main2))
        self.wait(1)
        self.play(fadeInTex(main3))
        self.wait(1)
        self.play(fadeInTex(main4))
        self.wait(1)
        self.play(fadeInTex(main5))
        self.wait(1)
        self.play(fadeInTex(main6))
        self.wait(1)
        self.play(fadeInTex(main_final))

        clearScreen(self, 4)

        area1 = nMath("Area", "= \\frac{\\pi r^2}{4} = \\frac{\\pi xy}{4}").to_edge(UP)

        area2 = nMath("=\\frac{\\pi(4)(9)}{4}").next_to(
            area1[1], DOWN, buff=0.5, aligned_edge=LEFT
        )

        area3 = nMath("=9\\pi").next_to(area2, DOWN, buff=0.5, aligned_edge=LEFT)

        self.play(fadeInTex(area1))
        self.wait(1)
        self.play(fadeInTex(area2))
        self.wait(1)
        self.play(fadeInTex(area3))
        self.wait(4)


class Thumbnail(Scene):
    def construct(self):
        f = 0.7
        x = 4 * f
        y = 9 * f
        r = 6 * f

        pr = np.sqrt(x**2 + r**2)
        qr = np.sqrt(y**2 + r**2)

        R = ORIGIN + 3.5 * LEFT + 2.5 * DOWN
        P = R + UP * pr
        Q = R + RIGHT * qr
        T = (x * Q + y * P) / (x + y)

        triangle = Polygon(P, Q, R, stroke_color=GREY_N800, stroke_width=8)
        rightAngle1 = RightAngle(
            Line(R, Q), Line(R, P), color=GREY_N800, length=0.5, stroke_width=6
        )

        quarterCircle = Sector(
            radius=r,
            arc_center=R,
            stroke_color=GREY_N800,
            stroke_width=8,
            color=YELLOW,
            angle=PI / 2,
            z_index=-20,
        )

        self.add(triangle, rightAngle1, quarterCircle)
        self.wait(10)
