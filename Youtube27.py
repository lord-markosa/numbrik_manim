from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        O = ORIGIN

        # OPTIMUM FOR 1ST DEMO
        A = O + 4.5 * UP + 2.5 * LEFT
        B = O + 5 * LEFT
        C = O + 2.5 * RIGHT

        triangle = Polygon(
            A, B, C, stroke_color=[GREY_N200, GREY_N800], sheen_direction=UP + RIGHT
        )

        triangle.move_to(ORIGIN)
        A, B, C = triangle.get_vertices()

        BC = Line(B, C)
        D = BC.get_projection(A)
        AC = Line(A, C)
        E = AC.get_projection(B)
        AB = Line(A, B)
        F = AB.get_projection(C)

        AP = Line(A, D, color=GREY_N200)
        BQ = Line(B, E, color=GREY_N200)
        CR = Line(C, F, color=GREY_N200)

        H = line_intersection([A, D], [B, E])

        P = (A + H) / 2
        Q = (B + H) / 2
        R = (C + H) / 2

        npCircle = Circle.from_three_points(D, E, F, color=GREY_N50)

        A_ = (B + C) / 2
        B_ = (A + C) / 2
        C_ = (B + A) / 2

        self.add(
            triangle,
            AP,
            BQ,
            CR,
            npCircle,
        )
        self.wait(5)


class TakeIntro(Scene):
    def construct(self):
        radius = 2
        circle1 = (
            Circle(
                radius=radius,
                fill_opacity=0.7,
                sheen_direction=RIGHT,
            )
            .set_color_by_gradient([WHITE, GREEN_N100])
            .set_stroke(
                color=[GREY_N400, GREY_N800],
                width=6,
            )
        )
        circle2 = (
            circle1.copy()
            .set_color_by_gradient([WHITE, NUMBRIK_COLOR])
            .set_stroke(
                color=[GREY_N400, GREY_N800],
                width=6,
            )
        )

        circle1.shift(3 * LEFT)
        circle2.shift(3 * RIGHT)

        tangent = DashedLine(
            2.5 * UP,
            2.5 * DOWN,
            color=RED_N50,
            stroke_width=6,
        )

        poi = Dot(ORIGIN, 0.1, color=BLACK)

        self.play(Create(circle1), Create(circle2), run_time=2)
        self.wait(1)
        self.play(circle1.animate.shift(RIGHT), circle2.animate.shift(LEFT))
        self.play(Create(tangent))
        self.play(FadeIn(poi))

        self.wait(1)

        self.play(FadeOut(poi))
        l = 0.6
        self.play(circle1.animate.shift(l * RIGHT), circle2.animate.shift(l * LEFT))

        poi1 = Dot(UP * np.sqrt(radius**2 - (radius - l) ** 2), color=BLACK, radius=0.1)
        poi2 = Dot(
            DOWN * np.sqrt(radius**2 - (radius - l) ** 2), color=BLACK, radius=0.1
        )
        self.play(FadeIn(poi1, poi2))

        self.wait(2)
        self.play(FadeOut(circle1, circle2, tangent, poi1, poi2))

        # Triangle vertices (non-collinear)
        A = LEFT * 2.8
        B = RIGHT * 2
        C = UP * 3

        # Draw triangle
        triangle = Polygon(
            A, B, C, stroke_color=GREY_N800, stroke_width=6, sheen_direction=LEFT
        )

        circumcircle = Circle.from_three_points(
            A,
            B,
            C,
            stroke_color=[GREY_N100, GREY_N400],
            stroke_width=6,
            sheen_direction=RIGHT,
        )

        A_dot, B_dot, C_dot = [Dot(p, color=GREY_N200) for p in (A, B, C)]

        VGroup(A_dot, B_dot, C_dot, triangle, circumcircle).move_to(ORIGIN).scale(1.2)

        A, B, C = triangle.get_vertices()

        A_label = MathTex("A").next_to(A_dot, DOWN + LEFT, buff=0.2)
        B_label = MathTex("B").next_to(B_dot, DOWN + RIGHT, buff=0.2)
        C_label = MathTex("C").next_to(C_dot, UP, buff=0.2)

        self.play(FadeIn(A_dot, B_dot, C_dot, scale=1.2))
        self.wait(1)
        self.play(Create(circumcircle))
        self.wait(1)
        self.play(Create(triangle))
        self.wait(1)
        self.play(FadeOut(circumcircle, A_dot, B_dot, C_dot))
        self.wait(1)

        # Circumcircle: find perpendicular bisectors intersection
        def perp_bisector(p1, p2, length=5):
            mid = (p1 + p2) / 2
            dir_vec = p2 - p1
            perp = np.array([-dir_vec[1], dir_vec[0], 0])
            perp *= 1 / np.linalg.norm(perp)
            return Line(
                mid - perp * length / 2, mid + perp * length / 2, color=NUMBRIK_COLOR
            )

        createMidPointMarks = lambda line: always_redraw(
            lambda: VGroup(
                createLineMarks(
                    Line(line.get_start(), line.get_center()), themeColor=NUMBRIK_COLOR
                ),
                createLineMarks(
                    Line(line.get_center(), line.get_end()), themeColor=NUMBRIK_COLOR
                ),
            )
        )

        bis_ab = perp_bisector(A, B)
        bis_bc = perp_bisector(B, C)
        midPointMarks_ab = createMidPointMarks(Line(A, B))
        midPointMarks_bc = createMidPointMarks(Line(B, C))

        perpMark_ab = getRightAngle(A, (A + B) / 2, bis_ab.get_end(), length=0.3)
        perpMark_bc = getRightAngle(C, (B + C) / 2, bis_bc.get_end(), length=0.3)

        # Animate bisectors
        self.play(
            LaggedStart(
                FadeIn(midPointMarks_ab),
                Create(bis_ab),
                Create(perpMark_ab),
                FadeIn(midPointMarks_bc),
                Create(bis_bc),
                Create(perpMark_bc),
                lag_ratio=0.7,
            )
        )
        self.play(Create(circumcircle))
        self.wait(2)

        self.play(
            FadeOut(
                midPointMarks_ab,
                midPointMarks_bc,
                bis_ab,
                bis_bc,
                perpMark_ab,
                perpMark_bc,
                circumcircle,
            )
        )

        A_ = (B + C) / 2
        B_ = (A + C) / 2
        C_ = (B + A) / 2

        npCircle = Circle.from_three_points(
            A_,
            B_,
            C_,
            stroke_color=[GREY_N200, GREY_N800],
            sheen_direction=UP + RIGHT,
        )

        pointMarker = lambda point: Dot(point, color=GREY_N400, radius=0.05)

        pointA_ = pointMarker(A_)
        pointB_ = pointMarker(B_)
        pointC_ = pointMarker(C_)

        createMidPointMarks = lambda line: VGroup(
            createLineMarks(
                Line(line.get_start(), line.get_center()), themeColor=NUMBRIK_COLOR
            ),
            createLineMarks(
                Line(line.get_center(), line.get_end()), themeColor=NUMBRIK_COLOR
            ),
        )

        midPointMarksA = createMidPointMarks(Line(B, C))
        midPointMarksB = createMidPointMarks(Line(A, C))
        midPointMarksC = createMidPointMarks(Line(A, B))

        self.play(
            LaggedStart(
                AnimationGroup(
                    Create(pointA_),
                ),
                FadeIn(midPointMarksA),
                AnimationGroup(
                    Create(pointB_),
                ),
                FadeIn(midPointMarksB),
                AnimationGroup(
                    Create(pointC_),
                ),
                FadeIn(midPointMarksC),
                Create(npCircle),
                lag_ratio=0.5,
            )
        )

        grp1 = VGroup(
            triangle,
            npCircle,
            midPointMarksA,
            midPointMarksB,
            midPointMarksC,
            pointA_,
            pointB_,
            pointC_,
        )

        triangle2 = triangle.copy()

        self.play(
            grp1.animate.shift(LEFT * 2.5).scale(0.8),
            triangle2.animate.shift(RIGHT * 2.5).scale(0.8),
        )
        self.wait(1)

        A2, B2, C2 = triangle2.get_vertices()

        D = Line(B2, C2).get_projection(A2)
        E = Line(A2, C2).get_projection(B2)
        F = Line(A2, B2).get_projection(C2)

        AD = Line(A2, D, color=GREY_N200)
        CF = Line(C2, F, color=GREY_N200)
        BE = Line(B2, E, color=GREY_N200)

        rtAngleD = getRightAngle(B2, D, A2, color=GREY_N200, length=0.15)
        rtAngleF = getRightAngle(C2, F, A2, color=GREY_N200, length=0.15)
        rtAngleE = getRightAngle(A2, E, B2, color=GREY_N200, length=0.15)

        npCircle2 = Circle.from_three_points(
            D,
            E,
            F,
            stroke_color=[GREY_N100, GREY_N400],
            stroke_width=6,
            sheen_direction=RIGHT,
        )

        self.play(
            LaggedStart(
                Create(AD),
                Create(rtAngleD),
                Create(BE),
                Create(rtAngleE),
                Create(CF),
                Create(rtAngleF),
                Create(npCircle2),
                lag_ratio=0.5,
            )
        )
        self.wait(1)

        grp2 = VGroup(
            triangle2,
            npCircle2,
            AD,
            BE,
            CF,
            rtAngleD,
            rtAngleE,
            rtAngleF,
        )

        grp3 = grp2.copy().move_to(ORIGIN).scale(1.8)

        triangle3 = grp3[0]
        triangle3.z_index = 1
        A3, B3, C3 = triangle3.get_vertices()

        A__ = ((B3 + C3) / 2,)
        B__ = (A3 + C3) / 2
        C__ = (B3 + A3) / 2

        A3_, B3_, C3_ = [Dot(p, color=GREY_N200) for p in (A__, B__, C__)]

        self.play(
            ReplacementTransform(grp1[0], grp3[0]),
            ReplacementTransform(grp2[0], grp3[0]),
            ReplacementTransform(grp1[1], grp3[1]),
            ReplacementTransform(grp2[1], grp3[1]),
            ReplacementTransform(grp2[2:], grp3[2:]),
            ReplacementTransform(pointA_, A3_),
            ReplacementTransform(pointB_, B3_),
            ReplacementTransform(pointC_, C3_),
            FadeOut(
                midPointMarksA,
                midPointMarksB,
                midPointMarksC,
            ),
        )
        self.play(
            grp3[1]
            .animate.set_opacity(1)
            .set_color_by_gradient([WHITE, NUMBRIK_COLOR_50])
            .set_stroke(
                color=[GREY_N100, GREY_N400],
                width=6,
            )
        )

        self.wait(1)

        self.play(
            GrowArrow(
                Arrow(A3_.get_center() + 1.5 * RIGHT, A3_.get_center(), color=RED_N100)
            ),
            GrowArrow(
                Arrow(B3_.get_center() + 1.5 * LEFT, B3_.get_center(), color=RED_N100)
            ),
            GrowArrow(
                Arrow(
                    C3_.get_center() + +1.5 * (LEFT + DOWN) / np.sqrt(2),
                    C3_.get_center(),
                    color=RED_N100,
                )
            ),
            GrowArrow(
                Arrow(
                    grp3[2].get_end() + 1.5 * (RIGHT + UP) / np.sqrt(2),
                    grp3[2].get_end(),
                    color=RED_N100,
                )
            ),
            GrowArrow(
                Arrow(
                    grp3[3].get_end() + 1.5 * (LEFT + UP) / np.sqrt(2),
                    grp3[3].get_end(),
                    color=RED_N100,
                )
            ),
            GrowArrow(
                Arrow(
                    grp3[4].get_end() + +1.5 * (RIGHT + DOWN) / np.sqrt(2),
                    grp3[4].get_end(),
                    color=RED_N100,
                )
            ),
        )

        self.wait(10)


