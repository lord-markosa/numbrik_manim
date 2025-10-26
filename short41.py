from manim import *
from utils import *


class Template(Scene):
    def construct(self):
        O = ORIGIN + 2 * DOWN + 2 * LEFT

        A = O + 3 * UP
        B = A + 4 * RIGHT
        C = O + 4 * RIGHT

        outerCircle = Sector(
            radius=5,
            arc_center=O,
            angle=PI / 2,
            # color=YELLOW,
            stroke_color=GREY_N100,
            stroke_width=5,
        )

        self.add(outerCircle)

        rect = Polygon(O, A, B, C, color=GREY_N400)
        self.add(rect)

        circle1 = Sector(
            radius=1,
            arc_center=B,
            angle=PI / 2,
            start_angle=PI,
            color=YELLOW,
            stroke_color=GREY_N400,
            stroke_width=5,
        )
        self.add(circle1)

        circle2 = Sector(
            radius=2,
            arc_center=C,
            angle=PI / 2,
            start_angle=PI / 2,
            color=VIOLET_N50,
            stroke_color=GREY_N400,
            stroke_width=5,
        )
        self.add(circle2)

        circle3 = Sector(
            radius=3,
            arc_center=A,
            angle=-PI / 2,
            color=GREEN_N100,
            stroke_color=GREY_N400,
            stroke_width=5,
        )
        self.add(circle3)

        # mark the yellow circle length
        mark1 = DoubleArrow(
            B + RIGHT * 0.3,
            B + RIGHT * 0.3 + DOWN,
            color=GREY_N800,
            buff=0,
            tip_length=0.2,
            stroke_width=2,
        )
        self.add(mark1)

        mark1_ = DoubleArrow(
            B + UP * 0.3,
            B + UP * 0.3 + LEFT,
            color=GREY_N800,
            buff=0,
            tip_length=0.2,
            stroke_width=2,
        )
        self.add(mark1_)

        # mark the violet circle length
        mark2 = DoubleArrow(
            B + RIGHT * 0.3 + DOWN,
            C + RIGHT * 0.3,
            color=GREY_N800,
            buff=0,
            tip_length=0.2,
            stroke_width=2,
        )
        self.add(mark2)

        # mark the green circle length
        mark3 = DoubleArrow(
            O + LEFT * 0.3,
            A + LEFT * 0.3,
            color=GREY_N800,
            buff=0,
            tip_length=0.2,
            stroke_width=2,
        )
        self.add(mark3)
        mark3_ = DoubleArrow(
            A + UP * 0.3 + RIGHT * 3,
            A + UP * 0.3,
            color=GREY_N800,
            buff=0,
            tip_length=0.2,
            stroke_width=2,
        )
        self.add(mark3_)

        # create the common normal (diagonal of the rectangle)
        diagonal = DashedLine(
            A, C, color=WHITE, dash_length=0.15, dashed_ratio=0.8, stroke_width=5
        )
        self.add(diagonal)

        # def highlight_diagonal():
        #     objects_to_fade = [
        #         outerCircle,
        #         rect,
        #         circle1,
        #         circle2,
        #         circle3,
        #         mark1,
        #         mark1_,
        #         mark2,
        #         mark3,
        #         mark3_,
        #     ]

        #     for obj in objects_to_fade:
        #         obj.save_state()

        #     self.play(*[obj.animate.set_opacity(0.2) for obj in objects_to_fade])
        #     self.play(
        #         diagonal.animate.set_color(RED_N100).scale(1.1),
        #         rate_func=there_and_back_with_pause,
        #     )
        #     self.play(*[Restore(obj) for obj in objects_to_fade])
        # self.play(*[obj.animate.set_opacity(1) for obj in objects_to_fade])

        # obj.set_color(GREY)

        # Call the function to highlight diagonal
        # highlight_diagonal()

        self.wait(5)


