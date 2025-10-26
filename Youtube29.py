from manim import *
from utils import *


class Pizza1(Scene):
    def construct(self):
        olives = Circle(0.15, BLACK, stroke_width=15)
        tomato = Square(0.2, color=RED_N, fill_opacity=1).rotate(PI / 3)
        capsicum = Rectangle(GREEN_N200, 0.1, 0.3, fill_opacity=1).rotate(PI / 6)

        pizzaSlice = VGroup(
            Sector(
                2.3,
                angle=PI / 3,
                color=LIGHT_BROWN,
                stroke_color=GREY_N400,
                stroke_width=4,
                fill_opacity=1,
            ),
            Sector(
                2,
                angle=PI / 3,
                color=YELLOW_N50,
                stroke_color=GREY_N400,
                stroke_width=4,
                fill_opacity=1,
            ),
            olives.copy().shift(0.5 * UP + 1.5 * RIGHT),
            olives.copy().shift(UP + RIGHT),
            tomato.copy().shift(0.3 * UP + RIGHT),
            capsicum.shift(UP * 0.4 + RIGHT * 0.5),
        )

        self.play(FadeIn(pizzaSlice))
        self.wait(1)

        pizza = VGroup(pizzaSlice)

        for i in range(0, 5):
            pizza.add(pizzaSlice.copy())

        self.play(
            Rotate(pizza[1], 2 * PI / 3, OUT, ORIGIN),
            Rotate(pizza[2], PI / 3, OUT, ORIGIN),
            Rotate(pizza[3], -PI, OUT, ORIGIN),
            Rotate(pizza[4], -2 * PI / 3, OUT, ORIGIN),
            Rotate(pizza[5], -PI / 3, OUT, ORIGIN),
            run_time=2,
        )
        self.wait(1)

        self.play(
            pizza[1].animate.shift(
                0.4 * np.cos(PI / 6) * LEFT + 0.4 * np.sin(PI / 6) * UP
            )
        )

        self.wait(5)


class Pizza2(Scene):
    def construct(self):
        olives = Circle(0.15, BLACK, stroke_width=15)
        tomato = Square(0.2, color=RED_N, fill_opacity=1).rotate(PI / 3)
        capsicum = Rectangle(GREEN_N200, 0.1, 0.3, fill_opacity=1).rotate(PI / 6)

        pizzaSlice = VGroup(
            Sector(
                2.3,
                angle=PI / 2,
                color=LIGHT_BROWN,
                stroke_color=GREY_N400,
                stroke_width=4,
                fill_opacity=1,
            ),
            Sector(
                2,
                angle=PI / 2,
                color=YELLOW_N50,
                stroke_color=GREY_N400,
                stroke_width=4,
                fill_opacity=1,
            ),
            olives.copy().shift(UP + 0.4 * RIGHT),
            olives.copy().shift(0.5 * UP + 1.5 * RIGHT),
            olives.copy().shift(1.1 * UP + 1.1 * RIGHT),
            tomato.copy().shift(1.6 * UP + 0.5 * RIGHT),
            tomato.copy().rotate(PI / 3).shift(0.3 * UP + RIGHT),
            capsicum.rotate(PI / 10).shift(UP * 0.4 + RIGHT * 0.4),
            capsicum.copy().rotate(PI / 6).shift(UP * 0.3 + RIGHT * 0.4),
        )

        self.play(FadeIn(pizzaSlice))
        self.wait(1)

        pizza = VGroup(pizzaSlice)

        for i in range(0, 3):
            pizza.add(pizzaSlice.copy())

        self.play(
            Rotate(pizza[1], PI / 2, OUT, ORIGIN),
            Rotate(pizza[2], -PI, OUT, ORIGIN),
            Rotate(pizza[3], -PI / 2, OUT, ORIGIN),
            run_time=2,
        )
        self.wait(1)

        self.play(
            pizza[0].animate.shift(
                0.4 * np.cos(PI / 4) * RIGHT + 0.4 * np.sin(PI / 4) * UP
            )
        )

        self.wait(5)


