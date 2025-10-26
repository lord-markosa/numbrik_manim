from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        eqn1 = nMath("a \\equiv b \\pmod c", color=BLACK)
        self.play(FadeIn(eqn1, scale=1.2), run_time=2)
        # self.add(eqn1)
        clearScreen(self, 2)

        title = MathTex(
            "\\text{Modular Arithmetic}",
            color=NUMBRIK_COLOR,
            # tex_template=TexFontTemplates.droid_sans,
        ).scale(2)
        self.play(Write(title), run_time=2.5, rate_func=smoothstep)
        self.wait(1)
        clearScreen(self, 2)

        eq1_ = nMath("n \\div 8")
        eq1 = nMath("n \\div 8", "\\Rightarrow remainder = 2")
        eq2 = nMath(
            "S", "= \\{ n \\mid n = 8q + 2,\\ q \\in \\mathbb{Z} \\}", color=BLACK
        )

        self.play(fadeInTex(eq1_))
        self.wait(1)
        self.play(TransformMatchingTex(eq1_, eq1))
        self.wait(1)
        self.play(FadeOut(eq1, shift=UP), fadeInTex(eq2))
        self.wait(1)

        eq3 = nMath("= \\{", "2,", "10", ",", "18", ", 26, ...", "\\}").shift(
            DOWN * 0.5
        )

        eq3_ = nMath(
            "= \\{", "-14, -6, ", "2,", "10", ",", "18", ", 26, ...", "\\}"
        ).shift(DOWN * 0.5)

        self.play(eq2.animate.shift(UP * 0.5))
        self.play(fadeInTex(eq3))
        self.wait(1)
        self.play(TransformMatchingTex(eq3, eq3_))
        self.wait(1)
        hgls = solidHighlight(self, [eq3_[3], eq3_[5]], unhighlight=False)

        eq4 = nMath("10", "\\equiv", "18", " \\pmod 8").shift(DOWN)
        # self.add(eq4)
        self.play(
            eq2.animate.shift(0.5 * UP),
            eq3_.animate.shift(0.5 * UP),
            hgls[0].animate.shift(0.5 * UP),
            hgls[1].animate.shift(0.5 * UP),
        )

        self.play(
            TransformFromCopy(eq3_[3], eq4[0]),
            TransformFromCopy(eq3_[5], eq4[2]),
            FadeIn(eq4[1], eq4[3:]),
        )
        clearScreen(self, 2)

        self.play(FadeIn(eqn1))
        self.wait(1)

        eq5 = nMath(
            "a \\equiv b \\pmod c",
            "\\,\\iff\\, c \\, \\text{ divides } \\, a - b",
            color=BLACK,
        )

        self.play(TransformMatchingTex(eqn1, eq5))
        clearScreen(self, 2)

        prop1 = nMath(
            r"\text{If } a \equiv b \pmod{m}, \quad c \equiv d \pmod{m}",
            color=NUMBRIK_COLOR,
        ).shift(UP)
        prop2 = nMath(r"\Rightarrow a \pm c \equiv b \pm d \pmod{m}", color=BLACK)
        prop3 = nMath(
            r"\Rightarrow ac \equiv bd \pmod{m}",
            color=BLACK,
        ).shift(DOWN)

        self.play(fadeInTex(prop1))
        self.wait(1)
        self.play(fadeInTex(prop2))
        self.play(fadeInTex(prop3))

        clearScreen(self, 1)

        # Step 2: Reduce 13 mod 11
        step1 = nMath("13 \\equiv 2 \\pmod{11}").to_edge(UP)

        self.play(fadeInTex(step1))
        self.wait(1)

        step2 = nMath("2^5", "= 32", "\\equiv", "-1", "\\pmod{11}").next_to(
            step1, DOWN, buff=0.5
        )
        self.play(fadeInTex(step2))
        self.wait(1)

        step3 = nMath(
            "(", "2^5", ")^{14}", "\\equiv", "(", "-1", ")^{14}", "\\pmod{11}"
        ).next_to(step2, DOWN, buff=0.5)

        self.play(TransformMatchingTex(step2.copy(), step3))
        self.wait(1)

        step3_ = nMath("2^{70} \\equiv 1 \\pmod{11}").next_to(step3, 0)
        self.play(Transform(step3, step3_))
        self.wait(1)

        step4 = nMath(
            "2^3 = 8 \\pmod{11}",
        ).next_to(step3_, DOWN, buff=0.75)

        self.play(fadeInTex(step4))
        self.wait(1)

        step5 = nMath(
            "2^{70}\\cdot2^3 \\equiv 1\\cdot8 \\pmod{11}",
        ).next_to(step4, DOWN, buff=0.75)

        hgls = solidHighlight(
            self, [step3_, step4], color=YELLOW_N50, buff=0.2, unhighlight=False
        )
        self.play(fadeInTex(step5))

        step5_ = nMath(
            "13^{73} \\equiv",
            "2^{73} \\equiv",
            "8 \\pmod{11}",
        ).next_to(step5, DOWN, buff=0.5)

        self.play(fadeInTex(step5_))
        self.wait(1)

        step5__ = nMath(
            "13^{73} \\equiv",
            "8 \\pmod{11}",
        ).next_to(step5, DOWN, buff=0.5)

        self.play(TransformMatchingTex(step5_, step5__))

        highlight(self, step5__, buff=0.2, color=RED_N100, unhighlight=False)
        clearScreen(self, 2)

        step5 = nMath("14 \\equiv 3 \\pmod{11}").to_edge(UP)

        step6 = nMath("3^3 = 27 \\equiv 5 \\pmod{11}").next_to(step5, DOWN, buff=0.5)

        step7 = nMath("14^{3} \\equiv", "3^3 \\equiv", "5 \\pmod{11}").next_to(
            step6, DOWN, buff=0.5
        )
        step7_ = nMath("14^{3} \\equiv", "5 \\pmod{11}").next_to(step7, 0)

        self.play(fadeInTex(step5))
        self.wait(1)
        self.play(fadeInTex(step6))
        self.wait(1)
        self.play(fadeInTex(step7))
        self.play(TransformMatchingTex(step7, step7_))
        highlight(self, step7_, buff=0.2, color=RED_N100)

        step5__.to_edge(UP)
        self.play(
            FadeOut(step5, step6),
        )
        self.play(
            LaggedStart(
                FadeIn(step5__),
                step7_.animate.next_to(step5__, DOWN, buff=0.5),
                lag_ratio=0.5,
            )
        )

        result = nMath("13^{73} + 14^{3}", "\\equiv 8 + 5 \\pmod{11}").next_to(
            step7_, DOWN, buff=0.75
        )

        result2 = nMath("\\equiv 13 \\pmod{11}").next_to(
            result[1], DOWN, buff=0.5, aligned_edge=LEFT
        )

        result3 = nMath("\\equiv 2 \\pmod{11}").next_to(
            result2, DOWN, buff=0.5, aligned_edge=LEFT
        )

        final = nMath("13^{73} + 14^{3}", "\\equiv 2 \\pmod{11}")

        self.play(fadeInTex(result))
        self.wait(1)
        self.play(fadeInTex(result2))
        self.wait(1)
        self.play(fadeInTex(result3))
        self.wait(1)

        self.play(
            LaggedStart(
                FadeOut(step5__, step7_, result[1], result2),
                AnimationGroup(
                    result[0].animate.next_to(final[0], 0, aligned_edge=LEFT),
                    result3.animate.next_to(final[1], 0, aligned_edge=LEFT),
                ),
                lag_ratio=0.5,
            )
        )

        highlight(self, final, buff=0.2, color=RED, unhighlight=False)
        solidHighlight(self, final[1][1], buff=0.2, unhighlight=False)

        self.wait(2)


