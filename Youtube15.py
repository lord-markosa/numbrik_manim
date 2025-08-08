from manim import *
from utils import *
import numpy as np


class GeometryProof(Scene):
    def construct(self):
        # Fixed positions
        side = 5
        themeColor = GREY_N500

        D = ORIGIN + 2 * DOWN
        C = D + RIGHT * side
        B = D + LEFT * side
        theta = 22.5 * DEGREES
        length_AC = side / np.cos(theta) * (1 + 1 / np.sqrt(2))
        A = C + length_AC * (LEFT * np.cos(theta) + UP * np.sin(theta))
        E = D + side * np.tan(theta) * UP

        # Define points and labels
        labels = {
            "A": nText("A").next_to(A, UP),
            "B": nText("B").next_to(B, DOWN + 0.1 * LEFT),
            "C": nText("C").next_to(C, DOWN + 0.1 * RIGHT),
            "D": nText("D").next_to(D, DOWN + 0.1 * RIGHT),
            "E": nText("E").next_to(E, UP + 0.1 * RIGHT),
        }

        # Draw triangle ABC
        triangle = Polygon(A, B, C, color=themeColor)

        # Draw line AD
        AD = Line(A, D, color=themeColor)

        DE = DashedLine(D, E, color=themeColor)
        BE = Line(B, E, color=themeColor)

        # 1. Problem Statement
        self.play(
            Create(triangle),
            FadeIn(labels["A"], shift=0.5 * DOWN),
            FadeIn(labels["B"], labels["C"], shift=0.5 * UP),
        )

        # 2. Draw AD
        self.play(Create(AD), FadeIn(labels["D"]))

        DC = Line(D, C, color=themeColor)
        DB = Line(D, B, color=themeColor)
        BC = Line(B, C, color=themeColor)

        DC_marks = createLineMarks(DC).shift(0.5 * LEFT)
        DB_marks = createLineMarks(DB).shift(0.2 * RIGHT)

        self.play(BC.animate.set_color(YELLOW), rate_func=smooth)
        self.play(BC.animate.set_opacity(0), rate_func=smooth)
        self.play(Create(DC_marks), Create(DB_marks))
        self.wait(1)

        # 2.25 Draw the angle ADB
        angleADB = Angle(Line(D, A), Line(D, B), radius=0.6, color=themeColor)
        labelADB = (
            nMath("45^\\circ")
            .move_to(D + np.sin(theta) * UP + np.cos(theta) * LEFT)
            .scale(0.8)
        )
        self.play(Create(angleADB), FadeIn(labelADB, shift=0.5 * RIGHT))
        self.wait(1)

        # 2.5 Draw the angle ACB and ABC
        angleACB = Angle(Line(C, A), Line(C, B), radius=1.2, color=themeColor)
        labelACB = (
            nMath("x")
            .move_to(C + 0.8 * np.sin(theta) * UP + 1.6 * np.cos(theta) * LEFT)
            .scale(0.8)
        )

        angleABC = Angle(Line(B, C), Line(B, A), radius=0.6, color=themeColor)
        labelABC = (
            nMath("3x")
            .move_to(B + np.sin(theta) * UP + np.cos(theta) * RIGHT)
            .scale(0.8)
        )

        self.play(Create(angleACB), FadeIn(labelACB, shift=0.5 * RIGHT))
        self.play(Create(angleABC), FadeIn(labelABC, shift=0.5 * LEFT))
        self.wait(1)

        # 4. FadeOut AD and ADB and draw ED
        self.play(FadeOut(angleABC, labelABC))
        self.wait(1)
        self.play(Create(BE), FadeIn(labels["E"]))
        self.wait(1)

        # 5. Show how BE divides angle ABC
        angleEBC = Angle(Line(B, C), Line(B, E), radius=1.2, color=themeColor)
        labelEBC = (
            nMath("x")
            .move_to(B + 0.8 * np.sin(PI / 8) * UP + 1.6 * np.cos(theta) * RIGHT)
            .scale(0.8)
        )

        ## TODO: highlight angle ebc and angle ecb then show the other part of angle abc
        self.play(Create(angleEBC), FadeIn(labelEBC))
        highlight(self, [labelEBC, labelACB], color=RED_N100)
        self.wait(1)

        angleABE = Angle(Line(B, E), Line(B, A), radius=0.9, color=themeColor)
        labelABE = (
            nMath("2x")
            .move_to(angleABE.get_center() + UP * 0.35 + RIGHT * 0.35)
            .scale(0.8)
        )

        self.play(Create(angleABE), FadeIn(labelABE))
        self.wait(1)

        # 6. Construct DE and show DE is perpendicular to BC
        self.play(Create(DE))
        self.wait(1)

        ## TODO: highlight the triangles ebd and ecd
        areaEBD = getTriangularRegion(E, B, D, YELLOW_N50)
        areaECD = getTriangularRegion(E, C, D, GREEN_N100)
        self.play(FadeIn(areaEBD))
        self.play(FadeIn(areaECD))
        self.wait(2)
        self.play(areaEBD.animate.set_opacity(0), areaECD.animate.set_opacity(0))

        angleEDC = RightAngle(Line(D, C), Line(D, E), color=themeColor)
        self.play(Create(angleEDC))
        self.wait(1)

        # 7. Show angle ADE is 45 degrees
        angleADE = Angle(Line(D, E), Line(D, A), radius=0.8, color=themeColor)
        labelADE = (
            nMath("45^\\circ")
            .move_to(angleADE.get_center() + UP * 0.4 + LEFT * 0.1)
            .scale(0.8)
        )

        self.play(DE.animate.set_color(YELLOW))
        self.play(BC.animate.set_opacity(1))
        self.play(DE.animate.set_color(themeColor), BC.animate.set_opacity(0))

        ## TODO: highlight the 45 degrees
        self.play(Create(angleADE), FadeIn(labelADE))

        ## TODO: highlight median ad
        self.play(AD.animate.set_color(YELLOW))
        self.wait(1)
        self.play(AD.animate.set_color(themeColor))
        self.wait(1)

        # 8. Show exterior angle AEB is 2x
        areaABE = getTriangularRegion(A, B, E)
        self.play(FadeIn(areaABE))
        self.wait(1)
        self.play(areaABE.animate.set_opacity(0))
        self.wait(1)

        angleAEB = Angle(Line(E, A), Line(E, B), radius=1, color=themeColor)
        labelAEB = nMath("2x").move_to(angleAEB.get_center() + LEFT * 0.4).scale(0.8)
        self.play(Create(angleAEB), FadeIn(labelAEB))
        highlight(self, [labelEBC, labelACB], color=RED_N100)
        self.wait(1)

        # # 4.5 Highlight triangle EAB
        self.play(areaABE.animate.set_opacity(1))
        self.wait(1)
        self.play(areaABE.animate.set_opacity(0))
        self.wait(1)

        # 9. Draw perpendicular to BE passing through A
        P = BE.get_projection(A)
        labelP = nText("P").next_to(P, DOWN + 0.1 * RIGHT)
        AP = DashedLine(P, A, color=themeColor)
        angleAPB = RightAngle(Line(P, A), Line(P, B), color=themeColor, length=0.3)
        self.play(Create(AP), FadeIn(labelP), Create(angleAPB))
        self.wait(2)

        # 10. Draw the circle for quad ABDE
        circumcircle = Circle.from_three_points(A, B, D, color=GREY_N400)
        self.play(Create(circumcircle))
        self.wait(4)