class Statement1(Scene):
    def construct(self):
        eqn2 = nMath(
            "\\text{1 slice} \\;\\;", "\\text{OF THE}", "\\;\\; \\text{6 slices}"
        ).shift(UP * 0.5)
        eqn1 = nMath("1\\ pizza \\div 6").next_to(eqn2, DOWN, buff=0.5)

        eqn2[1].set_color(ORANGE_N400)
        eqn2[2].set_color(VIOLET_N100)

        eqn3 = nMath(
            "\\text{1 slice = }",
            "\\frac{1}{6}",
            "\\;\\text{of the Pizza}",
            # color=,
        ).next_to(eqn1, DOWN, buff=0.65)

        eqn3[2].set_color(GREY_N400)

        # self.add(eqn2, eqn3)
        self.play(fadeInTex(eqn2))
        self.play(fadeInTex(eqn1))
        self.wait(2)
        self.play(fadeInTex(eqn3))

        self.wait(5)


class Statement2(Scene):
    def construct(self):
        # eqn1 = nMath("\\text{one of the four pieces}").shift(UP)
        eqn2 = nMath(
            "\\text{1 slice} \\;\\;", "\\text{OF THE}", "\\;\\; \\text{4 slices}"
        ).shift(UP * 0.5)

        eqn2[1].set_color(ORANGE_N400)
        eqn2[2].set_color(VIOLET_N100)

        eqn3 = nMath("\\frac{1}{4}", "\\;\\text{of the Pizza}").next_to(
            eqn2, DOWN, buff=0.65
        )

        eqn3[1].set_color(GREY_N400)

        # self.add(eqn2, eqn3)
        self.play(fadeInTex(eqn2))
        self.wait(2)
        self.play(fadeInTex(eqn3))

        self.wait(5)


class FractionIntro(Scene):
    def construct(self):
        title = (
            MathTex(
                "Fractions", tex_template=TexFontTemplates.droid_sans, color=GREY_N800
            )
            .scale(1.3)
            .to_edge(UP, buff=0.8)
        )

        subtitle = (
            MathTex(
                '\\text{"Part of the whole"}',
                tex_template=TexFontTemplates.droid_sans,
                color=GREY_N300,
            )
            .scale(0.9)
            .next_to(title, DOWN, buff=0.6)
        )

        eqn = nMath(
            "\\text{3 parts} \\;\\;", "\\text{OF THE}", "\\;\\; \\text{7 parts}"
        )
        eqn2 = (
            MathTex(
                "\\frac{3}{7}",
                tex_template=TexFontTemplates.droid_sans,
                color=GREY_N800,
            )
            .scale(1.3)
            .next_to(eqn, DOWN, buff=0.75)
        )

        eqn2_ = (
            MathTex(
                "\\frac{3}{7}",
                '\\text{ -- say as "three-seventh"}',
                tex_template=TexFontTemplates.droid_sans,
                color=GREY_N800,
            )
            .scale(1.1)
            .next_to(eqn, DOWN, buff=0.75)
        )

        eqn[1].set_color(ORANGE_N400)
        eqn[2].set_color(VIOLET_N100)

        # highlight(self, eqn2, buff=0.25, corner_radius=0.15, unhighlight=False)

        self.add(title)
        self.wait(1)
        self.play(Write(subtitle), run_time=2.5)

        # self.add(subtitle, eqn, eqn2)
        self.play(fadeInTex(eqn))
        self.wait(1)
        self.play(Write(eqn2), run_time=2)
        self.wait(1)
        self.play(TransformMatchingTex(eqn2, eqn2_))
        self.wait(1)
        eqn2.shift(1.7 * UP + 1.8 * LEFT)

        # Explaining Numerator and denominator
        # eqn2.shift(UP + 1.8 * LEFT)
        # self.play( eqn2.animate.shift(1.5 * UP))
        self.play(FadeOut(eqn, shift=UP), TransformMatchingTex(eqn2_, eqn2))

        hgl1 = solidHighlight(self, eqn2[0][0], buff=0.1, animate=False)
        pointer1 = Arrow(
            eqn2[0][0].get_right(),
            eqn2[0][0].get_right() + 2 * RIGHT + 0.2 * UP,
            color=GREY_N300,
        )
        numerator = nText("Numerator").next_to(
            pointer1,
            RIGHT,
        )

        hgl2 = solidHighlight(self, eqn2[0][-1], buff=0.1, animate=False)
        pointer2 = Arrow(
            eqn2[0][-1].get_right(),
            eqn2[0][-1].get_right() + 2 * RIGHT + 0.2 * DOWN,
            color=GREY_N300,
        )
        denominator = nText("Denominator").next_to(
            pointer2,
            RIGHT,
        )

        denomSub = (
            nText("(D for DOWN)")
            .scale(0.7)
            .next_to(denominator, DOWN, buff=0.3)
            .set_color(RED_N100)
        )
        self.play(
            (FadeIn(highlight) for highlight in hgl1),
        )
        self.play(
            LaggedStart(
                GrowArrow(pointer1),
                fadeInTex(numerator),
                lag_ratio=0.5,
            )
        )
        self.play(
            (FadeIn(highlight) for highlight in hgl2),
        )
        self.play(
            LaggedStart(
                GrowArrow(pointer2),
                fadeInTex(denominator),
                fadeInTex(denomSub),
                lag_ratio=0.5,
            )
        )

        self.wait(1)

        eqn4 = (
            MathTex(
                "\\frac{3}{7}",
                "\\;\\;\\text{is same as}\\;\\;",
                "3\\div 7 = 0.428",
                tex_template=TexFontTemplates.droid_sans,
                color=GREY_N800,
            ).to_edge(DOWN, buff=1)
            # .next_to(eqn, DOWN, buff=0.75)
        )

        eqn4[1].set_color(RED_N100)
        self.play(fadeInTex(eqn4))

        self.wait(5)


