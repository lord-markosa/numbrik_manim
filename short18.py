from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        themeColor = GREY_N500

        question = (
            MathTex(
                "\\text{Find the diameter of the circle}",
                color=BLACK,
            )
            .scale(0.8)
            .arrange(DOWN)
            .to_edge(UP)
        )

        self.play(FadeIn(question, shift=UP))

        # R = 4  # Radius of the main quarter circle

        f = 0.8  # Scale factor
        A = ORIGIN + 2.7 * LEFT
        B = A + 6 * f * RIGHT
        C = B + 2 * f * UP
        D = C + 5 * f * LEFT
        E = D + 2 * f * DOWN
        F = B + f * RIGHT
        G = B + 3 * f * DOWN

        AB = Line(A, B, color=themeColor)
        BC = Line(B, C, color=themeColor)
        CD = Line(C, D, color=themeColor)
        DE = DashedLine(D, E, color=themeColor)
        BF = Line(B, F, color=themeColor)
        BG = Line(B, G, color=themeColor)
        AE = Line(A, E, color=themeColor)
        DG = DashedLine(G, D, color=GREY_N400)

        labels = {
            "A": nText("A").next_to(A, LEFT).scale(0.7),
            "B": nText("B").move_to(B + 0.3 * DOWN + 0.3 * RIGHT).scale(0.7),
            "C": nText("C").move_to(C + 0.3 * RIGHT + 0.3 * UP).scale(0.7),
            "D": nText("D").move_to(D + 0.3 * LEFT + 0.3 * UP).scale(0.7),
            "F": nText("F").move_to(F + 0.3 * RIGHT + 0.3 * DOWN).scale(0.7),
            "G": nText("G").move_to(G + 0.2 * RIGHT + 0.2 * DOWN).scale(0.7),
        }

        circle = Circle.from_three_points(A, C, D, color=themeColor)

        angleABC = RightAngle(Line(B, C), Line(B, A), color=themeColor, length=0.3)
        angleBCD = RightAngle(Line(C, D), Line(C, B), color=themeColor, length=0.3)
        angleAED = RightAngle(Line(E, B), Line(E, D), color=themeColor, length=0.3)

        lengthMarkerAB = lengthMarker(
            A + 0.3 * DOWN, B + 0.3 * DOWN, "6", scale=0.8, buff=0.1
        )
        lengthMarkerBC = lengthMarker(B + RIGHT, C + RIGHT, "2", scale=0.8, buff=0)
        dashedCD_extd = DashedLine(C, C + RIGHT * 1.2, color=themeColor)
        dashedAB_extd = DashedLine(B, B + RIGHT * 1.2, color=themeColor)
        lengthMarkerCD = lengthMarker(
            D + 0.3 * UP, C + 0.3 * UP, "5", scale=0.8, buff=0.5
        )

        self.play(Create(AB), Create(BC), Create(CD), Create(circle))

        self.play(
            Create(angleABC),
            Create(angleBCD),
            FadeIn(labels["A"], labels["B"], labels["C"], labels["D"]),
        )
        self.play(
            Create(dashedCD_extd),
            Create(dashedAB_extd),
            FadeIn(lengthMarkerAB[1], lengthMarkerAB[2]),
            FadeIn(lengthMarkerBC[1], lengthMarkerBC[2]),
            FadeIn(lengthMarkerCD[1], lengthMarkerCD[2]),
            run_time=0.5,
        )
        self.play(
            GrowArrow(lengthMarkerAB[0]),
            GrowArrow(lengthMarkerBC[0]),
            GrowArrow(lengthMarkerCD[0]),
            run_time=0.5,
        )
        self.wait(2)
        self.play(Create(DE), Create(angleAED))
        self.wait(1)
        self.play(Create(BF), FadeIn(labels["F"]))
        self.wait(1)

        arrow1 = CurvedArrow(
            (A + E) / 2 + DOWN * 0.1, (B + F) / 2 + DOWN * 0.3, color=ORANGE
        )
        self.play(AE.animate.set_color(YELLOW))
        self.play(Create(arrow1), BF.animate.set_color(YELLOW))
        self.wait(1)
        self.play(
            FadeOut(arrow1), AE.animate.set_opacity(0), BF.animate.set_color(themeColor)
        )
        self.wait(1)
        self.play(Create(BG), FadeIn(labels["G"]))

        arrow2 = CurvedArrow(
            (B + C) / 2 + LEFT * 0.3, (B + G) / 2 + LEFT * 0.3, color=ORANGE
        )

        arrow3 = CurvedArrow(
            (B + A) / 2 + DOWN * 0.1 + LEFT, (B + F) / 2 + DOWN * 0.3, color=ORANGE
        )

        self.play(BC.animate.set_color(YELLOW))
        self.play(
            Create(arrow2),
            BC.animate.set_color(themeColor),
            BG.animate.set_color(YELLOW),
        )
        self.wait(1)
        self.play(BG.animate.set_color(themeColor), FadeOut(arrow2))
        self.play(AB.animate.set_color(YELLOW))
        self.play(
            Create(arrow3),
            AB.animate.set_color(themeColor),
            BF.animate.set_color(YELLOW),
        )
        self.wait(1)
        self.play(BF.animate.set_color(themeColor), FadeOut(arrow3))
        self.wait(2)
        self.play(Create(DG))
        self.wait(5)


class Statements(Scene):
    def construct(self):
        statement1 = nMath("CB\\cdot", "BG", "=", "AB \\cdot", "BF").to_edge(UP)
        statement2 = nMath("\\Rightarrow 2\\cdot", "x", "=", "6 \\cdot", "1").next_to(
            statement1, DOWN, buff=0.5
        )
        statement3 = nMath("\\Rightarrow x = 3").next_to(statement2, DOWN, buff=0.5)
        statement4 = nMath("CD^2 + CG^2 = DG^2").to_edge(UP)
        statement5 = nMath("\\Rightarrow D = 5\\sqrt{2}").next_to(
            statement4, DOWN, buff=0.5
        )

        self.play(FadeIn(statement1[0]))
        self.play(FadeIn(statement1[1]))
        self.play(FadeIn(statement1[2:4]))
        self.play(FadeIn(statement1[4]))
        self.wait(1)
        self.play(FadeIn(statement2))
        self.wait(1)
        self.play(FadeIn(statement3))

        clearScreen(self, 4)

        self.play(FadeIn(statement4))
        self.wait(1)
        self.play(FadeIn(statement5))
        self.wait(4)