class Solve(Scene):
    def construct(self):
        O = ORIGIN + 2 * DOWN + 2 * LEFT

        A = O + 3 * UP
        B = A + 4 * RIGHT
        C = O + 4 * RIGHT

        outerCircle = Sector(
            radius=5,
            arc_center=O,
            angle=PI / 2,
            # color=YELLOW,
            stroke_color=GREY_N100,
            stroke_width=5,
            z_index=-0.1,
            fill_opacity=0,
        )

        self.add(outerCircle)

        rect = Polygon(O, A, B, C, stroke_color=GREY_N400, stroke_width=4)
        self.add(rect)

        circle1 = Sector(
            radius=1,
            arc_center=B,
            angle=PI / 2,
            start_angle=PI,
            color=YELLOW,
            stroke_color=GREY_N400,
            stroke_width=5,
        )
        self.add(circle1)

        circle2 = Sector(
            radius=2,
            arc_center=C,
            angle=PI / 2,
            start_angle=PI / 2,
            color=VIOLET_N50,
            stroke_color=GREY_N400,
            stroke_width=5,
        )
        self.add(circle2)

        circle3 = Sector(
            radius=3,
            arc_center=A,
            angle=-PI / 2,
            color=GREEN_N100,
            stroke_color=GREY_N400,
            stroke_width=5,
        )
        self.add(circle3)

        # mark the yellow circle length
        mark1 = DoubleArrow(
            B + RIGHT * 0.3,
            B + RIGHT * 0.3 + DOWN,
            color=GREY_N800,
            buff=0,
            tip_length=0.2,
            stroke_width=2,
        )
        # self.add(mark1)

        mark1_ = DoubleArrow(
            B + UP * 0.3,
            B + UP * 0.3 + LEFT,
            color=GREY_N800,
            buff=0,
            tip_length=0.2,
            stroke_width=2,
        )
        # self.add(mark1_)

        # mark the violet circle length
        mark2 = DoubleArrow(
            B + RIGHT * 0.3 + DOWN,
            C + RIGHT * 0.3,
            color=GREY_N800,
            buff=0,
            tip_length=0.2,
            stroke_width=2,
        )
        # self.add(mark2)

        # mark the green circle length
        mark3 = DoubleArrow(
            O + LEFT * 0.3,
            A + LEFT * 0.3,
            color=GREY_N800,
            buff=0,
            tip_length=0.2,
            stroke_width=2,
        )
        # self.add(mark3)
        mark3_ = DoubleArrow(
            A + UP * 0.3 + RIGHT * 3,
            A + UP * 0.3,
            color=GREY_N800,
            buff=0,
            tip_length=0.2,
            stroke_width=2,
        )
        # self.add(mark3_)

        mark4 = DoubleArrow(
            O + DOWN * 0.3,
            C + DOWN * 0.3,
            color=GREY_N800,
            buff=0,
            tip_length=0.2,
            stroke_width=2,
        )

        label1 = nMath("1").next_to(mark1, RIGHT, buff=0.1).scale(0.8)
        label2 = nMath("x").next_to(mark2, RIGHT, buff=0.1).scale(0.8)
        label3 = nMath("x+1").next_to(mark3, LEFT, buff=0.1).scale(0.8)
        label1_ = nMath("1").next_to(mark1_, UP, buff=0.1).scale(0.8)
        label3_ = nMath("x+1").next_to(mark3_, UP, buff=0.1).scale(0.8)
        label4 = nMath("x+2").next_to(mark4, DOWN, buff=0.1).scale(0.8)

        # create the common normal (diagonal of the rectangle)
        diagonal = DashedLine(
            A, C, color=WHITE, dash_length=0.15, dashed_ratio=0.8, stroke_width=5
        )
        # self.add(diagonal)

        objects_to_fade = [
            outerCircle,
            # rect,
            circle1,
            circle2,
            circle3,
            # mark1,
            # mark1_,
            # mark2,
            # mark3,
            # mark3_,
        ]

        def highlightObject(objects_to_hgl, objects_to_fade, extraAnimation=None):
            for obj in objects_to_fade:
                obj.save_state()

            if len(objects_to_fade):
                self.play(*[obj.animate.set_opacity(0.2) for obj in objects_to_fade])

            hglGroup = VGroup()
            for obj in objects_to_hgl:
                hglGroup.add(obj)

            self.play(
                hglGroup.animate.scale(1.05).set_stroke(color=RED_N100),
                rate_func=there_and_back_with_pause,
            )

            if extraAnimation != None:
                self.play(extraAnimation)

            if len(objects_to_fade):
                self.play(*[Restore(obj) for obj in objects_to_fade])

        highlightObject([circle1, circle2, circle3], [])

        highlightObject([outerCircle], [])
        self.wait(1)

        highlightObject([circle1], [])
        self.wait()

        self.play(GrowArrow(mark1), FadeIn(label1, shift=0.5 * LEFT))
        self.wait(1)

        highlightObject([circle1, circle2, circle3], [])

        self.wait(1)
        self.play(GrowArrow(mark2), FadeIn(label2, shift=0.5 * LEFT))

        rt1 = getRightAngle(O, A, B, length=0.2, stroke_width=3, color=GREY_N400)
        rt2 = getRightAngle(A, B, C, length=0.2, stroke_width=3, color=GREY_N400)
        rt3 = getRightAngle(B, C, O, length=0.2, stroke_width=3, color=GREY_N400)
        rt4 = getRightAngle(C, O, A, length=0.2, stroke_width=3, color=GREY_N400)

        self.play(
            LaggedStart(
                Create(rt1), Create(rt2), Create(rt3), Create(rt4), lag_ratio=0.2
            )
        )
        highlightObject([rect, rt1, rt2, rt3, rt4], [])
        self.wait(1)

        self.play(FadeIn(mark3, shift=LEFT * 4.3), FadeIn(label3, shift=RIGHT * 0.5))
        self.wait(1)

        self.play(
            LaggedStart(
                ReplacementTransform(mark3.copy(), mark3_),
                FadeIn(label3_, shift=DOWN * 0.5),
                lag_ratio=0.5,
            )
        )
        self.wait(1)
        self.play(
            LaggedStart(
                GrowArrow(mark1_),
                FadeIn(label1_, shift=DOWN * 0.5),
                lag_ratio=0.3,
            )
        )
        self.wait(1)

        self.play(
            LaggedStart(
                FadeIn(mark4, shift=DOWN * 3.3),
                FadeIn(label4, shift=UP * 0.5),
                lag_ratio=0.3,
            )
        )
        self.wait(1)

        triangle = (
            getTriangularRegion(O, A, C, color=GREY_N800)
            .set_opacity(0.5)
            .set_z_index(1)
        )
        self.play(Create(diagonal))
        self.wait(2)
        self.play(FadeIn(triangle))

        self.wait(4)

        self.play(
            LaggedStart(
                FadeOut(
                    triangle, diagonal, mark1_, mark3_, mark4, label1_, label3_, label4
                ),
                Transform(
                    label2, nMath("2").next_to(mark2, RIGHT, buff=0.1).scale(0.8)
                ),
                Transform(label3, nMath("3").next_to(mark3, LEFT, buff=0.1).scale(0.8)),
                lag_ratio=0.7,
            )
        )

        # self.play(*[obj.animate.set_opacity(1) for obj in objects_to_fade])

        # obj.set_color(GREY)

        # Call the function to highlight diagonal
        # highlight_diagonal()

        self.wait(5)


