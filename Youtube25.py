from manim import *
from utils import *


class Intro(Scene):
    def construct(self):
        question = MathTex(
            "\\text{Evaluate: } \\sqrt{-4}\\sqrt{-9}",
            color=BLACK,
        )
        options1 = VGroup(
            MathTex("A)", " \\ -6", color=BLACK),
            MathTex("B)", " \\ 5", color=BLACK),
            MathTex("C)", " \\ 6", color=BLACK),
            MathTex("D)", " \\ 36", color=BLACK),
        ).arrange(DOWN, aligned_edge=LEFT, center=False, buff=0.5)

        VGroup(question, options1).arrange(DOWN, buff=0.75, aligned_edge=LEFT).to_edge(
            LEFT
        ).shift(RIGHT)

        options1.shift(0.3 * RIGHT)

        val0 = ValueTracker(0)

        def get_percent1(val, next_ref, color, buff=0.75):
            value_str = f"{int(val.get_value())}%"
            percent_tex = nText(value_str, color=color).next_to(
                next_ref,
                RIGHT,
                buff=buff,
            )
            hgl = highlight(self, next_ref, buff=0.14, color=color, animate=0)

            bck = solidHighlight(
                self, percent_tex, buff=0.2, color=BLACK, animate=False
            )[0]

            return VGroup(bck, percent_tex, hgl)

        percent1 = always_redraw(
            lambda: get_percent1(val0, options1[0], color=GREEN_N100)
        )

        self.play(FadeIn(question, options1))
        self.wait(2)
        # self.remove(options1, percent1)
        self.play(FadeIn(percent1))
        self.play(val0.animate.set_value(42), run_time=2)
        self.wait(2)

        options2 = (
            VGroup(
                MathTex("A)", "\\ 6", color=BLACK),
                MathTex("B)", "\\ -6", color=BLACK),
                MathTex("C)", " \\ \\pm6", color=BLACK),
                MathTex("D)", " \\ \\text{undefined}", color=BLACK),
            )
            .arrange(DOWN, aligned_edge=LEFT, center=False, buff=0.5)
            .next_to(options1, 0, aligned_edge=LEFT)
        )
        # self.add(options2)

        self.play(
            LaggedStart(FadeOut(percent1), Transform(options1, options2), lag_ratio=0.5)
        )
        self.wait(2)

        val1 = ValueTracker(0)
        val2 = ValueTracker(0)
        val3 = ValueTracker(0)
        val4 = ValueTracker(0)

        chart = always_redraw(
            lambda: BarChart(
                values=[
                    val1.get_value(),
                    val2.get_value(),
                    val3.get_value(),
                    val4.get_value(),
                ],
                bar_names=[
                    "one",
                    "two",
                    "three",
                    "four",
                ],
                y_range=[0, 60, 10],
                y_length=3.5,
                x_length=5,
                x_axis_config={"font_size": 36},
                axis_config={
                    "include_ticks": False,
                    "include_numbers": False,
                    "color": GRAY_D,
                    "font_size": 24,
                    "tip_shape": StealthTip,
                    "stroke_width": 4,
                },
                bar_colors=[
                    "#009be2",
                    "#7769d1",
                    "#d755a3",
                    "#ff6361",
                ],
            ).shift(3.5 * RIGHT + DOWN * 0.3)
        )

        barLabels = always_redraw(
            lambda: VGroup(
                nText("A", color=BLACK).next_to(chart.bars[0], DOWN, buff=0.4),
                nText("B", color=BLACK).next_to(chart.bars[1], DOWN, buff=0.4),
                nText("C", color=BLACK).next_to(chart.bars[2], DOWN, buff=0.4),
                nText("D", color=BLACK).next_to(chart.bars[3], DOWN, buff=0.4),
            )
        )

        percents = always_redraw(
            lambda: VGroup(
                get_percent1(val1, options2[0], color="#8bdaff", buff=0.75),
                get_percent1(val2, options2[1], color="#beb4ff", buff=0.75),
                get_percent1(val3, options2[2], color="#ff9fd8", buff=0.75),
                get_percent1(val4, options2[3], color="#ff9c9a", buff=0.75),
            )
        )

        self.play(FadeIn(chart, barLabels, percents))

        self.play(
            val1.animate.set_value(8),
            val2.animate.set_value(55),
            val3.animate.set_value(11),
            val4.animate.set_value(26),
            run_time=2,
        )

        self.wait(10)


class WrongDemo(Scene):
    def construct(self):
        stmt = nMath("i = \\sqrt{-1}").to_edge(UP)
        stmt2 = nMath("\\frac{1}{i} = \\frac{1}{\\sqrt{-1}}").next_to(
            stmt, DOWN, buff=0.5
        )
        stmt3 = nMath("\\frac{1}{i} = \\sqrt{\\frac{1}{-1}}").next_to(
            stmt2, DOWN, buff=0.5
        )
        stmt4 = nMath("\\frac{1}{i} = \\sqrt{-1}", "= i").next_to(stmt3, DOWN, buff=0.5)
        stmt5 = nMath("\\frac{1}{i} = i").next_to(stmt4, DOWN, buff=0.5)
        stmt6 = nMath("1 =", "i\\cdot i", "=i^2 =", "-1").next_to(stmt4, DOWN, buff=0.5)
        stmt7 = nMath("1 =", "-1").next_to(stmt6, 0)

        self.play(fadeInTex(stmt))
        self.wait(0.5)
        self.play(fadeInTex(stmt2))
        self.wait(0.5)
        self.play(fadeInTex(stmt3))
        self.wait(0.5)
        self.play(fadeInTex(stmt4))
        self.wait(0.5)
        self.play(fadeInTex(stmt6))
        self.wait(1)
        self.play(TransformMatchingTex(stmt6, stmt7))
        self.wait(2)
        pointer = CurvedArrow(
            stmt2.get_left() + 0.5 * LEFT,
            stmt3.get_left() + 0.5 * LEFT,
            color=RED_N100,
            radius=1,
        )
        hgl = highlight(self, stmt3, buff=0.2, color=RED_N100, animate=False)
        self.play(LaggedStart(Create(pointer), Create(hgl[0]), lag_ratio=0.6))

        self.wait(5)


class CorrectDemo(Scene):
    def construct(self):
        stmt = nMath(
            "\\sqrt{a}\\sqrt{b} = \\sqrt{a\\times b} = \\sqrt{ab}",
        )
        stmt2 = nMath(
            "\\text{is defined for } a, b \\in \\mathbb{R}^+", color=GREY_N800
        ).shift(DOWN * 0.5)
        self.play(fadeInTex(stmt))
        self.wait(1)
        self.play(stmt.animate.shift(UP * 0.75), fadeInTex(stmt2))
        highlight(self, stmt2, buff=0.2, unhighlight=False)
        self.wait(10)


class part1(Scene):
    def construct(self):
        title = (
            MathTex("\\text{The Wrong Approach}", color=RED_N100)
            .scale(1.2)
            .to_edge(UP)
            .shift(0.5 * DOWN)
        )
        self.play(Write(title))

        stmt = nMath(
            "\\sqrt{-4}\\sqrt{-9} = \\sqrt{(-4)\\times(-9)} = \\sqrt{36}",
        )

        self.play(fadeInTex(stmt))
        self.wait(2)
        self.play(stmt.animate.shift(0.5 * UP))

        res1 = nMath("= 6").next_to(stmt, DOWN, buff=0.75)
        self.play(Write(res1))
        self.wait(1)

        res2 = nMath("= 6", "\\; \\text{ or }\\pm 6").next_to(res1, 0)
        self.play(TransformMatchingTex(res1, res2))

        hgl = highlight(self, res2[1], buff=0.2, color=RED_N100, unhighlight=False)

        self.wait(1)
        self.play(FadeOut(*hgl), TransformMatchingTex(res2, res1))

        self.wait(10)