class Take5(Scene):
    def construct(self):
        O = ORIGIN + 2.25 * DOWN

        distx = ValueTracker(1.2)
        disty = ValueTracker(5)

        getA = lambda: O + disty.get_value() * UP + distx.get_value() * RIGHT

        B = O + LEFT * 4
        C = O + RIGHT * 4

        triangle = always_redraw(
            lambda: Polygon(
                getA(),
                B,
                C,
                stroke_color=GREY_N500,
                stroke_width=6,
                sheen_direction=LEFT,
            )
        )

        self.add(triangle)

        getD = lambda: Line(B, C).get_projection(getA())
        getE = lambda: Line(getA(), C).get_projection(B)
        getF = lambda: Line(getA(), B).get_projection(C)

        AD = always_redraw(lambda: Line(getA(), getD(), color=GREY_N200))

        getH = lambda: line_intersection([getA(), getF()], [B, getF()])

        getP = lambda: (getA() + getH()) / 2
        getQ = lambda: (B + getH()) / 2
        getR = lambda: (C + getH()) / 2

        getA_ = lambda: (B + C) / 2
        getB_ = lambda: (getA() + C) / 2
        getC_ = lambda: (B + getA()) / 2

        npCircle = always_redraw(
            lambda: Circle.from_three_points(
                getD(),
                getE(),
                getF(),
                stroke_color=[GREY_N200, GREY_N800],
                sheen_direction=UP + RIGHT,
            )
        )

        pointMarker = lambda point: Dot(point, color=GREY_N400, radius=0.05)

        labelA = always_redraw(lambda: nMath("A").next_to(getA(), UP, buff=0.3))
        labelB = nMath("B").next_to(B, DOWN + LEFT, buff=0.3)
        labelC = nMath("C").next_to(C, DOWN + RIGHT, buff=0.3)

        self.play(Create(triangle))
        self.play(FadeIn(labelA, labelB, labelC, scale=1.1))
        self.wait(1)

        pointA_ = always_redraw(lambda: pointMarker(getA_()))
        pointB_ = always_redraw(lambda: pointMarker(getB_()))
        pointC_ = always_redraw(lambda: pointMarker(getC_()))

        labelA_ = always_redraw(lambda: nMath("A'").next_to(getA_(), DOWN, buff=0.3))
        labelB_ = always_redraw(
            lambda: nMath("B'").next_to(getB_(), RIGHT + 0.5 * UP, buff=0.2)
        )
        labelC_ = always_redraw(
            lambda: nMath("C'").next_to(getC_(), LEFT + 0.5 * UP, buff=0.2)
        )

        createMidPointMarks = lambda line: always_redraw(
            lambda: VGroup(
                createLineMarks(
                    Line(line.get_start(), line.get_center()), themeColor=NUMBRIK_COLOR
                ),
                createLineMarks(
                    Line(line.get_center(), line.get_end()), themeColor=NUMBRIK_COLOR
                ),
            )
        )

        midPointMarksA = createMidPointMarks(Line(B, C))
        midPointMarksB = createMidPointMarks(Line(getA(), C))
        midPointMarksC = createMidPointMarks(Line(getA(), B))

        self.play(
            LaggedStart(
                AnimationGroup(
                    Create(pointA_),
                    FadeIn(
                        labelA_,
                    ),
                ),
                FadeIn(midPointMarksA),
                AnimationGroup(
                    Create(pointB_),
                    FadeIn(
                        labelB_,
                    ),
                ),
                FadeIn(midPointMarksB),
                AnimationGroup(
                    Create(pointC_),
                    FadeIn(
                        labelC_,
                    ),
                ),
                FadeIn(midPointMarksC),
                lag_ratio=0.5,
            )
        )

        self.wait(1)
        self.play(FadeOut(midPointMarksA, midPointMarksB, midPointMarksC))
        self.wait(1)

        lineA_C_ = always_redraw(
            lambda: DashedLine(getA_(), getC_(), color=GREY_N200),
        )

        lineC_B_ = always_redraw(lambda: DashedLine(getC_(), getB_(), color=GREY_N200))

        self.play(Create(lineA_C_))
        self.play(Create(lineC_B_))

        parallelgm = getRegion(
            getA_(),
            C,
            getB_(),
            getC_(),
            gradient_color=[WHITE, GREEN_N100],
            sheen_direction=RIGHT,
        )

        self.play(FadeIn(parallelgm))
        self.wait(1)

        # def parallelMarks(lineA, lineB, color=NUMBRIK_COLOR_200):
        #     angle = lineA.get_angle()
        #     lineAMark = (
        #         ArrowTriangleFilledTip(start_angle=0, color=color)
        #         .move_to(lineA.get_center())
        #         .rotate(angle)
        #     )
        #     lineBMark = (
        #         ArrowTriangleFilledTip(start_angle=angle, color=color)
        #         .move_to(lineB.get_center())
        #         .rotate(angle)
        #     )
        #     return VGroup(lineAMark, lineBMark)

        # parallelMarks1 = always_redraw(
        #     lambda: parallelMarks(Line(getA_(), getC_()), Line(getB_(), C))
        # )

        # parallelMarks2 = always_redraw(
        #     lambda: parallelMarks(
        #         Line(getC_(), getB_()),
        #         Line(getA_(), C),
        #         color=GREEN_N200,
        #     )
        # )

        # self.play(Create(parallelMarks1), Create(parallelMarks2))
        # self.wait(1)
        # self.play(FadeOut(parallelMarks1, parallelMarks2))
        # self.wait(1)

        angleMarker1 = always_redraw(
            lambda: getAngle(C, getD(), getB_(), color=GREY_N200, radius=0.5)
        )
        angleMarker1_adj = always_redraw(
            lambda: VGroup(
                getAngle(getB_(), getD(), B, color=GREY_N200, radius=0.6),
                getAngle(getB_(), getD(), B, color=GREY_N200, radius=0.7),
            )
        )
        angleMarker2 = always_redraw(
            lambda: getAngle(getB_(), C, getD(), color=GREY_N200, radius=0.5)
        )

        angleMarker3 = always_redraw(
            lambda: getAngle(getA_(), getC_(), getB_(), color=GREY_N200, radius=0.5)
        )

        self.play(
            LaggedStart(Create(angleMarker2), Create(angleMarker3), lag_ratio=0.5)
        )
        self.wait(1)
        self.play(FadeOut(parallelgm))
        self.wait(1)

        rtAngleD = always_redraw(
            lambda: getRightAngle(getA(), getD(), B, color=GREY_N200, length=0.3)
        )

        labelD = always_redraw(lambda: nMath("D").next_to(getD(), DOWN, buff=0.34))

        self.play(
            LaggedStart(Create(AD), Create(rtAngleD), FadeIn(labelD), lag_ratio=0.4)
        )
        self.wait(1)

        triADC = getRegion(
            getA(),
            getD(),
            C,
            gradient_color=[YELLOW_N40, WHITE],
            sheen_direction=RIGHT,
        )

        self.play(FadeIn(triADC))
        self.wait(1)

        lineDB_ = always_redraw(lambda: Line(getD(), getB_(), color=GREY_N200))

        self.play(Create(lineDB_))
        self.wait(1)

        eqMarker1 = always_redraw(
            lambda: createLineMarks(Line(getB_(), getA()), themeColor=NUMBRIK_COLOR)
        )
        eqMarker2 = always_redraw(
            lambda: createLineMarks(Line(getB_(), C), themeColor=NUMBRIK_COLOR)
        )
        eqMarker3 = always_redraw(
            lambda: createLineMarks(Line(getD(), getB_()), themeColor=NUMBRIK_COLOR)
        )

        self.play(
            LaggedStart(
                FadeIn(eqMarker1), FadeIn(eqMarker2), FadeIn(eqMarker3), lag_ratio=0.4
            )
        )
        self.wait(1)

        self.play(FadeOut(triADC))
        self.wait(1)

        triDB_C = getRegion(
            getB_(),
            getD(),
            C,
            gradient_color=[WHITE, GREEN_N100],
            sheen_direction=RIGHT,
        )
        self.play(FadeIn(triDB_C))
        self.wait(1)

        # self.play(FadeOut(eqMarker1, eqMarker2, eqMarker3, rtAngleD))
        # self.wait(1)
        self.play(Create(angleMarker1))
        self.wait(1)

        self.play(
            FadeOut(
                triDB_C,
                eqMarker1,
                eqMarker2,
                eqMarker3,
            )
        )
        self.wait(1)

        self.play(Create(npCircle))
        self.wait(1)

        self.play(Create(angleMarker1_adj), FadeOut(rtAngleD))

        solidHighlight(self, [angleMarker3, angleMarker1_adj], buff=0.1, wait_time=1)

        self.play(FadeOut(angleMarker1_adj), FadeIn(rtAngleD))
        self.wait(1)

        self.play(distx.animate.set_value(-1.5), run_time=2.5)
        self.wait(1)

        lineA_B_ = always_redraw(lambda: DashedLine(getA_(), getB_(), color=RED_N100))

        hgl = solidHighlight(
            self, [angleMarker3, angleMarker1], buff=0.1, wait_time=1, unhighlight=False
        )

        self.play(Create(lineA_B_))
        self.wait(1)

        self.play(FadeOut(*hgl, lineA_B_))
        self.wait(2)

        self.play(Uncreate(npCircle))
        self.play(
            FadeOut(
                lineC_B_,
                rtAngleD,
                lineDB_,
                angleMarker3,
                angleMarker1,
                angleMarker2,
                AD,
            )
        )

        # Other two altitudes

        lineA_B_ = always_redraw(lambda: DashedLine(getA_(), getB_(), color=GREY_N200))

        labelE = always_redraw(
            lambda: nMath("E").next_to(getE(), RIGHT + 0.5 * UP, buff=0.2)
        )

        BE = always_redraw(lambda: Line(B, getE(), color=GREY_N200))

        rtAngleE = always_redraw(
            lambda: getRightAngle(B, getE(), C, color=GREY_N200, length=0.3)
        )

        lineEC_ = Line(getC_(), getE(), color=GREY_N200)

        angleMarker1 = getAngle(getA(), getE(), getC_(), color=GREY_N200)
        angleMarker3 = getAngle(getB_(), getA_(), getC_(), color=GREY_N200)

        self.play(
            LaggedStart(
                Create(lineA_B_),
                Create(BE),
                FadeIn(labelE),
                Create(rtAngleE),
                Create(lineEC_),
                lag_ratio=0.5,
            )
        )

        self.play(
            LaggedStart(Create(angleMarker1), Create(angleMarker3), lag_ratio=0.5)
        )
        self.wait(1)

        self.play(Create(npCircle))
        self.wait(1)

        self.play(Uncreate(npCircle))
        self.play(FadeOut(lineEC_, rtAngleE, angleMarker1, angleMarker3, BE, lineA_C_))

        rtAngleF = always_redraw(
            lambda: getRightAngle(C, getF(), getA(), color=GREY_N200, length=0.3)
        )

        CF = always_redraw(lambda: Line(C, getF(), color=GREY_N200))

        labelF = always_redraw(
            lambda: nMath("F").next_to(getF(), LEFT + 0.5 * UP, buff=0.2)
        )

        self.play(
            LaggedStart(
                Create(lineC_B_),
                Create(CF),
                FadeIn(labelF),
                Create(rtAngleF),
                lag_ratio=0.5,
            )
        )
        self.wait(1)

        self.play(Create(npCircle))
        self.wait(1)

        self.play(FadeOut(lineA_B_, lineC_B_))
        self.play(
            LaggedStart(
                Create(AD),
                Create(rtAngleD),
                Create(BE),
                Create(rtAngleE),
                lag_ratio=0.5,
            )
        )
        self.wait(2)

        self.play(distx.animate.set_value(1.2), run_time=3)

        self.wait(5)


