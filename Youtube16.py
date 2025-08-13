from manim import *
from utils import *


class FactorialDivisibility(Scene):
    def construct(self):
        # Context
        preCtx = nMath("N! = 1 \\cdot 2 \\cdot 3 \\cdots N").shift(UP)
        self.play(FadeIn(preCtx, scale=1.2))
        clearScreen(self, 2)

        # Title
        title = nMath(
            "\\text{Given:} \\, \\, \\, ", "n!/12^{12} \\in \\mathbb{N}"
        ).shift(UP)
        subtitle = (
            nMath("\\text{Find minimum }n \\in \\mathbb{N}")
            .set_color(GREY_N500)
            .next_to(title, DOWN, buff=0.5)
        )

        self.play(FadeIn(title, scale=1.2))
        self.wait(1)
        self.play(FadeIn(subtitle, shift=0.5 * UP))
        self.wait(4)

        self.play(
            title[1].animate.move_to(ORIGIN + 2 * UP),
            FadeOut(title[0]),
            FadeOut(subtitle),
        )
        self.wait(1)

        # Step 1: Factorization
        step1 = (
            nMath("12^{12} = (2^2 \\cdot 3)^{12} = 2^{24} \\cdot 3^{12}")
            .set_color(GREY_N500)
            .next_to(title[1], DOWN, buff=0.75)
        )
        self.play(FadeIn(step1, shift=0.5 * UP))
        self.wait(2)

        step12 = (
            nMath(
                "2^{24} \\, | \\, n! \\hspace{8pt} \\text{\\&} \\hspace{8pt} 3^{12} \\, | \\, n!"
            )
            .set_color(GREY_N500)
            .next_to(step1, DOWN, buff=0.5)
        )
        self.play(FadeIn(step12, shift=0.5 * UP))

        clearScreen(self, 4)

        # Legendre's formula
        preLegendre = (
            nText("Highest power of a prime p in n!").set_color(GREY_N400).shift(2 * UP)
        )

        legendre = nMath(
            "v_p(n) = \\left\\lfloor \\frac{n}{p} \\right\\rfloor + "
            "\\left\\lfloor \\frac{n}{p^2} \\right\\rfloor + "
            "\\left\\lfloor \\frac{n}{p^3} \\right\\rfloor + \\cdots"
        ).next_to(preLegendre, DOWN, buff=0.6)

        postLegendre = (
            (
                nMath(
                    "\\text{where } \\lfloor x \\rfloor \\text{ is the integer part of x}"
                ).set_color(GREY_N400)
            )
            .next_to(legendre, DOWN, buff=0.75)
            .scale(0.9)
        )

        self.play(FadeIn(preLegendre, shift=0.5 * UP))
        self.wait(1)
        self.play(FadeIn(legendre, scale=1.2))
        self.play(FadeIn(postLegendre))
        highlight(self, legendre, buff=0.2, wait_time=1)
        clearScreen(self, 1)

        # Step 4: Check 3-power requirement
        check3 = nText("For p = 3").set_color(GREY_N500).shift(3 * UP)
        self.play(FadeIn(check3, shift=0.5 * UP))
        self.wait(1)

        legendre3 = nMath(
            "v_3(n) = \\left\\lfloor \\frac{n}{3} \\right\\rfloor + ",
            "\\left\\lfloor \\frac{n}{9} \\right\\rfloor + ",
            "\\left\\lfloor \\frac{n}{27} \\right\\rfloor + \\cdots",
        ).next_to(check3, DOWN, buff=0.5)

        calc26 = nMath(
            "v_3(26) = \\left\\lfloor \\frac{26}{3} \\right\\rfloor + "
            "\\left\\lfloor \\frac{26}{9} \\right\\rfloor + 0 = 10"
        ).next_to(legendre3, DOWN, buff=0.75)

        calc27 = nMath(
            "v_3(27) = \\left\\lfloor \\frac{27}{3} \\right\\rfloor + "
            "\\left\\lfloor \\frac{27}{9} \\right\\rfloor + "
            "\\left\\lfloor \\frac{27}{27} \\right\\rfloor + 0 = 13"
        ).next_to(calc26, DOWN, buff=0.5)

        self.play(FadeIn(legendre3))
        self.wait(1)
        solidHighlight(self, legendre3[2], buff=0.2, wait_time=1)
        self.wait(1)
        self.play(FadeIn(calc26))
        self.wait(2)
        self.play(FadeIn(calc27))
        clearScreen(self, 2)

        # Step 5: Check 2-power requirement
        check2 = nText("For p = 2").set_color(GREY_N500).shift(3 * UP)
        self.play(FadeIn(check2, shift=0.5 * UP))
        self.wait(1)

        legendre2 = nMath(
            "v_2(n) = \\left\\lfloor \\frac{n}{2} \\right\\rfloor + "
            "\\left\\lfloor \\frac{n}{4} \\right\\rfloor + "
            "\\left\\lfloor \\frac{n}{8} \\right\\rfloor +",
            "\\left\\lfloor \\frac{n}{32} \\right\\rfloor +",
            "\\left\\lfloor \\frac{n}{16} \\right\\rfloor + \\cdots",
        ).next_to(check2, DOWN, buff=0.5)

        calc27 = nMath(
            "v_2(27) = \\left\\lfloor \\frac{27}{2} \\right\\rfloor + "
            "\\left\\lfloor \\frac{27}{4} \\right\\rfloor + "
            "\\left\\lfloor \\frac{27}{8} \\right\\rfloor +",
            "\\left\\lfloor \\frac{27}{16} \\right\\rfloor + 0 = 23",
        ).next_to(legendre2, DOWN, buff=0.75)

        calc28 = nMath(
            "v_2(28) = \\left\\lfloor \\frac{28}{2} \\right\\rfloor + "
            "\\left\\lfloor \\frac{28}{4} \\right\\rfloor + "
            "\\left\\lfloor \\frac{28}{8} \\right\\rfloor +",
            "\\left\\lfloor \\frac{28}{16} \\right\\rfloor + 0 = 25",
        ).next_to(calc27, DOWN, buff=0.5)

        self.play(FadeIn(legendre2))
        self.wait(2)
        self.play(FadeIn(calc27))
        self.wait(2)
        self.play(FadeIn(calc28))
        clearScreen(self, 2)

        # Step 6: Conclusion
        final1 = (
            nMath("\\text{For }3^{12} \\, | \\, n! \\, : \\hspace{8pt} n \\ge 27")
            .set_color(GREY_N500)
            .shift(2 * UP)
        )
        final2 = (
            nMath("\\text{For }2^{24} \\, | \\, n! \\, : \\hspace{8pt} n \\ge 28")
            .set_color(GREY_N500)
            .next_to(final1, DOWN, buff=0.5)
        )

        final = nMath("\\Rightarrow n \\ge 28").next_to(final2, DOWN, buff=0.75)

        self.play(FadeIn(final1))
        self.wait(1)
        self.play(FadeIn(final2))
        self.wait(1)
        self.play(FadeIn(final, scale=1.2))
        highlight(self, final, buff=0.2, wait_time=4)
