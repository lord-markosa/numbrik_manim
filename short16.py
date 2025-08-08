from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        question = (
            VGroup(
                MathTex(
                    "\\text{Which of the following are equal to }30^\\circ?",
                    color=GREY_N800,
                ),
            )
            .arrange(DOWN)
            .to_edge(UP)
        )

        highlightColor = GREEN_N100
        themeColor = GREY_N500
        radius = 4
        O = ORIGIN + 2 * DOWN
        A = O + LEFT * radius
        B = O + RIGHT * radius
        C = O + radius * (np.sin(PI / 3) * UP + np.cos(PI / 3) * LEFT)
        D = O + radius * (np.cos(PI / 3) * LEFT)

        center = Dot(O, radius=0.05, color=themeColor)

        diameter = Line(A, B, color=BLACK)
        semicircle = ArcBetweenPoints(B, A, angle=PI, color=BLACK)

        triangle_arc = always_redraw(lambda: Polygon(A, B, C, color=BLACK))

        CD = DashedLine(C, D, color=themeColor)
        CO = Line(C, O, color=themeColor)

        ## PART 1: Problem Introduction

        anglex = Angle(Line(C, A), Line(C, D), color=themeColor, radius=0.9)
        angley = Angle(Line(C, D), Line(C, O), color=themeColor, radius=1.05)
        anglez = Angle(Line(C, O), Line(C, B), color=themeColor, radius=0.9)
        anglew = Angle(Line(B, C), Line(B, A), color=themeColor, radius=0.9)
        anglePerp = RightAngle(Line(D, O), Line(D, C), color=themeColor)

        labelx = nText("x").move_to(anglex.get_center() + 0.5 * DOWN + 0.1 * LEFT)
        labely = nText("y").move_to(angley.get_center() + 0.5 * DOWN + 0.1 * RIGHT)
        labelz = nText("z").move_to(anglez.get_center() + 0.4 * DOWN + 0.35 * RIGHT)
        labelw = nText("w").move_to(anglew.get_center() + 0.5 * LEFT + 0.15 * UP)

        labelA = Text("A", color=themeColor, font_size=32).next_to(A, DOWN)
        labelB = Text("B", color=themeColor, font_size=32).next_to(B, DOWN)
        labelC = Text("C", color=themeColor, font_size=32).next_to(C, UP)
        labelD = Text("D", color=themeColor, font_size=32).next_to(D, DOWN)
        labelO = Text("O", color=themeColor, font_size=32).next_to(O, DOWN)

        lineDA_marks = createLineMarks(Line(D, A))
        lineDO_marks = createLineMarks(Line(D, O))

        self.play(Create(semicircle), FadeIn(question, shift=UP))
        self.play(Create(triangle_arc), Create(center))
        self.play(Create(CD), Create(CO))
        self.play(
            Create(anglex),
            Create(angley),
            Create(anglez),
            Create(anglew),
            Create(anglePerp),
            Create(lineDA_marks),
            Create(lineDO_marks),
        )
        self.play(
            FadeIn(
                labelx, labely, labelz, labelw, labelA, labelB, labelC, labelD, labelO
            )
        )
        self.wait(4)

        # Solution

        # 1. highlight area aoc
        area = getTriangularRegion(A, O, C)
        self.play(FadeIn(area))
        self.wait(1)
        self.play(area.animate.set_opacity(0))
        self.wait(1)

        # 3. highlight AC, highlightOC
        AC = Line(A, C, color=highlightColor)
        OC = Line(O, C, color=highlightColor)
        self.play(FadeIn(AC))
        self.play(FadeIn(OC))
        self.wait(1)
        # 4. wait(1), highlight AO
        AO = Line(A, O, color=highlightColor)
        self.play(FadeIn(AO))
        self.wait(1)
        # 4. unhighlight
        self.play(FadeOut(AO, AC, OC))
        # 5. highlight triangle OCB
        area = getTriangularRegion(O, C, B)
        # 6. unhighlight
        self.play(FadeIn(area))
        self.wait(1)
        self.play(FadeOut(area))
        # 7. highlight OC, then OB
        OB = Line(O, B, color=highlightColor)
        self.play(FadeIn(OC))
        self.play(FadeIn(OB))
        self.wait(1)
        # 8. unhighlight
        self.play(FadeOut(OC, OB))
        # 9. highlight the exterior angle AOC
        angleAOC = Angle(Line(O, C), Line(O, A), color=RED_N100, radius=0.6)
        self.play(Create(angleAOC))
        self.wait(1)
        self.play(FadeOut(angleAOC))

        self.wait(4)


class Statements(Scene):
    def construct(self):
        # x = y
        # x + y = 60
        # => x = y = 30
        # z = w
        # z + w = 60
        # => z = w = 30

        statement_groups = [
            [
                r"x = y",
                r"x + y = 60^\circ",
                r"\Rightarrow x = y = 30^\circ",
            ],
            [
                r"z = w",
                r"z + w = 60^\circ",
                r"\Rightarrow z = w = 30^\circ",
            ],
        ]

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


class Options(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        options = (
            VGroup(
                MathTex("A) \\ \\text{x only}", color=BLACK),
                MathTex("B) \\ \\text{x and y}", color=BLACK),
                MathTex("C) \\ \\text{x, y and z}", color=BLACK),
                MathTex("D) \\ \\text{All of them}", color=BLACK),
            )
            .arrange(DOWN, center=False, buff=0.25, aligned_edge=LEFT)
            .to_edge(UP)
        )

        self.play(FadeIn(options))
        self.wait(5)

        self.wait(1)
        self.play(Create(SurroundingRectangle(options[3], corner_radius=0.1, buff=0.1)))
        self.wait(4)
