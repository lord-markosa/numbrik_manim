from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        addBackground(self)

        eq1 = nMath("x+y = 8", color=BLACK).shift(UP * 2.8)
        eq2 = nMath("xy = 24", color=BLACK).shift(UP * 1.8)

        self.add(eq1, eq2)

        P = LEFT * 2
        Q = RIGHT * 2
        line = Line(P, Q, color=BLACK)
        dot1 = Dot(P, radius=0.05, color=BLACK)
        dot2 = Dot(Q, radius=0.05, color=BLACK)
        mid = Dot(line.get_center(), radius=0.05, color=BLACK)
        labelx = nMath("x").next_to(P, DOWN, buff=0.3)
        labely = nMath("y").next_to(Q, DOWN, buff=0.3)
        labelmid = nMath("\\frac{x+y}{2}").next_to(line.get_center(), DOWN, buff=0.3)

        arrowLeft = Arrow(line.get_center(), P, color=GREY_N400, buff=0.1).shift(
            UP * 0.3
        )
        labelLeftArrow = nMath("r").next_to(arrowLeft, UP, buff=0.1)
        arrowRight = Arrow(line.get_center(), Q, color=GREY_N400, buff=0.1).shift(
            UP * 0.3
        )
        labelRightArrow = nMath("r").next_to(arrowRight, UP, buff=0.1)
        # self.add(line, dot1, dot2, labelx, labely, mid, labelmid)

        self.play(
            LaggedStart(
                Create(line),
                FadeIn(dot1, dot2),
                FadeIn(labelx, labely, shift=0.5 * UP),
                lag_ratio=0.4,
            )
        )
        self.play(
            LaggedStart(
                FadeIn(mid),
                FadeIn(labelmid, shift=0.5 * UP),
                lag_ratio=0.4,
            )
        )
        self.play(
            Transform(labelmid, nMath("4").next_to(line.get_center(), DOWN, buff=0.3))
        )
        self.play(
            LaggedStart(
                GrowArrow(arrowLeft),
                FadeIn(labelLeftArrow, shift=DOWN * 0.5),
                GrowArrow(arrowRight),
                FadeIn(labelRightArrow, shift=DOWN * 0.5),
                lag_ratio=0.4,
            )
        )

        eq01 = nMath("x = 4", "-", "r").shift(1.5 * DOWN)
        eq02 = nMath("y = 4", "+", "r").next_to(eq01, DOWN, buff=0.4)

        self.wait(1)
        self.play(LaggedStart(fadeInTex(eq01), fadeInTex(eq02), lag_ratio=0.3))
        self.wait(1)

        self.play(
            LaggedStart(
                FadeOut(
                    line,
                    dot1,
                    dot2,
                    mid,
                    labelx,
                    labely,
                    labelmid,
                    arrowLeft,
                    arrowRight,
                    labelLeftArrow,
                    labelRightArrow,
                ),
                VGroup(eq01, eq02).animate.shift(UP * 2),
                lag_ratio=0.5,
            )
        )

        eq3 = nMath("(4-r)", "(4+r)", "=", "24").shift(1.5 * DOWN)
        eq31 = nMath("16-r^2", "=", "24").next_to(eq3, DOWN, buff=0.5)
        eq32 = nMath("r^2", "=", "16-24").next_to(eq3, DOWN, buff=0.5)
        eq33 = nMath("r^2", "=", "-8").next_to(eq3, DOWN, buff=0.5)
        eq34 = nMath("r =", "\\pm", "2\\sqrt{2}i").next_to(eq3, DOWN, buff=0.5)

        # self.add(arrowLeft, arrowRight, labelLeftArrow, labelRightArrow)

        self.play(fadeInTex(eq3))
        self.wait(1)
        self.play(fadeInTex(eq31))
        self.wait(1)
        self.play(TransformMatchingTex(eq31, eq32))
        self.wait(1)
        self.play(TransformMatchingTex(eq32, eq33))
        self.wait(1)
        self.play(TransformMatchingTex(eq33, eq34))

        # self.play(
        #     LaggedStart(FadeOut(eq3), eq34.animate.next_to(eq3, 0), lag_ratio=0.5)
        # )

        cp1 = eq34[2].copy()
        cp2 = eq34[2].copy()
        self.play(
            LaggedStart(
                AnimationGroup(
                    FadeOut(eq01[2], eq02[2]),
                    eq01[0:2].animate.shift(0.5 * LEFT),
                    eq02[0:2].animate.shift(0.5 * LEFT),
                ),
                AnimationGroup(
                    cp1.animate.next_to(eq01[2], 0, aligned_edge=LEFT + DOWN).shift(
                        0.5 * LEFT
                    ),
                    cp2.animate.next_to(eq02[2], 0, aligned_edge=LEFT + DOWN).shift(
                        0.5 * LEFT
                    ),
                ),
                FadeOut(eq3, eq34),
                lag_ratio=0.5,
            )
        )
        self.wait(1)

        self.play(Swap(VGroup(eq01[1], cp1), VGroup(eq02[1], cp2)))
        self.wait(1)
        self.play(FadeOut(eq01[0:2], eq02[0:2], cp1, cp2))

        eq4 = nMath("p^2 - 8p + 24 = 0").next_to(eq01, 0)
        eq5 = nMath("\\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}").next_to(
            eq4, DOWN, buff=0.7
        )

        self.play(fadeInTex(eq4))
        self.wait(1)
        self.play(fadeInTex(eq5))

        self.wait(4)
