from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        eqn = (
            nMath(
                "x^3 =",
                "303",
                "^3",
                "+",
                "404",
                "^3",
                "+",
                "505",
                "^3",
            )
            .scale(2)
            .to_edge(UP)
        )

        # solidHighlight(self, eqn[2])

        eqn1 = (
            nMath("x^3 =", "101^3", "\\times", "\\left(", "3^3 + 4^3 +5^3", "\\right)")
            .scale(2)
            .next_to(eqn, DOWN, buff=0.75)
        )

        eqn2 = (
            nMath("x^3 =", "101^3", "\\times", "216")
            .scale(2)
            .next_to(eqn1, DOWN, buff=0.5)
        )

        eqn3 = (
            nMath("x^3 =", "101^3", "\\times", "6^3")
            .scale(2)
            .next_to(eqn1, DOWN, buff=0.5)
        )

        eqn4 = nMath("x =", "101", "\\times", "6").scale(2).next_to(eqn3, DOWN, buff=1)

        eqn5 = nMath("x =", "606").scale(2).next_to(eqn3, DOWN, buff=1)

        hgl1 = SurroundingRectangle(
            eqn[1:], corner_radius=0.3, buff=0.25, color=YELLOW, stroke_width=6
        )

        hgl2 = solidHighlight(self, [eqn[1], eqn[4], eqn[7]], animate=False)

        self.play(FadeIn(eqn, scale=1.2))
        self.wait(2)
        self.play(Create(hgl1), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(hgl1))
        self.wait(1)

        self.play(FadeIn(hgl2[0]), run_time=0.5)
        self.play(FadeIn(hgl2[1]), run_time=0.5)
        self.play(FadeIn(hgl2[2]), run_time=0.5)
        self.wait(1)

        self.play(
            LaggedStart(
                FadeIn(eqn1[0]), FadeIn(eqn1[1]), FadeIn(eqn1[2]), lag_ratio=0.6
            )
        )
        self.play(fadeInTex(eqn1[3:]))
        self.wait(1)
        solidHighlight(self, eqn1[4], buff=0.2, corner_radius=0.3)

        self.play(*[FadeOut(h) for h in hgl2])
        self.wait(1)

        self.play(
            LaggedStart(
                TransformFromCopy(eqn1[0], eqn2[0]),
                TransformFromCopy(eqn1[1], eqn2[1]),
                TransformFromCopy(eqn1[2], eqn2[2]),
                fadeInTex(eqn2[3]),
                lag_ratio=0.5,
            )
        )

        self.wait(1)
        self.play(TransformMatchingTex(eqn2, eqn3))
        self.wait(1)
        self.play(TransformFromCopy(eqn3, eqn4))
        self.wait(1)
        self.play(TransformMatchingTex(eqn4, eqn5))

        self.wait(10)


class Options(Scene):
    def construct(self):
        options = (
            VGroup(
                MathTex("A) \\ 216", color=BLACK),
                MathTex("B) \\ 1212", color=BLACK),
                MathTex("C) \\ 606", color=BLACK),
                MathTex("D) \\ 101", color=BLACK),
            )
            .arrange(DOWN, aligned_edge=LEFT, center=False, buff=0.5)
            .to_edge(UP)
        )

        self.play(FadeIn(options))
        self.wait(4)

        self.play(Create(SurroundingRectangle(options[2], corner_radius=0.1, buff=0.1)))
        self.wait(5)


class Statements(Scene):
    def construct(self):
        statement = Text("Find x", color=BLACK)
        self.play(FadeIn(statement))
        self.wait(6)