class Statement(Scene):
    def construct(self):
        question = VGroup(
            MathTex(
                "\\text{Find the remainder when } 13^{73} + 14^3",
                color=BLACK,
            ),
            MathTex(
                "\\text{is divided by } 11.",
                color=BLACK,
            ),
        ).arrange(DOWN, buff=0.5)

        self.add(question)
        self.wait(1)


class Correction2(Scene):
    def construct(self):
        prop1 = nMath(
            r"\text{If } a \equiv b \pmod{m}, \quad c \equiv d \pmod{m}",
            color=NUMBRIK_COLOR,
        ).shift(1.5 * UP)
        prop2 = nMath(
            r"\Rightarrow a \pm c \equiv b \pm d \pmod{m}", color=BLACK
        ).shift(0.5 * UP)
        prop3 = nMath(
            r"\Rightarrow ac \equiv bd \pmod{m}",
            color=BLACK,
        ).shift(0.5 * DOWN)
        prop4 = nMath(
            r"\Rightarrow a^n \equiv b^n \pmod{m}",
            color=BLACK,
        ).shift(1.5 * DOWN)

        self.play(fadeInTex(prop1))
        self.wait(1)
        self.play(fadeInTex(prop2))
        self.play(fadeInTex(prop3))
        self.play(fadeInTex(prop4))
        self.wait(10)


class Thumbnail(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        eqn = (
            nMath(
                "( \\,",
                "13^",
                "{73}",
                "+",
                "14^",
                "3",
                "\\,)",
                "\\div",
                "11",
                color=WHITE,
            )
            .scale(3)
            .set_color_by_tex_to_color_map(
                {
                    "73": GREEN_N50,
                    "3": GREEN_N50,
                    "1": YELLOW,
                }
            )
        )
        self.add(eqn)

        self.wait(10)