class Pizza3(Scene):
    def construct(self):
        olives = Circle(0.15, BLACK, stroke_width=15)
        tomato = Square(0.2, color=RED_N, fill_opacity=1).rotate(PI / 3)
        capsicum = Rectangle(GREEN_N200, 0.1, 0.3, fill_opacity=1).rotate(PI / 6)

        pizzaSlice = VGroup(
            Sector(
                2.3,
                angle=PI / 3,
                color=LIGHT_BROWN,
                stroke_color=GREY_N400,
                stroke_width=4,
                fill_opacity=1,
            ),
            Sector(
                2,
                angle=PI / 3,
                color=YELLOW_N50,
                stroke_color=GREY_N400,
                stroke_width=4,
                fill_opacity=1,
            ),
            olives.copy().shift(0.5 * UP + 1.5 * RIGHT),
            olives.copy().shift(UP + RIGHT),
            tomato.copy().shift(0.3 * UP + RIGHT),
            capsicum.shift(UP * 0.4 + RIGHT * 0.5),
        )

        self.wait(1)

        pizza = VGroup(pizzaSlice)

        for i in range(0, 5):
            pizza.add(pizzaSlice.copy())

            # self.play(
        pizza[1].rotate(2 * PI / 3, OUT, ORIGIN)
        pizza[2].rotate(PI / 3, OUT, ORIGIN)
        pizza[3].rotate(-PI, OUT, ORIGIN)
        pizza[4].rotate(-2 * PI / 3, OUT, ORIGIN)
        pizza[5].rotate(-PI / 3, OUT, ORIGIN)
        # run_time=2,
        # )
        # self.wait(1)
        self.add(pizza)

        self.play(
            pizza[1:3].animate.shift(
                0.4 * np.cos(PI / 3) * LEFT + 0.4 * np.sin(PI / 3) * UP
            )
        )

        self.play(
            pizza[3:5].animate.shift(
                0.4 * np.cos(PI / 3) * LEFT + 0.4 * np.sin(PI / 3) * DOWN
            ),
            VGroup(pizza[0], pizza[5]).animate.shift(0.4 * RIGHT),
        )

        self.wait(5)


