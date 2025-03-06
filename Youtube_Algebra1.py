from manim import *
from constants import NUMBRIK_COLOR, TITLE_TEXT_POSITION


class AlgebraIntroduction(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Algebra", color=NUMBRIK_COLOR).scale(
            1.2).move_to(TITLE_TEXT_POSITION)
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeOut(title), run_time=0.5)
        self.wait(1)

        # Transition to Arithmetic Expressions
        numbers_intro = Text("Arithmetic Expressions", color=NUMBRIK_COLOR).move_to(
            TITLE_TEXT_POSITION+UP)
        equation = MathTex("2 + 2 = 4").next_to(numbers_intro, DOWN, buff=0.5)
        equation2 = MathTex(
            "2 + 5 - 6/2 = 4").next_to(equation, DOWN, buff=0.5)
        self.play(Write(numbers_intro))
        self.play(Write(equation), run_time=1.5)
        self.play(Write(equation2), run_time=1.5)
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # BODMAS

        bodmas = Text("BODMAS").scale(1.2).move_to(
            TITLE_TEXT_POSITION+2*UP)
        bodmas[0].set_color(PURPLE)
        bodmas[1].set_color(BLUE)
        bodmas[2].set_color(GREEN)
        bodmas[3].set_color(YELLOW)
        bodmas[4].set_color(ORANGE)
        bodmas[5].set_color(RED)
        self.play(Write(bodmas), run_time=1.5)

        brackets = Text("Brackets", color=PURPLE).next_to(
            bodmas, DOWN, buff=0.5)
        self.play(Write(brackets), run_time=1.5)
        orders = Text("Orders (Exponents)", color=BLUE).next_to(brackets, DOWN)
        self.play(Write(orders), run_time=1.5)
        division = Text("Division", color=GREEN).next_to(orders, DOWN)
        self.play(Write(division), run_time=1.5)
        multiplication = Text(
            "Multiplication", color=YELLOW).next_to(division, DOWN)
        self.play(Write(multiplication), run_time=1.5)
        addition = Text("Addition", color=ORANGE).next_to(multiplication, DOWN)
        self.play(Write(addition), run_time=1.5)
        subtraction = Text("Subtraction", color=RED).next_to(addition, DOWN)
        self.play(Write(subtraction), run_time=1.5)
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Introduction to Variables
        equation3 = MathTex("2 +", "something",
                            "= 5").move_to(TITLE_TEXT_POSITION)
        equation3[1].set_color(ORANGE)
        equation4 = MathTex("2 +", "something", "-2",
                            "= 5 - 2").next_to(equation3, DOWN, buff=0.5)
        equation4[1].set_color(ORANGE)
        equation5 = MathTex("something", "= 3").next_to(
            equation4, DOWN, buff=0.5)
        equation5[0].set_color(ORANGE)
        self.play(Write(equation3), run_time=1.5)
        self.wait(2)
        self.play(Write(equation4), run_time=2.5)
        self.wait(1)
        self.play(Write(equation5), run_time=1.5)
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        equation6 = MathTex(
            "2 + x = 5").move_to(TITLE_TEXT_POSITION+2*UP)
        description = Text("where x is a variable").next_to(
            equation6, DOWN).scale(0.5)
        self.play(Write(equation6), run_time=1.5)
        self.play(Write(description), run_time=1.5)
        self.wait(2)

        equation7 = MathTex(
            "x + x + x = 6").next_to(description, DOWN, buff=0.5)
        self.play(Write(equation7), run_time=1.5)
        self.wait(2)

        equation8_1 = MathTex(
            "x + x + x + x... (100) = 400").next_to(equation7, DOWN, buff=0.5)
        self.play(Write(equation8_1), run_time=1.5)
        self.wait(1)
        equation8 = MathTex(
            r"\Rightarrow 100 \times x = 400").next_to(equation8_1, DOWN, buff=0.5)
        self.play(Write(equation8), run_time=1.5)
        self.wait(1)
        equation9 = MathTex(
            r"\Rightarrow 100x = 400").next_to(equation8, DOWN, buff=0.5)
        self.play(Write(equation9), run_time=1.5)
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Expressions
        equation10 = MathTex(
            "A", "x", "+", "B").move_to(TITLE_TEXT_POSITION)
        self.play(Write(equation10), run_time=1.5)
        self.play(equation10[0].animate.set_color(BLUE),
                  equation10[1].animate.set_color(BLUE))
        self.play(equation10[3].animate.set_color(GREEN))

        equation11 = MathTex(
            "3", r"\cdot", "2", "+", "4", "=", "10").next_to(equation10, DOWN, buff=0.5)
        self.play(TransformFromCopy(equation10[0], equation11[0]))
        self.play(Write(equation11[1]))
        self.play(TransformFromCopy(equation10[1], equation11[2]))
        self.play(TransformFromCopy(equation10[2], equation11[3]))
        self.play(TransformFromCopy(equation10[3], equation11[4]))
        self.play(Write(equation11[5:7]))

        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Equations
        desc2 = Text("Equations", color=NUMBRIK_COLOR).move_to(
            TITLE_TEXT_POSITION+UP)
        self.play(Write(desc2), run_time=1.5)
        equation12 = MathTex("2 + x = 5").next_to(desc2, DOWN, buff=0.5)
        self.play(Write(equation12), run_time=1.5)
        self.wait(2)
        desc3 = Text("Inequality", color=NUMBRIK_COLOR).next_to(
            equation12, DOWN, buff=0.5)
        self.play(Write(desc3), run_time=1.5)
        equation13 = MathTex("2 + x > 5").next_to(desc3, DOWN, buff=0.5)
        self.play(Write(equation13), run_time=1.5)
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Additional information
        equation14_1 = MathTex(r"x + x + x + x").move_to(
            TITLE_TEXT_POSITION+UP)
        self.play(Write(equation14_1), run_time=1.5)
        equation15_1 = MathTex(r"= 4x").next_to(equation14_1, DOWN, buff=0.5)
        self.play(TransformFromCopy(equation14_1, equation15_1), run_time=1.5)
        self.wait(2)

        equation14 = MathTex(r"x \cdot x \cdot x \cdot x").next_to(
            equation15_1, DOWN, buff=1)
        self.play(Write(equation14), run_time=1.5)
        equation15 = MathTex(r"= x^4").next_to(equation14, DOWN, buff=0.5)
        self.play(TransformFromCopy(equation14, equation15), run_time=1.5)
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