class Take6(Scene):
    def construct(self):
        O = ORIGIN + 2.25 * DOWN

        distx = ValueTracker(1.2)
        disty = ValueTracker(5)

        getA = lambda: O + disty.get_value() * UP + distx.get_value() * RIGHT

        B = O + LEFT * 4
        C = O + RIGHT * 4

        triangle = always_redraw(
            lambda: Polygon(
                getA(),
                B,
                C,
                stroke_color=GREY_N500,
                stroke_width=6,
                sheen_direction=LEFT,
            )
        )

        getD = lambda: Line(B, C).get_projection(getA())
        getE = lambda: Line(getA(), C).get_projection(B)
        getF = lambda: Line(getA(), B).get_projection(C)

        AD = always_redraw(lambda: Line(getA(), getD(), color=GREY_N200))

        getH = lambda: line_intersection([getA(), getD()], [B, getE()])

        getP = lambda: (getA() + getH()) / 2
        getQ = lambda: (B + getH()) / 2
        getR = lambda: (C + getH()) / 2

        getA_ = lambda: (B + C) / 2
        getB_ = lambda: (getA() + C) / 2
        getC_ = lambda: (B + getA()) / 2

        npCircle = always_redraw(
            lambda: Circle.from_three_points(
                getD(),
                getE(),
                getF(),
                stroke_color=[GREY_N200, GREY_N800],
                sheen_direction=UP + RIGHT,
            )
        )

        pointMarker = lambda point: Dot(point, color=GREY_N400, radius=0.05)

        pointA_ = always_redraw(lambda: pointMarker(getA_()))
        pointB_ = always_redraw(lambda: pointMarker(getB_()))
        pointC_ = always_redraw(lambda: pointMarker(getC_()))

        labelA = always_redraw(lambda: nMath("A").next_to(getA(), UP, buff=0.3))
        labelB = nMath("B").next_to(B, DOWN + LEFT, buff=0.3)
        labelC = nMath("C").next_to(C, DOWN + RIGHT, buff=0.3)

        labelA_ = always_redraw(lambda: nMath("A'").next_to(getA_(), DOWN, buff=0.3))
        labelB_ = always_redraw(
            lambda: nMath("B'").next_to(getB_(), RIGHT + 0.5 * UP, buff=0.2)
        )
        labelC_ = always_redraw(
            lambda: nMath("C'").next_to(getC_(), LEFT + 0.5 * UP, buff=0.2)
        )
        lineA_C_ = always_redraw(
            lambda: DashedLine(getA_(), getC_(), color=GREY_N200),
        )
        lineC_B_ = always_redraw(lambda: DashedLine(getC_(), getB_(), color=GREY_N200))

        def parallelMarks(lineA, lineB, color=NUMBRIK_COLOR_200):
            angle = lineA.get_angle()
            lineAMark = (
                ArrowTriangleFilledTip(start_angle=0, color=color)
                .move_to(lineA.get_center())
                .rotate(angle)
            )
            lineBMark = (
                ArrowTriangleFilledTip(start_angle=0, color=color)
                .move_to(lineB.get_center())
                .rotate(angle)
            )
            return VGroup(lineAMark, lineBMark)

        BE = always_redraw(lambda: Line(B, getE(), color=GREY_N200))
        CF = always_redraw(lambda: Line(C, getF(), color=GREY_N200))

        rtAngleD = always_redraw(
            lambda: getRightAngle(getA(), getD(), B, color=GREY_N200, length=0.3)
        )
        rtAngleF = always_redraw(
            lambda: getRightAngle(C, getF(), getA(), color=GREY_N200, length=0.3)
        )

        rtAngleE = always_redraw(
            lambda: getRightAngle(B, getE(), C, color=GREY_N200, length=0.3)
        )

        linePA_ = always_redraw(lambda: Line(getP(), getA_(), color=GREY_N200))
        linePC_ = always_redraw(lambda: DashedLine(getC_(), getP(), color=GREY_N200))

        rtAngleC_ = always_redraw(
            lambda: getRightAngle(getA_(), getC_(), getP(), length=0.3, color=GREY_N200)
        )

        labelD = always_redraw(lambda: nMath("D").next_to(getD(), DOWN, buff=0.34))

        labelF = always_redraw(
            lambda: nMath("F").next_to(getF(), LEFT + 0.5 * UP, buff=0.2)
        )

        labelE = always_redraw(
            lambda: nMath("E").next_to(getE(), RIGHT + 0.5 * UP, buff=0.2)
        )

        labelH = nMath("H").next_to(getH(), DOWN + RIGHT, buff=0.2)

        self.add(
            triangle,
            npCircle,
            AD,
            BE,
            CF,
            labelA,
            labelB,
            labelC,
            pointA_,
            labelA_,
            pointB_,
            labelB_,
            pointC_,
            labelC_,
            rtAngleD,
            rtAngleE,
            rtAngleF,
            labelD,
            labelE,
            labelF,
        )
        self.wait(2)

        # FadeOut(CF, labelF, rtAngleF),
        self.play(FadeIn(labelH))
        self.wait(1)

        labelP = nMath("P").next_to(getP(), RIGHT + UP, buff=1.2)

        arrow = (
            Arrow(
                labelP.get_left(),
                getP(),
                buff=0.2,
                stroke_width=10,
                tip_length=0.5,
            )
            .set_color_by_gradient([RED_N100])
            .set_sheen_direction(RIGHT + 0.5 * UP)
        )

        arrow2 = (
            Arrow(
                getQ() + 1.8 * DOWN + 0.5 * LEFT,
                getQ(),
                buff=0.2,
                stroke_width=10,
                tip_length=0.5,
            )
            .set_color_by_gradient([RED_N100])
            .set_sheen_direction(RIGHT + 0.5 * UP)
        )

        arrow3 = (
            Arrow(
                getR() + 1.9 * DOWN + 0.3 * RIGHT,
                getR(),
                buff=0.2,
                stroke_width=10,
                tip_length=0.5,
            )
            .set_color_by_gradient([RED_N100])
            .set_sheen_direction(RIGHT + 0.5 * UP)
        )

        self.play(
            LaggedStart(
                GrowArrow(arrow), GrowArrow(arrow2), GrowArrow(arrow3), lag_ratio=0.5
            )
        )
        self.wait(2)
        self.play(
            FadeIn(labelP),
            FadeOut(arrow3, arrow2, CF, rtAngleF, labelF),
            arrow.animate.set_color(RED_N50),
        )
        solidHighlight(self, labelP, buff=0.15)

        self.play(Create(linePA_))
        self.wait(1)
        self.play(Create(lineA_C_))
        self.play(Create(linePC_))
        self.play(Create(rtAngleC_))
        self.wait(1)
        self.play(FadeOut(linePA_), Uncreate(npCircle))
        self.wait(1)

        parallelMarks1 = parallelMarks(lineA_C_, Line(C, getB_()))
        self.play(FadeIn(parallelMarks1))
        self.wait(1)

        parallelMarks2 = parallelMarks(
            linePC_, Line(BE.get_center(), getH()), color=GREEN_N200
        )

        hgl = solidHighlight(self, [rtAngleC_, rtAngleE], buff=0.2, unhighlight=False)

        self.play(FadeIn(parallelMarks2))
        self.wait(1)

        region1 = getRegion(
            B, getH(), getA(), gradient_color=[WHITE, YELLOW_N50], sheen_direction=RIGHT
        )

        self.play(FadeOut(parallelMarks1, *hgl))
        self.play(FadeIn(region1))

        self.wait(1)

        def highlightLines(points):
            """
            Given a list of (pt1, pt2) tuples, returns a list of highlighted Lines.
            """
            return [Line(pt1, pt2, color=YELLOW, stroke_width=5) for pt1, pt2 in points]

        hglLine = highlightLines([(getA(), getH())])
        self.play(FadeOut(region1))
        self.play(FadeIn(*hglLine))
        self.wait(1)

        self.play(
            FadeOut(
                lineA_C_,
                linePC_,
                labelH,
                BE,
                rtAngleC_,
                parallelMarks2,
                labelE,
                rtAngleE,
                labelB_,
                arrow,
                labelP,
                *hglLine,
            )
        )

        self.play(Create(npCircle))

        self.play(distx.animate.set_value(2.5), run_time=2)

        radiusNp = always_redraw(
            lambda: Arrow(
                npCircle.get_center(),
                npCircle.get_center() + npCircle.get_radius() * LEFT,
                color=RED_N100,
                buff=0,
            )
        )

        self.play(GrowArrow(radiusNp))
        self.wait(2)
        self.play(FadeOut(radiusNp))

        self.wait(5)


