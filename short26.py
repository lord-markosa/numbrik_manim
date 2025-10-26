from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        addBackground(self)

        r = 3.5
        theta = 40 / 180 * PI
        random_angle = PI / 2 * 1.2

        stroke_color = GREY_N800

        circle = Circle(r, color=stroke_color)
        center = Dot(ORIGIN, radius=0.05, color=stroke_color)
        diameter = Line(r * LEFT, r * RIGHT, color=stroke_color)

        # Construction line for the isosceles triangle
        line1 = DashedLine(ORIGIN, r * RIGHT, color=stroke_color)
        line1.rotate(theta, IN, ORIGIN)

        # Construction line for the isosceles triangle
        line2 = DashedLine(ORIGIN, r * RIGHT, color=stroke_color)
        line2.rotate(PI - theta, IN, ORIGIN)

        # Parallel base line
        line3 = Line(line1.get_end(), line2.get_end(), color=stroke_color)

        # Instruction Line for 25 degrees
        line4 = Line(diameter.get_end(), line3.get_end(), color=stroke_color)

        P = RIGHT * r * np.cos(random_angle) + UP * r * np.sin(random_angle)

        # Instruction line for the top angle
        line5 = Line(line3.get_start(), P, color=stroke_color)
        line6 = Line(line3.get_end(), P, color=stroke_color)

        def angleConstructor(A, B, C, radi=0.7):
            return Angle(Line(B, A), Line(B, C), color=stroke_color, radius=radi)

        def doubleAngleConstructor(A, B, C, radi=0.7):
            return VGroup(
                angleConstructor(A, B, C, radi), angleConstructor(A, B, C, radi + 0.2)
            )

        # given angle
        angle1 = angleConstructor(
            diameter.get_start(), diameter.get_end(), line4.get_end(), 1
        )
        # to find angle
        angle2 = angleConstructor(line3.get_end(), P, line3.get_start(), 0.7)

        # helper angles
        angle3 = doubleAngleConstructor(
            diameter.get_start(), ORIGIN, line3.get_end(), 0.7
        )
        angle4 = angleConstructor(line3.get_end(), ORIGIN, line3.get_start(), 0.5)

        # isosceles triangle base angles
        angle7 = doubleAngleConstructor(
            line3.get_start(), line3.get_end(), line2.get_start(), 0.7
        )
        angle8 = doubleAngleConstructor(
            line1.get_start(), line3.get_start(), line3.get_end(), 0.7
        )

        arrow_tip1 = ArrowTriangleFilledTip(color=stroke_color, start_angle=0).shift(
            LEFT * 1.8
        )
        arrow_tip2 = ArrowTriangleFilledTip(color=stroke_color, start_angle=0).move_to(
            line3.get_center()
        )

        # angle Labels
        # center Label
        label0 = nMath("O").next_to(center, UP, buff=0.2)

        # given Angle
        label1 = (
            nMath("25^\\circ")
            .next_to(
                angle1,
                UP,
            )
            .shift(RIGHT * 0.2)
        )
        # angle to find
        label2 = nMath("x", color=RED_N).next_to(angle2, DOWN).shift(RIGHT * 0.1)

        label3 = nMath("50^\\circ").next_to(angle3, LEFT, buff=0.1).shift(DOWN * 0.25)

        label4 = nMath("80^\\circ").next_to(angle4, DOWN, buff=0.2)

        label2_ = nMath("40^\\circ").next_to(angle2, DOWN, buff=0.4).shift(RIGHT * 0.1)

        label5 = nMath("50^\\circ").next_to(angle7, RIGHT, buff=0.1).shift(UP * 0.1)
        label6 = nMath("50^\\circ").next_to(angle8, LEFT, buff=0.1).shift(UP * 0.1)

        # self.add(label1, label2_, label3, label4, label0)

        # self.add(
        #     circle,
        #     diameter,
        #     center,
        #     line3,
        #     line4,
        #     line5,
        #     line6,
        #     angle1,
        #     angle2,
        #     angle3,
        #     angle4,
        #     angle5,
        #     angle7,
        #     angle8,
        #     line1,
        #     line2,
        #     arrow_tip1,
        #     arrow_tip2,
        # )

        self.add(
            circle,
            diameter,
            center,
            line3,
            line4,
            line5,
            line6,
            angle1,
            angle2,
            label0,
            label1,
            label2,
        )

        hgl1 = solidHighlight(
            self,
            [VGroup(angle1, label1), VGroup(angle2, label2)],
            buff=0.25,
            corner_radius=0.4,
            animate=False,
        )

        hgl2 = getTriangularRegion(ORIGIN, line3.get_start(), line3.get_end())

        hgl3 = solidHighlight(
            self,
            VGroup(angle2, label2_),
            buff=0.25,
            corner_radius=0.4,
            animate=False,
        )

        self.wait(4)
        self.play(
            LaggedStart(
                diameter.animate.set_color(RED_N).set_stroke(width=6),
                FadeIn(arrow_tip1),
                line3.animate.set_color(RED_N).set_stroke(width=6),
                FadeIn(arrow_tip2),
                lag_ratio=0.6,
            )
        )
        self.play(
            diameter.animate.set_color(stroke_color).set_stroke(
                width=DEFAULT_STROKE_WIDTH
            ),
            line3.animate.set_color(stroke_color).set_stroke(
                width=DEFAULT_STROKE_WIDTH
            ),
        )
        self.wait(1)
        self.play(FadeIn(hgl1[0]))
        self.wait(1)
        self.play(FadeIn(hgl1[1]))
        self.wait(1)
        self.play(
            hgl1[0].animate.set_opacity(0),
            hgl1[1].animate.set_opacity(0),
        )
        self.play(Create(line2))
        self.play(Create(angle3[1]))
        self.wait(1)
        self.play(FadeIn(label3))
        self.wait(1)
        self.play(Create(line1))
        self.play(FadeIn(hgl2))
        self.wait(1)
        self.play(FadeOut(line4, angle1, label1))
        self.play(
            LaggedStart(
                Create(angle3[0]), Create(angle7), Create(angle8), lag_ratio=0.5
            )
        )
        self.play(FadeIn(label5, label6))
        self.wait(1)
        self.play(Create(angle4))
        self.play(FadeIn(label4))
        self.play(hgl2[0].animate.set_opacity(0), FadeOut(label5, label6))
        self.wait(1)

        self.play(Transform(label2, label2_))
        self.play(FadeIn(*hgl3))

        self.wait(10)