class Explainer1(Scene):
    def construct(self):
        stmt = (
            MathTex("\\text{Why }\\sqrt{36} \\ne \\pm 6\\,?", color=BLACK)
            .shift(1.5 * UP)
            .scale(1.1)
        )

        self.play(fadeInTex(stmt))
        self.wait(1)

        stmt1 = nMath("x^2 = 36", color=GREY_N800).next_to(stmt, DOWN, buff=1)
        self.play(fadeInTex(stmt1))
        self.wait(1)
        axes = (
            getAxis(
                x_range=[-4, 4, 1],
                y_range=[-1, 10, 1],
                x_length=8,
                y_length=7,
                color=GREY_D,
            )
            .scale(0.9)
            .shift(2.5 * RIGHT)
        )

        A = axes.c2p(-2.5, 6.25)
        B = axes.c2p(2.5, 6.25)
        A_x = axes.c2p(-2.5, 0)
        B_x = axes.c2p(2.5, 0)

        y36 = DashedLine(A + LEFT, B + RIGHT, color=GREY_N400)
        labely36 = nMath("y=36").next_to(B, UP, buff=0.2).shift(RIGHT).scale(0.8)
        xm6 = DashedLine(A, A_x, color=GREY_N400)
        x6 = DashedLine(B, B_x, color=GREY_N400)

        labelm6 = nMath("-6").next_to(A_x, DOWN, buff=0.2).scale(0.8)
        label6 = nMath("6").next_to(B_x, DOWN, buff=0.2).scale(0.8)

        parabola = axes.plot(lambda x: x**2, x_range=[-2.8, 2.8], color=BLACK)
        graphLabel = (
            nMath("y = x^2").next_to(axes.c2p(0, 8.8), RIGHT, buff=0.3).scale(0.8)
        )

        self.play(
            LaggedStart(
                VGroup(stmt, stmt1).animate.to_edge(LEFT).shift(RIGHT),
                FadeIn(axes),
                Create(parabola),
                FadeIn(graphLabel),
                lag_ratio=0.5,
            )
        )
        self.play(Create(y36), fadeInTex(labely36))
        self.play(Create(x6), FadeIn(label6), Create(xm6), FadeIn(labelm6))
        self.wait(1)

        stmt2 = nMath("x = \\pm6").next_to(stmt1, DOWN, buff=0.5)
        self.play(fadeInTex(stmt2))
        self.wait(1)

        stmt3 = nMath("x = \\sqrt{36}", color=GREY_N800).next_to(stmt1, 0, buff=0.75)

        stmt4 = nMath("x = 6").next_to(stmt3, DOWN, buff=0.5)

        axes2 = (
            getAxis(
                x_range=[-1, 10, 1],
                y_range=[-2, 4, 1],
                x_length=7,
                y_length=6,
                color=GREY_D,
            )
            .scale(0.9)
            .shift(2.5 * RIGHT)
        )

        A = axes2.c2p(4.84, 2.2)
        Ay = axes2.c2p(0, 2.2)
        Ax = axes2.c2p(4.84, 0)

        root = axes2.plot(lambda x: x**0.5, x_range=[0, 8], color=BLACK)
        root2 = axes2.plot(lambda x: -(x**0.5), x_range=[0, 8], color=RED_N100)

        self.play(
            LaggedStart(
                FadeOut(
                    stmt1, stmt2, y36, labely36, x6, label6, xm6, labelm6, graphLabel
                ),
                AnimationGroup(Transform(axes, axes2), Transform(parabola, root)),
                lag_ratio=0.5,
            )
        )
        y6 = DashedLine(A, Ay, color=GREY_N400)
        x36 = DashedLine(A, Ax, color=GREY_N400)

        label36 = nMath("36").next_to(Ax, DOWN, buff=0.2).scale(0.8)
        label6 = nMath("6").next_to(Ay, LEFT, buff=0.2).scale(0.8)
        graphLabel = nMath("y = \\sqrt{x}").next_to(root.get_end(), UP).scale(0.8)

        self.play(fadeInTex(graphLabel), fadeInTex(stmt3))

        self.play(Create(x36), fadeInTex(label36))
        self.play(Create(y6), fadeInTex(label6))
        self.wait(1)
        self.play(fadeInTex(stmt4))

        self.wait(1)
        self.play(
            FadeOut(stmt4, stmt3),
        )
        stmt5 = nMath("\\sqrt{36} = 6").next_to(stmt3, 0)
        self.play(fadeInTex(stmt5))
        highlight(self, stmt5, buff=0.2, unhighlight=0, color=RED_N100)

        # self.add(axes2, y6, x36, labelm6, label6, root, root2)
        self.wait(10)


class Part2(Scene):
    def construct(self):
        stmt = MathTex(
            "\\text{What about }k^{\\frac{n}{m}} \\text{ where } k<0 \\, ?",
            color=BLACK,
        ).scale(1.1)

        self.play(fadeInTex(stmt))
        self.wait(1)

        context = (
            nMath("(-ve \\;  Number)^{Fraction}")
            .next_to(stmt, DOWN, buff=0.75)
            .shift(UP)
        )
        self.play(LaggedStart(stmt.animate.shift(UP), Write(context), lag_ratio=0.5))
        self.wait(1)

        stmt2 = nMath("(-5)^\\frac{2}{3}").next_to(context, DOWN, buff=0.5)
        self.play(FadeIn(stmt2))
        solidHighlight(self, stmt2, buff=0.2, unhighlight=False)

        # self.add(stmt)

        self.wait(10)


class Statement5(Scene):
    def construct(self):
        eq3 = nMath("\\text{Complex functions are multivalued!}")
        self.play(fadeInTex(eq3))
        self.wait(10)


# class Explainer32(Scene):
#     def construct(self):
#         eq1 = nMath("z = -5 = 5e^{i\\pi}").shift(2 * UP)
#         eq2 = nMath(
#             "e^{i\\pi} = e^{i(\\pi+2\\pi)} = e^{i(\\pi + 4\\pi)} = ..."
#         ).next_to(eq1, DOWN, buff=0.5)
#         eq3 = nMath(
#             "... = e^{i(\\pi-2\\pi)} = e^{i\\pi} = e^{i(\\pi+2\\pi)} = e^{i(\\pi + 4\\pi)} = ..."
#         ).next_to(eq1, DOWN, buff=0.5)

#         eq4 = nMath("z = -5 = 5e^{(2n+1)\\pi}").next_to(eq3, DOWN, buff=0.5)
#         eq5 = nMath("f(-5) = (5e^{(2n+1)\\pi})^{\\frac{2}{3}}").next_to(
#             eq4, DOWN, buff=0.5
#         )
#         self.add(eq1, eq3, eq4, eq5)
#         self.wait(10)


# class Explainer33(Scene):
#     def construct(self):
#         eq1 = nMath("f(z) = z^\\frac{1}{2}").shift(2 * UP)
#         eq2 = nMath("f(-1) = (e^{(2n+1)\\pi})^{\\frac{1}{2}}").next_to(
#             eq1, DOWN, buff=0.5
#         )
#         eq3 = nMath("\\sqrt{-1} = \\pm i").next_to(eq2, DOWN, buff=0.5)
#         eq4 = nMath("\\sqrt{-4}\\cdot\\sqrt{-9} = (\\pm2i)(\\pm3i) = (\\pm6)").next_to(
#             eq3, DOWN, buff=0.5
#         )
#         self.add(eq1, eq2, eq3, eq4)
#         self.wait(10)


class Final(Scene):
    def construct(self):
        eq1 = nMath(
            "\\sqrt{-x} = i\\sqrt{x} \\quad \\text{for }\\; x \\ge 0", color=BLACK
        )
        self.add(eq1)
        self.wait(10)


class Case1Title(Scene):
    def construct(self):
        caseTitle = nMath(
            "\\text{Case 1: Exponential Function - } \\; f(x) = a^x",
            color=GREY_N500,
        ).scale(1.1)

        self.play(Write(caseTitle), run_time=3)
        self.wait(5)


class Part2Case1(Scene):
    def construct(self):
        axes = getAxis([-5, 5], [-5, 18], x_length=7, y_length=6)

        plot = axes.plot(
            lambda x: 2**x + 0.1,
            [-4, 4],
            stroke_color=[GREEN_A, GREEN],
            sheen_direction=UP + RIGHT,
            stroke_width=6,
        )
        functionLabel = nMath("y = a^x").to_corner(UR, buff=0.8)
        plotLabel = MathTex("a > 1", color=GREY_E).next_to(plot, RIGHT, buff=0.1)
        hgl1 = highlight(self, plotLabel, buff=0.2, color=GREEN_N200, animate=False)

        plot2 = axes.plot(
            lambda x: 2 ** (-x) + 0.1,
            [-4, 4],
            stroke_color=[BLUE_A, NUMBRIK_COLOR],
            sheen_direction=UP + LEFT,
            stroke_width=6,
        )
        plot2Label = MathTex("0 < a < 1", color=GREY_E).next_to(plot2, LEFT, buff=0.1)
        hgl2 = highlight(self, plot2Label, buff=0.2, color=NUMBRIK_COLOR, animate=False)

        self.play(
            LaggedStart(
                Create(axes),
                fadeInTex(functionLabel),
                Create(plot),
                Write(plotLabel),
                Create(*hgl1),
                Create(plot2),
                Write(plot2Label),
                Create(*hgl2),
                lag_ratio=0.7,
            )
        )

        self.wait(5)


class Part2Case1Conclusion(Scene):
    def construct(self):
        conclusion = nMath("(-5)^\\frac{2}{3} = \\,Undefined")
        self.play(fadeInTex(conclusion))
        highlight(self, conclusion, buff=0.2, unhighlight=False)
        self.wait(5)