class Pizza4(Scene):
    def construct(self):
        olives = Circle(0.15, BLACK, stroke_width=15)
        tomato = Square(0.2, color=RED_N, fill_opacity=1).rotate(PI / 3)
        capsicum = Rectangle(GREEN_N200, 0.1, 0.3, fill_opacity=1).rotate(PI / 6)

        pizzaSlice = VGroup(
            Sector(
                2.3,
                angle=PI / 2,
                color=LIGHT_BROWN,
                stroke_color=GREY_N400,
                stroke_width=4,
                fill_opacity=1,
            ),
            Sector(
                2,
                angle=PI / 2,
                color=YELLOW_N50,
                stroke_color=GREY_N400,
                stroke_width=4,
                fill_opacity=1,
            ),
            olives.copy().shift(UP + 0.4 * RIGHT),
            olives.copy().shift(0.5 * UP + 1.5 * RIGHT),
            olives.copy().shift(1.1 * UP + 1.1 * RIGHT),
            tomato.copy().shift(1.6 * UP + 0.5 * RIGHT),
            tomato.copy().rotate(PI / 3).shift(0.3 * UP + RIGHT),
            capsicum.rotate(PI / 10).shift(UP * 0.4 + RIGHT * 0.4),
            capsicum.copy().rotate(PI / 6).shift(UP * 0.3 + RIGHT * 0.4),
        )

        # self.play(FadeIn(pizzaSlice))
        self.wait(1)

        pizza = VGroup(pizzaSlice)

        for i in range(0, 3):
            pizza.add(pizzaSlice.copy())

        # self.play(
        pizza[1].rotate(PI / 2, OUT, ORIGIN)
        pizza[2].rotate(-PI, OUT, ORIGIN)
        pizza[3].rotate(-PI / 2, OUT, ORIGIN)
        #     run_time=2,
        # )

        self.add(pizza)
        self.wait(1)

        self.play(
            pizza[0:2].animate.shift(0.2 * UP), pizza[2:].animate.shift(DOWN * 0.2)
        )

        self.wait(5)


class Statements3(Scene):
    def construct(self):
        eqn = nMath("\\frac{2}{6}", "\\;\\text{of the Pizza}")
        eqn2 = nMath("\\frac{2}{6}", "= \\frac{1}{3}").next_to(eqn, DOWN, buff=0.6)

        # self.add(eqn)

        eqn3 = nMath("\\frac{2}{4}", "\\;\\text{of the Pizza}")
        eqn4 = nMath(
            "\\frac{2}{4}", "= \\frac{1}{2}", "\\;\\text{of the Pizza}"
        ).next_to(eqn3, DOWN, buff=0.6)

        # self.add(eqn3)

        self.play(fadeInTex(eqn))
        self.wait(1)
        self.play(fadeInTex(eqn2))
        highlight(self, eqn2, buff=0.2)
        self.wait(2)

        self.play(FadeOut(eqn2, eqn))

        self.play(fadeInTex(eqn3))
        self.wait(1)
        self.play(fadeInTex(eqn4))
        highlight(self, eqn4, buff=0.2)

        self.wait(2)