class Take7(Scene):
    def construct(self):
        O = ORIGIN + 2.25 * DOWN

        distx = ValueTracker(2.5)
        disty = ValueTracker(5)

        getA = lambda: O + disty.get_value() * UP + distx.get_value() * RIGHT

        B = O + LEFT * 4
        C = O + RIGHT * 4

        triangle = always_redraw(
            lambda: Polygon(
                getA(),
                B,
                C,
                stroke_color=GREY_N500,
                stroke_width=6,
                sheen_direction=LEFT,
            )
        )

        getD = lambda: Line(B, C).get_projection(getA())
        getE = lambda: Line(getA(), C).get_projection(B)
        getF = lambda: Line(getA(), B).get_projection(C)

        AD = always_redraw(lambda: Line(getA(), getD(), color=GREY_N200))

        getH = lambda: line_intersection([getA(), getD()], [B, getE()])

        getP = lambda: (getA() + getH()) / 2
        getQ = lambda: (B + getH()) / 2
        getR = lambda: (C + getH()) / 2

        getA_ = lambda: (B + C) / 2
        getB_ = lambda: (getA() + C) / 2
        getC_ = lambda: (B + getA()) / 2

        npCircle = always_redraw(
            lambda: Circle.from_three_points(
                getD(),
                getE(),
                getF(),
                stroke_color=[GREY_N200, GREY_N800],
                sheen_direction=UP + RIGHT,
            )
        )

        pointMarker = lambda point: Dot(point, color=GREY_N400, radius=0.05)

        pointA_ = always_redraw(lambda: pointMarker(getA_()))
        pointB_ = always_redraw(lambda: pointMarker(getB_()))
        pointC_ = always_redraw(lambda: pointMarker(getC_()))

        labelA = always_redraw(lambda: nMath("A").next_to(getA(), UP, buff=0.3))
        labelB = nMath("B").next_to(B, DOWN + LEFT, buff=0.3)
        labelC = nMath("C").next_to(C, DOWN + RIGHT, buff=0.3)

        labelA_ = always_redraw(lambda: nMath("A'").next_to(getA_(), DOWN, buff=0.3))
        labelB_ = always_redraw(
            lambda: nMath("B'").next_to(getB_(), RIGHT + 0.5 * UP, buff=0.2)
        )
        labelC_ = always_redraw(
            lambda: nMath("C'").next_to(getC_(), LEFT + 0.5 * UP, buff=0.2)
        )

        lineA_C_ = always_redraw(
            lambda: DashedLine(getA_(), getC_(), color=GREY_N200),
        )
        lineC_B_ = always_redraw(lambda: DashedLine(getC_(), getB_(), color=GREY_N200))

        def parallelMarks(lineA, lineB, color=NUMBRIK_COLOR_200):
            angle = lineA.get_angle()
            lineAMark = (
                ArrowTriangleFilledTip(start_angle=0, color=color)
                .move_to(lineA.get_center())
                .rotate(angle)
            )
            lineBMark = (
                ArrowTriangleFilledTip(start_angle=0, color=color)
                .move_to(lineB.get_center())
                .rotate(angle)
            )
            return VGroup(lineAMark, lineBMark)

        BE = always_redraw(lambda: Line(B, getE(), color=GREY_N200))
        CF = always_redraw(lambda: Line(C, getF(), color=GREY_N200))

        rtAngleD = always_redraw(
            lambda: getRightAngle(getA(), getD(), B, color=GREY_N200, length=0.3)
        )
        rtAngleF = always_redraw(
            lambda: getRightAngle(C, getF(), getA(), color=GREY_N200, length=0.3)
        )

        rtAngleE = always_redraw(
            lambda: getRightAngle(B, getE(), C, color=GREY_N200, length=0.3)
        )

        linePA_ = always_redraw(lambda: Line(getP(), getA_(), color=GREY_N200))
        linePC_ = always_redraw(lambda: DashedLine(getC_(), getP(), color=GREY_N200))

        circumcircle = Circle.from_three_points(getA(), B, C)
        circumcenter = circumcircle.get_center()

        perp1 = DashedLine(getA_(), circumcenter, color=GREY_N200)
        perp2 = DashedLine(getC_(), circumcenter, color=GREY_N200)

        rtAngleC_ = getRightAngle(
            circumcenter, getC_(), getA(), length=0.3, color=GREY_N200
        )
        rtAngleA_ = getRightAngle(B, getA_(), circumcenter, length=0.3, color=GREY_N200)

        chord1 = Line(getC_(), getF())
        chord2 = Line(getA_(), getD())

        perp3 = DashedLine(chord1.get_center(), npCircle.get_center(), color=GREY_N200)
        perp4 = DashedLine(chord2.get_center(), npCircle.get_center(), color=GREY_N200)

        rtAngle3 = getRightAngle(
            npCircle.get_center(),
            chord1.get_center(),
            getA(),
            length=0.3,
            color=GREY_N200,
        )
        rtAngle4 = getRightAngle(
            npCircle.get_center(), chord2.get_center(), B, length=0.3, color=GREY_N200
        )

        centerLine = Line(circumcenter, getH(), color=GREY_N200)

        circumRadius = Line(circumcenter, getA(), color=GREY_N200)
        npRadius = Line(npCircle.get_center(), getP(), color=GREY_N200)

        region = getRegion(
            getA(),
            getH(),
            circumcenter,
            gradient_color=[WHITE, YELLOW_N50],
            sheen_direction=UP + RIGHT,
        )

        labelD = always_redraw(lambda: nMath("D").next_to(getD(), DOWN, buff=0.34))

        labelF = always_redraw(
            lambda: nMath("F").next_to(getF(), LEFT + 0.5 * UP, buff=0.2)
        )

        labelH = nMath("H").next_to(getH(), RIGHT, buff=0.25).shift(UP * 0.2)

        labelP = nMath("P").next_to(getP(), RIGHT + UP, buff=1.2)

        labelO = nMath("O").next_to(circumcenter, LEFT, buff=0.25).shift(DOWN * 0.2)

        N = (circumcenter + getH()) / 2

        labelN = nMath("N").next_to(N, DOWN, buff=0.1).shift(RIGHT * 0.3)

        arrow = (
            Arrow(
                labelP.get_left() + 0.1 * DOWN + 0.1 * LEFT,
                getP(),
                buff=0.2,
                stroke_width=10,
                tip_length=0.5,
            )
            .set_color_by_gradient([RED_N50])
            .set_sheen_direction(RIGHT + 0.5 * UP)
        )

        arrow2 = (
            Arrow(
                labelN.get_bottom() + DOWN * 1.7,
                labelN.get_bottom(),
                buff=0.2,
                stroke_width=10,
                tip_length=0.5,
            )
            .set_color_by_gradient([RED_N50])
            .set_sheen_direction(RIGHT + 0.5 * UP)
        )

        def highlightLines(points):
            """
            Given a list of (pt1, pt2) tuples, returns a list of highlighted Lines.
            """
            return [Line(pt1, pt2, color=YELLOW, stroke_width=5) for pt1, pt2 in points]

        self.add(
            triangle,
            npCircle,
            AD,
            pointA_,
            labelA_,
            pointB_,
            pointC_,
            labelC_,
            labelA,
            labelB,
            labelC,
            labelD,
            rtAngleD,
            # CF,
            # rtAngleD,
            # rtAngleF,
            # perp1,
            # perp2,
            # rtAngleC_,
            # rtAngleA_,
            # perp3,
            # perp4,
            # rtAngle3,
            # rtAngle4,
            # centerLine,
            # circumRadius,
            # npRadius,
            # region,
        )

        self.wait(2)
        # self.play(LaggedStart(Create(CF), Create(rtAngleF)))
        # self.wait(1)

        hgl = highlightLines([(getA(), B), (B, C)])

        circumcircle = Circle.from_three_points(getA(), B, C, stroke_color=GREY_A)

        self.play(Create(circumcircle))
        self.play(FadeIn(*hgl))
        self.play(
            LaggedStart(
                Create(perp1),
                Create(rtAngleA_),
                Create(perp2),
                Create(rtAngleC_),
                FadeIn(labelO),
                lag_ratio=0.5,
            )
        )
        self.play(FadeOut(*hgl, circumcircle))

        self.wait(1)

        hgl = highlightLines([(getA_(), getD()), (getC_(), getF())])

        self.play(FadeIn(labelF, *hgl))
        self.play(
            LaggedStart(
                Create(perp3),
                Create(rtAngle3),
                Create(perp4),
                Create(rtAngle4),
                FadeIn(labelN),
                lag_ratio=0.5,
            )
        )
        self.play(FadeOut(*hgl))
        self.play(
            LaggedStart(Create(CF), Create(rtAngleF), FadeIn(labelH), lag_ratio=0.5)
        )
        self.wait(1)
        self.play(Create(centerLine))
        self.wait(1)
        self.play(FadeIn(circumRadius, region))
        self.wait(1)

        self.play(GrowArrow(arrow2))
        solidHighlight(self, labelN, buff=0.15, wait_time=1)
        self.play(GrowArrow(arrow))
        self.play(FadeIn(labelP))
        self.play(Create(npRadius))

        # self.play(FadeOut(CF, rtAngleF))
        # self.wait(1)
        # self.play(Create(linePA_))
        # self.wait(1)
        # self.play(Create(lineA_C_))
        # self.play(Create(linePC_))
        # self.play(Create(rtAngleC_))
        # self.wait(1)
        # self.play(FadeOut(linePA_), Uncreate(npCircle))
        # self.wait(1)

        # parallelMarks1 = parallelMarks(lineA_C_, Line(C, getB_()))
        # self.play(FadeIn(parallelMarks1))
        # self.wait(1)

        # parallelMarks2 = parallelMarks(
        #     linePC_, Line(BE.get_center(), getH()), color=GREEN_N200
        # )
        # self.play(FadeIn(parallelMarks2))
        # self.wait(1)

        # region1 = getTriangularRegion(B, getH(), getA(), color=YELLOW_N50)

        # self.play(FadeOut(parallelMarks1), FadeIn(region1))

        self.wait(5)