class Case2Title(Scene):
    def construct(self):
        caseTitle = nMath(
            "\\text{Case 2: Power Functions - } \\; f(x) = x^\\frac{n}{m}",
            color=GREY_N500,
        ).scale(1.1)

        self.play(Write(caseTitle), run_time=3)
        self.wait(3)


class Part2Case2(Scene):
    def construct(self):
        axes = getAxis([-5, 5], [-17, 17], x_length=6, y_length=6).shift(1.5 * LEFT)

        functionLabel = nMath("y = x^\\frac{n}{m}").to_corner(UR, buff=0.8)

        plot = axes.plot(
            lambda x: x**2,
            [-4, 4],
            stroke_color=[GREEN_N100],
            stroke_width=6,
        )

        plotLabel = nMath("f(x) = x", "^2", color=GREY_E).next_to(axes, RIGHT, buff=0.7)

        plot2 = axes.plot(
            lambda x: x**3,
            [-2.5, 2.5],
            stroke_color=[GREEN_N100],
            stroke_width=6,
        )

        plotLabel2 = nMath("f(x) = x", "^3", color=GREY_E).next_to(plotLabel, 0)

        self.play(
            LaggedStart(
                Create(axes),
                Create(plot),
                # Create(plot2),
                # Write(plot2Label),
                lag_ratio=0.7,
            ),
            fadeInTex(plotLabel),
            fadeInTex(functionLabel),
        )
        self.wait(1)
        self.play(
            ReplacementTransform(plot, plot2),
            ReplacementTransform(plotLabel, plotLabel2),
        )

        plot3 = axes.plot(
            lambda x: x**4,
            [-2, 2],
            stroke_color=[GREEN_N100],
            stroke_width=6,
        )

        plotLabel3 = nMath("f(x) = x", "^4", color=GREY_E).next_to(
            plotLabel,
            0,
        )

        self.wait(1)
        self.play(
            ReplacementTransform(plot2, plot3),
            ReplacementTransform(plotLabel2, plotLabel3),
        )

        def power_(x):
            if x >= 0:
                return 5 * x ** (1 / 3)
            else:
                return x**2

        plot4 = axes.plot(
            lambda x: 5 * x ** (1 / 3) if x >= 0 else -5 * ((-x) ** (1 / 3)),
            [-4, 4],
            stroke_color=[GREEN_N100],
            stroke_width=6,
        )

        plotLabel4 = nMath("f(x) = x", "^\\frac{1}{3}", color=GREY_E).next_to(
            plotLabel, 0
        )

        self.wait(1)
        self.play(
            ReplacementTransform(plot3, plot4),
            ReplacementTransform(plotLabel3, plotLabel4),
        )

        plot45 = axes.plot(
            lambda x: 4 * x**0.5,
            [0, 4],
            stroke_color=[GREEN_N100],
            stroke_width=6,
        )

        plotLabel45 = nMath("f(x) = x", "^\\frac{1}{2}", color=GREY_E).next_to(
            plotLabel, 0
        )

        self.wait(1)
        self.play(
            ReplacementTransform(plot4, plot45),
            ReplacementTransform(plotLabel4, plotLabel45),
        )

        plot5 = axes.plot(
            lambda x: 3 * x ** (2 / 3) if x >= 0 else 3 * ((-x) ** (2 / 3)),
            [-4, 4],
            stroke_color=[GREEN_N100],
            stroke_width=6,
        )

        plotLabel5 = nMath("f(x) = x", "^\\frac{2}{3}", color=GREY_E).next_to(
            plotLabel, 0
        )

        self.wait(1)
        self.play(
            ReplacementTransform(plot45, plot5),
            ReplacementTransform(plotLabel45, plotLabel5),
        )

        plot6 = axes.plot(
            lambda x: 5 * x ** (1 / 4),
            [0, 4],
            stroke_color=[GREEN_N100],
            stroke_width=6,
        )

        plotLabel6 = nMath("f(x) = x", "^\\frac{1}{4}", color=GREY_E).next_to(
            plotLabel, 0
        )

        self.wait(1)
        self.play(
            ReplacementTransform(plot5, plot6),
            ReplacementTransform(plotLabel5, plotLabel6),
        )
        self.wait(1)

        marker = Circle(radius=2.2, color=RED_N100).move_to(
            axes.get_origin() + 1.5 * DOWN + 1.5 * LEFT
        )

        self.play(Create(marker))
        self.wait(0.5)

        labelCaution = (
            nMath("x \\ge 0 \\ for \\ m = even")
            .scale(0.9)
            .next_to(
                marker,
                RIGHT,
                buff=0.5,
            )
        )

        labelCaution.set_z_index(0.2)
        self.play(fadeInTex(labelCaution))
        # highlight(self, labelCaution, buff=0.2, color=RED_N100, unhighlight=False)

        self.wait(5)


class Part2Case2CoprimeExplainer(Scene):
    def construct(self):
        stmt1 = nMath("f(x) = x^\\frac{n}{m}, \\quad", "(n, m) = 1").shift(2.5 * UP)
        stmt1_ = nMath("n,\\, m \\text{ are coprime}", color=GREY_N800).next_to(
            stmt1, DOWN, buff=0.5
        )
        stmt2 = (
            nMath("(-1)^\\frac{1}{3} = -1").scale(0.9).next_to(stmt1_, DOWN, buff=0.75)
        )
        stmt3 = (
            nMath("(-1)^\\frac{2}{6}", "= \\sqrt[6]{(-1)^2} = 1")
            .scale(0.9)
            .next_to(stmt2, DOWN, buff=0.5)
        )
        stmt4 = (
            nMath("= \\left( \\sqrt[6]{-1} \\right)^2 = Undefined")
            .scale(0.9)
            .next_to(stmt3[1], DOWN, buff=0.2, aligned_edge=LEFT)
        )

        self.add(stmt1, stmt1_)

        self.wait(1)
        self.play(fadeInTex(stmt2))

        self.wait(1)
        self.play(fadeInTex(stmt3))

        self.wait(1)
        self.play(fadeInTex(stmt4))

        self.wait(10)


class Part2Case2Conclusion(Scene):
    def construct(self):
        conclusion = nMath("(-5)^\\frac{2}{3} = 2.92")
        self.play(fadeInTex(conclusion))
        highlight(self, conclusion, buff=0.2, unhighlight=False)
        self.wait(5)


class case3Title(Scene):
    def construct(self):
        theta = ValueTracker(PI / 3)

        caseTitle = nMath(
            "\\text{Case 3: Beyond domain -} \\; \\text{Complex Numbers}",
            color=GREY_N500,
        ).scale(1.1)

        self.play(Write(caseTitle), run_time=3)

        self.wait(5)


