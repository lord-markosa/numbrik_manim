from manim import *


class trial21(Scene):
    def construct(self):
        # Step 1: Display the original equation
        equation = MathTex("2^a + 2^b + ", "2^c", "=", "148").shift(3 * UP)

        self.play(Write(equation))
        self.wait(1)

        # Step 2: take 2^c common
        equation_step_2 = MathTex(
            "2^c", "\cdot (", "2^{a-c} + 2^{b-c} + 1", ")", " = ", "4", "\cdot", "37"
        ).next_to(equation, DOWN)

        self.play(TransformFromCopy(equation[1], equation_step_2[0]))
        self.play(Write(equation_step_2[1]))
        self.play(TransformFromCopy(equation[0:2], equation_step_2[2]))
        self.play(Write(equation_step_2[3:5]))
        self.play(TransformFromCopy(equation[3], equation_step_2[5:]))
        self.wait(1)

        # Step 3: Equate the relevant part
        equation_step_3 = MathTex("2^c", "=", "4", "\implies", "c = 2").next_to(
            equation_step_2, DOWN
        )
        equation_step_3[0].set_color(YELLOW)
        equation_step_3[2].set_color(YELLOW)
        equation_step_3[4].set_color(GREEN)

        self.play(
            equation_step_2[0].animate.set_color(YELLOW),
            TransformFromCopy(equation_step_2[0], equation_step_3[0]),
        )
        self.play(Write(equation_step_3[1]))
        self.play(
            equation_step_2[5].animate.set_color(YELLOW),
            TransformFromCopy(equation_step_2[5], equation_step_3[2]),
        )
        self.play(Write(equation_step_3[3:]), run_time=2)
        self.wait(1)

        # Step 4: Equate the relevant part
        equation_step_4 = MathTex("2^{a-c} + 2^{b-c}", "+ 1", "=", "37").next_to(
            equation_step_3, DOWN
        )
        equation_step_4[0:2].set_color(BLUE)
        equation_step_4[3].set_color(BLUE)

        self.play(
            TransformFromCopy(equation_step_2[2], equation_step_4[0:2]),
            equation_step_2[2].animate.set_color(BLUE),
        )
        self.play(Write(equation_step_4[2]))
        self.play(
            TransformFromCopy(equation_step_2[7], equation_step_4[3]),
            equation_step_2[7].animate.set_color(BLUE),
        )
        self.wait(1)

        # Step 5: Simplify the above
        equation_step_5 = (
            MathTex("2^{a-c} +", "2^{b-c}", "=", "36")
            .next_to(equation_step_3, DOWN)
            .set_color(BLUE)
        )

        self.play(
            Transform(equation_step_4[0], equation_step_5[0]),
            Transform(equation_step_4[1:], equation_step_5[1:]),
        )
        self.play(equation_step_5.animate.set_color(WHITE))
        self.wait(1)

        # Step 7: Take 2^{b-c} common
        equation_step_6 = MathTex(
            "2^{b-c}", "\cdot (", "2^{a-b} + 1", ") =", "4", "\cdot", "9"
        ).next_to(equation_step_5, DOWN)
        self.play(TransformFromCopy(equation_step_5[1], equation_step_6[0]))
        self.play(Write(equation_step_6[1]))
        self.play(TransformFromCopy(equation_step_5[0:2], equation_step_6[2]))
        self.play(Write(equation_step_6[3]))
        self.play(TransformFromCopy(equation_step_5[3], equation_step_6[4:]))
        self.wait(1)

        # Step 8: Equate the relevant part
        equation_step_7 = MathTex("2^{b-c}", "=", "4", "\implies", "b-c = 2").next_to(
            equation_step_6, DOWN
        )
        equation_step_7_ = MathTex("2^{b-c} = 4", "\implies", "b = 4").next_to(
            equation_step_6, DOWN
        )
        equation_step_7[0].set_color(PURPLE)
        equation_step_7[2].set_color(PURPLE)
        equation_step_7_[2].set_color(GREEN)

        self.play(
            TransformFromCopy(equation_step_6[0], equation_step_7[0]),
            equation_step_6[0].animate.set_color(PURPLE),
        )
        self.play(Write(equation_step_7[1]))
        self.play(
            TransformFromCopy(equation_step_6[4], equation_step_7[2]),
            equation_step_6[4].animate.set_color(PURPLE),
        )
        self.play(Write(equation_step_7[3:]), run_time=3)
        self.play(Transform(equation_step_7, equation_step_7_), run_time=2)
        self.wait(1)

        # Step 9: Fade out the final solution
        equation_step_8 = MathTex("2^{a-b} + 1", "=", "9").next_to(
            equation_step_7_, DOWN
        )
        equation_step_8[0].set_color(ORANGE)
        equation_step_8[2].set_color(ORANGE)

        self.play(
            TransformFromCopy(equation_step_6[2], equation_step_8[0]),
            equation_step_6[2].animate.set_color(ORANGE),
        )
        self.play(Write(equation_step_8[1]))
        self.play(
            TransformFromCopy(equation_step_6[6], equation_step_8[2]),
            equation_step_6[6].animate.set_color(ORANGE),
        )
        self.wait(1)

        equation_step_9 = (
            MathTex("2^{a-b} = 8").next_to(equation_step_7, DOWN).set_color(ORANGE)
        )
        self.play(Transform(equation_step_8, equation_step_9))
        self.play(equation_step_9.animate.set_color(WHITE))
        self.wait(1)

        equation_step_10 = MathTex("\implies a-b = 3").next_to(equation_step_9, DOWN)
        equation_step_10_ = MathTex("\implies", "a = 7").next_to(equation_step_9, DOWN)
        equation_step_10_[1].set_color(GREEN)

        self.play(Write(equation_step_10), run_time=3)
        self.play(Transform(equation_step_10, equation_step_10_))
        self.wait(5)
