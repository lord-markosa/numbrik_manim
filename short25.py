from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        def color(sq, color):
            sq_temp = sq.copy()
            sq_temp.z_index = -10
            sq_temp.set_opacity(1)
            sq_temp.set_color(color)

            return sq_temp

        O = ORIGIN + DOWN
        s = 0.9
        x = 0.5
        sq1 = Square(
            s,
            color=RED_N100,
            stroke_color=BLACK,
            fill_opacity=0.5,
        ).move_to(O)

        area1 = nMath("4", color=BLACK).scale(1.1).move_to(sq1.get_center())

        s2 = x + s
        sq2 = Square(s2, color=BLACK).move_to(
            O + RIGHT * (s + s2) / 2 + UP * (s2 - s) / 2
        )

        s3 = s2 + s
        sq3 = Square(s3, color=BLACK).move_to(
            O + DOWN * (s + s3) / 2 + RIGHT * (s3 - s) / 2
        )

        s4 = s3 + s
        sq4 = Square(s4, color=BLACK).move_to(
            O + LEFT * (s + s4) / 2 + DOWN * (s4 - s) / 2
        )

        s5 = s4 + s
        sq5 = Square(s5, color=BLACK).move_to(
            O + LEFT * (s5 - s) / 2 + UP * (s + s5) / 2
        )

        s6 = 4 * s
        sq6 = Square(s6, color=BLACK).move_to(
            O + RIGHT * (s6 + s) / 2 + UP * (2 * s2 - s + s6) / 2
        )

        colored_sq6 = color(sq6, YELLOW)

        self.add(sq2, sq3, sq4, sq5, sq6)
        self.play(FadeIn(sq1))
        self.play(FadeIn(area1, scale=1.2))
        self.play(FadeIn(colored_sq6))
        self.wait(4)
        self.play(FadeOut(area1))

        ## The region's logic below is CONFUSING & CONVOLUTED!!

        reg1 = sq1.copy()
        self.play(FadeIn(reg1))
        self.play(reg1.animate.shift(s * RIGHT), run_time=1.5)

        reg2 = VGroup(reg1, sq1)
        reg3 = reg2.copy()
        self.play(FadeIn(reg3))
        self.play(reg3.animate.shift(DOWN * s), run_time=1.5)

        reg4 = reg3.copy()
        self.play(reg4.animate.shift(DOWN * s), run_time=1.5)

        reg5 = VGroup(reg2, reg3, reg4)
        reg6 = reg5.copy()
        self.play(FadeIn(reg6))
        self.play(reg6.animate.shift(2 * s * LEFT), run_time=2)

        reg7 = VGroup(reg6[0][1].copy(), reg6[1][1].copy(), reg6[2][1].copy())

        self.play(FadeIn(reg7))
        self.play(reg7.animate.shift(LEFT * s), run_time=1.5)

        reg8 = VGroup(
            reg6.copy(),
            reg7.copy(),
            reg2[1].copy(),
            reg3[1].copy(),
            reg4[1].copy(),
        )

        self.play(FadeIn(reg8))
        self.play(reg8.animate.shift(3 * s * UP), run_time=3)

        reg9 = VGroup(reg8[2].copy(), reg8[1][0].copy(), reg8[0][0].copy())
        self.play(FadeIn(reg9))
        self.play(reg9.animate.shift(UP * s), run_time=1.5)

        reg9.add(reg8)
        self.play(reg9.animate.shift(UP * (s - x + 0.1)), run_time=1.5)

        # self.play()
        reg10 = reg9.copy()
        self.play(FadeIn(reg10))
        self.play(reg10.animate.shift(RIGHT * 4 * s), run_time=4)

        self.wait(10)


class Statements(Scene):
    def construct(self):
        question = (
            VGroup(
                MathTex(
                    "\\text{All are squares}",
                    color=BLACK,
                ),
                MathTex(
                    "\\text{Find the area of yellow one}",
                    color=BLACK,
                ),
            )
            .arrange(DOWN)
            .to_edge(UP)
        )

        self.add(question)
        clearScreen(self, 4)

        stmt2 = nMath("Area = 16\\times 4 = 64")
        self.play(fadeInTex(stmt2))
        self.wait(4)