class EulersEqn(Scene):
    def construct(self):
        axis = getAxis([-1, 5], [-1, 5])
        # .shift(LEFT * 2.5)
        labelx = axis.get_x_axis_label(
            nMath("Re", color=BLACK).scale(0.8), direction=DOWN, buff=0.5
        )
        labely = axis.get_y_axis_label(
            nMath("Im", color=BLACK).scale(0.8), direction=LEFT, buff=0.5
        )

        theta = ValueTracker(PI / 4)

        def getZ():
            return (
                axis.get_origin()
                + 4 * np.sin(theta.get_value()) * UP
                + 4 * np.cos(theta.get_value()) * RIGHT
            )

        z_vector = always_redraw(
            lambda: Arrow(
                axis.get_origin(),
                getZ(),
                buff=0,
            )
            .set_color_by_gradient([GREEN_N100, GREEN_N200])
            .set_sheen_direction(
                np.sin(theta.get_value()) * UP + np.cos(theta.get_value()) * RIGHT,
            )
        )

        helper1 = DashedLine(
            getZ(),
            axis.x_axis.get_projection(getZ()),
            color=GREY_N200,
            dash_length=0.1,
            dashed_ratio=0.8,
        )

        xcord = nText("x").next_to(helper1.get_end(), DOWN, buff=0.3)

        helper2 = DashedLine(
            getZ(),
            axis.y_axis.get_projection(getZ()),
            color=GREY_N200,
            dash_length=0.1,
            dashed_ratio=0.8,
        )

        ycord = nText("y").next_to(helper2.get_end(), LEFT, buff=0.3)

        labelZ = always_redraw(
            lambda: nMath("z").move_to(
                axis.get_origin()
                + 4.4 * np.sin(theta.get_value()) * UP
                + 4.4 * np.cos(theta.get_value()) * RIGHT,
            )
        )
        tmpLabelZ = labelZ.copy()

        self.play(
            LaggedStart(
                Create(axis),
                FadeIn(labelx, labely),
                GrowArrow(z_vector),
                FadeIn(tmpLabelZ),
                Create(helper1),
                FadeIn(xcord, shift=UP * 0.5),
                Create(helper2),
                FadeIn(ycord, shift=RIGHT * 0.5),
                lag_ratio=0.5,
            )
        )

        angle = always_redraw(
            lambda: Arc(
                0.5, 0, theta.get_value(), arc_center=axis.get_origin(), color=GREY_N400
            )
        )

        labelZFull = nMath("z", "= x + iy").next_to(tmpLabelZ, 0, aligned_edge=LEFT)

        self.play(TransformMatchingTex(tmpLabelZ, labelZFull))
        self.wait(1)

        # label1 = nMath("\\mathbf{\\theta} = \\;").to_edge(UP).shift(LEFT)
        # label2 = always_redraw(
        #     lambda: nText(
        #         "" + str(round(theta.get_value(), 2)) + " rad",
        #     ).next_to(label1, RIGHT, buff=0.2)
        # )

        labelAngle = (
            nMath(
                "\\mathbf{\\theta}",
            )
            .next_to(angle, RIGHT, buff=0.3)
            .shift(UP * 0.2)
        )

        labelR = nMath("r").next_to(z_vector, LEFT, buff=-1.2).shift(UP * 0.4)

        xDist = nMath("r\\cos{\\mathbf{\\theta}}").next_to(z_vector, UP, buff=0.2)
        yDist = nMath("r\\sin{\\mathbf{\\theta}}").next_to(z_vector, RIGHT, buff=0.2)

        # self.add(axis, labelx, labely, z_vector, helper1, xDist, yDist)
        # self.add(angle, labelR, labelZ, labelAngle)
        # shift_scene_up(self, LEFT * 3)

        # shift_scene_up(self, 3 * LEFT)

        eqn1 = nMath(
            "z",
            "=",
            "r\\cos{\\mathbf{\\theta}}",
            "+",
            "i",
            "r\\sin{\\mathbf{\\theta}}",
        ).next_to(labelZ[0], 0, aligned_edge=LEFT + DOWN)
        eqn2 = nMath(
            "z",
            "=",
            "r",
            "(",
            "\\cos{\\mathbf{\\theta}}",
            "+",
            "i",
            "\\sin{\\mathbf{\\theta}}",
            ")",
        ).next_to(labelZ[0], 0, aligned_edge=LEFT + DOWN)
        eqn3 = nMath("z", "=", "re^{i\\mathbf{\\theta}}").next_to(
            labelZ[0], 0, aligned_edge=LEFT + DOWN
        )
        # self.add(eqn1, eqn2, eqn3)

        self.play(LaggedStart(Create(angle), FadeIn(labelAngle), lag_ratio=0.5))
        self.wait(1)

        self.play(FadeOut(xcord, ycord, labelZFull), FadeIn(labelZ))
        self.wait(1)
        self.play(FadeIn(labelR))
        self.wait(1)
        self.play(LaggedStart(fadeInTex(xDist), fadeInTex(yDist), lag_ratio=0.5))
        self.wait(1)
        self.play(
            ReplacementTransform(labelZ[0], eqn1[0]),
            ReplacementTransform(xDist[0], eqn1[2]),
            ReplacementTransform(yDist[0], eqn1[5]),
            FadeIn(eqn1[1], eqn1[3:5]),
        )
        self.wait(0.5)
        self.play(TransformMatchingTex(eqn1, eqn2))
        self.wait(1)
        self.play(TransformMatchingTex(eqn2, eqn3))
        highlight(self, eqn3, buff=0.2, color=RED_N100, unhighlight=False)

        self.wait(5)


class Part2Case3Log(Scene):
    def construct(self):
        theta = ValueTracker(0)

        stmt1 = nMath("f(z)", "=", "\\ln{", "z", "}", color=GREY_N800).scale(1.1)

        stmt3 = (
            nMath(
                "f(z)",
                "=",
                "\\ln{",
                "r",
                "\\cdot",
                "e^{i\\mathbf{\\theta}}",
                "}",
                color=GREY_N800,
            )
            .scale(1.1)
            .next_to(stmt1, 0)
        )

        stmt4 = nMath(
            "f(z)",
            "=",
            "\\ln{z} =",
            "\\ln{",
            "r",
            "}",
            "+",
            "i\\mathbf{\\theta}",
            color=GREY_N800,
        ).scale(1.1)

        stmt2 = (
            nMath("z = r\\cdot e^{i\\mathbf{\\theta}}", color=GREY_N800)
            .scale(0.9)
            .next_to(stmt4, UP, buff=0.5)
        )

        label1 = nMath(
            "\\mathbf{\\theta} =",
        ).scale(0.8)

        label1[0][0].scale(1.1)

        stmt4[-1][1].scale(1.1)

        self.play(fadeInTex(stmt1))
        self.wait(1)

        # self.add(stmt2, stmt4)

        axes = getAxis().shift(LEFT * 3.5)

        z_vector = always_redraw(
            lambda: Arrow(
                axes.get_origin(),
                axes.get_origin()
                + 2.5 * np.sin(theta.get_value()) * UP
                + 2.5 * np.cos(theta.get_value()) * RIGHT,
                buff=0,
            )
            .set_color_by_gradient([GREEN_N100, GREEN_N200])
            .set_sheen_direction(
                np.sin(theta.get_value()) * UP + np.cos(theta.get_value()) * RIGHT,
            )
        )

        labelz1 = nMath("z = r\\cdot e^{i\\mathbf{\\theta}}").to_edge(UP)

        axes2 = getAxis(
            [-2, 2],
            [-7, 7],
        ).shift(RIGHT * 3.5)

        labelx = axes.get_x_axis_label(
            nMath("Re", color=GREY_N500).scale(0.6), direction=DOWN, buff=0.5
        )

        labely = axes.get_y_axis_label(
            nMath("Im", color=GREY_N500).scale(0.6), direction=LEFT, buff=0.5
        )

        labelx2 = axes2.get_x_axis_label(
            nMath("Re", color=GREY_N500).scale(0.6), direction=DOWN, buff=0.5
        )

        labely2 = axes2.get_y_axis_label(
            nMath("Im", color=GREY_N500).scale(0.6), direction=LEFT, buff=0.5
        )

        zPlane = (
            nText("z-plane", color=GREY_N100)
            .scale(0.8)
            .next_to(axes.y_axis, LEFT, buff=0.5)
            .shift(2 * UP)
        )

        fzPlane = (
            nText("f(z)-plane", color=GREY_N100)
            .scale(0.8)
            .next_to(axes2.y_axis, LEFT, buff=0.5)
            .shift(2 * UP)
        )

        dot = always_redraw(lambda: Dot(axes2.c2p(1, theta.get_value()), color=BLUE))

        # Animation part1
        self.play(TransformMatchingTex(stmt1, stmt3), run_time=1.5)
        self.wait(0.5)
        self.play(TransformMatchingTex(stmt3, stmt4), run_time=1.5)

        self.play(
            LaggedStart(
                stmt4.animate.scale(0.8).shift(DOWN * 2),
                Create(axes),
                FadeIn(labelx, labely),
                Create(axes2),
                FadeIn(labelx2, labely2),
                fadeInTex(zPlane),
                fadeInTex(fzPlane),
                lag_ratio=0.5,
            )
        )
        self.wait(1)

        self.play(GrowArrow(z_vector), FadeIn(dot))
        self.play(theta.animate.set_value(PI / 3))
        self.wait(1)

        # After animation part1
        label21 = always_redraw(
            lambda: nText("" + str(round(theta.get_value() / np.pi, 2)))
            .scale(0.8)
            .next_to(label1, RIGHT, buff=0.1)
        )

        label22 = always_redraw(
            lambda: nMath(
                "\\pi",
            )
            .scale(0.9)
            .next_to(label21, RIGHT, buff=0.1, aligned_edge=DOWN)
        )

        labelTheta = (
            VGroup(label1, label21, label22).move_to(ORIGIN).to_edge(UP, buff=0.7)
        )

        angle = always_redraw(
            lambda: Arc(
                0.5, 0, theta.get_value(), arc_center=axes.get_center(), color=GREY_N400
            )
        )

        labelAngle = (
            nMath(
                "\\mathbf{\\theta}",
            )
            .scale(0.9)
            .next_to(angle, RIGHT)
            .shift(UP * 0.2)
        )

        labelR = (
            nMath("r").scale(0.8).next_to(z_vector, LEFT, buff=-0.4).shift(UP * 0.2)
        )

        labelZ = (
            nMath("z")
            .scale(0.8)
            .move_to(
                axes.get_origin()
                + 2.85 * np.sin(theta.get_value()) * UP
                + 2.85 * np.cos(theta.get_value()) * RIGHT,
            )
        )

        dotZ = Dot(z_vector.get_end(), radius=0.05, color=GREY_N200)

        labelDot = (
            nMath("\\ln{z}")
            .move_to(axes2.c2p(1, theta.get_value()) + 0.7 * RIGHT)
            .scale(0.8)
        )

        pathHgl = DashedLine(
            axes2.c2p(1, theta.get_value()) + UP * 2.5,
            axes2.c2p(1, theta.get_value()) + DOWN * 3,
            color=YELLOW_N50,
            z_index=-0.2,
            dash_length=0.2,
            dashed_ratio=0.8,
        )

        path = TracedPath(
            lambda: axes2.c2p(1, theta.get_value()), stroke_color=BLUE, stroke_width=6
        )

        def mark():
            pointer = Arrow(
                z_vector.get_end(),
                dot.get_center(),
                color=GREY_N50,
                buff=0.3,
            ).set_opacity(0.5)

            markerDot = Dot(dot.get_center(), color=GREY_N200, z_index=-0.1)
            marker0 = Circle(arc_center=dot.get_center(), color=RED_N100, radius=0.3)

            self.play(
                LaggedStart(
                    GrowArrow(pointer),
                    Create(marker0),
                    lag_ratio=0.5,
                ),
            )
            self.add(markerDot)
            self.wait(1)
            self.play(FadeOut(pointer))

        # Animation part2
        self.play(
            LaggedStart(
                Create(dotZ),
                FadeIn(labelZ),
                FadeIn(labelR),
                Create(angle),
                FadeIn(labelAngle),
                FadeIn(labelDot),
                lag_ratio=0.3,
            )
        )
        self.wait(1)

        mark()
        self.wait(1)

        brace1 = Brace(stmt4[3:6], DOWN, color=GREY_N500)
        label3 = nText("constant").scale(0.7).next_to(brace1, DOWN)

        self.play(
            LaggedStart(
                Write(brace1),
                FadeIn(label3),
                FadeOut(labelZ, labelR, labelDot),
                ReplacementTransform(labelAngle, labelTheta),
                lag_ratio=0.5,
            )
        )

        self.wait(1)

        self.play(theta.animate.set_value(PI + 1), run_time=4, rate_func=there_and_back)
        self.wait(1)

        self.add(path)
        self.play(Create(pathHgl))
        self.wait(1)

        self.play(theta.animate.increment_value(2 * PI), run_time=3)
        mark()

        self.play(theta.animate.increment_value(-4 * PI), run_time=4)
        mark()

        # self.add(pathHgl)
        # self.play(theta.animate .set_value(2 * PI))

        # self.add(dot, axes, z_vector, path)

        # self.play(axes.animate.shift(LEFT * 2 + UP * 2).scale(0.8))
        # self.play(theta.animate.set_value(4 * PI))

        # self.play(LaggedStart(Create(axes), GrowArrow(z_vector), lag_ratio=0.7))
        # self.play(
        #     LaggedStart(
        #         FadeIn(labelZ),
        #         FadeIn(labelR),
        #         Create(angle),
        #         FadeIn(labelAngle),
        #         lag_ratio=0.5,
        #     )
        # )
        # self.wait(1)
        # self.play(
        #     FadeOut(labelR, labelAngle),
        #     axes.animate.shift(DOWN),
        #     FadeIn(label1, label2, shift=UP * 0.5),
        # )
        # self.play(
        #     theta.animate.increment_value(PI / 2), run_time=5, rate_func=there_and_back
        # )
        # self.wait(1)

        # self.play(
        #     LaggedStart(
        #         AnimationGroup(
        #             axes.animate.scale(0.6).shift(LEFT * 1.5).set_color(GREY_N200),
        #         ),
        #         Create(axes2),
        #         Create(dot),
        #         FadeIn(labelDot),
        #         lag_ratio=0.5,
        #     )
        # )
        # self.add(path)
        # self.wait(1)

        # def mark():
        #     markerDot = Dot(dot.get_center(), color=GREY_N200, z_index=-0.1)
        #     marker0 = Circle(arc_center=dot.get_center(), color=RED_N100, radius=0.3)
        #     markerPointer0 = Arrow(
        #         z_vector.get_end(), dot.get_center(), color=GREY_N100, buff=0.3
        #     )
        #     self.play(Create(marker0), GrowArrow(markerPointer0), Create(markerDot))

        # self.play(FadeOut(labelZ), FadeIn(dotZ))

        # mark()

        # self.play(theta.animate.increment_value(2 * PI), run_time=2)
        # mark()

        # self.play(theta.animate.increment_value(2 * PI), run_time=2)
        # mark()

        # self.play(theta.animate.set_value(-2 * PI + PI / 3), run_time=4)
        # mark()

        self.wait(5)


