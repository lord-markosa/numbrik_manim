from manim import *
from utils import *
import numpy as np


class GeometryProof(Scene):
    def construct(self):
        # Fixed positions
        themeColor = GREY_N500
        side = 3

        D = ORIGIN + 2 * DOWN
        C = D + RIGHT * side
        B = D + LEFT * side

        angleC = 30 * DEGREES

        # Angle ACB = 30 degrees, length AC = 3 + 3√3
        length_AC = side + 2 * side * np.cos(angleC)  # AC = 3sqrt(3)

        # Find vector from C to A using polar coordinates
        A = C + length_AC * UP * np.sin(angleC) + length_AC * LEFT * np.cos(angleC)

        # Define points and labels
        points = {
            "A": A,
            "B": B,
            "C": C,
            "D": D,
        }

        labels = {
            name: nText(name).next_to(points[name], DOWN if name != "A" else UP)
            for name in points
        }

        # Draw triangle ABC
        triangle = Polygon(points["A"], points["B"], points["C"], color=themeColor)

        # Draw line AD
        AD = Line(A, D, color=themeColor)

        # Construct E such that DE = DC and E lies on AC
        EDB = 60 * DEGREES
        E = D + side * np.sin(EDB) * UP + side * np.cos(EDB) * LEFT
        labelE = nText("E").move_to(
            E + 0.4 * UP + 0.1 * RIGHT,
        )

        DE = Line(points["D"], E, color=themeColor)
        BE = Line(points["B"], E, color=themeColor)

        # 1. Problem Statement
        self.play(
            Create(triangle),
            FadeIn(labels["A"], shift=0.5 * DOWN),
            FadeIn(labels["B"], labels["C"], shift=0.5 * UP),
        )

        # Draw the angle ACB
        angleACB = Angle(Line(C, A), Line(C, B), radius=0.7, color=themeColor)
        labelACB = (
            nMath("30^\\circ")
            .move_to(C + 0.9 * np.sin(PI / 8) * UP + 1.3 * np.cos(PI / 12) * LEFT)
            .scale(0.8)
        )
        self.play(Create(angleACB), FadeIn(labelACB, shift=0.5 * RIGHT))
        self.wait(1)

        # 2. Draw AD
        self.play(Create(AD), FadeIn(labels["D"]))

        DC = Line(D, C, color=themeColor)
        DB = Line(D, B, color=themeColor)
        BC = Line(B, C, color=themeColor)

        DC_marks = createLineMarks(DC).shift(0.5 * LEFT)
        DB_marks = createLineMarks(DB).shift(0.2 * LEFT)

        self.play(BC.animate.set_color(YELLOW), rate_func=smooth)
        self.play(BC.animate.set_opacity(0), rate_func=smooth)
        self.play(Create(DC_marks), Create(DB_marks))
        self.wait(1)

        # 3. Draw the angle ADB
        angleADB = Angle(Line(D, A), Line(D, B), radius=0.5, color=themeColor)
        labelADB = (
            nMath("45^\\circ")
            .move_to(D + 0.9 * np.sin(PI / 8) * UP + np.cos(PI / 8) * LEFT)
            .scale(0.8)
        )
        self.play(Create(angleADB), FadeIn(labelADB, shift=0.5 * RIGHT))
        self.wait(1)

        # 3.5 Angle to find
        angleBAD = Angle(Line(A, B), Line(A, D), radius=0.9, color=themeColor)
        labelBAD = (
            Text("?")
            .set_color(RED_N100)
            .scale(0.8)
            .move_to(angleBAD.get_center() + 0.4 * DOWN + 0.2 * RIGHT)
        )
        self.play(Create(angleBAD))
        self.play(FadeIn(labelBAD, shift=UP * 0.5))
        self.wait(5)

        # 4. FadeOut AD and ADB and draw ED
        self.play(FadeOut(angleADB, AD, labelADB, angleBAD, labelBAD))
        self.wait(1)
        marks_DE = createLineMarks(DE)

        self.play(Create(DE), FadeIn(labelE))
        self.play(Create(marks_DE))
        self.wait(1)

        # 4.5 Highlight triangle EDC

        triangleEDC_area = Polygon(
            C, E, D, color=YELLOW, fill_opacity=1, stroke_width=0
        )
        triangleEDC_area.z_index = -10
        self.play(FadeIn(triangleEDC_area))
        self.wait(2)

        # 5. draw angle CED and the draw angle EDB

        doubleAngleACB = Angle(Line(C, A), Line(C, B), radius=0.8, color=RED_N100)
        angleDEC = Angle(Line(E, D), Line(E, C), radius=0.7, color=RED_N100)
        doubleAngleDEC = Angle(Line(E, D), Line(E, C), radius=0.8, color=RED_N100)
        self.play(
            Create(angleDEC),
            Create(doubleAngleACB),
            Create(doubleAngleDEC),
            angleACB.animate.set_color(RED_N100),
        )
        self.wait(1)
        angleEDB = Angle(Line(D, E), Line(D, B), radius=0.5, color=themeColor)
        labelEDB = (
            nMath("60^\\circ")
            .move_to(D + np.sin(PI / 8) * UP + np.cos(PI / 8) * LEFT)
            .scale(0.8)
        )
        self.play(Create(angleEDB))
        self.wait(2)

        self.play(FadeIn(labelEDB, shift=0.5 * RIGHT))
        self.wait(1)

        self.play(
            triangleEDC_area.animate.set_opacity(0),
            FadeOut(doubleAngleACB, doubleAngleDEC, angleDEC),
            angleACB.animate.set_color(themeColor),
        )

        # 6. Create BE
        self.play(Create(BE))

        # 6.5 highlight triangle EDB equilateral triangle
        triangleBED_area = Polygon(
            B, E, D, color=YELLOW, fill_opacity=1, stroke_width=0
        )
        triangleBED_area.z_index = -10
        self.play(FadeIn(triangleBED_area))
        self.wait(2)

        BE_marks = createLineMarks(BE)
        self.play(Create(BE_marks))
        self.wait(2)

        # 7. Fade In AD
        self.play(FadeOut(angleEDB, labelEDB), triangleBED_area.animate.set_opacity(0))
        self.play(Create(AD), FadeIn(angleADB, labelADB))
        self.wait(1)

        # 8. highlight triangle AED
        triangleAED_area = Polygon(
            A, E, D, color=YELLOW, fill_opacity=1, stroke_width=0
        )
        triangleAED_area.z_index = -10
        self.play(FadeIn(triangleAED_area))
        self.wait(2)

        # 9. Draw angle ACD and EDA both

        angleEDA = Angle(Line(D, E), Line(D, A), radius=1, color=themeColor)
        doubleAngleEDA = Angle(Line(D, E), Line(D, A), radius=1.1, color=RED_N100)
        angleEAD = Angle(Line(A, D), Line(A, C), radius=1, color=themeColor)
        doubleAngleEAD = Angle(Line(A, D), Line(A, C), radius=1.1, color=RED_N100)

        self.play(Create(angleEDA))
        self.wait(2)
        self.play(Create(angleEAD))
        self.wait(2)
        self.play(
            Create(doubleAngleEDA),
            Create(doubleAngleEAD),
            angleEDA.animate.set_color(RED_N100),
            angleEAD.animate.set_color(RED_N100),
        )

        # 9.5 triangle AED is isosceles draw equal marks highlight the sides
        AE_marks = createLineMarks(Line(A, E))
        self.play(Create(AE_marks))
        self.wait(1)

        self.play(
            FadeOut(
                AD,
                angleEAD,
                angleEDA,
                labelADB,
                angleADB,
                doubleAngleEAD,
                doubleAngleEDA,
            ),
            triangleAED_area.animate.set_opacity(0),
        )
        self.wait(1)

        # 10. highlight triangle AEB
        triangleAEB_area = Polygon(
            A, E, B, color=YELLOW, fill_opacity=1, stroke_width=0
        )
        triangleAEB_area.z_index = -10
        self.play(FadeIn(triangleAEB_area))
        self.wait(1)

        angleBED = Angle(Line(E, B), Line(E, D), radius=0.5, color=themeColor)
        self.play(Create(angleBED))
        self.wait(1)
        angleDEC.set_color(themeColor)
        self.play(Create(angleDEC))
        self.wait(1)

        # 11. angle AEB is 90 degrees and triangle is isosceles
        angleAEB = RightAngle(Line(E, A), Line(E, B), color=themeColor)
        angleEAB = Angle(Line(A, B), Line(A, E), radius=0.7, color=themeColor)
        labelEAB = (
            nMath("45^\\circ")
            .scale(0.8)
            .move_to(angleEAB.get_center() + 0.4 * DOWN + 0.3 * RIGHT)
        )

        self.play(Create(angleAEB))
        self.wait(2)

        self.play(FadeOut(angleBED, angleDEC))
        self.wait(1)
        self.play(Create(angleEAB))
        self.play(FadeIn(labelEAB))
        self.wait(2)
        self.play(FadeOut(labelEAB), triangleAEB_area.animate.set_opacity(0))
        self.play(FadeIn(AD))
        self.wait(1)

        # 12. angle BAD is 30 degrees

        labelBAD = (
            nMath("30^\\circ")
            .scale(0.8)
            .move_to(angleBAD.get_center() + 0.5 * DOWN + 0.3 * RIGHT)
        )

        self.play(Create(angleBAD))
        self.play(FadeIn(labelBAD))
        highlight(self, labelBAD, buff=0.12, color=RED_N, wait_time=5)

        self.wait(2)