class Statements4(Scene):
    def construct(self):
        title = (
            MathTex(
                "\\text{Cancelling out common factors!}",
                tex_template=TexFontTemplates.droid_sans,
                color=GREY_N800,
            )
            .scale(1.1)
            .to_edge(UP, buff=0.8)
        )
        self.add(title)

        def animateCancellation(eqn, eqn11, eqn12):
            self.play(FadeIn(eqn))
            self.wait(1)
            self.play(TransformMatchingTex(eqn, eqn11), run_time=1.5)
            self.wait(1)
            hgl1 = highlight(
                self,
                [eqn11[2][0], eqn11[2][4]],
                buff=0.1,
                color=RED_N100,
                unhighlight=False,
            )
            hgl2 = highlight(
                self,
                [eqn12[2][0], eqn12[2][4]],
                buff=0.1,
                color=RED_N100,
                animate=False,
            )
            self.play(
                TransformMatchingTex(eqn11, eqn12),
                Transform(hgl1[0], hgl2[0]),
                Transform(hgl1[1], hgl2[1]),
            )

            pointer1 = CurvedArrow(
                eqn12[2][2].get_top() + 0.2 * UP,
                eqn12[4][0].get_top() + 0.2 * UP,
                color=RED_N100,
                angle=-PI / 2,
            )
            hgl3 = solidHighlight(
                self, [eqn12[2][2], eqn12[2][-1]], buff=0.1, animate=False
            )
            pointer2 = CurvedArrow(
                eqn12[2][-1].get_bottom() + 0.2 * DOWN,
                eqn12[4][-1].get_bottom() + 0.2 * DOWN,
                color=RED_N100,
                angle=PI / 2,
            )
            self.play(FadeIn(highlight) for highlight in hgl3)

            self.play(
                LaggedStart(
                    Create(pointer1),
                    Create(pointer2),
                    lag_ratio=0.5,
                ),
            )

            self.wait(1)

            self.play(FadeOut(eqn12, pointer1, pointer2, *hgl1, *hgl2, *hgl3))

        animateCancellation(
            nMath("\\frac{2}{6}"),
            nMath(
                "\\frac{2}{6}",
                "=",
                "\\frac{2\\times 1}{2 \\times 3}",
            ),
            nMath(
                "\\frac{2}{6}",
                "=",
                "\\frac{2\\times 1}{2 \\times 3}",
                "=",
                "\\frac{1}{3}",
            ),
        )

        animateCancellation(
            nMath("\\frac{2}{4}"),
            nMath(
                "\\frac{2}{4}",
                "=",
                "\\frac{2\\times 1}{2 \\times 2}",
            ),
            nMath(
                "\\frac{2}{4}",
                "=",
                "\\frac{2\\times 1}{2 \\times 2}",
                "=",
                "\\frac{1}{2}",
            ),
        )

        animateCancellation(
            nMath("\\frac{9}{12}"),
            nMath(
                "\\frac{9}{12}",
                "=",
                "\\frac{3\\times 3}{3 \\times 4}",
            ),
            nMath(
                "\\frac{9}{12}",
                "=",
                "\\frac{3\\times 3}{3 \\times 4}",
                "=",
                "\\frac{3}{4}",
            ),
        )

        eqn3 = nMath(
            "\\frac{3}{9}", "=", "\\frac{1\\times 3}{3 \\times 3}", "=", "\\frac{1}{3}"
        )
        # .next_to(eqn2, DOWN, buff=0.6)
        self.play(fadeInTex(eqn3))

        pointer1 = CurvedArrow(
            eqn3[0][0].get_top() + 0.2 * UP,
            eqn3[2][0:3].get_top() + 0.2 * UP,
            color=RED_N100,
            angle=-PI / 2,
        )
        hgl1 = solidHighlight(
            self, [eqn3[2][0:3], eqn3[2][4:]], buff=0.1, animate=False
        )
        pointer2 = CurvedArrow(
            eqn3[0][-1].get_bottom() + 0.2 * DOWN,
            eqn3[2][4:].get_bottom() + 0.2 * DOWN,
            color=RED_N100,
            angle=PI / 2,
        )
        # self.add(pointer1, pointer2, *hgl1)
        self.play(FadeIn(highlight) for highlight in hgl1)
        self.play(Create(pointer1), Create(pointer2))

        self.wait(3)

        self.play(FadeOut(eqn3, pointer1, pointer2, *hgl1))
        self.wait(1)


class CancellingFactors2(Scene):
    def construct(self):
        title = (
            MathTex(
                "\\text{Cancelling out common factors!}",
                tex_template=TexFontTemplates.droid_sans,
                color=GREY_N800,
            )
            .scale(1.1)
            .to_edge(UP, buff=0.8)
        )
        self.add(title)
        primes = nMath(
            "2", ", \\;", "3", ", \\;", "5", ", \\;", "7", color=BLACK
        ).shift(UP * 1.5)

        eqn = nMath("\\frac{12}{18}").shift(DOWN * 0.6)

        self.play(fadeInTex(primes))
        self.play(fadeInTex(eqn))

        self.wait(2)
        hgl = solidHighlight(self, primes[0], buff=0.15, unhighlight=False)
        self.wait(1)

        eqn2 = nMath("\\frac{12}{18}", "=", "\\frac{6 \\times 2}{9 \\times 2}").shift(
            DOWN * 0.6
        )
        eqn3 = nMath(
            "\\frac{12}{18}",
            "=",
            "\\frac{6 \\times 2}{9 \\times 2}",
            "=",
            "\\frac{6}{9}",
        ).shift(DOWN * 0.6)

        # self.add(primes)
        # self.add(eqn)
        self.play(TransformMatchingTex(eqn, eqn2), run_time=1.5)
        self.wait(1)
        self.play(TransformMatchingTex(eqn2, eqn3), run_time=1.5)
        self.wait(1)

        eqn4 = nMath("\\frac{6}{9}").shift(DOWN * 0.6)
        eqn5 = nMath("\\frac{6}{9}", "=", "\\frac{2 \\times 3}{3 \\times 3}").shift(
            DOWN * 0.6
        )
        eqn6 = nMath(
            "\\frac{6}{9}", "=", "\\frac{2 \\times 3}{3 \\times 3}", "=", "\\frac{2}{3}"
        ).shift(DOWN * 0.6)

        eqnFinal = nMath("\\frac{2}{3}").shift(DOWN * 0.6)

        self.play(TransformMatchingTex(eqn3, eqn4), run_time=1.5)
        self.wait(1)
        hgl2 = solidHighlight(self, primes[2], buff=0.15, animate=False)
        self.play(ReplacementTransform(*hgl, *hgl2))
        self.wait(1)
        self.play(TransformMatchingTex(eqn4, eqn5), run_time=1.5)
        self.wait(1)
        self.play(TransformMatchingTex(eqn5, eqn6), run_time=1.5)
        self.wait(1)
        self.play(TransformMatchingTex(eqn6, eqnFinal), run_time=1.5)

        self.wait(10)


