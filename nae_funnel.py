from manim import *
from utils import *


class BernoulliDemo(Scene):
    def construct(self):
        # Create the funnel (triangle shape)
        funnel = Polygon(
            LEFT * 3 + UP * 3,  # left wide
            RIGHT * 3 + UP * 3,  # right wide
            RIGHT * 0.5,  # narrow right
            RIGHT * 0.5 + 2 * DOWN,  # bottom point right
            LEFT * 0.5 + 2 * DOWN,  # bottom point left
            LEFT * 0.5,  # narrow left
            color=BLACK,
        )

        # Ball at the mouth of funnel
        ball = Circle(radius=1, color=YELLOW, fill_opacity=1, stroke_color=BLACK).shift(
            UP
        )

        # Add funnel and ball
        self.add(funnel, ball)

        # Define air flow arrows
        arrows = VGroup()
        for x in [-0.35, 0, 0.35]:
            arrow = Arrow(
                DOWN * 3.2 + RIGHT * x,
                DOWN * 1.2 + RIGHT * x,
                buff=0.1,
                color=GREY_C,
                tip_length=0.35,
            )
            arrows.add(arrow)

        self.play([GrowArrow(a) for a in arrows])
        self.play(ball.animate.shift(0.3 * UP))

        # Animate repeated airflow effect
        moving_arrows = VGroup(
            Arrow(
                start=RIGHT * 0.5 + 0.2 * UP,
                end=RIGHT * 3 + UP * 3.2,
                buff=0.6,
                color=GREY_C,
                tip_length=0.5,
            ),
            Arrow(
                start=LEFT * 0.5 + 0.2 * UP,
                end=LEFT * 3 + UP * 3.2,
                buff=0.6,
                tip_length=0.5,
                color=GREY_C,
            ),
        )

        # for x in [-0.8, 0, 0.8]:
        #     start = UP * 2 + RIGHT * x
        #     end = DOWN * 1.2 + RIGHT * x
        #     m_arrow = Arrow(start=start, end=end, buff=0.1, color=BLUE)
        #     moving_arrows.add(m_arrow)

        # # Loop the flow movement
        # flow_animation = AnimationGroup(
        #     *[
        #         Succession(FadeIn(a), FadeOut(a, shift=DOWN * 0.5))
        #         for a in moving_arrows
        #     ],
        #     lag_ratio=0.3,
        # )

        # # Keep repeating for airflow illusion
        self.play(*[GrowArrow(a) for a in moving_arrows])
        self.wait(5)

        arc = Arc(
            radius=1.05,
            start_angle=7 * PI / 6,
            angle=2 * PI / 3,
            stroke_width=16,
            color=NUMBRIK_COLOR,
            arc_center=ball.get_center(),
        )

        labelP1 = nMath("P_1").next_to(ORIGIN, DOWN, buff=0.1).scale(1.4)
        labelP2 = nMath("P_0").next_to(ball, UP, buff=1).scale(1.4)
        label1 = nMath("P_0, v_0").next_to(arrows[2], RIGHT, buff=0.75).scale(1.4)
        label2 = (
            nMath("v1")
            .next_to(moving_arrows[0], RIGHT, buff=-0.2)
            .scale(1.4)
            .shift(0.3 * DOWN)
        )

        self.play(FadeIn(label1), FadeIn(label2))
        self.wait(1)
        self.play(Create(arc))
        self.play(Write(labelP1), Write(labelP2), run_time=1.5)

        force = Arrow(2.8 * UP, ball.get_center(), color=RED_N, stroke_width=8, buff=0)

        self.wait(1)
        self.play(GrowArrow(force))
        self.wait(10)


class Statements(Scene):
    def construct(self):
        stmt1 = nMath("Area", "\\times", "v", "= Volume\\,Rate = Constant").shift(UP)
        stmt2 = nMath(
            "Area \\downarrow \\,\\, \\Rightarrow \\,\\, v \\uparrow"
        ).next_to(stmt1, DOWN, buff=0.6)
        stmt3 = nMath("\\Rightarrow v_1 > v_0").next_to(stmt2, DOWN, buff=0.6)

        highl81 = solidHighlight(self, stmt1[0], buff=0.2, color=RED_A, animate=False)
        highl82 = solidHighlight(
            self, stmt1[2], buff=0.15, color=GREEN_A, animate=False
        )

        self.play(fadeInTex(stmt1))
        self.wait(1)
        self.play(
            (FadeIn(highlight) for highlight in highl81),
            (FadeIn(highlight) for highlight in highl82),
        )
        self.wait(1)
        self.play(fadeInTex(stmt2))
        self.wait(1)
        self.play(fadeInTex(stmt3))

        clearScreen(self, 3)
        stmt0 = nMath("\\text{Bernoulli's Equation}").shift(2.3 * UP)
        stmt1 = nMath("P", "+", "\\frac{1}{2}\\rho", "v", "^2", "= Constant").shift(UP)
        stmt2 = (
            nMath("v \\uparrow \\,\\, \\Rightarrow \\,\\, P \\downarrow")
            .next_to(stmt1, DOWN, buff=0.6)
            .scale(1.2)
        )
        stmt3 = (
            nMath("v_1 > v_0 \\,\\, \\Rightarrow \\,\\, P_1 < P_0")
            .next_to(stmt2, DOWN, buff=0.6)
            .scale(1.2)
        )
        self.play(fadeInTex(stmt0))
        self.play(fadeInTex(stmt1))
        self.wait(1)
        highl81 = solidHighlight(self, stmt1[0], buff=0.2, color=GREEN_A, animate=False)
        highl82 = solidHighlight(self, stmt1[3], buff=0.15, color=RED_A, animate=False)
        self.play(
            (FadeIn(highlight) for highlight in highl81),
            (FadeIn(highlight) for highlight in highl82),
        )
        self.play(fadeInTex(stmt2))
        self.wait(1)
        self.play(fadeInTex(stmt3))
        self.wait(10)