class GeometryExplanation(Scene):
    def construct(self):
        statement_groups = [
            [
                r"\text{In } \triangle EBD \text{ and } \triangle ECD:",
                r"BD = CD \quad (\text{AD is median})",
                r"EB = EC \quad (\triangle EBC \text{ is isosceles})",
                r"BE = BE \quad (\text{common})",
                r"\Rightarrow \triangle EBD \cong \triangle ECD \quad (\text{SSS})",
                r"\Rightarrow \angle BDE = \angle CDE",
            ],
            [
                r"\angle BDE + \angle CDE = 180^\circ",
                r"\Rightarrow \angle BDE = \angle CDE = 90^\circ",
                r"\Rightarrow ED \perp BC",
                r"\Rightarrow \angle ADE = 45^\circ",
            ],
            [
                r"\triangle QBC \text{ is isosceles }",
                r"\Rightarrow \angle QCB = \angle QBC",
                r"\angle QAB = y",
                r"\angle QAC = y",
            ],
            [
                r"\angle BAE + \angle BDE = 180^\circ",
                r"\Rightarrow \angle BAE = 90^\circ",
                r"\text{In } \triangle ABC:", 
                r"\angle A + \angle B + \angle C = 180^\circ",
                r"\Rightarrow 90^\circ + 3x + x = 180^\circ",
                r"\Rightarrow x = 22.5^\circ",
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


class AngleBisectorAndPerpBisector(Scene):
    def construct(self):
        # Triangle vertices

        themeColor = GREY_N500
        len = 3
        th = 75 * DEGREES
        B = ORIGIN + 0.5 * DOWN + len * LEFT
        C = ORIGIN + 0.5 * DOWN + len * RIGHT
        A = C + len * (np.cos(th) * LEFT + np.sin(th) * UP)

        # Triangle sides
        triangle = Polygon(A, B, C, color=themeColor)

        # Midpoint of BC
        mid_BC = (B + C) / 2

        # Perpendicular bisector of BC
        dir_BC = C - B
        dir_BC_perp = np.array([-dir_BC[1], dir_BC[0], 0])  # 90 deg rotation
        dir_BC_perp = dir_BC_perp / np.linalg.norm(dir_BC_perp)

        line_perp = DashedLine(
            mid_BC - 2.5 * dir_BC_perp, mid_BC + 2 * dir_BC_perp, color=themeColor
        )

        # Angle bisector of angle A
        AB = B - A
        AC = C - A
        AB = AB / np.linalg.norm(AB)
        AC = AC / np.linalg.norm(AC)
        bisector_dir = AB + AC
        bisector_dir = bisector_dir / np.linalg.norm(bisector_dir)

        angle_bisector = Line(A, A + 6 * bisector_dir, color=themeColor)

        # Compute circumcircle
        circumcircle = Circle.from_three_points(A, B, C, color=GREY_N400)

        # Intersection point of bisectors
        def intersection_point(P1, d1, P2, d2):
            """
            P1, d1: point and direction for line 1
            P2, d2: point and direction for line 2
            Solves: P1 + t*d1 = P2 + s*d2
            """
            A_mat = np.array([d1[:2], -d2[:2]]).T
            b_vec = P2[:2] - P1[:2]
            t_s = np.linalg.solve(A_mat, b_vec)
            return P1 + t_s[0] * d1

        I = intersection_point(A, bisector_dir, mid_BC, dir_BC_perp)

        # Labels
        labels = VGroup(
            nText("A").move_to(A + 0.3 * RIGHT + 0.3 * UP),
            nText("B").move_to(B + 0.3 * DOWN + 0.3 * LEFT),
            nText("C").move_to(C + 0.3 * DOWN + 0.3 * RIGHT),
            nText("P").move_to(mid_BC + 0.3 * DOWN + 0.3 * LEFT),
            nText("Q").move_to(I + 0.4 * DOWN + 0.3 * LEFT),
        )

        # 1. Add everything
        self.play(Create(triangle), FadeIn(labels[0:3]))
        self.wait(1)

        perpAngle = RightAngle(
            Line(mid_BC, I), Line(mid_BC, C), color=themeColor, length=0.3
        )
        self.play(Create(line_perp), FadeIn(labels[3]))
        self.play(Create(perpAngle))
        self.wait(1)

        # 2. Draw the perpendicular bisector
        marksBP = createLineMarks(Line(B, mid_BC))
        marksCP = createLineMarks(Line(C, mid_BC))
        self.play(Create(marksBP), Create(marksCP))
        self.wait(1)

        # 3. Draw the circumcircle and mark the point of intersection
        self.play(Create(circumcircle))
        self.wait(1)
        self.play(FadeIn(labels[4]))
        self.wait(1)
        IC = Line(I, C, color=GREY_N400)
        IB = Line(I, B, color=GREY_N400)

        self.play(Create(IC), Create(IB))
        self.wait(1)
        IA = Line(I, A, color=GREY_N400)
        self.play(Create(IA))
        self.wait(1)

        ## TODO; highlight triangle QBC
        areaQBC = getTriangularRegion(I, B, C)
        self.play(FadeIn(areaQBC))
        self.wait(1)
        self.play(areaQBC.animate.set_opacity(0))
        self.wait(1)

        # 4. show the equal angles and hence IA is the angle bisector
        ## TODO: highlight the chord BQ and keep it highlighted
        angleBCI = Angle(Line(C, B), Line(C, I), radius=0.6, color=RED_N)
        labelBCI = (
            nMath("y")
            .scale(0.8)
            .move_to(angleBCI.get_center() + 0.4 * LEFT + 0.2 * DOWN)
        )

        angleBAI = Angle(Line(A, B), Line(A, I), radius=0.6, color=RED_N)
        labelBAI = (
            nMath("y")
            .scale(0.8)
            .move_to(angleBAI.get_center() + 0.2 * LEFT + 0.3 * DOWN)
        )

        angleCBI = Angle(Line(B, I), Line(B, C), radius=0.6, color=RED_N)
        labelCBI = (
            nMath("y")
            .scale(0.8)
            .move_to(angleCBI.get_center() + 0.4 * RIGHT + 0.2 * DOWN)
        )

        angleCAI = Angle(Line(A, I), Line(A, C), radius=0.6, color=RED_N)
        labelCAI = nMath("y").scale(0.8).move_to(angleCAI.get_center() + 0.4 * DOWN)

        self.play(IB.animate.set_color(YELLOW))
        self.play(FadeIn(labelBCI), Create(angleBCI))
        self.play(FadeIn(labelBAI), Create(angleBAI))
        self.play(
            angleBCI.animate.set_color(themeColor),
            angleBAI.animate.set_color(themeColor),
            IB.animate.set_color(themeColor),
        )
        self.wait(1)
        self.play(IC.animate.set_color(YELLOW))
        self.play(FadeIn(labelCBI), Create(angleCBI))
        self.play(FadeIn(labelCAI), Create(angleCAI))
        self.play(
            angleCBI.animate.set_color(themeColor),
            angleCAI.animate.set_color(themeColor),
            IC.animate.set_color(themeColor),
        )
        self.wait(1)

        self.play(IA.animate.set_color(YELLOW))
        self.wait(1)
        self.play(IA.animate.set_color(themeColor))
        highlight(self, labels[4], color=RED_N100)

        self.wait(4)