class Part3Case3PreFinal(Scene):
    def construct(self):
        theta = ValueTracker(0)

        stmt1 = nMath("f(z)", "=", "z^\\frac{2}{3}", color=GREY_N800).scale(1.1)

        stmt4 = nMath(
            "f(z)",
            "=",
            "z^\\frac{2}{3}",
            "=",
            "r^\\frac{2}{3}",
            "e^{i\\frac{2\\mathbf{\\theta}}{3}}",
            color=GREY_N800,
        ).scale(1.1)

        label1 = nMath(
            "\\mathbf{\\theta} =",
        ).scale(0.8)
        label1[0][0].scale(1.1)

        stmt4[-1][1].scale(1.1)

        axes = getAxis().shift(LEFT * 3.5)
        axes2 = getAxis(
            [-2, 2],
            [-7, 7],
        ).shift(RIGHT * 3.5)

        z_vector = always_redraw(
            lambda: Arrow(
                axes.get_origin(),
                axes.get_origin()
                + 2.5 * np.sin(theta.get_value()) * UP
                + 2.5 * np.cos(theta.get_value()) * RIGHT,
                buff=0,
            )
            .set_color_by_gradient([GREEN_N100, GREEN_N200])
            .set_sheen_direction(
                np.sin(theta.get_value()) * UP + np.cos(theta.get_value()) * RIGHT,
            )
        )

        fz_vector = always_redraw(
            lambda: Arrow(
                axes2.get_origin(),
                axes2.get_origin()
                + 1.8 * np.sin(2 / 3 * theta.get_value()) * UP
                + 1.8 * np.cos(2 / 3 * theta.get_value()) * RIGHT,
                buff=0,
            )
            .set_color_by_gradient([BLUE_A, NUMBRIK_COLOR_200])
            .set_sheen_direction(
                np.sin(theta.get_value()) * UP + np.cos(theta.get_value()) * RIGHT,
            )
        )

        zPlane = (
            nText("z-plane", color=GREY_N100)
            .scale(0.8)
            .next_to(axes.y_axis, LEFT, buff=1.2)
            .shift(3 * UP)
        )

        fzPlane = (
            nText("f(z)-plane", color=GREY_N100)
            .scale(0.8)
            .next_to(axes2.y_axis, RIGHT, buff=0.8)
            .shift(3 * UP)
        )

        labelx = axes.get_x_axis_label(
            nMath("Re", color=GREY_N500).scale(0.6), direction=DOWN, buff=0.5
        )

        labely = axes.get_y_axis_label(
            nMath("Im", color=GREY_N500).scale(0.6), direction=LEFT, buff=0.5
        )

        labelx2 = axes2.get_x_axis_label(
            nMath("Re", color=GREY_N500).scale(0.6), direction=DOWN, buff=0.5
        )

        labely2 = axes2.get_y_axis_label(
            nMath("Im", color=GREY_N500).scale(0.6), direction=LEFT, buff=0.5
        )

        # Animation part1
        self.play(fadeInTex(stmt1))
        self.wait(1)
        self.play(TransformMatchingTex(stmt1, stmt4), run_time=1.5)
        self.wait(0.5)

        self.play(
            LaggedStart(
                stmt4.animate.scale(0.8).shift(DOWN * 2.5),
                Create(axes),
                FadeIn(labelx, labely),
                Create(axes2),
                FadeIn(labelx2, labely2),
                fadeInTex(zPlane),
                fadeInTex(fzPlane),
                lag_ratio=0.5,
            )
        )
        self.wait(1)
        self.play(
            LaggedStart(
                GrowArrow(z_vector),
                GrowArrow(fz_vector),
                lag_ratio=0.5,
            )
        )
        self.play(theta.animate.set_value(PI), run_time=2)
        self.wait(1)

        # After Animation part1
        label21 = always_redraw(
            lambda: nText("" + str(round(theta.get_value() / np.pi, 2)))
            .scale(0.8)
            .next_to(label1, RIGHT, buff=0.1)
        )
        label22 = always_redraw(
            lambda: nMath(
                "\\pi",
            )
            .scale(0.9)
            .next_to(label21, RIGHT, buff=0.1, aligned_edge=DOWN)
        )

        labelTheta = (
            VGroup(label1, label21, label22).move_to(ORIGIN).to_edge(UP, buff=0.7)
        )

        labelPtZ = (
            nMath("-5")
            .scale(0.7)
            .next_to(axes.get_origin() + LEFT * 2.5, DOWN, buff=0.3)
        )

        angle = always_redraw(
            lambda: Arc(
                0.5, 0, theta.get_value(), arc_center=axes.get_center(), color=GREY_N400
            )
        )

        labelAngle = (
            nMath(
                "\\mathbf{\\theta} = \\pi",
            )
            .scale(0.8)
            .next_to(angle, RIGHT + UP, buff=0)
        )

        labelR = nMath("r = 5").scale(0.75).next_to(z_vector, UP, buff=0.1)

        dotZ = Dot(z_vector.get_end(), radius=0.05, color=GREY_N200)

        dot = always_redraw(
            lambda: Dot(axes2.c2p(1, theta.get_value()), color=GREEN_N200)
        )

        def mark():
            pointer = Arrow(
                z_vector.get_end(),
                dot.get_center(),
                color=GREY_N50,
                buff=0.3,
            ).set_opacity(0.5)

            markerDot = Dot(dot.get_center(), color=GREY_N200, z_index=-0.1)
            marker0 = Circle(arc_center=dot.get_center(), color=RED_N100, radius=0.3)

            self.play(
                LaggedStart(
                    GrowArrow(pointer),
                    Create(marker0),
                    lag_ratio=0.5,
                ),
            )
            self.add(markerDot)
            self.wait(1)
            self.play(FadeOut(pointer))

        labelPtfZ2 = (
            nMath("5^\\frac{2}{3}e^{i\\frac{2\\pi}{3}}")
            .scale(0.7)
            .next_to(fz_vector.get_end(), UP + LEFT, buff=0.25)
        )

        def mark(label):
            pointer = Arrow(
                z_vector.get_end(),
                fz_vector.get_end(),
                color=GREY_N50,
                buff=0.3,
            ).set_opacity(0.5)

            markerDot = Dot(
                fz_vector.get_end(),
                color=GREY_N100,
            )
            marker0 = Circle(arc_center=fz_vector.get_end(), color=RED_N100, radius=0.3)

            self.play(
                LaggedStart(
                    GrowArrow(pointer),
                    FadeIn(markerDot),
                    Create(marker0),
                    FadeIn(label),
                    lag_ratio=0.5,
                ),
            )
            self.wait(1)
            self.play(FadeOut(pointer))

        # Animation part2

        self.play(
            LaggedStart(
                Create(dotZ),
                FadeIn(labelPtZ),
                FadeIn(labelR),
                Create(angle),
                FadeIn(labelAngle),
                lag_ratio=0.3,
            )
        )
        mark(labelPtfZ2)

        self.play(
            LaggedStart(
                FadeOut(labelR),
                ReplacementTransform(labelAngle, labelTheta),
                lag_ratio=0.5,
            )
        )

        self.wait(1)

        self.play(theta.animate.set_value(-PI), run_time=3)
        labelPtfZ3 = (
            nMath("5^\\frac{2}{3}e^{-i\\frac{2\\pi}{3}}")
            .scale(0.7)
            .next_to(fz_vector.get_end(), UP + LEFT, buff=0.25)
        )
        mark(labelPtfZ3)
        self.wait(1)

        self.play(theta.animate.set_value(3 * PI), run_time=4.5)
        labelPtfZ1 = (
            nMath("5^\\frac{2}{3}")
            .scale(0.7)
            .next_to(fz_vector.get_end(), DOWN, buff=0.4)
        )
        mark(labelPtfZ1)
        self.wait(1)

        self.wait(5)