class Comparision(Scene):
    def construct(self):
        title = (
            MathTex(
                "\\text{Which is greater?}",
                tex_template=TexFontTemplates.droid_sans,
                color=GREY_N800,
            )
            .scale(1.1)
            .to_edge(UP, buff=0.8)
        )
        self.add(title)

        eqn = nMath("\\frac{1}{6}").shift(3 * LEFT + DOWN * 2)
        eqn2 = nMath("\\frac{1}{6}", "=", "\\frac{1\\times 4}{6\\times 4}").shift(
            3 * LEFT + DOWN * 2
        )
        eqn3 = nMath(
            "\\frac{1}{6}", "=", "\\frac{1\\times 4}{6\\times 4}", "=", "\\frac{4}{24}"
        ).shift(3 * LEFT + DOWN * 2)

        eqn4 = nMath("\\frac{1}{4}").shift(3 * RIGHT + DOWN * 2)
        eqn5 = nMath("\\frac{1}{4}", "=", "\\frac{1\\times 6}{4\\times 6}").shift(
            3 * RIGHT + DOWN * 2
        )
        eqn6 = nMath(
            "\\frac{1}{4}", "=", "\\frac{1\\times 6}{4\\times 6}", "=", "\\frac{6}{24}"
        ).shift(3 * RIGHT + DOWN * 2)
        self.play(fadeInTex(eqn), fadeInTex(eqn4))
        self.wait(1)
        self.play(ReplacementTransform(eqn, eqn2), run_time=1.5)
        self.wait(1)
        self.play(TransformMatchingTex(eqn2, eqn3), run_time=1.5)
        self.wait(1)

        self.play(ReplacementTransform(eqn4, eqn5), run_time=1.5)
        self.wait(1)
        self.play(TransformMatchingTex(eqn5, eqn6), run_time=1.5)
        self.wait(1)

        self.wait(2)

        greater = (
            MathTex(
                "\\mathbf{<}",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.droid_sans,
            )
            .scale(1.2)
            .shift(2 * DOWN)
        )

        self.play(FadeIn(greater))

        self.wait(10)


class Circle24Highlight4(Scene):
    def construct(self):
        R = 2
        n = 24
        sector_angle = TAU / n

        # Create 24 equal sectors (pie pieces)
        sectors = VGroup()
        for i in range(n):
            start = i * sector_angle
            sec = Sector(
                R,
                start_angle=start,
                angle=sector_angle,
                fill_opacity=0.6,
                stroke_color=BLACK,
                stroke_width=1,
                color=YELLOW_N50,
            )
            sectors.add(sec)

        # Put all sectors centered
        sectors.move_to(ORIGIN)

        # Outline circle for crisp border
        outline = Circle(radius=R, stroke_color=BLACK, stroke_width=2)
        outline.move_to(ORIGIN)

        # Add sectors to scene (draw as a block for performance)
        self.play(
            LaggedStart(*[FadeIn(sec, scale=0.8) for sec in sectors], lag_ratio=0.02)
        )
        self.wait(0.6)

        # Choose 4 sectors to highlight — equally spaced: every 6th sector
        highlight_indices = [0, 1, 2, 3]
        highlights = VGroup(*[sectors[i] for i in highlight_indices])

        # Animate highlight: change fill color to purple and add glow
        self.play(
            *[
                sectors[i].animate.set_fill(RED_N100, opacity=0.9)
                for i in highlight_indices
            ],
            run_time=1,
        )

        self.wait(1.5)

        self.wait(2)


