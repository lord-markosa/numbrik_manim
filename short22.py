from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        eqn = nMath("x^x =", "2^", "{2048}").scale(2)
        self.play(Write(eqn), run_time=2)
        self.wait(1)

        solidHighlight(self, eqn[2])

        eqn1 = (
            nMath("x^x =", "2^", "{k \\cdot \\frac{2048}{k}}")
            .scale(2)
            .shift(0.2 * UP + 0.3 * RIGHT)
        )

        self.play(
            LaggedStart(
                Transform(eqn[2], eqn1[2][2:6]),
                Write(eqn1[2][0:2]),
                FadeIn(eqn1[2][6:], shift=UP),
                lag_ratio=0.7,
            )
        )
        self.wait(1)
        solidHighlight(self, [eqn1[2][0], eqn1[2][7]], buff=0.12)

        clarify = (
            nMath("k = 2^n \\, \\, \\because 2048 = 2^{11}")
            .scale(1.5)
            .shift(1.8 * DOWN)
        )
        self.play(fadeInTex(clarify))
        self.wait(1)
        self.play(FadeOut(clarify))

        def auto_anim(eqn1, k, eqn2_=None):
            if eqn2_:
                self.play(FadeOut(eqn2_))
                self.wait(1)

            eqn2 = (
                nMath(
                    "x^x =", "2^", "{" + str(k) + "\\cdot \\frac{2048}{" + str(k) + "}}"
                )
                .scale(2)
                .shift(0.2 * UP + 0.3 * RIGHT)
            )
            self.play(
                ReplacementTransform(eqn1[2][0], eqn2[2][0]),
                ReplacementTransform(eqn1[2][7], eqn2[2][7]),
            )
            self.wait(1)

            eqn2_ = (
                nMath(str(2**k) + "^{" + str(int(2048 / k)) + "}")
                .scale(2)
                .shift(1.8 * DOWN)
            )

            self.play(fadeInTex(eqn2_))
            self.wait(1)

            return eqn2, eqn2_

        eqn2, eqn2_ = auto_anim(eqn1, 2)
        eqn3, eqn3_ = auto_anim(eqn2, 4, eqn2_)
        eqn4, eqn4_ = auto_anim(eqn3, 8, eqn3_)

        solidHighlight(self, eqn4_[0][0:3], buff=0.15, wait_time=4)

        self.wait(10)


class Options(Scene):
    def construct(self):
        options = (
            VGroup(
                MathTex("A) \\ 64", color=BLACK),
                MathTex("B) \\ 128", color=BLACK),
                MathTex("C) \\ 256", color=BLACK),
                MathTex("D) \\ 512", color=BLACK),
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
