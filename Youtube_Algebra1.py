from manim import *

# ======= IN PROGRESS =======


class AlgebraIntroduction(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Algebra", color=BLUE).scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Transition to Numbers
        numbers_intro = Text("Numbers").scale(1.2)
        self.play(Write(numbers_intro))
        self.wait(1)
        equation = MathTex("3 + 2 = 5").scale(1.2)
        self.play(Transform(numbers_intro, equation))
        self.wait(2)
        self.play(FadeOut(equation))

        # Introduction to Variables
        variables_intro = Text("Variables").scale(1.2)
        self.play(Write(variables_intro))
        self.wait(1)
        variable_example = MathTex("x + 2 = 5").scale(1.2)
        self.play(Transform(variables_intro, variable_example))
        self.wait(2)

        # Clear screen
        self.play(FadeOut(variables_intro))

        # Solving for x
        self.play(variable_example.animate.shift(UP * 2))
        solve_step1 = MathTex("x + 2 = 5").next_to(variable_example, DOWN)
        solve_step2 = MathTex("x = 5 - 2").next_to(solve_step1, DOWN)
        solve_step3 = MathTex("x = 3").next_to(solve_step2, DOWN)
        self.play(Write(solve_step1))
        self.wait(1)
        self.play(Transform(solve_step1, solve_step2))
        self.wait(1)
        self.play(Transform(solve_step2, solve_step3))
        self.wait(2)
        self.play(FadeOut(variable_example), FadeOut(solve_step3))

        # # Introduction to Expressions
        # expressions_intro = Text("Expressions").scale(1.2)
        # self.play(Write(expressions_intro))
        # self.wait(1)
        # expression_example = MathTex("2x + 3").scale(1.2)
        # self.play(Transform(expressions_intro, expression_example))
        # self.wait(2)
        # self.play(FadeOut(expression_example))

        # # Introduction to Equations
        # equations_intro = Text("Equations").scale(1.2)
        # self.play(Write(equations_intro))
        # self.wait(1)
        # equation_example = MathTex("2x + 3 = 7").scale(1.2)
        # self.play(Transform(equations_intro, equation_example))
        # self.wait(2)

        # # Solving the equation
        # self.play(equation_example.animate.shift(UP * 2))
        # eq_solve_step1 = MathTex("2x + 3 = 7").next_to(equation_example, DOWN)
        # eq_solve_step2 = MathTex("2x + 3 - 3 = 7 - 3").next_to(eq_solve_step1, DOWN)
        # eq_solve_step3 = MathTex("2x = 4").next_to(eq_solve_step2, DOWN)
        # eq_solve_step4 = MathTex("x = \\frac{4}{2}").next_to(eq_solve_step3, DOWN)
        # eq_solve_step5 = MathTex("x = 2").next_to(eq_solve_step4, DOWN)
        # self.play(Write(eq_solve_step1))
        # self.wait(1)
        # self.play(Transform(eq_solve_step1, eq_solve_step2))
        # self.wait(1)
        # self.play(Transform(eq_solve_step2, eq_solve_step3))
        # self.wait(1)
        # self.play(Transform(eq_solve_step3, eq_solve_step4))
        # self.wait(1)
        # self.play(Transform(eq_solve_step4, eq_solve_step5))
        # self.wait(2)
        # self.play(FadeOut(eq_solve_step5), FadeOut(equation_example))

        # # Conclusion
        # conclusion = Text("Great job!\nKeep practicing Algebra!", color=GREEN).scale(1.2)
        # self.play(Write(conclusion))
        # self.wait(3)
        # self.play(FadeOut(conclusion))
        # self.wait(1)
