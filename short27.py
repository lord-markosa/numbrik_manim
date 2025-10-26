from manim import *
from utils import *
import numpy as np


class PentagonWithDiagonals(Scene):
    def construct(self):
        addBackground(self)

        stroke_color = GREY_N800
        # Create a regular pentagon
        pentagon = RegularPolygon(n=5, color=stroke_color, radius=3.2)

        # Get vertices of the pentagon
        E, A, B, C, D = pentagon.get_vertices()

        diagonal1 = Line(A, D, color=stroke_color)

        sideLength = lengthMarkerV2(B, C, "1", shift=0.4 * DOWN)

        diagonal1Length = lengthMarkerV2(A, D, "?", buff=0.2, shift=0.45 * DOWN)

        # self.add(diagonal1Length, sideLength)
        self.add(diagonal1, pentagon, sideLength, diagonal1Length)

        perp1 = DashedLine(E, diagonal1.get_center(), color=stroke_color)
        perpAngle = RightAngle(
            Line(perp1.get_end(), E),
            Line(diagonal1.get_center(), A),
            color=stroke_color,
        )
        self.wait(2)

        halfAngle = Angle(Line(E, A), perp1, color=stroke_color, radius=0.7)
        halfAngleLabel = (
            nMath("54^\\circ").next_to(halfAngle, DOWN, buff=0.2).shift(LEFT * 0.2)
        )

        self.play(
            LaggedStart(
                Create(perp1),
                Create(perpAngle),
                Create(halfAngle),
                FadeIn(halfAngleLabel),
                lag_ratio=0.6,
            )
        )

        temp_diagLabel = lengthMarkerV2(
            A, D, "2\\sin{54^\\circ}", buff=0.3, shift=0.45 * DOWN
        )

        self.play(Transform(diagonal1Length, temp_diagLabel))

        self.wait(4)
        self.play(
            FadeOut(
                diagonal1Length, perp1, perpAngle, halfAngle, halfAngleLabel, sideLength
            )
        )

        def getDiagonal(A, B):
            return DashedLine(A, B, color=stroke_color)

        diagonal2 = getDiagonal(A, C)
        diagonal3 = getDiagonal(B, D)

        # self.add(diagonal2, diagonal3)

        circumcircle = Circle(3.2, color=GREY_N100, z_index=-10)
        # self.add(circumcircle)
        self.play(Create(circumcircle), Create(diagonal2), Create(diagonal3))

        def getHighlighter(A, B):
            return Line(A, B, color=YELLOW, stroke_width=6)

        BD = getHighlighter(B, D)
        AC = getHighlighter(A, C)
        AB = getHighlighter(A, B)
        CD = getHighlighter(C, D)
        BC = getHighlighter(C, B)
        AD = getHighlighter(A, D)

        label_BD = nMath("x").next_to((BD.get_center() + D) / 2, LEFT, buff=0.5)
        label_AC = nMath("x").next_to((AC.get_center() + A) / 2, RIGHT, buff=0.5)
        label_AB = nMath("1").next_to(AB.get_center(), LEFT)
        label_CD = nMath("1").next_to(CD.get_center(), RIGHT)
        label_BC = nMath("1").next_to(BC.get_center(), DOWN, buff=0.1)
        label_AD = nMath("x").next_to(AD.get_center(), UP, buff=0.2)

        self.play(
            FadeIn(
                label_BD,
                label_AC,
                label_AB,
                label_CD,
                label_BC,
                label_AD,
            )
        )
        self.wait(2)

        self.play(LaggedStart(FadeIn(AC), FadeIn(BD), lag_ratio=0.7))
        self.play(FadeOut(BD, AC))
        self.wait(0.25)

        self.play(LaggedStart(FadeIn(AB), FadeIn(CD), lag_ratio=0.6))
        self.play(FadeOut(AB, CD))
        self.wait(0.25)

        self.play(LaggedStart(FadeIn(AD), FadeIn(BC), lag_ratio=0.6))
        self.play(FadeOut(BC, AD))

        self.wait(10)