class Statements(Scene):
    def construct(self):
        stmt1 = nMath("diagonal =", "(x) + (x+1)")
        stmt2 = nMath("diagonal =", "2x+1")

        stmt3 = nMath("(x+1)^2 + (x+2)^2 = (2x+1)^2")

        stmt4 = nMath("2x^2 - 2x - 4", "= 0").next_to(stmt3, DOWN, buff=0.5)
        stmt41 = nMath("x^2 - x - 2", "= 0").next_to(stmt4, 0, aligned_edge=DOWN)
        stmt42 = (
            nMath("(x-2)(x+1)", "= 0")
            .next_to(stmt4, 0, aligned_edge=DOWN)
            .shift(DOWN * 0.1)
        )
        stmt43 = nMath("x = 2").next_to(stmt4, 0, aligned_edge=DOWN)

        stmt5 = nMath("Area =", "\\frac{\\pi(1^2 + 2^2 + 3^2)}{4}")
        stmt6 = nMath("Area =", "\\frac{7\\pi}{2}")

        self.play(fadeInTex(stmt1))
        self.wait(1)
        self.play(TransformMatchingTex(stmt1, stmt2))
        clearScreen(self, 2)

        self.play(fadeInTex(stmt3))
        self.wait(1)
        self.play(fadeInTex(stmt4))
        self.wait(0.5)
        self.play(TransformMatchingTex(stmt4, stmt41), run_time=1.5)
        self.wait(0.5)
        self.play(TransformMatchingTex(stmt41, stmt42), run_time=1.5)
        self.wait(0.5)
        self.play(TransformMatchingTex(stmt42, stmt43), run_time=1.5)

        clearScreen(self, 2)

        self.play(fadeInTex(stmt5))
        self.wait(1)
        self.play(TransformMatchingTex(stmt5, stmt6), run_time=1.5)

        self.wait(5)
