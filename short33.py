from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        question = MathTex(
            "\\int^{1}_{-1}",
            "|x|",
            "+",
            "\\sqrt{1-x^2}",
            "\\;\\; dx",
            color=BLACK,
        ).to_edge(UP)
        question[3:].shift(0.05 * DOWN)

        options = (
            VGroup(
                MathTex("A) \\ 2", color=BLACK),
                MathTex("B) \\ \\pi+2", color=BLACK),
                MathTex("C) \\ 2 + \\sqrt{2}", color=BLACK),
                MathTex("D) \\ 1 + \\frac{\\pi}{2}", color=BLACK),
            )
            .arrange(DOWN, buff=0.35, aligned_edge=LEFT)
            .next_to(question, DOWN, buff=1, aligned_edge=LEFT)
        )

        hgl1 = solidHighlight(self, question[1], buff=0.15, animate=False)

        self.add(question, options)
        self.wait(4)

        axis = getAxis(
            x_range=[-2, 2], y_range=[-0.5, 2], x_length=5, y_length=12.5 / 4
        ).next_to(question, DOWN, buff=1)

        absPlot = VGroup(
            axis.plot(lambda x: -x, x_range=[-1.5, 0], color=GREY_N400),
            axis.plot(lambda x: x, x_range=[0, 1.5], color=GREY_N400),
        )

        perp1 = DashedLine(
            axis.c2p(1, 1), axis.x_axis.get_projection(axis.c2p(1, 1)), color=GREY_N400
        )

        label1 = nText("1").next_to(
            axis.x_axis.get_projection(axis.c2p(1, 1)), DOWN, buff=0.3
        )

        perp2 = DashedLine(
            axis.c2p(-1, 1),
            axis.x_axis.get_projection(axis.c2p(-1, 1)),
            color=GREY_N400,
        )

        label2 = nText("-1").next_to(
            axis.x_axis.get_projection(axis.c2p(-1, 1)), DOWN, buff=0.3
        )

        region1 = getTriangularRegion(
            axis.c2p(1, 1),
            axis.x_axis.get_projection(axis.c2p(1, 1)),
            axis.get_origin(),
        )

        region2 = getTriangularRegion(
            axis.c2p(-1, 1),
            axis.x_axis.get_projection(axis.c2p(-1, 1)),
            axis.get_origin(),
        )

        label3 = nText("1").next_to(
            axis.y_axis.get_projection(axis.c2p(1, 1)), LEFT, buff=0.2
        )

        square = Square(
            perp1.get_length(),
            fill_color=YELLOW,
            stroke_color=GREY_N400,
            fill_opacity=1,
        ).move_to(axis.c2p(0.5, 0.5))

        # Animations hub 1

        self.play(FadeOut(options))
        self.wait(1)
        self.play(FadeIn(*hgl1))
        self.wait(1)
        self.play(LaggedStart(FadeIn(axis), Create(absPlot), lag_ratio=0.5))
        self.wait(1)
        self.play(
            LaggedStart(
                Create(perp2),
                FadeIn(label2),
                Create(perp1),
                FadeIn(label1),
                lag_ratio=0.5,
            )
        )
        self.play(
            FadeIn(region2),
            FadeIn(region1),
        )
        self.wait(1)
        tmpGrp = VGroup(region2, perp2.copy())
        self.play(
            LaggedStart(
                Rotate(tmpGrp, -PI / 2, OUT, axis.get_origin()),
                FadeIn(label3),
                lag_ratio=0.5,
            )
        )
        self.wait(1)
        self.play(FadeIn(square))
        # self.remove(region1, region2)
        self.play(
            LaggedStart(
                FadeOut(
                    axis,
                    perp1,
                    perp2,
                    region1,
                    label1,
                    region2,
                    label2,
                    absPlot,
                    label3,
                    tmpGrp,
                ),
                square.animate.next_to(question[1], DOWN, buff=1.2),
                lag_ratio=0.5,
            )
        )
        label3.move_to(square.get_center())
        self.play(FadeIn(label3))
        self.wait(1)

        axis2 = getAxis(x_range=[-2, 2], y_range=[-2, 2], x_length=5, y_length=5)
        # axis2.shift(axis.get_origin() - axis2.get_origin())

        hgl2 = solidHighlight(self, question[3], buff=0.15, animate=False)

        eq1 = nMath("x^2", "+", "y", "^2", "=", "1").next_to(question, DOWN, buff=0.75)
        # self.add(eq1)
        eq2 = nMath("y", "^2", "=", "1", "-", "x^2").next_to(question, DOWN, buff=0.75)
        # self.add(eq2)
        eq3 = nMath("y", "=", "\\pm", "\\sqrt{", "1", "-", "x^2", "}").next_to(
            question, DOWN, buff=0.75
        )
        eq4 = nMath("y", "=", "-", "\\sqrt{", "1", "-", "x^2", "}").move_to(
            axis2.get_origin()
        )

        axis2.next_to(eq1, DOWN, buff=0.75)

        circle = Circle(square.get_arc_length() / 4, stroke_color=GREY_N400).move_to(
            axis2.get_origin()
        )

        region3 = Sector(
            square.get_arc_length() / 4,
            angle=PI,
            arc_center=circle.get_center(),
            z_index=-1,
            color=YELLOW,
            stroke_color=GREY_N400,
            stroke_width=DEFAULT_STROKE_WIDTH,
        )

        # Animation hub 2

        self.play(
            FadeOut(square, label3),
            Transform(hgl1[0], hgl2[0]),
        )
        self.wait(1)
        self.play(fadeInTex(eq1))
        label1.next_to(circle, RIGHT, buff=0.2).shift(DOWN * 0.3)
        label2.next_to(circle, LEFT, buff=0.2).shift(DOWN * 0.3)
        positive = (
            nText("+").next_to(circle, LEFT, buff=-0.3).shift(1.25 * UP).scale(1.2)
        )
        negative = (
            nText("-").next_to(circle, LEFT, buff=-0.3).shift(1.25 * DOWN).scale(1.2)
        )
        self.play(
            LaggedStart(
                FadeIn(axis2),
                Create(circle),
                FadeIn(label1, label2),
                lag_ratio=0.5,
            ),
        )
        self.wait(1)
        self.play(TransformMatchingTex(eq1, eq2), run_time=2)
        self.play(TransformMatchingTex(eq2, eq3), run_time=3)
        self.wait(1)
        self.play(
            FadeIn(positive, negative),
        )
        highlight(self, [positive, negative], buff=0.1, color=RED, wait_time=1)

        self.wait(1)
        self.play(FadeIn(region3))
        self.wait(1)

        self.play(
            LaggedStart(
                FadeOut(axis2, eq3, circle, negative, positive, label1, label2),
                region3.animate.next_to(square, RIGHT, buff=0.5, aligned_edge=DOWN),
                FadeIn(square, label3),
                lag_ratio=0.5,
            )
        )
        label4 = nMath("\\frac{\\pi}{2}").move_to(region3.get_center()).scale(0.8)
        self.play(FadeIn(label4))
        self.wait(1)

        final = nMath("Area =", "1", "+", "\\frac{\\pi}{2}").shift(1.5 * DOWN)
        self.play(
            FadeIn(final[0], final[2]),
            ReplacementTransform(label3, final[1]),
            ReplacementTransform(label4, final[3]),
        )
        self.wait(1)
        self.play(FadeOut(square, region3, final))
        self.play(FadeIn(options))
        highlight(self, options[3], buff=0.2, color=RED_N100, unhighlight=False)

        self.wait(5)