class Part3Case3Final(Scene):
    def construct(self):
        theta = ValueTracker(0)

        stmt1 = nMath("f(z)", "=", "z^\\frac{1}{2}", color=GREY_N800).scale(1.1)

        stmt4 = nMath(
            "f(z)",
            "=",
            "z^\\frac{1}{2}",
            "=",
            "\\sqrt{r}",
            "e^{i\\frac{\\mathbf{\\theta}}{2}}",
            color=GREY_N800,
        ).scale(1.1)

        label1 = nMath(
            "\\mathbf{\\theta} =",
        ).scale(0.8)

        label1[0][0].scale(1.1)

        stmt4[-1][1].scale(1.1)

        axes = getAxis().shift(LEFT * 3.5)
        axes2 = getAxis(
            [-2, 2],
            [-7, 7],
        ).shift(RIGHT * 3.5)

        z_vector = always_redraw(
            lambda: Arrow(
                axes.get_origin(),
                axes.get_origin()
                + 2 * np.sin(theta.get_value()) * UP
                + 2 * np.cos(theta.get_value()) * RIGHT,
                buff=0,
            )
            .set_color_by_gradient([GREEN_N100, GREEN_N200])
            .set_sheen_direction(
                np.sin(theta.get_value()) * UP + np.cos(theta.get_value()) * RIGHT,
            )
        )

        labelPtZ = (
            nMath("-1").scale(0.7).next_to(axes.get_origin() + LEFT * 2, DOWN, buff=0.3)
        )

        fz_vector = always_redraw(
            lambda: Arrow(
                axes2.get_origin(),
                axes2.get_origin()
                + 2 * np.sin(0.5 * theta.get_value()) * UP
                + 2 * np.cos(0.5 * theta.get_value()) * RIGHT,
                buff=0,
            )
            .set_color_by_gradient([BLUE_A, NUMBRIK_COLOR_200])
            .set_sheen_direction(
                np.sin(theta.get_value()) * UP + np.cos(theta.get_value()) * RIGHT,
            )
        )

        dot = always_redraw(
            lambda: Dot(axes2.c2p(1, theta.get_value()), color=GREEN_N200)
        )

        zPlane = (
            nText("z-plane", color=GREY_N100)
            .scale(0.8)
            .next_to(axes.y_axis, LEFT, buff=1.2)
            .shift(3 * UP)
        )

        fzPlane = (
            nText("f(z)-plane", color=GREY_N100)
            .scale(0.8)
            .next_to(axes2.y_axis, RIGHT, buff=0.8)
            .shift(3 * UP)
        )

        labelx = axes.get_x_axis_label(
            nMath("Re", color=GREY_N500).scale(0.6), direction=DOWN, buff=0.5
        )

        labely = axes.get_y_axis_label(
            nMath("Im", color=GREY_N500).scale(0.6), direction=LEFT, buff=0.5
        )

        labelx2 = axes2.get_x_axis_label(
            nMath("Re", color=GREY_N500).scale(0.6), direction=DOWN, buff=0.5
        )

        labely2 = axes2.get_y_axis_label(
            nMath("Im", color=GREY_N500).scale(0.6), direction=LEFT, buff=0.5
        )

        # Animation part1

        self.play(fadeInTex(stmt1))
        self.wait(1)
        self.play(TransformMatchingTex(stmt1, stmt4), run_time=1.5)
        self.wait(0.5)

        self.play(
            LaggedStart(
                stmt4.animate.scale(0.8).shift(DOWN * 2.5),
                Create(axes),
                FadeIn(labelx, labely),
                Create(axes2),
                FadeIn(labelx2, labely2),
                fadeInTex(zPlane),
                fadeInTex(fzPlane),
                lag_ratio=0.5,
            )
        )
        self.wait(1)

        self.play(LaggedStart(GrowArrow(z_vector), GrowArrow(fz_vector), lag_ratio=0.4))
        self.wait(1)
        self.play(theta.animate.set_value(PI))

        # After animation part1

        label21 = always_redraw(
            lambda: nText("" + str(round(theta.get_value() / np.pi, 2)))
            .scale(0.8)
            .next_to(label1, RIGHT, buff=0.1)
        )

        label22 = always_redraw(
            lambda: nMath(
                "\\pi",
            )
            .scale(0.9)
            .next_to(label21, RIGHT, buff=0.1, aligned_edge=DOWN)
        )

        labelTheta = (
            VGroup(label1, label21, label22).move_to(ORIGIN).to_edge(UP, buff=0.7)
        )

        angle = always_redraw(
            lambda: Arc(
                0.4, 0, theta.get_value(), arc_center=axes.get_center(), color=GREY_N400
            )
        )

        labelAngle = (
            nMath(
                "\\mathbf{\\theta} = \\pi",
            )
            .scale(0.8)
            .next_to(angle, RIGHT + UP, buff=0)
        )

        labelR = nMath("r = 1").scale(0.7).next_to(z_vector, UP, buff=0.1)

        dotZ = Dot(z_vector.get_end(), radius=0.05, color=GREY_N200)

        def mark():
            pointer = Arrow(
                z_vector.get_end(),
                dot.get_center(),
                color=GREY_N50,
                buff=0.3,
            ).set_opacity(0.5)

            markerDot = Dot(dot.get_center(), color=GREY_N200, z_index=-0.1)
            marker0 = Circle(arc_center=dot.get_center(), color=RED_N100, radius=0.3)

            self.play(
                LaggedStart(
                    GrowArrow(pointer),
                    Create(marker0),
                    lag_ratio=0.5,
                ),
            )
            self.add(markerDot)
            self.wait(1)
            self.play(FadeOut(pointer))

        labelPtfZ2 = nMath("i").scale(0.7).next_to(fz_vector.get_end(), RIGHT, buff=0.5)

        def mark(label):
            pointer = Arrow(
                z_vector.get_end(),
                fz_vector.get_end(),
                color=GREY_N50,
                buff=0.3,
            ).set_opacity(0.5)

            markerDot = Dot(
                fz_vector.get_end(),
                color=GREY_N100,
            )
            marker0 = Circle(arc_center=fz_vector.get_end(), color=RED_N100, radius=0.3)

            self.play(
                LaggedStart(
                    GrowArrow(pointer),
                    FadeIn(markerDot),
                    Create(marker0),
                    FadeIn(label),
                    lag_ratio=0.5,
                ),
            )
            self.wait(1)
            self.play(FadeOut(pointer))

        # Animation part2

        self.play(
            LaggedStart(
                Create(dotZ),
                FadeIn(labelR),
                FadeIn(labelPtZ),
                Create(angle),
                FadeIn(labelAngle),
                lag_ratio=0.5,
            )
        )
        self.wait(1)
        mark(labelPtfZ2)

        self.play(
            LaggedStart(
                FadeOut(labelR),
                ReplacementTransform(labelAngle, labelTheta),
                lag_ratio=0.5,
            )
        )

        self.wait(1)

        self.play(theta.animate.set_value(-PI), run_time=3)
        labelPtfZ3 = (
            nMath("-i").scale(0.7).next_to(fz_vector.get_end(), RIGHT, buff=0.5)
        )
        mark(labelPtfZ3)
        self.wait(1)

        # self.play(theta.animate.set_value(3 * PI), run_time=4.5)
        # labelPtfZ1 = (
        #     nMath("5^\\frac{2}{3}")
        #     .scale(0.7)
        #     .next_to(fz_vector.get_end(), DOWN, buff=0.4)
        # )
        # mark(labelPtfZ1)
        # self.wait(1)

        self.wait(5)


