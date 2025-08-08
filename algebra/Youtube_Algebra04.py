from manim import *
from utils import *


class Quadratics(Scene):
    def construct(self):
        self.intro_scene()
        clearScreen(self)
        self.overview()
        clearScreen(self)
        self.basic_graph()
        clearScreen(self)
        self.graph_parabola()
        clearScreen(self)
        self.factorization_example1()
        clearScreen(self)
        self.factorization_example2()
        clearScreen(self)
        self.factorization_example3()
        clearScreen(self)
        self.complete_the_square_example()
        clearScreen(self)

    def intro_scene(self):
        displayTitle(self, "Quadratic Expressions")

    def overview(self):
        animateTextSeq(
            self,
            [
                Text("Linear Expression", color=NUMBRIK_COLOR).scale(0.8),
                MathTex("a", "x", " + b").set_color_by_tex("x", PURE_GREEN),
                Text("Quadratic Expression", color=NUMBRIK_COLOR).scale(0.8),
                MathTex("a", "x^2", " + b", "x", " + c").set_color_by_tex(
                    "x", PURE_GREEN
                ),
            ],
        )

        clearScreen(self)

        animateTextSeq(
            self,
            [
                MathTex("x^2"),
                Text("For x = 1, we get").scale(0.6),
                MathTex("value = 1^2 = 1"),
                Text("For x = 2, we get").scale(0.6),
                MathTex("value = 2^2 = 4"),
                Text("Let's graph these").scale(0.5),
            ],
        )

        clearScreen(self)

        animateTextSeq(
            self,
            [
                MathTex("y = x^2").scale(1.2),
                Text("Parabola", color=NUMBRIK_COLOR),
            ],
        )

    def basic_graph(self):
        plane = (
            NumberPlane(
                x_range=[-5, 5, 1],
                x_length=6,
                y_range=[0, 16, 1],
                y_length=6,
                background_line_style={"stroke_color": YELLOW, "stroke_opacity": 0.3},
            )
            .add_coordinates()
            .shift(2 * LEFT)
        )

        def sq_func(x):
            return x * x

        discreteX = [x for x in range(-4, 5)]
        discreteY = [sq_func(x) for x in discreteX]

        self.play(Create(plane))

        value_table = (
            Table(
                [*[[str(x), str(y)] for x, y in zip(discreteX, discreteY)]],
                col_labels=[MathTex("x"), MathTex("y = x^2")],
                include_outer_lines=True,
                line_config={
                    "stroke_color": YELLOW,
                    "stroke_width": 0.5,
                    "stroke_opacity": 0.5,
                },
            )
            .shift(4 * RIGHT)
            .scale(0.5)
        )

        self.play(
            Create(value_table.get_rows()[0]),
            Create(value_table.get_vertical_lines()),
            Create(value_table.get_horizontal_lines()),
        )

        for i, (x, y) in enumerate(zip(discreteX, discreteY)):
            dot = Dot(point=plane.c2p(x, y), color=GREEN_E)
            row = value_table.get_rows()[i + 1]  # +1 to skip header row
            self.play(AnimationGroup(Create(row), Create(dot), lag_ratio=0.5))

        parabola = plane.plot(sq_func, x_range=[-4, 4]).set_color(NUMBRIK_COLOR)

        self.play(Create(parabola))

        self.wait(2)

    def graph_parabola(self):
        x_0 = ValueTracker(0)
        y_0 = ValueTracker(0)

        plane1 = (
            NumberPlane(
                x_range=[-5, 5, 1],
                x_length=7,
                y_range=[-1, 16, 2],
                y_length=6,
                background_line_style={"stroke_color": YELLOW, "stroke_opacity": 0.3},
            )
            .add_coordinates()
            .shift(2 * LEFT)
        )

        func1 = always_redraw(
            lambda: plane1.plot(
                lambda x: (x - x_0.get_value()) ** 2 + y_0.get_value(),
                x_range=[-(12**0.5) + x_0.get_value(), 12**0.5 + x_0.get_value()],
            ).set_color(NUMBRIK_COLOR)
        )

        equation_text = (
            MathTex("y = x^2").shift(4 * RIGHT + UP).set_color(NUMBRIK_COLOR)
        )
        new_equation_text = (
            always_redraw(lambda: MathTex("y = (x -", "x_0", ")^2 +", "y_0"))
            .next_to(equation_text, 0)
            .set_color(NUMBRIK_COLOR)
        )
        new_equation_text[1].set_color(GREEN_E)
        new_equation_text[3].set_color(GREEN_E)

        x_0_label = (
            MathTex(r"x_0 = \qquad").next_to(equation_text, 2 * DOWN).set_color(GREEN_E)
        )
        y_0_label = (
            MathTex(r"y_0 = \qquad").next_to(x_0_label, 1.2 * DOWN).set_color(GREEN_E)
        )

        x0_value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=1)
            .set_value(x_0.get_value())
            .next_to(x_0_label, RIGHT, buff=0.1)
            .shift(0.1 * RIGHT)
            .set_color(GREEN_E)
        )

        y0_value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=1)
            .set_value(y_0.get_value())
            .next_to(y_0_label, RIGHT, buff=0.1)
            .shift(0.1 * RIGHT)
            .set_color(GREEN_E)
        )

        vertex = always_redraw(
            lambda: Dot(color=GREEN_E).move_to(
                plane1.c2p(x_0.get_value(), (y_0.get_value()))
            )
        )

        self.play(
            LaggedStart(DrawBorderThenFill(plane1)),
            Create(func1),
            Create(equation_text),
            Create(vertex),
        )
        self.play(Transform(equation_text, new_equation_text))
        self.play(Write(x_0_label), Write(y_0_label), Write(x0_value), Write(y0_value))

        self.play(x_0.animate.set_value(2), run_time=2)
        self.play(y_0.animate.set_value(4), run_time=2)
        self.play(x_0.animate.set_value(-2), run_time=3)
        self.play(y_0.animate.set_value(0), run_time=2)
        self.play(x_0.animate.set_value(0), run_time=2)
        self.wait(2)

    def animate_factorization_steps(self, lines):
        lines[0].move_to(TITLE_TEXT_POSITION + UP)

        for i in range(1, len(lines)):
            lines[i].next_to(lines[i - 1], DOWN, buff=0.5)

        for i, line in enumerate(lines):
            line.shift(3 * LEFT)

        self.play(Write(lines[0]), run_time=1.5)
        self.play(TransformFromCopy(lines[0][1], lines[1][1]), run_time=1.5)
        self.play(
            TransformFromCopy(lines[0][0], lines[1][0]),
            TransformFromCopy(lines[0][2], lines[1][2]),
            run_time=1.5,
        )
        self.play(Write(lines[2]), run_time=1.5)
        self.play(Write(lines[3]), run_time=1.5)

    def factorization_example1(self):
        displayTitle(self, "Factorization of Quadratics")
        clearScreen(self)

        factorize_title = (
            MathTex("x^2 +", "5", "x+", "6")
            .to_edge(UP)
            .set_color_by_tex("5", GREEN)
            .set_color_by_tex("6", BLUE)
        )
        self.play(Write(factorize_title))
        self.wait(1)

        animateTextSeq(
            self,
            [
                MathTex("5", "=", "p", "+", "q").set_color_by_tex_to_color_map(
                    {"p": ORANGE, "q": YELLOW, "5": GREEN}
                ),
                MathTex("6", "=", "p", "\\cdot", "q").set_color_by_tex_to_color_map(
                    {"p": ORANGE, "q": YELLOW, "6": BLUE}
                ),
                MathTex("6", "=", "1", "\\cdot", "6"),
                MathTex("6", "=", "2", "\\cdot", "3"),
            ],
            shift_val=3 * RIGHT,
        )

        self.animate_factorization_steps(
            [
                MathTex("x^2", "+ 5x", "+ 6").set_color_by_tex_to_color_map(
                    {"5x": GREEN, "6": BLUE}
                ),
                MathTex("x^2 +", "2x + 3x", "+ 6").set_color_by_tex_to_color_map(
                    {"2x": GREEN, "6": BLUE}
                ),
                MathTex("x(x + 2) + 3(x + 2)"),
                MathTex("(x + 2)(x + 3)"),
            ]
        )

    def factorization_example2(self):
        factorize_title = (
            MathTex("x^2", "- x", "-12")
            .to_edge(UP)
            .set_color_by_tex_to_color_map({"-12": BLUE, "- x": GREEN})
        )
        self.play(Write(factorize_title))
        self.wait(1)

        lines1 = animateTextSeq(
            self,
            [
                MathTex("-1", "=", "p", "+", "q").set_color_by_tex_to_color_map(
                    {"p": ORANGE, "q": YELLOW, "-1": GREEN}
                ),
                MathTex("-12", "=", "p", "\\cdot", "q").set_color_by_tex_to_color_map(
                    {"p": ORANGE, "q": YELLOW, "-12": BLUE}
                ),
                MathTex("-12", "=", "-1", "\\cdot", "12"),
                MathTex("-12", "=", "-2", "\\cdot", "6"),
                MathTex("-12", "=", "-3", "\\cdot", "4"),
            ],
            shift_val=3 * RIGHT,
        )

        correctSplit = MathTex("-12", "=", "3", "\\cdot", "-4").next_to(lines1[-1], 0)

        self.play(Transform(lines1[-1], correctSplit))
        self.wait(2)

        lines = [
            MathTex("x^2", "- x", "- 12").set_color_by_tex("- x", GREEN),
            MathTex("x^2", "+ 3x - 4x", "- 12").set_color_by_tex("3x", GREEN),
            MathTex("x(x + 3) - 4(x + 3)"),
            MathTex("(x -4)(x + 3)"),
        ]

        self.animate_factorization_steps(lines)

    def factorization_example3(self):
        factorize_title = (
            MathTex("3", "x^2", "-5x", "-12")
            .to_edge(UP)
            .set_color_by_tex_to_color_map({"-12": BLUE, "-5x": GREEN, "3": BLUE})
        )
        self.play(Write(factorize_title))
        self.wait(1)

        lines1 = animateTextSeq(
            self,
            [
                MathTex("-5", "=", "p", "+", "q").set_color_by_tex_to_color_map(
                    {"p": ORANGE, "q": YELLOW, "-5": GREEN}
                ),
                MathTex(
                    "-12\\cdot3", "=", "p", "\\cdot", "q"
                ).set_color_by_tex_to_color_map(
                    {"p": ORANGE, "q": YELLOW, "-12\\cdot3": BLUE}
                ),
                MathTex("-36", "=", "-1", "\\cdot", "36"),
                MathTex("-36", "=", "-2", "\\cdot", "18"),
                MathTex("-36", "=", "-3", "\\cdot", "12"),
                MathTex("-36", "=", "-4", "\\cdot", "9"),
            ],
            shift_val=3 * RIGHT + DOWN,
        )

        correctSplit = MathTex("-36", "=", "4", "\\cdot", "-9").next_to(lines1[-1], 0)

        self.play(Transform(lines1[-1], correctSplit))
        self.wait(2)

        lines = [
            MathTex("3x^2", "-5x", "-12").set_color_by_tex("-5x", GREEN),
            MathTex("3x^2", "+ 4x - 9x", "-12").set_color_by_tex("4x", GREEN),
            MathTex("x(3x + 4) - 3(3x + 4)"),
            MathTex("(3x + 4)(x - 3)"),
        ]

        self.animate_factorization_steps(lines)

    def complete_the_square_example(self):
        displayTitle(self, "Completing the square")
        clearScreen(self)

        lastEqn1 = animateTextSeq(
            self,
            [
                MathTex("x^2 + 5x + 6"),
                MathTex("x^2 + 2\\left(\\frac{5}{2}\\right)x + 6"),
                MathTex(
                    "x^2 + 2\\left(\\frac{5}{2}\\right)x",
                    "+ \\left(\\frac{5}{2}\\right)^2",
                    "- \\left(\\frac{5}{2}\\right)^2",
                    "+ 6",
                ).set_color_by_tex("\\left(\\frac{5}{2}\\right)^2", RED),
            ],
            shift_val=UP + 2 * LEFT,
        )

        finalEqn = MathTex(
            "\\left( x + \\frac{5}{2} \\right)^2", "- \\frac{25}{4} + 6"
        ).next_to(lastEqn1[-1], DOWN, buff=0.5)

        finalEqn_ = MathTex(
            "\\left( x + \\frac{5}{2} \\right)^2", "- \\frac{1}{4}"
        ).next_to(finalEqn, 0)

        justifyingExp1 = (
            MathTex("(a + b)^2 = a^2 + 2ab + b^2")
            .next_to(finalEqn, RIGHT, buff=0.7)
            .scale(0.8)
        )
        self.play(Write(justifyingExp1), run_time=1)

        self.play(TransformFromCopy(lastEqn1[-1][0:2], finalEqn[0]), run_time=1)
        self.play(TransformFromCopy(lastEqn1[-1][2], finalEqn[1]), run_time=1)

        self.play(Transform(finalEqn, finalEqn_), run_time=1.5)
        self.play(finalEqn_.animate.set_color(NUMBRIK_COLOR), run_time=1)

        clearScreen(self)

        lastEqn2 = animateTextSeq(
            self,
            [
                MathTex("\\left( x + \\frac{5}{2} \\right)^2 - \\frac{1}{4}").set_color(
                    NUMBRIK_COLOR
                ),
                MathTex("\\left( x + \\frac{5}{2} \\right)^2 - \\frac{1}{2^2}"),
                MathTex(
                    "\\left( x + \\frac{5}{2} - \\frac{1}{2}\\right)",
                    "\\left( x + \\frac{5}{2} + \\frac{1}{2}\\right)",
                ),
            ],
            shift_val=UP + 2 * LEFT,
        )

        justifyingExp2 = (
            MathTex("(a^2 - b^2) = (a - b)(a + b)")
            .next_to(lastEqn2[1], RIGHT, buff=0.5)
            .scale(0.8)
        )

        self.play(Write(justifyingExp2))

        finalEqn2 = MathTex("\\left( x + 2 \\right)", "\\left( x + 3 \\right)").next_to(
            lastEqn2[-1], DOWN, buff=0.5
        )

        self.play(TransformFromCopy(lastEqn2[-1][0], finalEqn2[0]))
        self.play(TransformFromCopy(lastEqn2[-1][1], finalEqn2[1]))

        self.wait(2)
