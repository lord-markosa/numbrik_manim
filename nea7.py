from manim import *
from utils import *


class Bottle(Scene):
    def construct(self):
        bottle = Polygon(
            2 * UP + LEFT,
            DOWN + LEFT,
            1.5 * DOWN + 0.25 * LEFT,
            1.8 * DOWN + 0.25 * LEFT,
            1.8 * DOWN + 0.25 * RIGHT,
            1.5 * DOWN + 0.25 * RIGHT,
            DOWN + RIGHT,
            2 * UP + RIGHT,
            color=BLACK,
        )

        water = Polygon(
            UP + LEFT,
            DOWN + LEFT,
            1.5 * DOWN + 0.25 * LEFT,
            1.8 * DOWN + 0.25 * LEFT,
            1.8 * DOWN + 0.25 * RIGHT,
            1.5 * DOWN + 0.25 * RIGHT,
            DOWN + RIGHT,
            UP + RIGHT,
            color=BLUE,
            fill_opacity=1,
            z_index=-10,
        )

        fallingWater = Polygon(
            1.5 * DOWN + 0.21 * LEFT,
            2.5 * DOWN + 0.21 * LEFT,
            2.5 * DOWN + 0.21 * RIGHT,
            1.5 * DOWN + 0.21 * RIGHT,
            color=BLUE,
            fill_opacity=1,
            z_index=-10,
        )

        vortex = Polygon(
            1.1 * UP + 0.5 * LEFT,
            1.8 * DOWN + 0.05 * LEFT,
            2.6 * DOWN + 0.05 * LEFT,
            2.6 * DOWN + 0.05 * RIGHT,
            1.8 * DOWN + 0.05 * RIGHT,
            1.1 * UP + 0.5 * RIGHT,
            color=WHITE,
            fill_opacity=1,
            z_index=-9,
        )

        straw = Polygon(
            1.1 * UP + 0.05 * LEFT,
            2.6 * DOWN + 0.05 * LEFT,
            2.6 * DOWN + 0.05 * RIGHT,
            1.1 * UP + 0.05 * RIGHT,
            color=WHITE,
            stroke_width=2,
            stroke_color=BLACK,
            fill_opacity=1,
            z_index=-9,
        )

        water.round_corners(0.1)
        bottle.round_corners(0.1)
        fallingWater.round_corners(0.1)

        waterBottle = VGroup(water, bottle, fallingWater, vortex, straw)

        waterBottle.scale(1.5).shift(LEFT * 1.8)

        self.add(water, bottle, fallingWater)
        eq1 = nMath("P \\times V = constant").shift(3 * RIGHT)
        eq2 = nMath("V \\uparrow \\;", "\\Rightarrow P \\downarrow").next_to(
            eq1, DOWN, buff=0.5
        )
        # self.add(eq1, eq2)

        air = Ellipse(height=1, width=2.5, color=RED_N100).next_to(water, UP, buff=0.2)

        arrow = CurvedArrow(
            air.get_right(),
            eq1.get_top() + 0.4 * UP + 0.4 * LEFT,
            color=RED_N100,
            angle=-PI / 3,
        )

        arrow2 = Arrow(
            1.2 * UP, 2.8 * DOWN, color=BLUE_E, stroke_width=10, tip_length=0.6
        ).shift(4 * LEFT)

        arrow3 = Arrow(
            3 * DOWN + water.get_center(),
            water.get_center(),
            color=YELLOW,
            stroke_width=10,
            tip_length=0.6,
            z_index=-1,
        )

        nozzlePointer = CurvedArrow(
            ORIGIN + 1.5 * DOWN + 0.5 * RIGHT,
            water.get_center() + 2 * DOWN + 0.5 * RIGHT,
            angle=-PI / 3,
            color=RED_N,
        )

        air_bubble = Ellipse(
            width=1, height=0.75, color=WHITE, fill_opacity=1, z_index=-1
        ).move_to(water.get_center() + DOWN)

        # self.add(air, arrow, arrow2, air_bubble)

        arrow4 = Arrow(
            3.6 * DOWN + water.get_center(),
            water.get_center() + 3.2 * UP,
            color=GREY_B,
            stroke_width=8,
            tip_length=0.4,
            z_index=-1,
        )

        # Part 1
        self.play(LaggedStart(Create(air), Create(arrow), lag_ratio=0.7))
        self.play(fadeInTex(eq1))
        self.wait(0.5)
        self.play(GrowArrow(arrow2))
        self.wait(0.5)
        self.play(fadeInTex(eq2))
        self.wait(0.5)
        self.play(
            LaggedStart(
                FadeIn(air_bubble),
                air_bubble.animate.scale(2.2).shift(UP * 1.8),
            ),
            GrowArrow(arrow3),
            rate_func=smooth,
            run_time=4,
        )
        self.wait(0.5)
        self.play(Create(nozzlePointer))
        self.wait(2)

        # Part 2
        self.play(
            FadeOut(nozzlePointer, arrow3, air_bubble, eq2, eq1, arrow2, arrow, air)
        )
        self.play(FadeIn(vortex))
        self.wait(1)

        eq1 = nMath("P_{inside} = P_{outside} = P_{air}").shift(3 * RIGHT)

        self.play(
            Create(arrow4),
            LaggedStart(Create(air), Create(arrow), lag_ratio=0.5),
        )
        self.play(
            fadeInTex(eq1),
        )
        self.wait(2)

        # Part3
        self.play(FadeOut(arrow4), Transform(vortex, straw))
        self.wait(1)
        self.play(Create(nozzlePointer))

        # self.add(straw, nozzlePointer)

        self.wait(10)