class Circle24Highlight6(Scene):
    def construct(self):
        R = 2
        n = 24
        sector_angle = TAU / n

        # Create 24 equal sectors (pie pieces)
        sectors = VGroup()
        for i in range(n):
            start = i * sector_angle
            sec = Sector(
                R,
                start_angle=start,
                angle=sector_angle,
                fill_opacity=0.6,
                stroke_color=BLACK,
                stroke_width=1,
                color=YELLOW_N50,
            )
            sectors.add(sec)

        # Put all sectors centered
        sectors.move_to(ORIGIN)

        # Outline circle for crisp border
        outline = Circle(radius=R, stroke_color=BLACK, stroke_width=2)
        outline.move_to(ORIGIN)

        # Add sectors to scene (draw as a block for performance)
        self.play(
            LaggedStart(*[FadeIn(sec, scale=0.8) for sec in sectors], lag_ratio=0.02)
        )
        self.wait(0.6)

        # Choose 4 sectors to highlight — equally spaced: every 6th sector
        highlight_indices = [0, 1, 2, 3, 4, 5]
        highlights = VGroup(*[sectors[i] for i in highlight_indices])

        # Animate highlight: change fill color to purple and add glow
        self.play(
            *[
                sectors[i].animate.set_fill(RED_N100, opacity=0.9)
                for i in highlight_indices
            ],
            run_time=1,
        )

        self.wait(1.5)

        self.wait(2)


class AddSubFraction(Scene):
    def construct(self):
        title = (
            MathTex(
                "\\text{Make the denominator same}",
                tex_template=TexFontTemplates.droid_sans,
                color=GREY_N800,
            )
            .scale(1.1)
            .to_edge(UP, buff=0.8)
        )
        self.add(title)

        eqn = nMath("\\frac{4}{9}", "+", "\\frac{1}{2}")
        eqn2_ = nMath("\\frac{4 \\times 2}{9 \\times 2}", "+", "\\frac{1}{2}").shift(
            DOWN * 0.8
        )
        eqn2 = nMath(
            "\\frac{4 \\times 2}{9 \\times 2}", "+", "\\frac{1 \\times 9}{2 \\times 9}"
        ).shift(DOWN * 0.8)
        eqn31 = nMath(
            "\\frac{8}{9 \\times 2}", "+", "\\frac{1 \\times 9}{2 \\times 9}"
        ).shift(DOWN * 0.8)
        eqn32 = nMath("\\frac{8}{18}", "+", "\\frac{1 \\times 9}{2 \\times 9}").shift(
            DOWN * 0.8
        )
        eqn33 = nMath("\\frac{8}{18}", "+", "\\frac{9}{2 \\times 9}").shift(DOWN * 0.8)
        eqn3 = nMath("\\frac{8}{18}", "+", "\\frac{9}{18}").shift(DOWN * 0.8)
        eqn4 = nMath("\\frac{8+9}{18}").next_to(eqn3, DOWN, buff=0.6)
        eqn4_ = nMath("\\frac{8+9}{18}", "= \\frac{17}{18}").next_to(
            eqn3, DOWN, buff=0.6
        )
        # self.add(eqn, eqn2, eqn3, eqn4_)

        self.play(fadeInTex(eqn))
        self.wait(1)
        self.play(eqn.animate.shift(UP * 0.8), ReplacementTransform(eqn.copy(), eqn2_))
        self.wait(1)
        self.play(ReplacementTransform(eqn2_, eqn2))
        self.wait(1)
        self.play(TransformMatchingTex(eqn2, eqn31))
        self.wait(1)
        self.play(TransformMatchingTex(eqn31, eqn32))
        self.wait(1)
        self.play(TransformMatchingTex(eqn32, eqn33))
        self.wait(1)
        self.play(TransformMatchingTex(eqn33, eqn3))
        self.wait(1)
        self.play(TransformMatchingTex(eqn3.copy(), eqn4))
        self.wait(1)
        self.play(TransformMatchingTex(eqn4, eqn4_))

        self.wait(5)


class FractionsDef(Scene):
    def construct(self):
        eqn = nMath("\\frac{part}{whole}").scale(1.2)
        self.add(eqn)
        self.wait(1)
        hgl = solidHighlight(self, eqn[0][5:], buff=0.1, unhighlight=False)
        self.play(FadeOut(*hgl))

        self.wait(4)