class Ptolemy(Scene):
    def construct(self):
        addBackground(self)

        stroke_color = GREY_N800
        r = 3
        circle = Circle(3, color=stroke_color)

        def getPointsOnCircum(ang):
            return r * (np.sin(ang) * UP + np.cos(ang) * RIGHT)

        A = getPointsOnCircum(PI / 4)
        B = getPointsOnCircum(3 * PI / 4)
        C = getPointsOnCircum(PI + PI / 6)
        D = getPointsOnCircum(2 * PI - PI / 6)

        cyclicQuad = Polygon(A, B, C, D, color=stroke_color)

        labelA = nMath("D").next_to(A, RIGHT + UP, buff=0.2)
        labelB = nMath("A").next_to(B, LEFT + UP, buff=0.2)
        labelC = nMath("B").next_to(C, LEFT + DOWN, buff=0.2)
        labelD = nMath("C").next_to(D, RIGHT + DOWN, buff=0.2)

        # self.add(labelA, labelB, labelC, labelD)

        diag1 = DashedLine(A, C, color=stroke_color)
        diag2 = DashedLine(B, D, color=stroke_color)

        # self.add(circle, diag1, diag2)
        # self.add(cyclicQuad)

        self.play(
            LaggedStart(
                Create(cyclicQuad),
                Create(circle),
                AnimationGroup(
                    Create(diag1),
                    Create(diag2),
                ),
                FadeIn(labelA, labelB, labelC, labelD),
                lag_ratio=0.4,
            )
        )
        self.wait(1)

        def getHighlighter(A, B):
            return Line(A, B, color=YELLOW, stroke_width=7)

        BD = getHighlighter(B, D)
        AC = getHighlighter(A, C)
        AB = getHighlighter(A, B)
        CD = getHighlighter(C, D)
        BC = getHighlighter(C, B)
        AD = getHighlighter(A, D)

        self.play(LaggedStart(FadeIn(BD), FadeIn(AC), lag_ratio=0.7))
        self.play(FadeOut(BD, AC))
        self.wait(0.25)

        self.play(LaggedStart(FadeIn(AB), FadeIn(CD), lag_ratio=0.6))
        self.play(FadeOut(AB, CD))
        self.wait(0.25)

        self.play(LaggedStart(FadeIn(BC), FadeIn(AD), lag_ratio=0.6))
        self.play(FadeOut(BC, AD))

        self.wait(4)


class Statements(Scene):
    def construct(self):
        addBackground(self)

        eq1 = nMath(
            "AC",
            "\\cdot",
            "BD",
            "=",
            "AD",
            "\\cdot",
            "BC",
            "\\;+\\;",
            "AB",
            "\\cdot",
            "CD",
        ).to_edge(UP)

        def writeEq(eq):
            self.play(
                LaggedStart(FadeIn(eq[0]), FadeIn(eq[1]), FadeIn(eq[2]), lag_ratio=0.7)
            )
            self.wait(0.25)

            self.play(
                LaggedStart(
                    FadeIn(eq[3]),
                    FadeIn(eq[4]),
                    FadeIn(eq[5]),
                    FadeIn(eq[6]),
                    lag_ratio=0.6,
                )
            )
            self.wait(0.25)

            self.play(
                LaggedStart(
                    FadeIn(eq[7]),
                    FadeIn(eq[8]),
                    FadeIn(eq[9]),
                    FadeIn(eq[10]),
                    lag_ratio=0.6,
                )
            )

        writeEq(eq1)
        self.wait(1)
        self.play(FadeOut(eq1))

        eq2 = nMath(
            "x",
            "\\cdot",
            "x",
            "=",
            "1",
            "\\cdot",
            "1",
            "\\;+\\;",
            "x",
            "\\cdot",
            "1",
        ).to_edge(UP)

        eq3 = nMath("x^2", "-", "x", "-", "1", "=", "0").next_to(eq2, 0, buff=0.5)

        eq4 = nMath("x", "=", "\\frac{1+\\sqrt{5}}{2}").next_to(eq3, DOWN, buff=0.6)

        eq5 = nMath('\\text{"Golden Ratio"}').next_to(eq4, DOWN, buff=0.6)

        hgl = solidHighlight(self, eq4, buff=0.2, corner_radius=0.2, animate=False)

        writeEq(eq2)
        self.wait(1)
        self.play(Transform(eq2, eq3))
        self.play(fadeInTex(eq4))
        self.play(FadeIn(*hgl))
        self.play(fadeInTex(eq5))

        self.wait(10)


class ProblemStatement(Scene):
    def construct(self):
        addBackground(self)
        question = (
            VGroup(
                MathTex(
                    "\\text{Given a unit regular pentagon}",
                    color=GREY_N800,
                ),
                MathTex(
                    "\\text{Find its diagonal length}",
                    color=GREY_N800,
                ),
            )
            .arrange(DOWN)
            .to_edge(UP)
        )

        self.add(question)
        self.wait(10)