class Statements1(Scene):
    def construct(self):
        stmt1 = nMath(
            "\\angle B'C'A'",
            "=",
            "\\angle B'CD",
        )
        stmt2 = nMath("\\angle B'C'A'", "=", "\\angle B'CD", "=", "\\angle B'DC")
        self.play(fadeInTex(stmt1))
        self.wait(2)
        self.play(TransformMatchingTex(stmt1, stmt2), run_time=2)
        self.wait(2)

        stmt3 = nMath("\\angle B'DA'", "+", "\\angle B'C'A'", "=", "180^\\circ")

        self.play(
            LaggedStart(
                FadeOut(stmt2, shift=UP * 0.75), fadeInTex(stmt3), lag_ratio=0.5
            )
        )
        self.wait(2)

        stmt4 = nMath(
            "\\angle B'DA'",
            "=",
            "\\angle B'C'A'",
        )

        self.play(TransformMatchingTex(stmt3, stmt4), run_time=2)

        clearScreen(self, 1)


class Statements2(Scene):
    def construct(self):
        stmt1 = nMath(
            "A'C'",
            "\\parallel",
            "AC",
        )
        stmt2 = nMath(
            "A'C'", "\\parallel", "AC", "\\Rightarrow", "BE", "\\perp", "A'C',AC"
        )

        stmt3 = nMath("\\Rightarrow BE", "\\parallel", "C'P")

        stmt4 = nMath("\\text{P is the mid point of AH}")

        self.play(fadeInTex(stmt1))
        self.wait(2)
        self.play(TransformMatchingTex(stmt1, stmt2), run_time=2)
        self.wait(2)
        self.play(TransformMatchingTex(stmt2, stmt3))
        self.wait(2)

        self.play(FadeOut(stmt3))
        self.wait(2)
        self.play(fadeInTex(stmt4))

        clearScreen(self, 1)