class MultivaluedFunctions(Scene):
    def construct(self):
        set1 = Ellipse(
            1.5,
            4,
            stroke_color=[GREY_N200, GREY_N500],
            sheen_direction=UP + RIGHT,
            stroke_width=6,
        ).shift(1.5 * LEFT + DOWN * 0.5)
        label1 = (
            nMath(
                "z \\in \\mathbb{C}",
            )
            .next_to(set1, UP, buff=0.7)
            .shift(UP * 0.05)
        )
        set2 = Ellipse(
            1.5,
            4,
            stroke_color=[GREY_N200, GREY_N500],
            sheen_direction=UP + RIGHT,
            stroke_width=6,
        ).shift(1.5 * RIGHT + DOWN * 0.5)
        label2 = nMath("f(z) \\in \\mathbb{C}").next_to(set2, UP, buff=0.7)
        self.add(label1, label2)
        self.add(set1, set2)

        z1 = nMath("z_1", color=GREEN_N200).move_to(set1.get_center())

        fz2 = nMath("p_2", color=GREEN_N200).move_to(set2.get_center())
        fz1 = nMath("p_1", color=GREEN_N200).next_to(fz2, UP, buff=0.5)
        fz3 = nMath("p_3", color=GREEN_N200).next_to(fz2, DOWN, buff=0.5)

        self.add(z1, fz1, fz2, fz3)

        def mark(fz):
            markerPointer0 = Arrow(
                z1.get_right(), fz.get_left(), color=RED_N100, buff=0.3
            )
            self.play(GrowArrow(markerPointer0))
            return markerPointer0

        tmp1 = mark(fz1)
        tmp2 = mark(fz2)
        tmp3 = mark(fz3)

        self.wait(2)
        self.play(FadeOut(tmp1, tmp3), tmp2.animate.set_color(GREY_N400))

        self.wait(5)


class PrincipalBranchTitle(Scene):
    def construct(self):
        principalBranch = nMath("\\text{Principal Branch}", color=GREY_N800).scale(1.1)
        self.play(Write(principalBranch), run_time=2.5)

        self.wait(5)


