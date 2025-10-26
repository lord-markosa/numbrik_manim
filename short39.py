from manim import *
from utils import *


class Template(Scene):
    def construct(self):
        ellipse = (
            Ellipse(4, 3, fill_opacity=1)
            .set_color_by_gradient([NUMBRIK_COLOR40, NUMBRIK_COLOR, VIOLET_N1000])
            .set_sheen_direction(RIGHT)
            .set_stroke(
                color=[GREY_N200, GREY_N400],
            )
        ).shift(UP * 1.5)
        self.add(ellipse)

        eqn1 = nMath(
            "\\frac{x^2}{a^2}", "+", "\\frac{y^2}{b^2}", "=", "1", color=BLACK
        ).next_to(ellipse, DOWN, buff=1)

        eqn2 = nMath(
            "\\frac{y^2}{b^2}", "=", "1", "-", "\\frac{x^2}{a^2}", color=BLACK
        ).next_to(ellipse, DOWN, buff=1)

        eqn3 = nMath(
            "y^2",
            "=",
            "b^2",
            "\\left(",
            "1",
            "-",
            "\\frac{x^2}{a^2}",
            "\\right)",
            color=BLACK,
        ).next_to(ellipse, DOWN, buff=1)

        eqn4 = nMath(
            "y",
            "=",
            "\\pm",
            "\\frac{b}{a}",
            "\\sqrt{a^2 - x^2}",
            color=BLACK,
        ).next_to(ellipse, DOWN, buff=1)

        # self.add(eqn4)

        # self.play(TransformMatchingTex(eqn2, eqn3))

        area = (
            nMath("Area", "=", "2", "\\int^{a}_{-a}", "y", "\\, dx")
            .next_to(eqn4, DOWN, buff=0.5)
            .shift(UP * 0.5)
        )
        # area = 2 * nMath("\\int^{a}_{-a}y\\,dx").next_to(eqn4, DOWN, buff=0.75)

        area2 = (
            nMath(
                "Area",
                "=",
                "2",
                "\\int^{a}_{-a}",
                "\\frac{b}{a}",
                "\\sqrt{a^2 - x^2}",
                "\\, dx",
            )
            .next_to(eqn4, DOWN, buff=0.5)
            .shift(UP * 0.5)
        )

        area3 = (
            nMath(
                "Area",
                "=",
                "2",
                "\\frac{b}{a}",
                "\\int^{a}_{-a}",
                "\\sqrt{a^2 - x^2}",
                "\\, dx",
            )
            .next_to(eqn4, DOWN, buff=0.5)
            .shift(UP * 0.5)
        )

        hgl = solidHighlight(
            self, area3[4:], buff=0.12, color=YELLOW_N50, animate=False
        )
        hgl = hgl[0]
        hgl.set_color_by_gradient(
            [YELLOW_B, YELLOW_N40, YELLOW_N50, YELLOW]
        ).set_sheen_direction(RIGHT)
        self.add(hgl)

        self.add(area3)

        axes = getAxis()
        axes.move_to(ellipse.get_center())
        self.add(axes)
        circle = Circle(2, arc_center=ellipse.get_center())

        # labelA = lengthMarkerV2(
        #     ellipse.get_top() + 2 * RIGHT,
        #     ellipse.get_top() + 2 * LEFT,
        #     "a",
        #     shift=0.5 * UP,
        # )
        # self.add(labelA)

        # labelB = lengthMarkerV2(
        #     ellipse.get_right(),
        #     ellipse.get_right() + 1.5 * UP,
        #     "b",
        #     shift=RIGHT * 0.5,
        # )
        # self.add(labelB)

        helper1 = DashedLine(
            ellipse.get_top() + LEFT,
            ellipse.get_top() + RIGHT * 2,
            color=GREY_N400,
        )
        self.add(helper1)

        helper2 = DashedLine(
            ellipse.get_right() + DOWN,
            ellipse.get_right() + UP * 1.5,
            color=GREY_N400,
        )
        self.add(helper2)

        labelPt = nMath("(a, b)").next_to(
            ellipse.get_top() + RIGHT * 2, RIGHT + UP, buff=0.1
        )
        self.add(labelPt)

        # ellipse.set_opacity(0.3)

        # semicircle = Sector(
        #     radius=1.95, arc_center=ellipse.get_center(), color=YELLOW, angle=PI
        # )
        # circle.set_stroke([GREY_N200, GREY_N500]).set_sheen_direction(RIGHT)

        # self.add(circle)
        # self.add(semicircle)

        self.wait(5)