class Statements3(Scene):
    def construct(self):
        stmt1 = nMath("OA", "=", "2", "\\cdot", "NP")
        stmt2 = nMath("NP", "=", "\\frac{OA}{2}")

        stmt3 = nMath("R_{nine\\,point}", "=", "\\frac{R}{2}")

        self.play(fadeInTex(stmt1))
        self.wait(2)
        self.play(TransformMatchingTex(stmt1, stmt2), run_time=2)
        self.wait(2)
        self.play(
            Transform(stmt2[0], stmt3[0]),
            Transform(stmt2[1], stmt3[1]),
            Transform(stmt2[2], stmt3[2]),
            run_time=2,
        )

        clearScreen(self, 1)


class StatementIntro(Scene):
    def construct(self):
        stmt1 = nMath(
            "\\text{Prove that all 6 points lie on the same circle!}", color=GREY_N500
        ).shift(UP * 0.75)
        stmt2 = nMath(
            "\\text{Where are the other 3 of 9 points?}", color=GREY_N500
        ).shift(DOWN * 0.5)

        self.play(fadeInTex(stmt1))
        self.wait(2)
        self.play(fadeInTex(stmt2))
        self.wait(3)


class TakeIntro2(Scene):
    def construct(self):
        radius = 2
        circle1 = (
            Circle(
                radius=radius,
                fill_opacity=0.7,
                sheen_direction=RIGHT,
            )
            .set_color_by_gradient([WHITE, GREEN_N100])
            .set_stroke(
                color=[GREY_N400, GREY_N800],
                width=6,
            )
        )
        circle2 = (
            circle1.copy()
            .set_color_by_gradient([WHITE, NUMBRIK_COLOR])
            .set_stroke(
                color=[GREY_N400, GREY_N800],
                width=6,
            )
        )

        circle1.shift(3 * LEFT)
        circle2.shift(3 * RIGHT)

        tangent = DashedLine(
            2.5 * UP,
            2.5 * DOWN,
            color=RED_N50,
            stroke_width=6,
        )

        poi = Dot(ORIGIN, 0.1, color=BLACK)

        self.play(Create(circle1), Create(circle2), run_time=2)
        self.wait(1)
        self.play(circle1.animate.shift(RIGHT), circle2.animate.shift(LEFT))
        self.play(Create(tangent))
        self.play(FadeIn(poi))

        self.wait(1)

        self.play(FadeOut(poi))
        l = 0.6
        self.play(circle1.animate.shift(l * RIGHT), circle2.animate.shift(l * LEFT))

        poi1 = Dot(UP * np.sqrt(radius**2 - (radius - l) ** 2), color=BLACK, radius=0.1)
        poi2 = Dot(
            DOWN * np.sqrt(radius**2 - (radius - l) ** 2), color=BLACK, radius=0.1
        )
        self.play(FadeIn(poi1, poi2))
        self.wait(2)

        pt1 = Dot(UP * radius, color=BLACK, radius=0.1)
        pt2 = Dot((DOWN + RIGHT) * radius / np.sqrt(2), color=BLACK, radius=0.1)
        pt3 = Dot((DOWN + LEFT) * radius / np.sqrt(2), color=BLACK, radius=0.1)
        self.play(Transform(poi1, pt1), Transform(poi2, VGroup(pt2, pt3)))

        self.wait(2)

        self.play(circle2.animate.move_to(ORIGIN), circle1.animate.move_to(ORIGIN))
        self.wait(2)
        self.play(FadeOut(circle1, circle2, tangent, poi1, poi2))


