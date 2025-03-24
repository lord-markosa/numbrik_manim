from manim import *
from utils import *


class LinearEqn(Scene):
    def construct(self):
        shots = [
            self.intro,
            self.graphWarmUp,
            self.graph1,
            self.systemOfLinearEquationIllus,
            self.systemOfLinearEquation,
            self.methodsToSolve,
            self.substitution,
            self.elimination,
            self.crossMultiplication,
            self.crossMultiplicationExample,
        ]

        for shot in shots:
            shot()
            clearScreen(self)

    def createCandyScene(self):
        # Load images from the assets folder
        image1 = ImageMobject("assets/chocobars.webp")
        image2 = ImageMobject("assets/gummies.png")
        images = [image1, image2]
        labels = [
            [MathTex("Chocobars \\ \\$5/oz"), MathTex("Gummies \\ \\$3/oz")],
            [MathTex("x \\ oz"), MathTex("y \\ oz")],
        ]

        for i, image in enumerate(images):
            image.height = 2
            image.move_to(TITLE_TEXT_POSITION + UP + (i - 0.5) * RIGHT * 6)
            labels[0][i].next_to(image, DOWN)

            self.play(FadeIn(image))
            self.play(Write(labels[0][i]))

        self.wait(1)

        for i, label in enumerate(labels[1]):
            label.next_to(labels[0][i], DOWN)
            self.play(Write(label))

        self.wait(1)

    def intro(self):
        displayTitle(self, "Linear Equations")

        self.createCandyScene()

        animateTextSeq(
            self,
            [
                MathTex("Total \\ Money \\ you \\ have: \\ \\$120"),
                MathTex("5x + 3y = 120"),
            ],
            shift_val=2 * DOWN,
        )

        self.wait(3)

    def graphWarmUp(self):
        animateTextSeq(
            self,
            [
                Text("Linear Equation in 2 variables", color=NUMBRIK_COLOR),
                MathTex("5x + 3y = 120"),
                MathTex("\\Rightarrow y = \\frac{120 - 5x}{3}"),
            ],
        )

    def graph1(self):
        plane = (
            NumberPlane(
                x_range=[-1, 32, 3],
                x_length=6,
                y_range=[-1, 36, 3],
                y_length=7,
                background_line_style={"stroke_color": YELLOW, "stroke_opacity": 0.3},
                axis_config={"include_numbers": False},
            )
            .add_coordinates()
            .shift(2 * LEFT)
        )

        def linear_func(x):
            return round((120 - 5 * x) / 3, 2)

        discreteX = [x for x in range(3, 25, 3)]
        discreteY = [linear_func(x) for x in discreteX]

        self.play(Create(plane))

        value_table = (
            Table(
                [*[[str(x), str(y)] for x, y in zip(discreteX, discreteY)]],
                col_labels=[
                    MathTex("x \\ (oz)").scale(1.1),
                    MathTex("y \\ (oz) = \\frac{120 - 5x}{3}").scale(1.1),
                ],
                include_outer_lines=True,
                line_config={
                    "stroke_color": YELLOW,
                    "stroke_width": 0.5,
                    "stroke_opacity": 0.5,
                },
            )
            .shift(4.5 * RIGHT)
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

        parabola = plane.plot(linear_func, x_range=[3, 24]).set_color(NUMBRIK_COLOR)

        self.play(Create(parabola))

        self.wait(2)

    def declareEquations(self, eq1, eq2, shift_val=UP):
        equations = animateTextSeq(
            self,
            [
                MathTex(eq1, color=NUMBRIK_COLOR),
                MathTex(eq2, color=NUMBRIK_COLOR),
            ],
            shift_val,
        )

        self.play(
            Write(MathTex("(1)").next_to(equations[0], 2 * RIGHT)),
            Write(MathTex("(2)").next_to(equations[1], 2 * RIGHT)),
        )

        self.wait(1)

        return equations

    def systemOfLinearEquationIllus(self):
        displayTitle(self, "System of Linear Equations")

        self.createCandyScene()

        animateTextSeq(
            self,
            [
                MathTex("Total \\ weight \\ you \\ can \\ carry: \\ 30 \\ oz"),
                MathTex("x + y = 30"),
            ],
            shift_val=2 * DOWN,
        )

        clearScreen(self)

        equations = self.declareEquations("5x + 3y = 120", "x + y = 30")

        animateTextSeq(
            self,
            [
                MathTex("\\Rightarrow y = 30 - x"),
                MathTex("\\Rightarrow 5x + 3(30 - x) = 120"),
            ],
            next_reference=equations[1],
        )

        clearScreen(self)

        animateTextSeq(
            self,
            [
                MathTex("5x + 3(30-x) = 120"),
                MathTex("5x + 90 - 3x = 120"),
                MathTex("2x = 30"),
                MathTex("x = 15"),
                MathTex("y = 30 - 15 = 15"),
            ],
        )

    def systemOfLinearEquation(self):
        eqns = animateTextSeq(
            self,
            [
                self.generalEquationForm1,
                self.generalEquationForm2,
            ],
            shift_val=2 * UP,
        )

        group = VGroup()

        axes1 = (
            Axes(
                x_range=[-1, 5, 1],
                x_length=3,
                y_range=[-1, 5, 1],
                y_length=3,
            )
            .next_to(eqns[-1], DOWN, buff=1)
            .shift(4 * LEFT)
        )

        axes2 = axes1.copy().shift(4 * RIGHT)
        axes3 = axes1.copy().shift(8 * RIGHT)

        axes = [axes1, axes2, axes3]

        coeff = [
            [[1, 2, 3], [2, 1, 3]],
            [[1, 1, 1], [1, 1, 2]],
            [[1, 1, 2], [1, 1, 2]],
        ]

        conditions = [
            MathTex("\\frac{a_{1}}{a_{2}}}", "\\neq", "\\frac{b_{1}}{b_{2}}"),
            MathTex(
                "\\frac{a_{1}}{a_{2}}}",
                "=",
                "\\frac{b_{1}}{b_{2}}",
                "\\neq",
                "\\frac{c_{1}}{c_{2}}",
            ),
            MathTex(
                "\\frac{a_{1}}{a_{2}}}",
                "=",
                "\\frac{b_{1}}{b_{2}}",
                "=",
                "\\frac{c_{1}}{c_{2}}",
            ),
        ]

        nature = [
            Text("Unique Solution", color=NUMBRIK_COLOR, font_size=30),
            Text("No Solution", color=RED, font_size=30),
            Text("Infinite Solution", color=NUMBRIK_COLOR, font_size=30),
        ]

        consistencies = [
            Text("Consistent", font_size=30),
            Text("Inconsistent", font_size=30),
            Text("Consistent", font_size=30),
        ]

        lines = []

        for i, ax in enumerate(axes):
            lines.append(
                [
                    ax.plot(
                        lambda x: (coeff[i][0][2] - coeff[i][0][0] * x)
                        / coeff[i][0][1],
                        x_range=[
                            -1,
                            (coeff[i][0][2] + coeff[i][0][1]) / coeff[i][0][0],
                        ],
                        color=NUMBRIK_COLOR,
                    ),
                    ax.plot(
                        lambda x: (coeff[i][1][2] - coeff[i][1][0] * x)
                        / coeff[i][1][1],
                        x_range=[
                            -1,
                            (coeff[i][1][2] + coeff[i][1][1]) / coeff[i][1][0],
                        ],
                        color=NUMBRIK_COLOR,
                    ),
                ]
            )

            conditions[i].set_color_by_tex_to_color_map(
                {"a_{1}": YELLOW, "b_{1}": ORANGE, "c_{1}": GREEN}
            ).next_to(ax, DOWN)

            group.add(ax, *lines[i], conditions[i])

            self.play(Create(ax))
            self.play(Create(lines[i][0]), Create(lines[i][1]), run_time=1.5)
            self.wait(1)
            self.play(Write(conditions[i]), run_time=1.5)
            self.wait(2)

        self.play(FadeOut(eqns[0]), FadeOut(eqns[1]))

        self.play(group.animate.shift(2 * UP), run_time=1.5)

        for i in range(3):
            nature[i].next_to(conditions[i], DOWN, buff=0.5)
            consistencies[i].next_to(nature[i], DOWN, buff=0.5)

            self.play(Write(nature[i]), run_time=1.5)
            self.wait(1)
            self.play(Write(consistencies[i]), run_time=1.5)
            self.wait(2)

    def methodsToSolve(self):
        displayTitle(self, "Methods to Solve Linear Equations")

        animateTextSeq(
            self,
            [
                Text("Substitution Method", color=NUMBRIK_COLOR),
                Text("Elimination Method", color=NUMBRIK_COLOR),
                Text("Cross Multiplication Trick", color=NUMBRIK_COLOR),
            ],
            shift_val=DOWN,
            iterative_callback=lambda line: self.play(
                line.animate.scale(0.6), line.animate.set_color(WHITE), run_time=1
            ),
            line_buffer=0.75,
        )

    def substitution(self):
        displayTitle(self, "Substitution Method")

        eqns = self.declareEquations("2x + y = 3", "x + 2y = 3", shift_val=2 * UP)

        animateTextSeq(
            self,
            [
                MathTex("y = 3 - 2x"),
                MathTex("x + 2(3 - 2x) = 3"),
                MathTex("x + 6 - 4x = 3"),
                MathTex("-3x = -3"),
                MathTex("x = 1 \\ \\Rightarrow y = 1"),
            ],
            next_reference=eqns[1],
        )

    def elimination(self):
        displayTitle(self, "Elimination Method")

        eqns = self.declareEquations("2x + y = 11", "x + 3y = 18", shift_val=2 * UP)

        animateTextSeq(
            self,
            [
                MathTex("2\\times (2)\\implies 2x + 6y = 36"),
                MathTex("(2) - (1)\\implies 2x + 6y - (2x + y) = 36 - 11"),
                MathTex("5y = 25"),
                MathTex("y = 5 \\ \\Rightarrow x = 18 - 3(5) = 3"),
            ],
            next_reference=eqns[1],
        )

    def crossMultiplication(self):
        displayTitle(self, "Cross Multiplication Trick")

        eqns = animateTextSeq(
            self,
            [self.generalEquationForm1, self.generalEquationForm2],
            shift_val=2 * UP,
        )

        equationGroup = VGroup(eqns[0], eqns[1])

        table = MobjectTable(
            [
                [MathTex("x"), MathTex("y"), MathTex("1")],
                [
                    MathTex("a_{1}", color=YELLOW),
                    MathTex("b_{1}", color=ORANGE),
                    MathTex("c_{1}", color=GREEN),
                ],
                [
                    MathTex("a_{2}", color=YELLOW),
                    MathTex("b_{2}", color=ORANGE),
                    MathTex("c_{2}", color=GREEN),
                ],
            ],
            line_config={
                "stroke_opacity": 0,
            },
        ).next_to(eqns[1], 0)

        self.play(
            LaggedStart(
                FadeOut(equationGroup), FadeIn(table), lag_ratio=0.25, run_time=2
            )
        )

        eqn1 = MathTex(
            "\\frac{x}{b_{1}c_{2} - b_{2}c_{1}}",
            "=",
            "\\frac{-y}{a_{1}c_{2} - a_{2}c_{1}}",
            "=",
            "\\frac{1}{a_{1}b_{2} - a_{2}b_{1}}",
        ).next_to(table, DOWN, buff=0.75)

        eqn1[0][2:4].set_color(ORANGE)
        eqn1[0][7:9].set_color(ORANGE)

        eqn1[0][4:6].set_color(GREEN)
        eqn1[0][9:11].set_color(GREEN)

        eqn1[2][3:5].set_color(YELLOW)
        eqn1[2][8:10].set_color(YELLOW)

        eqn1[2][5:7].set_color(GREEN)
        eqn1[2][10:12].set_color(GREEN)

        eqn1[4][2:4].set_color(YELLOW)
        eqn1[4][7:9].set_color(YELLOW)

        eqn1[4][4:6].set_color(ORANGE)
        eqn1[4][9:11].set_color(ORANGE)

        def createArrow(st, en):
            return Arrow(
                start=table.get_entries(st),
                end=table.get_entries(en),
                stroke_width=3,
            )

        # Animation sequence

        ## Part 1
        self.play(Write(eqn1[0][0:2]))
        tmp = createArrow((2, 2), (3, 3))
        self.play(Create(tmp))
        self.play(
            TransformFromCopy(table.get_entries((2, 2)), eqn1[0][2:4]),
            TransformFromCopy(table.get_entries((3, 3)), eqn1[0][4:6]),
        )
        self.play(FadeOut(tmp))
        self.play(Write(eqn1[0][6]))
        tmp = createArrow((3, 2), (2, 3))
        self.play(Create(tmp))
        self.play(
            TransformFromCopy(table.get_entries((3, 2)), eqn1[0][7:9]),
            TransformFromCopy(table.get_entries((2, 3)), eqn1[0][9:11]),
        )
        self.play(FadeOut(tmp))
        ## End of Part 1

        self.play(Write(eqn1[1]))

        ## Part 2
        self.play(Write(eqn1[2][0:3]))
        tmp = createArrow((2, 1), (3, 3))
        self.play(Create(tmp))
        self.play(
            TransformFromCopy(table.get_entries((2, 1)), eqn1[2][3:5]),
            TransformFromCopy(table.get_entries((3, 3)), eqn1[2][5:7]),
        )
        self.play(FadeOut(tmp))
        self.play(Write(eqn1[2][7]))
        tmp = createArrow((3, 1), (2, 3))
        self.play(Create(tmp))
        self.play(
            TransformFromCopy(table.get_entries((3, 1)), eqn1[2][8:10]),
            TransformFromCopy(table.get_entries((2, 3)), eqn1[2][10:12]),
        )
        self.play(FadeOut(tmp))
        ## End of Part 2

        self.play(Write(eqn1[3]))

        ## Part 3
        self.play(Write(eqn1[4][0:2]))
        tmp = createArrow((2, 1), (3, 2))
        self.play(Create(tmp))
        self.play(
            TransformFromCopy(table.get_entries((2, 1)), eqn1[4][2:4]),
            TransformFromCopy(table.get_entries((3, 2)), eqn1[4][4:6]),
        )
        self.play(FadeOut(tmp))
        self.play(Write(eqn1[4][6]))
        tmp = createArrow((3, 1), (2, 2))
        self.play(Create(tmp))
        self.play(
            TransformFromCopy(table.get_entries((3, 1)), eqn1[4][7:9]),
            TransformFromCopy(table.get_entries((2, 2)), eqn1[4][9:11]),
        )
        self.play(FadeOut(tmp))
        ## End of Part 3

    def crossMultiplicationExample(self):
        eqns = animateTextSeq(
            self,
            [
                MathTex("3x+y=13", color=NUMBRIK_COLOR),
                MathTex("2x+3y=18", color=NUMBRIK_COLOR),
                MathTex("3x+y-13=0"),
                MathTex("2x+3y-18=0"),
            ],
            shift_val=UP,
        )

        equationGroup = VGroup(*eqns)

        table = MobjectTable(
            [
                [MathTex("x"), MathTex("y"), MathTex("1")],
                [
                    MathTex("3", color=YELLOW),
                    MathTex("1", color=ORANGE),
                    MathTex("-13", color=GREEN),
                ],
                [
                    MathTex("2", color=YELLOW),
                    MathTex("3", color=ORANGE),
                    MathTex("-18", color=GREEN),
                ],
            ],
            line_config={
                "stroke_opacity": 0,
            },
        ).next_to(eqns[1], 0)

        self.play(
            LaggedStart(
                FadeOut(equationGroup), FadeIn(table), lag_ratio=0.25, run_time=2
            )
        )

        eqn1 = MathTex(
            "\\frac{x}{1\\cdot-18 - 3\\cdot-13}",
            "=",
            "\\frac{-y}{3\\cdot-18 - 2\\cdot-13}",
            "=",
            "\\frac{1}{3\\cdot3 - 2\\cdot1}",
        ).next_to(table, DOWN, buff=0.75)

        eqn1[0][2:4].set_color(ORANGE)
        eqn1[0][8:10].set_color(ORANGE)

        eqn1[0][4:7].set_color(GREEN)
        eqn1[0][10:13].set_color(GREEN)

        eqn1[2][3:5].set_color(YELLOW)
        eqn1[2][5:8].set_color(YELLOW)

        eqn1[2][9:11].set_color(GREEN)
        eqn1[2][11:14].set_color(GREEN)

        eqn1[4][2:4].set_color(YELLOW)
        eqn1[4][6:8].set_color(YELLOW)

        eqn1[4][4].set_color(ORANGE)
        eqn1[4][8].set_color(ORANGE)

        def createArrow(st, en):
            return Arrow(
                start=table.get_entries(st),
                end=table.get_entries(en),
                stroke_width=3,
            )

        # self.play(Create(eqn1))

        # Animation sequence

        ## Part 1
        self.play(Write(eqn1[0][0:2]))
        tmp = createArrow((2, 2), (3, 3))
        self.play(Create(tmp))
        self.play(
            TransformFromCopy(table.get_entries((2, 2)), eqn1[0][2:4]),
            TransformFromCopy(table.get_entries((3, 3)), eqn1[0][4:7]),
        )
        self.play(FadeOut(tmp))
        self.play(Write(eqn1[0][7]))
        tmp = createArrow((3, 2), (2, 3))
        self.play(Create(tmp))
        self.play(
            TransformFromCopy(table.get_entries((3, 2)), eqn1[0][8:10]),
            TransformFromCopy(table.get_entries((2, 3)), eqn1[0][10:13]),
        )
        self.play(FadeOut(tmp))
        ## End of Part 1

        self.wait(1)

        self.play(Write(eqn1[1]))

        ## Part 2
        self.play(Write(eqn1[2][0:3]))
        tmp = createArrow((2, 1), (3, 3))
        self.play(Create(tmp))
        self.play(
            TransformFromCopy(table.get_entries((2, 1)), eqn1[2][3:5]),
            TransformFromCopy(table.get_entries((3, 3)), eqn1[2][5:8]),
        )
        self.play(FadeOut(tmp))
        self.play(Write(eqn1[2][8]))
        tmp = createArrow((3, 1), (2, 3))
        self.play(Create(tmp))
        self.play(
            TransformFromCopy(table.get_entries((3, 1)), eqn1[2][9:11]),
            TransformFromCopy(table.get_entries((2, 3)), eqn1[2][11:14]),
        )
        self.play(FadeOut(tmp))
        ## End of Part 2

        self.wait(1)

        self.play(Write(eqn1[3]))

        ## Part 3
        self.play(Write(eqn1[4][0:2]))
        tmp = createArrow((2, 1), (3, 2))
        self.play(Create(tmp))
        self.play(
            TransformFromCopy(table.get_entries((2, 1)), eqn1[4][2:4]),
            TransformFromCopy(table.get_entries((3, 2)), eqn1[4][4]),
        )
        self.play(FadeOut(tmp))
        self.play(Write(eqn1[4][5]))
        tmp = createArrow((3, 1), (2, 2))
        self.play(Create(tmp))
        self.play(
            TransformFromCopy(table.get_entries((3, 1)), eqn1[4][6:8]),
            TransformFromCopy(table.get_entries((2, 2)), eqn1[4][8]),
        )
        self.play(FadeOut(tmp))
        ## End of Part 3

        self.wait(1)

        self.play(
            Write(
                MathTex(
                    "\\Rightarrow \\frac{x}{21} = \\frac{-y}{-28} = \\frac{1}{7} \\quad \\Rightarrow x=3, \\ y=4"
                ).next_to(eqn1, DOWN, buff=0.5)
            ),
            run_time=2.5,
        )

    generalEquationForm1 = MathTex(
        "a_{1}", "x", "+", "b_{1}", "y", "+", "c_{1}", "= 0"
    ).set_color_by_tex_to_color_map({"a_{1}": YELLOW, "b_{1}": ORANGE, "c_{1}": GREEN})
    generalEquationForm2 = MathTex(
        "a_{2}", "x", "+", "b_{2}", "y", "+", "c_{2}", "= 0"
    ).set_color_by_tex_to_color_map({"a_{2}": YELLOW, "b_{2}": ORANGE, "c_{2}": GREEN})