class AreaOfEllipse(Scene):
    def construct(self):
        ellipse = (
            Ellipse(4, 3, fill_opacity=1)
            .set_color_by_gradient([WHITE, BLUE_C])
            .set_sheen_direction(UP + RIGHT)
            .set_stroke(color=[GREY_N200, GREY_N400], width=4)
            .shift(UP * 1.2)
        )

        helper1 = DashedLine(
            ellipse.get_top() + LEFT * 2,
            ellipse.get_top() + RIGHT * 2,
            sheen_direction=RIGHT,
            dash_length=0.15,
            dashed_ratio=0.8,
        ).set_color_by_gradient(GREY_N100, GREY_N400)

        helper2 = DashedLine(
            ellipse.get_right() + DOWN * 1.5,
            ellipse.get_right() + UP * 1.5,
            sheen_direction=RIGHT,
            dash_length=0.15,
            dashed_ratio=0.8,
        ).set_color_by_gradient(GREY_N100, GREY_N400)

        axes = (
            getAxis(x_length=6, y_length=5)
            .set_color_by_gradient(GREY_N400, GREY_N500)
            .set_sheen_direction(RIGHT)
            .move_to(ellipse.get_center())
            .set_z_index(0.1)
        )

        labelPt = nMath(
            "(a, b)", gradient_color=[NUMBRIK_COLOR_100, NUMBRIK_COLOR]
        ).next_to(ellipse.get_top() + RIGHT * 2, RIGHT + UP, buff=0.1)

        self.play(
            LaggedStart(
                DrawBorderThenFill(
                    ellipse, stroke_color=[GREY_N200, GREY_N400], stroke_width=4
                ),
                FadeIn(axes),
                AnimationGroup(Create(helper1), Create(helper2)),
                fadeInTex(labelPt),
                lag_ratio=0.4,
            )
        )

        eqn1 = nMath(
            "\\frac{x^2}{a^2}",
            "+",
            "\\frac{y^2}{b^2}",
            "=",
            "1",
            color=GREY_N500,
        ).to_edge(DOWN)

        eqn1[0].shift(DOWN * 0.05)

        self.play(Write(eqn1), run_time=2)
        self.play(
            FadeOut(helper1, helper2, labelPt),
        )

        eqn2 = nMath(
            "\\frac{y^2}{b^2}", "=", "1", "-", "\\frac{x^2}{a^2}", color=BLACK
        ).to_edge(DOWN)

        eqn3 = nMath(
            "y^2",
            "=",
            "b^2",
            "\\left(",
            "1",
            "-",
            "\\frac{x^2}{a^2}",
            "\\right)",
            color=BLACK,
        ).to_edge(DOWN)

        eqn4 = nMath(
            "y",
            "=",
            "\\pm",
            "\\frac{b}{a}",
            "\\sqrt{a^2 - x^2}",
            color=BLACK,
        ).next_to(eqn3, 0, aligned_edge=UP)

        self.wait(1)

        self.play(
            TransformMatchingTex(eqn1, eqn2),
        )
        self.wait(0.5)
        self.play(TransformMatchingTex(eqn2, eqn3))
        self.wait(0.5)
        self.play(TransformMatchingTex(eqn3, eqn4))
        self.wait(2)

        area = nMath(
            "Area", "=", "2", "\\int^{a}_{-a}", "y", "\\, dx", color=GREY_N500
        ).to_edge(DOWN)

        self.play(FadeOut(eqn4, shift=UP), FadeIn(area, shift=UP))
        self.wait(0.4)

        area2 = nMath(
            "Area",
            "=",
            "2",
            "\\int^{a}_{-a}",
            "\\frac{b}{a}",
            "\\sqrt{a^2 - x^2}",
            "\\, dx",
            color=GREY_N500,
        ).to_edge(DOWN)

        area3 = nMath(
            "Area",
            "=",
            "2",
            "\\frac{b}{a}",
            "\\int^{a}_{-a}",
            "\\sqrt{a^2 - x^2}",
            "\\, dx",
            color=GREY_N500,
        ).to_edge(DOWN)

        self.play(TransformMatchingTex(area, area2))
        self.wait(1)
        self.play(TransformMatchingTex(area2, area3))
        self.wait(2)

        hgl = solidHighlight(
            self, area3[4:], buff=0.12, color=YELLOW_N50, animate=False
        )
        hgl = hgl[0]

        hgl2 = solidHighlight(
            self, area3[5], buff=0.12, color=YELLOW_N50, animate=False
        )
        hgl2 = hgl2[0]

        hgl.set_color_by_gradient(
            [YELLOW_B, YELLOW_N40, YELLOW_N50, YELLOW]
        ).set_sheen_direction(RIGHT)

        axes.move_to(ellipse.get_center())
        circle = Circle(2, arc_center=ellipse.get_center(), color=RED_N100)

        semicircle = Sector(
            radius=1.95,
            arc_center=ellipse.get_center(),
            color=YELLOW,
            angle=PI,
            fill_opacity=0.8,
            z_index=0.05,
        )

        self.play(FadeIn(hgl))
        self.wait(1)
        hgl3 = hgl.copy()
        self.play(ReplacementTransform(hgl, hgl2))
        self.wait(1)
        self.play(
            LaggedStart(ellipse.animate.set_opacity(0.4), Create(circle), lag_ratio=0.5)
        )
        self.wait(0.25)
        self.play(ReplacementTransform(hgl2, hgl3))
        self.play(FadeIn(semicircle))
        self.wait(0.25)

        AreaPointer = CurvedArrow(
            hgl3.get_top() + RIGHT + 0.3 * UP,
            semicircle.get_center() + RIGHT + DOWN + 0.2 * UP,
            color=GREY_N800,
            z_index=2,
        )
        self.play(Create(AreaPointer))

        self.wait(1)

        self.play(FadeOut(AreaPointer))
        self.wait(0.25)

        self.play(
            FadeOut(semicircle, circle),
            ellipse.animate.set_opacity(1),
        )
        self.play(FadeOut(hgl3))
        area4 = nMath(
            "Area",
            "=",
            "2",
            "\\frac{b}{a}",
            "\\frac{\\pi a^2}{2}",
            color=GREY_N500,
        ).next_to(area3, 0)
        self.play(TransformMatchingTex(area3, area4))
        self.wait(1)
        final = nMath(
            "Area",
            "=",
            "\\pi a b",
            color=GREY_N500,
        ).next_to(area4, 0)
        self.play(TransformMatchingTex(area4, final))
        self.wait(1)

        highlight(self, final, buff=0.25, color=RED_N100, unhighlight=False)

        # labelA = lengthMarkerV2(
        #     ellipse.get_top() + 2 * RIGHT,
        #     ellipse.get_top() + 2 * LEFT,
        #     "a",
        #     shift=0.5 * UP,
        # )
        # self.add(labelA)

        # labelB = lengthMarkerV2(
        #     ellipse.get_right(),
        #     ellipse.get_right() + 1.5 * UP,
        #     "b",
        #     shift=RIGHT * 0.5,
        # )
        # self.add(labelB)

        # ellipse.set_opacity(0.3)

        # semicircle = Sector(
        #     radius=1.95, arc_center=ellipse.get_center(), color=YELLOW, angle=PI
        # )
        # circle.set_stroke([GREY_N200, GREY_N500]).set_sheen_direction(RIGHT)

        # self.add(circle)
        # self.add(semicircle)

        self.wait(5)


class AreaUnderCurve(Scene):
    def construct(self):
        eq = (
            nMath("\\int^{b}_{a} f(x) \\,dx")
            .set_color_by_gradient([GREY_N400, GREY_N800])
            .set_sheen_direction(RIGHT)
            .to_edge(UP)
        )

        axis = getAxis(
            x_range=[-2, 7], y_range=[-1, 4], x_length=4.5, y_length=4
        ).shift(1.2 * DOWN)

        fn = axis.plot(lambda x: np.sqrt(x + 2) + 0.25, [-1, 5], color=GREY_N400)
        area = axis.get_area(
            fn,
            x_range=[1, 4],
            color=[WHITE, YELLOW],
            sheen_direction=RIGHT + UP,
            z_index=-1,
            opacity=1,
        )

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
                AnimationGroup(Write(eq), run_time=2),
                FadeIn(axis),
                Create(fn),
                FadeIn(labelGraph),
                Create(perp1),
                FadeIn(label1),
                Create(perp2),
                FadeIn(label2),
                lag_ratio=0.3,
            ),
            run_time=3,
        )
        self.play(LaggedStart(Write(brace), GrowArrow(pointer), lag_ratio=0.5))
        self.play(FadeIn(area))

        self.wait(5)