class Context(Scene):
    def construct(self):
        eq = (
            nMath("\\int^{b}_{a} f(x) dx")
            .set_color_by_gradient([GREY_N200, GREY_N800])
            .set_sheen_direction(RIGHT)
        )

        axis = getAxis(
            x_range=[-2, 7], y_range=[-1, 4], x_length=4.5, y_length=4
        ).shift(1.2 * DOWN)

        ## Animation hub 1
        self.add(eq)
        self.wait(1)
        self.play(LaggedStart(eq.animate.to_edge(UP), FadeIn(axis), lag_ratio=0.4))

        fn = axis.plot(lambda x: np.sqrt(x + 2) + 0.25, [-1, 5], color=GREY_N400)
        area = axis.get_area(fn, x_range=[1, 4], color=YELLOW, z_index=-1, opacity=1)

        perp1 = DashedLine(
            axis.c2p(1, np.sqrt(3) + 0.25),
            axis.x_axis.get_projection(axis.c2p(1, np.sqrt(3) + 0.25)),
            color=GREY_N400,
        )

        label1 = nMath(
            "a",
            gradient_color=[NUMBRIK_COLOR_50, NUMBRIK_COLOR_DARK],
            sheen_direction=RIGHT,
        ).next_to(
            axis.x_axis.get_projection(axis.c2p(1, np.sqrt(3) + 0.25)), DOWN, buff=0.3
        )

        perp2 = DashedLine(
            axis.c2p(4, np.sqrt(6) + 0.25),
            axis.x_axis.get_projection(axis.c2p(4, np.sqrt(6) + 0.25)),
            color=GREY_N400,
        )

        label2 = nMath(
            "b",
            gradient_color=[NUMBRIK_COLOR_50, NUMBRIK_COLOR_DARK],
            sheen_direction=RIGHT,
        ).next_to(
            axis.x_axis.get_projection(axis.c2p(4, np.sqrt(6) + 0.25)), DOWN, buff=0.2
        )

        labelGraph = (
            nMath(
                "y = f(x)",
                gradient_color=[NUMBRIK_COLOR_50, NUMBRIK_COLOR_DARK],
                sheen_direction=RIGHT,
            )
            .scale(0.8)
            .next_to(fn.get_end(), UP, buff=0.3)
            .shift(RIGHT * 0.3)
        )

        brace = Brace(
            eq,
            DOWN,
            buff=0.2,
            sheen_direction=RIGHT,
        ).set_color_by_gradient([GREY_N100, GREY_N800])

        pointer = Arrow(
            brace.get_bottom(), area.get_center() + DOWN * 0.5, color=RED_N100
        )

        # Animations hub 2
        self.play(
            LaggedStart(
                Create(fn),
                FadeIn(labelGraph),
                Create(perp1),
                FadeIn(label1),
                Create(perp2),
                FadeIn(label2),
                lag_ratio=0.4,
            )
        )
        self.play(LaggedStart(Write(brace), GrowArrow(pointer), lag_ratio=0.5))
        self.play(FadeIn(area))

        self.wait(5)