class GeometryExplanation(Scene):
    def construct(self):
        statement_groups = [
            [
                r"\text{In }\triangle ABC, \angle C = 30^\circ",
                r"\text{D is the midpoint of } BC",
                r"\angle ADB = 45^\circ",
            ],
            [r"\text{Construct E on AC such that } ED = DC"],
            [
                r"\triangle EDC \text{ is isosceles }",
                r"\Rightarrow \angle DEC = \angle DCE = 30^\circ",
                r"\angle EDB = \angle DEC + \angle DCE = 60^\circ",
            ],
            [r"\text{Now, join } BE"],
            [
                r"\text{ED = DB and } \angle EDB = 60^\circ",
                r"\Rightarrow \triangle BED \text{ is equilateral}",
                r"\Rightarrow BD = ED = BE",
            ],
            [
                r"\angle EDB = 60^\circ, \angle ADB = 45^\circ",
                r"\Rightarrow \angle EDA = \angle EDB - \angle ADB = 15^\circ",
            ],
            [
                r"\angle CAD = \angle EDA = 15^\circ",
                r"\triangle AED \text{ is isosceles}",
                r"\Rightarrow AE = ED",
            ],
            [
                r"\angle BED = 60^\circ, \angle CED = 30^\circ",
                r"\Rightarrow \angle AEB = 90^\circ",
            ],
            [
                r"\triangle AEB \text{ is isosceles}",
                r"\Rightarrow \angle BAC = 45^\circ",
                r"\angle CAD = 15^\circ",
                r"\angle DAB = \angle BAE - \angle CAD = 30^\circ",
            ],
        ]

        # Display each statement one by one
        for statements in statement_groups:
            prev = 0
            for stmt in statements:
                mathStmt = nMath(stmt)
                if prev == 0:
                    mathStmt.to_edge(UP)
                else:
                    mathStmt.next_to(prev, DOWN, buff=0.5)
                self.play(FadeIn(mathStmt))
                prev = mathStmt
                self.wait(1)
            clearScreen(self)


class Correction(Scene):
    def construct(self):
        statement_groups = [
            [
                r"\angle ADB = \angle CAD + \angle ACD",
                r"\Rightarrow \angle CAD = \angle ADB - \angle ACD=15^\circ",
            ],
        ]

        # Display each statement one by one
        for statements in statement_groups:
            prev = 0
            for stmt in statements:
                mathStmt = nMath(stmt)
                if prev == 0:
                    mathStmt.to_edge(UP)
                else:
                    mathStmt.next_to(prev, DOWN, buff=0.5)
                self.play(FadeIn(mathStmt))
                prev = mathStmt
                self.wait(1)
            clearScreen(self)