class ProblemStatement(Scene):
    def construct(self):
        addBackground(self)

        question = (
            VGroup(
                MathTex(
                    "\\text{Given a circle with center O}",
                    color=BLACK,
                ),
                MathTex(
                    "\\text{Find angle x}",
                    color=BLACK,
                ),
            )
            .arrange(DOWN, buff=0.35, aligned_edge=LEFT)
            .to_edge(UP)
        )

        self.add(question)
        self.wait(10)


class Options(Scene):
    def construct(self):
        addBackground(self)

        options = (
            VGroup(
                VGroup(
                    MathTex("A) \\ 25", color=BLACK),
                    MathTex("C) \\ 50", color=BLACK),
                ).arrange(DOWN, buff=0.35, aligned_edge=LEFT),
                VGroup(
                    MathTex("B) \\ 80", color=BLACK),
                    MathTex("D) \\ 40", color=BLACK),
                ).arrange(DOWN, buff=0.35, aligned_edge=LEFT),
            )
            .arrange(RIGHT, buff=2)
            .to_edge(UP)
        )

        self.play(FadeIn(options))
        self.wait(5)

        self.wait(1)
        self.play(
            Create(
                SurroundingRectangle(
                    options[1][1], corner_radius=0.1, buff=0.16, color=RED
                )
            )
        )
        self.wait(4)
