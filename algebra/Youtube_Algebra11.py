from manim import *
from utils import *
import math


class Logarithms(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)

        # Title
        displayTitle(self, "Logarithms")

        animateTextSeq(
            self, [MathTex("y=2^x"), MathTex("\\text{or}"), MathTex("y=e^x")]
        )

        clearScreen(self, 2)

        # Axes and exponential graph
        axes = Axes(
            x_range=[-8, 8],
            y_range=[-2, 6],
            x_length=7,
            y_length=7,
            axis_config={"tip_shape": StealthTip, "include_ticks": False},
        ).to_edge(LEFT)

        exp_graph = axes.plot(lambda x: 2**x, color=BLUE, x_range=[-7.5, 2.5])

        self.play(Create(axes), Create(exp_graph))
        self.wait(1)

        mainEqn = MathTex("2^x = 5", color=YELLOW).shift(2 * RIGHT + 2 * UP)

        self.play(
            Write(mainEqn),
            run_time=1,
        )

        self.wait(1)

        log2_5 = math.log(5, 2)
        point5 = axes.c2p(0, 5)
        point_log2_5 = axes.c2p(log2_5, 0)

        self.play(Create(Dot(point5)), Write(MathTex("5").next_to(point5, LEFT)))

        # Dashed lines connecting points
        point_on_graph = axes.c2p(log2_5, 5)

        dashed_line_x = DashedLine(start=point_on_graph, end=point_log2_5, color=GREEN)
        dashed_line_y = DashedLine(start=point_on_graph, end=point5, color=GREEN)

        self.play(Create(dashed_line_x), Create(dashed_line_y))
        self.wait(1)

        self.play(
            Create(Dot(point_log2_5)), Write(MathTex("?").next_to(point_log2_5, DOWN))
        )
        self.wait(1)

        lines = animateTextSeq(
            self,
            [MathTex("\\Rightarrow x = f(5, 2)"), MathTex("x = log_2(5)")],
            next_reference=mainEqn,
            line_buffer=0.75,
        )
        self.wait(1)

        self.play(
            lines[1].animate.set_color(GREEN_N100),
            Create(SurroundingRectangle(lines[1], buff=0.25)),
        )
        self.wait(1)

        clearScreen(self, 2)

        animateTextSeq(
            self,
            [
                MathTex(
                    "y=2^x", "\\Rightarrow", "x = log_2(y)"
                ).set_color_by_tex_to_color_map({"y=2^x": NUMBRIK_COLOR}),
                MathTex(
                    "y=log_2(x)", "\\text{ is the inverse of }", "y = 2^x"
                ).set_color_by_tex_to_color_map(
                    {"y=log_2(x)": GREEN_N100, "y = 2^x": NUMBRIK_COLOR}
                ),
            ],
        )

        self.wait(1)

        clearScreen(self, 2)

        # Axes and exponential graph
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-5, 5],
            x_length=7,
            y_length=7,
            axis_config={"tip_shape": StealthTip, "include_ticks": False},
        )

        exp_graph = axes.plot(lambda x: 2**x, color=GREEN_N100, x_range=[-4, 2])
        exp_graph_label = axes.get_graph_label(
            exp_graph, label="y = 2^x", direction=UP, buff=0.25
        )
        self.play(Create(axes), Create(exp_graph))
        self.play(Write(exp_graph_label))

        self.wait(1)

        dashed_line = DashedLine(
            start=axes.c2p(-4, -4), end=axes.c2p(4, 4), color=YELLOW
        )
        self.play(Create(dashed_line))

        self.wait(1)

        self.play(FadeOut(exp_graph_label))

        self.play(VGroup(axes, exp_graph).animate.rotate(PI, UP + RIGHT, ORIGIN))

        self.wait(1)

        self.play(
            Write(MathTex("y=log_2(x)", color=GREEN_N100).move_to(axes.c2p(-2, 4)))
        )

        clearScreen(self, 2)

        displayTitle(self, "Few more examples")

        animateTextSeq(
            self,
            [
                MathTex("2^3 = 8", "\\Rightarrow", "log_2(8) = 3"),
                MathTex("10^2 = 100", "\\Rightarrow", "log_{10}(100) = 2"),
                MathTex("e^1 = e", "\\Rightarrow", "ln(e) = 1"),
                MathTex("5^0 = 1", "\\Rightarrow", "log_5(1) = 0"),
                MathTex("3^4 = 81", "\\Rightarrow", "log_3(81) = 4"),
            ],
        )

        # # Show 2^x = 5
        # eq1 = MathTex("2^x = 5").next_to(axes, UP)
        # self.play(Write(eq1))
        # self.wait(1)

        # # x = log_2(5)
        # eq2 = MathTex("x = \\log_2(5)").next_to(eq1, DOWN)
        # self.play(Write(eq2))
        # self.wait(1)

        # # Inverse concept: swapping x and y
        # inverse_text = Text(
        #     "Logarithm is the inverse of exponential", font_size=32
        # ).next_to(axes, UP)
        # self.play(Transform(eq1, inverse_text), FadeOut(eq2))
        # self.wait(1)
        # self.play(FadeOut(eq1))

        # Draw y = x line
        # identity_line = axes.plot(lambda x: x, color=YELLOW, x_range=[-2, 4])
        # identity_label = MathTex("y = x").next_to(axes.c2p(3.5, 3.5), RIGHT)
        # self.play(Create(identity_line), Write(identity_label))

        # # Show rotated graph: log base 2
        # log_graph = axes.plot(lambda x: math.log(x, 2), color=RED, x_range=[0.1, 16])
        # log_label = axes.get_graph_label(
        #     log_graph, label="y = \\log_2(x)", direction=DOWN
        # )

        # self.play(Create(log_graph), Write(log_label))

        # grp = VGroup(axes, log_graph, exp_graph)

        # self.play(grp.animate.rotate(PI, UP + RIGHT, ORIGIN))

        # self.wait(2)

        # # Fade everything out
        # self.play(*[FadeOut(mob) for mob in self.mobjects])