class PrincipalBranchDemo(Scene):
    def construct(self):
        theta = ValueTracker(0)

        stmt1 = nMath("f(z)", "=", "z^\\frac{1}{2}", color=GREY_N800).scale(1.1)

        stmt4 = nMath(
            "f(z)",
            "=",
            "z^\\frac{1}{2}",
            "=",
            "\\sqrt{r}",
            "e^{i\\frac{\\mathbf{\\theta}}{2}}",
            color=GREY_N800,
        ).scale(1.1)

        label1 = nMath(
            "\\mathbf{\\theta} =",
        ).scale(0.8)

        label1[0][0].scale(1.1)

        stmt4[-1][1].scale(1.1)

        axes = getAxis().shift(LEFT * 3.5)
        axes2 = getAxis(
            [-2, 2],
            [-7, 7],
        ).shift(RIGHT * 3.5)

        z_vector = always_redraw(
            lambda: Arrow(
                axes.get_origin(),
                axes.get_origin()
                + 2 * np.sin(theta.get_value()) * UP
                + 2 * np.cos(theta.get_value()) * RIGHT,
                buff=0,
            )
            .set_color_by_gradient([GREEN_N100, GREEN_N200])
            .set_sheen_direction(
                np.sin(theta.get_value()) * UP + np.cos(theta.get_value()) * RIGHT,
            )
        )

        labelPtZ = (
            nMath("-1").scale(0.7).next_to(axes.get_origin() + LEFT * 2, DOWN, buff=0.3)
        )

        fz_vector = always_redraw(
            lambda: Arrow(
                axes2.get_origin(),
                axes2.get_origin()
                + 2 * np.sin(0.5 * theta.get_value()) * UP
                + 2 * np.cos(0.5 * theta.get_value()) * RIGHT,
                buff=0,
            )
            .set_color_by_gradient([BLUE_A, NUMBRIK_COLOR_200])
            .set_sheen_direction(
                np.sin(theta.get_value()) * UP + np.cos(theta.get_value()) * RIGHT,
            )
        )

        dot = always_redraw(
            lambda: Dot(axes2.c2p(1, theta.get_value()), color=GREEN_N200)
        )

        zPlane = (
            nText("z-plane", color=GREY_N100)
            .scale(0.8)
            .next_to(axes.y_axis, LEFT, buff=1.2)
            .shift(3 * UP)
        )

        fzPlane = (
            nText("f(z)-plane", color=GREY_N100)
            .scale(0.8)
            .next_to(axes2.y_axis, RIGHT, buff=0.8)
            .shift(3 * UP)
        )

        labelx = axes.get_x_axis_label(
            nMath("Re", color=GREY_N500).scale(0.6), direction=DOWN, buff=0.5
        )

        labely = axes.get_y_axis_label(
            nMath("Im", color=GREY_N500).scale(0.6), direction=LEFT, buff=0.5
        )

        labelx2 = axes2.get_x_axis_label(
            nMath("Re", color=GREY_N500).scale(0.6), direction=DOWN, buff=0.5
        )

        labely2 = axes2.get_y_axis_label(
            nMath("Im", color=GREY_N500).scale(0.6), direction=LEFT, buff=0.5
        )

        # Animation part1

        # self.play(fadeInTex(stmt1))
        # self.wait(1)
        # self.play(TransformMatchingTex(stmt1, stmt4), run_time=1.5)
        # self.wait(0.5)

        # self.play(
        #     LaggedStart(
        (stmt4.scale(0.8).shift(DOWN * 2.5),)
        #         Create(axes),
        #         FadeIn(labelx, labely),
        #         Create(axes2),
        #         FadeIn(labelx2, labely2),
        #         fadeInTex(zPlane),
        #         fadeInTex(fzPlane),
        #         lag_ratio=0.5,
        #     )
        # )
        # self.wait(1)

        # self.play(LaggedStart(GrowArrow(z_vector), GrowArrow(fz_vector), lag_ratio=0.4))
        # self.wait(1)
        # self.play(theta.animate.set_value(PI))

        self.add(
            axes,
            axes2,
            stmt4,
            labelx,
            labely,
            labelx2,
            labely2,
            zPlane,
            fzPlane,
            z_vector,
            fz_vector,
        )

        # After animation part1

        label21 = always_redraw(
            lambda: nText("" + str(round(theta.get_value() / np.pi, 2)))
            .scale(0.8)
            .next_to(label1, RIGHT, buff=0.1)
        )

        label22 = always_redraw(
            lambda: nMath(
                "\\pi",
            )
            .scale(0.9)
            .next_to(label21, RIGHT, buff=0.1, aligned_edge=DOWN)
        )

        labelTheta = (
            VGroup(label1, label21, label22).move_to(ORIGIN).to_edge(UP, buff=0.7)
        )

        angle = always_redraw(
            lambda: Arc(
                0.4, 0, theta.get_value(), arc_center=axes.get_center(), color=GREY_N400
            )
        )

        labelAngle = (
            nMath(
                "\\mathbf{\\theta} = \\pi",
            )
            .scale(0.8)
            .next_to(angle, RIGHT + UP, buff=0)
        )

        labelR = nMath("r = 1").scale(0.7).next_to(z_vector, UP, buff=0.1)

        dotZ = Dot(z_vector.get_end(), radius=0.05, color=GREY_N200)

        def mark():
            pointer = Arrow(
                z_vector.get_end(),
                dot.get_center(),
                color=GREY_N50,
                buff=0.3,
            ).set_opacity(0.5)

            markerDot = Dot(dot.get_center(), color=GREY_N200, z_index=-0.1)
            marker0 = Circle(arc_center=dot.get_center(), color=RED_N100, radius=0.3)

            self.play(
                LaggedStart(
                    GrowArrow(pointer),
                    Create(marker0),
                    lag_ratio=0.5,
                ),
            )
            self.add(markerDot)
            self.wait(1)
            self.play(FadeOut(pointer))

        labelPtfZ2 = nMath("i").scale(0.7).next_to(fz_vector.get_end(), RIGHT, buff=0.5)

        def mark(label):
            pointer = Arrow(
                z_vector.get_end(),
                fz_vector.get_end(),
                color=GREY_N50,
                buff=0.3,
            ).set_opacity(0.5)

            markerDot = Dot(
                fz_vector.get_end(),
                color=GREY_N100,
            )
            marker0 = Circle(arc_center=fz_vector.get_end(), color=RED_N100, radius=0.3)

            self.play(
                LaggedStart(
                    GrowArrow(pointer),
                    FadeIn(markerDot),
                    Create(marker0),
                    FadeIn(label),
                    lag_ratio=0.5,
                ),
            )
            self.wait(1)
            self.play(FadeOut(pointer))

        # Animation part2

        # self.play(
        #     LaggedStart(
        #         Create(dotZ),
        #         FadeIn(labelR),
        #         FadeIn(labelPtZ),
        #         Create(angle),
        #         FadeIn(labelAngle),
        #         lag_ratio=0.5,
        #     )
        # )
        # self.wait(1)
        # mark(labelPtfZ2)

        # self.play(
        #     LaggedStart(
        #         FadeOut(labelR),
        #         ReplacementTransform(labelAngle, labelTheta),
        #         lag_ratio=0.5,
        #     )
        # )

        # self.wait(1)

        # self.play(theta.animate.set_value(-PI), run_time=3)
        # labelPtfZ3 = (
        #     nMath("-i").scale(0.7).next_to(fz_vector.get_end(), RIGHT, buff=0.5)
        # )
        # mark(labelPtfZ3)
        # self.wait(1)

        labelArgument = (
            nMath("\\mathbf{\\theta} \\in [0, 2\\pi)").scale(0.9).to_edge(UP, buff=0.8)
        )

        self.add(
            angle,
            # labelTheta,
            # labelArgument,
        )

        self.play(fadeInTex(labelArgument))
        highlight(self, labelArgument, buff=0.2, unhighlight=False)

        self.play(theta.animate.set_value(2 * PI - 0.1), run_time=3)
        self.wait(1)
        self.play(theta.animate.set_value(0), run_time=3)
        self.wait(1)

        # self.play(theta.animate.set_value(3 * PI), run_time=4.5)
        # labelPtfZ1 = (
        #     nMath("5^\\frac{2}{3}")
        #     .scale(0.7)
        #     .next_to(fz_vector.get_end(), DOWN, buff=0.4)

        self.play(theta.animate.set_value(PI))
        self.wait(1)

        def mark():
            pointer = Arrow(
                z_vector.get_end(),
                fz_vector.get_end(),
                color=GREY_N50,
                buff=0.3,
            ).set_opacity(0.5)

            markerDot = Dot(
                fz_vector.get_end(),
                color=GREY_N100,
            )
            marker0 = Circle(arc_center=fz_vector.get_end(), color=RED_N100, radius=0.3)

            self.play(
                LaggedStart(
                    GrowArrow(pointer),
                    FadeIn(markerDot),
                    Create(marker0),
                    lag_ratio=0.5,
                ),
            )
            self.wait(1)
            self.play(FadeOut(pointer))

        mark()

        # )
        # mark(labelPtfZ1)
        # self.wait(1)

        self.wait(5)


class CorrectWay(Scene):
    def construct(self):
        eqn = nMath(
            "\\sqrt{-9}",
            "\\cdot",
            "\\sqrt{-4}",
        ).shift(UP)
        eqn2 = nMath(
            "=",
            "\\pm \\sqrt{9}i",
            "\\cdot",
            "\\pm \\sqrt{4}i",
        )
        eqn3 = nMath("= \\pm6").shift(DOWN)

        self.play(fadeInTex(eqn))
        self.wait(0.5)
        self.play(fadeInTex(eqn2))
        self.wait(0.5)
        self.play(fadeInTex(eqn3))
        self.wait(5)


class CorrectAnswer(Scene):
    def construct(self):
        eqn1 = nMath("\\sqrt{-9} = 3i, \\quad \\sqrt{-4} = 2i").shift(0.6**UP + LEFT)
        eqn2 = nMath(
            "\\sqrt{-9}",
            "\\cdot",
            "\\sqrt{-4}",
            "=",
            "3i",
            "\\cdot",
            "2i",
            "= 6i^2 = -6",
        ).shift(0.6 * DOWN)

        self.play(fadeInTex(eqn1))
        self.wait(0.5)
        self.play(fadeInTex(eqn2))

        self.wait(5)


class BranchingIllus(Scene):
    def construct(self):
        axes2 = getAxis(
            x_range=[-1, 10, 1],
            y_range=[-4, 4, 1],
            x_length=7,
            y_length=6,
            color=GREY_D,
        ).scale(0.9)

        graphLabel = (
            nMath("y = \\sqrt{x}", color=NUMBRIK_COLOR).shift(UP * 2.3).scale(0.8)
        )
        graphLabel2 = (
            nMath("y = -\\sqrt{x}", color=RED_N100).shift(DOWN * 2.3).scale(0.8)
        )

        root = axes2.plot(lambda x: x**0.5, x_range=[0, 8], color=NUMBRIK_COLOR)
        root2 = axes2.plot(lambda x: -(x**0.5), x_range=[0, 8], color=RED_N100)
        self.play(
            LaggedStart(
                FadeIn(axes2),
                Create(root),
                FadeIn(graphLabel),
                lag_ratio=0.5,
            )
        )
        self.wait(1)
        self.play(LaggedStart(Create(root2), FadeIn(graphLabel2), lag_ratio=0.5))

        self.wait(10)


class Thumbnail(Scene):
    def construct(self):
        addBackground(self)
        question = MathTex(
            "\\text{Evaluate: } \\sqrt{-4}\\sqrt{-9}",
            tex_template=TexFontTemplates.droid_sans,
            color=GREY_E,
        ).scale(1.2)
        options2 = VGroup(
            MathTex(
                "A)", "\\; \\ 6", tex_template=TexFontTemplates.droid_sans, color=GREY_E
            ),
            MathTex(
                "B)", "\\ -6", tex_template=TexFontTemplates.droid_sans, color=GREY_E
            ),
            MathTex(
                "C)",
                " \\ \\pm6",
                tex_template=TexFontTemplates.droid_sans,
                color=GREY_E,
            ),
            MathTex(
                "D)",
                "\\; \\ \\text{undefined}",
                tex_template=TexFontTemplates.droid_sans,
                color=GREY_E,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, center=False, buff=0.5)

        (
            VGroup(question, options2)
            .arrange(DOWN, buff=0.75, aligned_edge=LEFT)
            .to_edge(LEFT)
            .shift(0.8 * RIGHT)
        )

        options2.shift(RIGHT * 0.1)

        self.add(question, options2)

        self.wait(1)