class ReTake5(Scene):
    def construct(self):
        O = ORIGIN + 2.25 * DOWN

        distx = ValueTracker(1.2)
        disty = ValueTracker(5)

        getA = lambda: O + disty.get_value() * UP + distx.get_value() * RIGHT

        B = O + LEFT * 4
        C = O + RIGHT * 4

        triangle = always_redraw(
            lambda: Polygon(
                getA(),
                B,
                C,
                stroke_color=GREY_N500,
                stroke_width=6,
                sheen_direction=LEFT,
            )
        )

        self.add(triangle)

        getD = lambda: Line(B, C).get_projection(getA())
        getE = lambda: Line(getA(), C).get_projection(B)
        getF = lambda: Line(getA(), B).get_projection(C)

        AD = always_redraw(lambda: Line(getA(), getD(), color=GREY_N200))

        getH = lambda: line_intersection([getA(), getF()], [B, getF()])

        getP = lambda: (getA() + getH()) / 2
        getQ = lambda: (B + getH()) / 2
        getR = lambda: (C + getH()) / 2

        getA_ = lambda: (B + C) / 2
        getB_ = lambda: (getA() + C) / 2
        getC_ = lambda: (B + getA()) / 2

        npCircle = always_redraw(
            lambda: Circle.from_three_points(
                getD(),
                getE(),
                getF(),
                stroke_color=[GREY_N200, GREY_N800],
                sheen_direction=UP + RIGHT,
            )
        )

        pointMarker = lambda point: Dot(point, color=GREY_N400, radius=0.05)

        labelA = always_redraw(lambda: nMath("A").next_to(getA(), UP, buff=0.3))
        labelB = nMath("B").next_to(B, DOWN + LEFT, buff=0.3)
        labelC = nMath("C").next_to(C, DOWN + RIGHT, buff=0.3)

        self.play(Create(triangle))
        self.play(FadeIn(labelA, labelB, labelC, scale=1.1))
        self.wait(1)

        pointA_ = always_redraw(lambda: pointMarker(getA_()))
        pointB_ = always_redraw(lambda: pointMarker(getB_()))
        pointC_ = always_redraw(lambda: pointMarker(getC_()))

        labelA_ = always_redraw(lambda: nMath("A'").next_to(getA_(), DOWN, buff=0.3))
        labelB_ = always_redraw(
            lambda: nMath("B'").next_to(getB_(), RIGHT + 0.5 * UP, buff=0.2)
        )
        labelC_ = always_redraw(
            lambda: nMath("C'").next_to(getC_(), LEFT + 0.5 * UP, buff=0.2)
        )

        createMidPointMarks = lambda line: always_redraw(
            lambda: VGroup(
                createLineMarks(
                    Line(line.get_start(), line.get_center()), themeColor=NUMBRIK_COLOR
                ),
                createLineMarks(
                    Line(line.get_center(), line.get_end()), themeColor=NUMBRIK_COLOR
                ),
            )
        )

        midPointMarksA = createMidPointMarks(Line(B, C))
        midPointMarksB = createMidPointMarks(Line(getA(), C))
        midPointMarksC = createMidPointMarks(Line(getA(), B))

        self.play(
            LaggedStart(
                AnimationGroup(
                    Create(pointA_),
                    FadeIn(
                        labelA_,
                    ),
                ),
                FadeIn(midPointMarksA),
                AnimationGroup(
                    Create(pointB_),
                    FadeIn(
                        labelB_,
                    ),
                ),
                FadeIn(midPointMarksB),
                AnimationGroup(
                    Create(pointC_),
                    FadeIn(
                        labelC_,
                    ),
                ),
                FadeIn(midPointMarksC),
                lag_ratio=0.5,
            )
        )

        self.wait(1)
        self.play(FadeOut(midPointMarksA, midPointMarksB, midPointMarksC))
        self.wait(1)

        lineA_C_ = always_redraw(
            lambda: DashedLine(getA_(), getC_(), color=GREY_N200),
        )

        lineC_B_ = always_redraw(lambda: DashedLine(getC_(), getB_(), color=GREY_N200))

        self.play(Create(lineA_C_))
        self.play(Create(lineC_B_))

        parallelgm = getRegion(
            getA_(),
            C,
            getB_(),
            getC_(),
            gradient_color=[WHITE, GREEN_N100],
            sheen_direction=RIGHT,
        )

        self.play(FadeIn(parallelgm))
        self.wait(1)

        # def parallelMarks(lineA, lineB, color=NUMBRIK_COLOR_200):
        #     angle = lineA.get_angle()
        #     lineAMark = (
        #         ArrowTriangleFilledTip(start_angle=0, color=color)
        #         .move_to(lineA.get_center())
        #         .rotate(angle)
        #     )
        #     lineBMark = (
        #         ArrowTriangleFilledTip(start_angle=angle, color=color)
        #         .move_to(lineB.get_center())
        #         .rotate(angle)
        #     )
        #     return VGroup(lineAMark, lineBMark)

        # parallelMarks1 = always_redraw(
        #     lambda: parallelMarks(Line(getA_(), getC_()), Line(getB_(), C))
        # )

        # parallelMarks2 = always_redraw(
        #     lambda: parallelMarks(
        #         Line(getC_(), getB_()),
        #         Line(getA_(), C),
        #         color=GREEN_N200,
        #     )
        # )

        # self.play(Create(parallelMarks1), Create(parallelMarks2))
        # self.wait(1)
        # self.play(FadeOut(parallelMarks1, parallelMarks2))
        # self.wait(1)

        angleMarker1 = always_redraw(
            lambda: getAngle(C, getD(), getB_(), color=GREY_N200, radius=0.5)
        )
        angleMarker1_adj = always_redraw(
            lambda: VGroup(
                getAngle(getB_(), getD(), B, color=GREY_N200, radius=0.6),
                getAngle(getB_(), getD(), B, color=GREY_N200, radius=0.7),
            )
        )
        angleMarker2 = always_redraw(
            lambda: getAngle(getB_(), C, getD(), color=GREY_N200, radius=0.5)
        )

        angleMarker3 = always_redraw(
            lambda: getAngle(getA_(), getC_(), getB_(), color=GREY_N200, radius=0.5)
        )

        self.play(
            LaggedStart(Create(angleMarker2), Create(angleMarker3), lag_ratio=0.5)
        )
        self.wait(1)
        self.play(FadeOut(parallelgm))
        self.wait(1)

        rtAngleD = always_redraw(
            lambda: getRightAngle(getA(), getD(), B, color=GREY_N200, length=0.3)
        )

        labelD = always_redraw(lambda: nMath("D").next_to(getD(), DOWN, buff=0.34))

        self.play(
            LaggedStart(Create(AD), Create(rtAngleD), FadeIn(labelD), lag_ratio=0.4)
        )
        self.wait(1)

        triADC = getRegion(
            getA(),
            getD(),
            C,
            gradient_color=[YELLOW_N40, WHITE],
            sheen_direction=RIGHT,
        )

        self.play(FadeIn(triADC))
        self.wait(1)

        lineDB_ = always_redraw(lambda: Line(getD(), getB_(), color=GREY_N200))

        self.play(Create(lineDB_))
        self.wait(1)

        eqMarker1 = always_redraw(
            lambda: createLineMarks(Line(getB_(), getA()), themeColor=NUMBRIK_COLOR)
        )
        eqMarker2 = always_redraw(
            lambda: createLineMarks(Line(getB_(), C), themeColor=NUMBRIK_COLOR)
        )
        eqMarker3 = always_redraw(
            lambda: createLineMarks(Line(getD(), getB_()), themeColor=NUMBRIK_COLOR)
        )

        self.play(
            LaggedStart(
                FadeIn(eqMarker1), FadeIn(eqMarker2), FadeIn(eqMarker3), lag_ratio=0.4
            )
        )
        self.wait(1)

        self.play(FadeOut(triADC))
        self.wait(1)

        triDB_C = getRegion(
            getB_(),
            getD(),
            C,
            gradient_color=[WHITE, GREEN_N100],
            sheen_direction=RIGHT,
        )
        self.play(FadeIn(triDB_C))
        self.wait(1)

        # self.play(FadeOut(eqMarker1, eqMarker2, eqMarker3, rtAngleD))
        # self.wait(1)
        self.play(Create(angleMarker1))
        self.wait(1)

        self.play(
            FadeOut(
                triDB_C,
                eqMarker1,
                eqMarker2,
                eqMarker3,
            )
        )
        self.wait(1)

        self.play(Create(npCircle))
        self.wait(1)

        self.play(Create(angleMarker1_adj), FadeOut(rtAngleD))

        solidHighlight(self, [angleMarker3, angleMarker1_adj], buff=0.1, wait_time=1)

        self.play(FadeOut(angleMarker1_adj), FadeIn(rtAngleD))
        self.wait(1)

        self.play(distx.animate.set_value(-1.5), run_time=2.5)
        self.wait(1)

        lineA_B_ = always_redraw(lambda: DashedLine(getA_(), getB_(), color=RED_N100))

        hgl = solidHighlight(
            self, [angleMarker3, angleMarker1], buff=0.1, wait_time=1, unhighlight=False
        )

        self.play(Create(lineA_B_))
        self.wait(1)

        self.play(FadeOut(*hgl, lineA_B_))
        self.wait(2)

        self.play(Uncreate(npCircle))
        self.play(
            FadeOut(
                lineC_B_,
                lineDB_,
                angleMarker3,
                angleMarker1,
                angleMarker2,
            )
        )

        # Other two altitudes

        lineA_B_ = always_redraw(lambda: DashedLine(getA_(), getB_(), color=GREY_N200))

        labelE = always_redraw(
            lambda: nMath("E").next_to(getE(), RIGHT + 0.5 * UP, buff=0.2)
        )

        BE = always_redraw(lambda: Line(B, getE(), color=GREY_N200))

        rtAngleE = always_redraw(
            lambda: getRightAngle(B, getE(), C, color=GREY_N200, length=0.3)
        )

        lineEC_ = Line(getC_(), getE(), color=GREY_N200)

        angleMarker1 = getAngle(getA(), getE(), getC_(), color=GREY_N200)
        angleMarker3 = getAngle(getB_(), getA_(), getC_(), color=GREY_N200)

        rtAngleF = always_redraw(
            lambda: getRightAngle(C, getF(), getA(), color=GREY_N200, length=0.3)
        )

        CF = always_redraw(lambda: Line(C, getF(), color=GREY_N200))

        labelF = always_redraw(
            lambda: nMath("F").next_to(getF(), LEFT + 0.5 * UP, buff=0.2)
        )

        self.play(
            LaggedStart(
                Create(lineA_B_),
                Create(BE),
                FadeIn(labelE),
                Create(rtAngleE),
                Create(lineEC_),
                Create(angleMarker1),
                Create(angleMarker3),
                Create(lineC_B_),
                Create(CF),
                FadeIn(labelF),
                Create(rtAngleF),
                lag_ratio=0.5,
            )
        )

        # self.play(
        #     LaggedStart( lag_ratio=0.5)
        # )
        # self.wait(1)

        # self.play(Create(npCircle))
        # self.wait(1)

        # self.play(Uncreate(npCircle))
        # self.play(FadeOut(lineEC_, rtAngleE, angleMarker1, angleMarker3, BE, lineA_C_))

        # self.play(
        #     LaggedStart(

        #         lag_ratio=0.5,
        #     )
        # )
        # self.wait(1)

        self.play(Create(npCircle))
        self.wait(1)

        self.play(
            FadeOut(
                lineA_B_,
                lineC_B_,
                lineEC_,
                angleMarker1,
                angleMarker3,
                lineA_C_,
            )
        )
        # self.play(
        #     LaggedStart(
        #         Create(AD),
        #         Create(rtAngleD),
        #         Create(BE),
        #         Create(rtAngleE),
        #         lag_ratio=0.5,
        #     )
        # )
        # self.wait(2)

        self.play(distx.animate.set_value(1.2), run_time=3)

        self.wait(5)


