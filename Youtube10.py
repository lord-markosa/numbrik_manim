from manim import *
from utils import *


class TriangleConstruction(Scene):
    def construct(self):
        # Length of base AB
        themeColor = GREY_N500
        base_len = 7
        A = LEFT * base_len / 2 + DOWN
        B = RIGHT * base_len / 2 + DOWN

        # Angles at base: 48°, so angle at C is 84°
        angle_A = 48 * DEGREES
        angle_B = 48 * DEGREES
        angle_C = PI - angle_A - angle_B

        # Length of sides AC and BC (same since triangle is isosceles)
        side_len = 4.5

        # Find coordinates of point C using angle A from horizontal
        C = A + side_len * np.array([np.cos(angle_A), np.sin(angle_A), 0])

        # Draw triangle ABC
        tri = Polygon(A, B, C, color=themeColor)

        # Draw points A, B, C
        labelA = Text(
            "A", font_size=32, font="Comic Sans MS", color=NUMBRIK_COLOR
        ).next_to(A, LEFT + DOWN)

        labelB = Text(
            "B", font_size=32, font="Comic Sans MS", color=NUMBRIK_COLOR
        ).next_to(B, RIGHT + DOWN)

        labelC = Text(
            "C", font_size=32, font="Comic Sans MS", color=NUMBRIK_COLOR
        ).next_to(C, UP)

        # Create point X on AB such that AC = BX
        AC_len = np.linalg.norm(C - A)
        AB_vec = B - A
        AB_len = np.linalg.norm(AB_vec)
        AB_dir = AB_vec / AB_len

        # Point X is such that BX = AC => X is AB - AC from point B
        X = B - AB_dir * AC_len
        labelX = (
            Text("X", font_size=32, font="Comic Sans MS", color=NUMBRIK_COLOR)
            .scale(0.8)
            .next_to(X, DOWN)
        )

        # Join CX
        line_CX = Line(C, X, color=themeColor)

        # Mark angle CAB as 48°
        angle_CAB = Angle(Line(A, B), Line(A, C), radius=0.5, color=themeColor)

        angle_CAB_label = MathTex(
            "48^{\\circ}",
            font_size=28,
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(
            A,
            np.sin(24 * PI / 180) * UP + np.cos(24 * PI / 180) * RIGHT,
            buff=0.6,
        )

        # Mark angle ACX as 18°
        angle_ACX = Angle(Line(C, A), Line(C, X), radius=0.5, color=themeColor)
        angle_ACX_label = MathTex(
            "18^{\\circ}",
            font_size=28,
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(angle_ACX, UP + LEFT, buff=0.1)

        # Mark angle ABC as x
        angle_ABC = Angle(Line(B, C), Line(B, A), radius=0.6, color=themeColor)

        angle_ABC_label = MathTex(
            "x",
            font_size=28,
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(
            B,
            np.sin(18 * PI / 180) * UP + np.cos(18 * PI / 180) * LEFT,
            buff=0.75,
        )

        # equality markers

        def add_perpendicular_marks(line, mark_length=0.2, gap=0.08):
            # Get start and end points of the line
            start, end = line.get_start(), line.get_end()
            center = (start + end) / 2
            direction = end - start
            direction = direction / np.linalg.norm(direction)

            # Perpendicular direction in 2D
            perp = np.array([-direction[1], direction[0], 0])
            perp = perp / np.linalg.norm(perp)

            # Offset for the two marks
            offset = direction * gap / 2

            # Compute positions for the two marks
            mark1_center = center + offset
            mark2_center = center - offset

            # Create the two marks
            mark1 = Line(
                mark1_center - perp * mark_length / 2,
                mark1_center + perp * mark_length / 2,
                color=themeColor,
                stroke_width=4,
            )
            mark2 = Line(
                mark2_center - perp * mark_length / 2,
                mark2_center + perp * mark_length / 2,
                color=themeColor,
                stroke_width=4,
            )

            perp_marks = VGroup(mark1, mark2)
            self.play(Create(perp_marks))

            return perp_marks

        # ANIMATE PROBLEM INTRODUCTION

        self.play(Create(tri))
        self.play(FadeIn(labelA), FadeIn(labelB), FadeIn(labelC))
        self.wait(1)
        self.play(Create(angle_CAB), FadeIn(angle_CAB_label))
        self.wait(1)
        self.play(FadeIn(labelX), Create(line_CX))
        self.wait(1)
        add_perpendicular_marks(Line(B, X))
        add_perpendicular_marks(Line(A, C))
        self.wait(1)
        self.play(Create(angle_ACX), FadeIn(angle_ACX_label))
        self.wait(1)
        self.play(Create(angle_ABC), FadeIn(angle_ABC_label))
        highlight(self, angle_ABC_label, color=RED)
        self.wait(4)

        # SOLUTION

        # Take a point P on CX (say, 60% along the way)
        ratio = ValueTracker(0.3)

        def getP():
            return C + ratio.get_value() * (X - C)

        dotP = always_redraw(lambda: Dot(getP(), radius=0.05).set_color(themeColor))

        labelP = (
            Text("P", font_size=32, font="Comic Sans MS", color=NUMBRIK_COLOR)
            .scale(0.8)
            .move_to(getP() + 0.3 * RIGHT + 0.1 * UP)
        )

        # Join BP
        line_BP = always_redraw(lambda: Line(B, getP(), color=themeColor))

        self.play(FadeOut(angle_ABC, angle_ABC_label))
        self.play(Create(dotP), FadeIn(labelP), Create(line_BP))
        self.wait(1)

        # This P will be used as a constant for stuffs that are to be removed in further execution
        P = getP()

        perp_marks = add_perpendicular_marks(Line(B, P))
        self.wait(1)

        triangleBPX_area = Polygon(
            B, P, X, color=YELLOW_N50, fill_opacity=1, stroke_width=0
        )
        triangleBPX_area.z_index = -10
        self.play(FadeIn(triangleBPX_area))
        self.wait(1)

        # Draw the angles connected for the isosceles triangle BXP
        angle_CXB = Angle(Line(X, B), Line(X, C), radius=0.5, color=RED_N100)

        angle_CXB_label = MathTex(
            "66^{\\circ}",
            font_size=28,
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(
            X,
            np.sin(40 * PI / 180) * UP + np.cos(40 * PI / 180) * RIGHT,
            buff=0.6,
        )

        self.play(Create(angle_CXB))
        self.wait(1)
        highlight(self, [angle_CAB_label, angle_ACX_label], color=RED)

        self.play(angle_CXB.animate.set_color(themeColor), FadeIn(angle_CXB_label))
        self.wait(1)

        angle_XPB = Angle(Line(P, X), Line(P, B), radius=0.5, color=RED)

        angle_XPB_label = MathTex(
            "66^{\\circ}",
            font_size=28,
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(
            P,
            DOWN + 0.3 * RIGHT,
            buff=0.6,
        )

        self.play(Create(angle_XPB))
        self.play(angle_XPB.animate.set_color(themeColor), FadeIn(angle_XPB_label))
        self.wait(1)

        angle_PBX = always_redraw(
            lambda: Angle(Line(B, getP()), Line(B, X), radius=0.65, color=themeColor)
        )

        angle_PBX_label = MathTex(
            "48^{\\circ}",
            font_size=28,
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(
            B,
            np.sin(12 * PI / 180) * UP + np.cos(12 * PI / 180) * LEFT,
            buff=0.75,
        )

        self.play(angle_PBX.animate.set_color(themeColor), FadeIn(angle_PBX_label))
        highlight(self, angle_PBX_label, color=RED_N100)
        self.wait(1)

        # CLEAR A LITTLE BIT

        self.play(
            FadeOut(
                angle_CXB,
                angle_XPB,
                angle_CXB_label,
                angle_XPB_label,
                angle_ACX,
                angle_ACX_label,
                dotP,
            ),
            triangleBPX_area.animate.set_opacity(0),
        )
        self.wait(1)

        # Extend line BP beyond P to intersect AC
        BP_vec = P - B
        BP_dir = BP_vec / np.linalg.norm(BP_vec)

        # Find intersection with AC
        def line_intersection(p1, d1, p2, d2):
            # Solve p1 + t1*d1 = p2 + t2*d2
            A = np.array([d1[:2], -d2[:2]]).T
            b = p2[:2] - p1[:2]
            t = np.linalg.lstsq(A, b, rcond=None)[0]
            return p1 + t[0] * d1

        AC_vec = C - A
        AC_dir = AC_vec / np.linalg.norm(AC_vec)

        def getZ():
            return line_intersection(getP(), BP_dir, A, AC_dir)

        Z = getZ()

        # Draw dashed extension from P to intersection
        dashed_extension = Line(P, Z, color=themeColor)

        labelZ = (
            Text("Z", font_size=32, font="Comic Sans MS", color=NUMBRIK_COLOR)
            .next_to(Z, LEFT + 0.1 * UP, buff=0.2)
            .scale(0.8)
        )

        self.play(Create(dashed_extension))
        self.play(FadeIn(labelZ))
        self.wait(1)

        triangleABZ_area = Polygon(
            A, B, Z, color=YELLOW_N40, fill_opacity=1, stroke_width=0
        )
        triangleABZ_area.z_index = -10
        self.play(FadeIn(triangleABZ_area))
        self.wait(1)

        lineAZ = Line(A, Z, color=RED_N100)
        lineBZ = Line(B, Z, color=RED_N100)

        self.play(Create(lineAZ), Create(lineBZ))
        self.wait(1)

        self.play(triangleABZ_area.animate.set_opacity(0), FadeOut(lineAZ, lineBZ))

        lineCZ = always_redraw(lambda: Line(C, getZ(), color=RED_C))
        lineZP = always_redraw(lambda: Line(getZ(), getP(), color=RED_C))
        lineZP.z_index = 10

        self.play(Create(lineCZ), Create(lineZP))
        self.wait(1)

        # Create a curved arrow pointing towards line segment ZP
        arrow = always_redraw(
            lambda: CurvedArrow(
                getZ()
                + LEFT
                + np.linalg.norm(C - getZ()) * UP,  # start point (away from ZP)
                getZ()
                + 0.5 * (C - getZ())
                + 0.1 * UP
                + 0.1 * LEFT,  # end point (midpoint of ZP)
                angle=-PI / 3,
                color=ORANGE,
                stroke_width=6,
                tip_length=0.25,
            )
        )

        self.play(Create(arrow))
        self.wait(1)

        self.play(
            FadeOut(
                labelZ,
                labelP,
                dashed_extension,
                perp_marks,
            )
        )

        self.play(
            ratio.animate.set_value(0),
            angle_PBX_label.animate.next_to(
                B,
                np.sin(20 * PI / 180) * UP + np.cos(20 * PI / 180) * LEFT,
                buff=0.7,
            ),
            run_time=2,
        )

        self.play(FadeOut(arrow))

        labelC_ = (
            Text("C, Z, P", font_size=32, font="Comic Sans MS", color=NUMBRIK_COLOR)
            .next_to(labelC, 0)
            .scale(0.8)
        )

        self.play(Transform(labelC, labelC_))
        solidHighlight(self, angle_PBX_label, buff=0.1, wait_time=3)


class Statements(Scene):
    def construct(self):
        step01 = MathTex(
            "\\angle PXB",
            "= \\angle CAB + \\angle ACX",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        step02 = MathTex(
            "= 48^{\\circ} + 18^{\\circ}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step01[1], DOWN, buff=0.5, aligned_edge=LEFT)

        step03 = MathTex(
            "= 66^{\\circ}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step02, 0, aligned_edge=LEFT)

        self.play(FadeIn(step01, shift=0.5 * UP))
        self.wait(1)
        self.play(FadeIn(step02))
        self.wait(1)
        self.play(Transform(step02, step03))
        clearScreen(self, 2)

        step1 = MathTex(
            "\\text{Construct BP }: \\ BP = BX",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        step2 = MathTex(
            "\\Delta BPX \\text{ is isosceles.}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step1, DOWN, buff=0.5)

        step3 = MathTex(
            "\\angle PXB",
            "= \\angle XPB = 66^{\\circ}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step2, DOWN, buff=0.5)

        step4 = MathTex(
            "\\angle PBX =",
            "(180 - 2\\cdot66)^{\\circ}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step3, DOWN, buff=0.5)

        step5 = MathTex(
            "\\angle PBX =",
            "48^{\\circ}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step3, DOWN, buff=0.5)

        self.play(FadeIn(step1, shift=0.5 * UP))
        self.wait(1)
        self.play(FadeIn(step2))
        self.wait(1)
        self.play(FadeIn(step3))
        self.wait(1)
        self.play(FadeIn(step4))
        self.wait(1)
        self.play(Transform(step4[0], step5[0]), Transform(step4[1], step5[1]))
        highlight(self, step5, buff=0.2)

        clearScreen(self, 2)

        step11 = MathTex(
            "\\angle ZAB = \\angle ZBA",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        step12 = MathTex(
            "\\Delta ZAB \\text{ is isosceles.}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step11, DOWN, buff=0.5)

        step13 = MathTex(
            "\\Rightarrow AZ = BZ",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step12, DOWN, buff=0.5)

        step14 = MathTex(
            "AZ =",
            "AC - CZ",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step13, DOWN, buff=0.5)

        step15 = MathTex(
            "BZ =",
            "BP + PZ",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step14, DOWN, buff=0.5)

        step160 = MathTex(
            "AC - CZ",
            "=",
            "BP + PZ",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step13, DOWN, buff=0.5)

        step16 = MathTex(
            "\\left(\\because AC = BX = BP\\right)",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step160, DOWN, buff=0.5)

        step17 = MathTex(
            "CZ + PZ = 0",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step16, DOWN, buff=0.5)

        step18 = MathTex(
            "CZ = PZ = 0",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step17, DOWN, buff=0.5)

        self.play(FadeIn(step11, shift=0.5 * UP))
        self.wait(1)
        self.play(FadeIn(step12))
        self.wait(1)
        self.play(FadeIn(step13))
        self.wait(1)
        self.play(FadeIn(step14))
        self.wait(1)
        self.play(FadeIn(step15))
        self.wait(1)
        self.play(
            FadeOut(step14[0]), Transform(step14[1], step160[0]), FadeIn(step160[1])
        )
        self.play(FadeOut(step15[0]), Transform(step15[1], step160[2]))
        self.wait(1)
        self.play(FadeIn(step16))
        self.wait(1)
        self.play(FadeIn(step17))
        self.wait(1)
        self.play(FadeIn(step18))

        highlight(self, step18, buff=0.2, wait_time=4)
        clearScreen(self, 1)

        step21 = MathTex(
            "\\angle CBA = \\angle PBX",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        step22 = MathTex(
            "\\Rightarrow x = 48^{\\circ}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step21, DOWN, buff=0.5)

        self.play(FadeIn(step21))
        self.wait(1)
        self.play(FadeIn(step22))
        self.wait(2)