class Thumbnail(Scene):
    def construct(self):
        addBackground(self)
        O = ORIGIN + 2.25 * DOWN + 2 * RIGHT

        distx = ValueTracker(1.2)
        disty = ValueTracker(5)

        getA = lambda: O + disty.get_value() * UP + distx.get_value() * RIGHT

        B = O + LEFT * 4
        C = O + RIGHT * 4

        triangle = always_redraw(
            lambda: Polygon(
                getA(),
                B,
                C,
                stroke_color=[GREY_N400, GREY_N800],
                stroke_width=8,
                sheen_direction=UP + RIGHT,
            )
        )

        getD = lambda: Line(B, C).get_projection(getA())
        getE = lambda: Line(getA(), C).get_projection(B)
        getF = lambda: Line(getA(), B).get_projection(C)

        AD = always_redraw(lambda: Line(getA(), getD(), color=GREY_N400))

        getH = lambda: line_intersection([getA(), getD()], [B, getE()])

        getP = lambda: (getA() + getH()) / 2
        getQ = lambda: (B + getH()) / 2
        getR = lambda: (C + getH()) / 2

        getA_ = lambda: (B + C) / 2
        getB_ = lambda: (getA() + C) / 2
        getC_ = lambda: (B + getA()) / 2

        npCircle = always_redraw(
            lambda: Circle.from_three_points(
                getD(),
                getE(),
                getF(),
                stroke_color=[GREY_N200, GREY_N800],
                sheen_direction=UP + RIGHT,
                fill_opacity=1,
            )
            .set_color_by_gradient([PURPLE_A, NUMBRIK_COLOR_50])
            .set_stroke(GREY_N400)
        )

        pointMarker = lambda point: Dot(point, color=GREY_N500, radius=0.05)

        pointA_ = always_redraw(lambda: pointMarker(getA_()))
        pointB_ = always_redraw(lambda: pointMarker(getB_()))
        pointC_ = always_redraw(lambda: pointMarker(getC_()))

        labelA = always_redraw(lambda: nMath("A").next_to(getA(), UP, buff=0.3))
        labelB = nMath("B").next_to(B, DOWN + LEFT, buff=0.3)
        labelC = nMath("C").next_to(C, DOWN + RIGHT, buff=0.3)

        labelA_ = always_redraw(lambda: nMath("A'").next_to(getA_(), DOWN, buff=0.3))
        labelB_ = always_redraw(
            lambda: nMath("B'").next_to(getB_(), RIGHT + 0.5 * UP, buff=0.2)
        )
        labelC_ = always_redraw(
            lambda: nMath("C'").next_to(getC_(), LEFT + 0.5 * UP, buff=0.2)
        )
        lineA_C_ = always_redraw(
            lambda: DashedLine(getA_(), getC_(), color=GREY_N200),
        )
        lineC_B_ = always_redraw(lambda: DashedLine(getC_(), getB_(), color=GREY_N200))

        def parallelMarks(lineA, lineB, color=NUMBRIK_COLOR_200):
            angle = lineA.get_angle()
            lineAMark = (
                ArrowTriangleFilledTip(start_angle=0, color=color)
                .move_to(lineA.get_center())
                .rotate(angle)
            )
            lineBMark = (
                ArrowTriangleFilledTip(start_angle=0, color=color)
                .move_to(lineB.get_center())
                .rotate(angle)
            )
            return VGroup(lineAMark, lineBMark)

        BE = always_redraw(lambda: Line(B, getE(), color=GREY_N400))
        CF = always_redraw(lambda: Line(C, getF(), color=GREY_N400))

        rtAngleD = always_redraw(
            lambda: getRightAngle(getA(), getD(), B, color=GREY_N400, length=0.3)
        )
        rtAngleF = always_redraw(
            lambda: getRightAngle(C, getF(), getA(), color=GREY_N400, length=0.3)
        )

        rtAngleE = always_redraw(
            lambda: getRightAngle(B, getE(), C, color=GREY_N400, length=0.3)
        )

        linePA_ = always_redraw(lambda: Line(getP(), getA_(), color=GREY_N200))
        linePC_ = always_redraw(lambda: DashedLine(getC_(), getP(), color=GREY_N200))

        rtAngleC_ = always_redraw(
            lambda: getRightAngle(getA_(), getC_(), getP(), length=0.3, color=GREY_N200)
        )

        labelD = always_redraw(lambda: nMath("D").next_to(getD(), DOWN, buff=0.34))

        labelF = always_redraw(
            lambda: nMath("F").next_to(getF(), LEFT + 0.5 * UP, buff=0.2)
        )

        labelE = always_redraw(
            lambda: nMath("E").next_to(getE(), RIGHT + 0.5 * UP, buff=0.2)
        )

        labelH = nMath("H").next_to(getH(), DOWN + RIGHT, buff=0.2)

        self.add(
            npCircle,
            triangle,
            AD,
            BE,
            CF,
            pointA_,
            pointB_,
            pointC_,
            rtAngleD,
            rtAngleE,
            rtAngleF,
        )

        self.add(
            Arrow(getA_() + 1.5 * DOWN + 0.5 * LEFT, getA_(), color=RED_N),
            Arrow(getB_() + 1.5 * RIGHT, getB_(), color=RED_N),
            Arrow(
                getC_() + +1.5 * LEFT,
                getC_(),
                color=RED_N,
            ),
            Arrow(
                getE() + 1.5 * (RIGHT + UP) / np.sqrt(2),
                getE(),
                color=RED_N,
            ),
            Arrow(
                getF() + 1.5 * (LEFT + UP) / np.sqrt(2),
                getF(),
                color=RED_N,
            ),
            Arrow(
                getD() + +1.5 * DOWN + 0.5 * RIGHT,
                getD(),
                color=RED_N,
            ),
        )
        self.wait(2)
