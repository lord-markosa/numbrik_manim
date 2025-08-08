from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        # Problem Statement
        question = VGroup(
            MathTex(
                r"\lim_{n \to \infty} \frac{1}{n^2} \left(\lfloor x \rfloor + \lfloor 2x \rfloor + \cdots + \lfloor nx \rfloor \right)",
                tex_template=TexFontTemplates.comic_sans,
                color=NUMBRIK_COLOR,
            ),
            MathTex(
                r"\lfloor x \rfloor \text{ is the Greatest Integer Function of x}",
                tex_template=TexFontTemplates.comic_sans,
                color=NUMBRIK_COLOR,
            ).scale(0.9),
        ).arrange(DOWN, center=True, buff=0.5)

        self.play(FadeIn(question, shift=UP))
        self.wait(2)
        self.play(FadeOut(question))
        self.wait(1)

        gint_inequality = MathTex(
            r"(x - 1) ",
            "\\ < \\ ",
            r"\lfloor x \rfloor \leq x",
            tex_template=TexFontTemplates.comic_sans,
            color=NUMBRIK_COLOR,
        ).to_edge(UP)

        lessThan = MathTex("<", color=NUMBRIK_COLOR).next_to(gint_inequality[1], 0)

        self.play(FadeIn(gint_inequality[0], lessThan, gint_inequality[2:]))
        clearScreen(self, 1)
        self.wait(1)

        # Step 1: Define the sum S_n
        inequality = MathTex(
            r"kx - 1",
            "\\ < \\ ",
            r"\lfloor kx \rfloor \leq kx",
            tex_template=TexFontTemplates.comic_sans,
            color=NUMBRIK_COLOR,
        ).to_edge(UP)

        lt0 = lessThan.next_to(inequality[1], 0)

        self.play(FadeIn(inequality[0], lt0, inequality[2:]))
        self.wait(1)

        # Step 2: Sum over k = 1 to n
        summed = MathTex(
            r"\sum_{k=1}^{n} (kx - 1) ",
            "\\ < \\ ",
            r"\sum_{k=1}^{n} \lfloor kx \rfloor \leq \sum_{k=1}^{n} kx",
            tex_template=TexFontTemplates.comic_sans,
            color=NUMBRIK_COLOR,
        ).next_to(inequality, DOWN, buff=0.75)

        lt1 = lessThan.copy().next_to(summed[1], 0)

        self.play(FadeIn(summed[0], lt1, summed[2:]))
        self.wait(1)

        highlight(self, summed, buff=0.2)

        # Step 3: Simplify both bounds
        simplified = MathTex(
            r"x \cdot \frac{n(n+1)}{2} - n",
            "\\ < \\",
            r"\sum_{k=1}^{n} \lfloor kx \rfloor \leq x \cdot \frac{n(n+1)}{2}",
            tex_template=TexFontTemplates.comic_sans,
            color=NUMBRIK_COLOR,
        ).next_to(summed, DOWN, buff=0.7)

        lt2 = lessThan.copy().next_to(simplified[1], 0)


        self.play(FadeIn(simplified[0], lt2, simplified[2:]))
        self.wait(1)
        highlight(self, simplified, buff=0.2)

        clearScreen(self, 1)

        # Step 4: Divide by n^2
        divided = MathTex(
            r"\frac{x(n+1)}{2n} - \frac{1}{n}",
            "\\ < \\ ",
            r"\frac{1}{n^2} \sum \lfloor kx \rfloor \leq \frac{x(n+1)}{2n}",
            tex_template=TexFontTemplates.comic_sans,
            color=NUMBRIK_COLOR,
        ).to_edge(UP)

        lt3 = lessThan.copy().next_to(divided[1], 0)

        self.play(FadeIn(divided[0], lt3, divided[2:], shift=UP))
        self.wait(1)

        pre_final = MathTex(
            r"\lim_{n \to \infty}\frac{x(n+1)}{2n} - \frac{1}{n}",
            "\\ < \\ ",
            r"\lim_{n \to \infty}\frac{1}{n^2} \sum \lfloor kx \rfloor \leq \lim_{n \to \infty}\frac{x(n+1)}{2n}",
            tex_template=TexFontTemplates.comic_sans,
            color=NUMBRIK_COLOR,
        ).next_to(divided, DOWN, buff=0.75)

        lt4 = lessThan.copy().next_to(pre_final[1], 0)

        self.play(FadeIn(pre_final[0], lt4, pre_final[2:]))
        self.wait(1)

        pre_final2 = MathTex(
            r"\frac{x}{2}",
            "\\ < \\ ",
            r"\lim_{n \to \infty}\frac{1}{n^2} \sum \lfloor kx \rfloor \leq \frac{x}{2}",
            tex_template=TexFontTemplates.comic_sans,
            color=NUMBRIK_COLOR,
        ).next_to(pre_final, DOWN, buff=0.75)

        lt5 = lessThan.copy().next_to(pre_final2[1], 0)

        self.play(FadeIn(pre_final2[0], lt5, pre_final2[2:]))
        clearScreen(self, 1)

        # Step 5: Final limit using squeeze
        final_limit = MathTex(
            r"\lim_{n \to \infty} \frac{1}{n^2} \sum \lfloor kx \rfloor = \frac{x}{2}",
            tex_template=TexFontTemplates.comic_sans,
            color=NUMBRIK_COLOR,
        ).to_edge(UP)
        self.play(FadeIn(final_limit, shift=UP))

        self.wait(4)


class FloorFunctionGraph(Scene):
    def construct(self):
        # Set up the axes
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=7,
            y_length=7,
            tips=True,
            axis_config={
                "include_numbers": False,
                "color": GRAY_D,
                "font_size": 24,
                "tip_shape": StealthTip,
            },
        )

        self.play(Create(axes))

        # Add Text labels for numbers on both axes
        x_labels = VGroup()
        y_labels = VGroup()

        for x in range(-4, 5):
            if x == 0:
                continue
            label = Text(
                str(x), font_size=18, color=GREY, font="Comic Sans MS"
            ).move_to(axes.c2p(x, 0) + 0.3 * DOWN)
            x_labels.add(label)

        for y in range(-4, 5):
            if y == 0:
                continue
            label = Text(
                str(y), font_size=18, color=GREY, font="Comic Sans MS"
            ).move_to(axes.c2p(0, y) + 0.3 * LEFT)
            y_labels.add(label)

        self.play(FadeIn(x_labels), FadeIn(y_labels))
        self.wait(1)

        # Plot y = x
        line = axes.plot(lambda x: x, x_range=[-4.5, 4.5], color=NUMBRIK_COLOR)
        self.play(Create(line), run_time=2)
        self.wait(1)

        # Draw horizontal lines at integer y-values
        h_lines = VGroup()
        for y in range(-4, 5):
            h_line = Line(
                start=axes.c2p(-5, y),
                end=axes.c2p(5, y),
                color=GREY_B,
                stroke_opacity=0.3,
            )
            h_lines.add(h_line)
        self.play(Create(h_lines), run_time=3)
        self.wait(1)

        # Illustrate the floor step for a few points
        for x_val in [1.8, 2.8, -1.2]:
            dot_on_line = Dot(axes.c2p(x_val, x_val), color=RED)
            floor_val = (
                int(x_val) if x_val >= 0 or x_val == int(x_val) else int(x_val) - 1
            )
            dot_on_step = Dot(axes.c2p(x_val, floor_val), color=NUMBRIK_COLOR)
            vertical_drop = DashedLine(
                start=axes.c2p(x_val, x_val - 0.1),
                end=axes.c2p(x_val, floor_val + 0.1),
                color=GREY_B,
            )
            self.play(FadeIn(dot_on_line))
            self.play(Create(vertical_drop))
            self.play(FadeIn(dot_on_step))
            self.wait(0.3)
            self.play(
                FadeOut(dot_on_line), FadeOut(dot_on_step), FadeOut(vertical_drop)
            )

        # Plot the floor function y = floor(x)
        floor_graph = VGroup()
        for x in range(-4, 5):
            step = Line(
                start=axes.c2p(x, x),
                end=axes.c2p(x + 0.9, x),
                color=RED,
                stroke_width=4,
            )

            # left_dot = Dot(axes.c2p(x, x), color=RED)
            right_dot = Dot(axes.c2p(x + 1, x), color=RED)
            right_dot.set_fill(RED, opacity=0).set_stroke(RED, width=2)  # Open circle

            # Highlight the relevant part of y = x
            highlight = Line(
                start=axes.c2p(x, x),
                end=axes.c2p(x + 1, x + 1),
                color=YELLOW,
                stroke_width=4,
                z_index=2,
            )

            # Show the area between y = x and y = floor(x)
            area = Polygon(
                axes.c2p(x, x),
                axes.c2p(x + 1, x + 1),
                axes.c2p(x + 1, x),
                axes.c2p(x, x),
                fill_color=YELLOW_N50,
                fill_opacity=0.3,
                stroke_opacity=0,
                z_index=-10,
            )

            if x in [-2, 1, 2]:
                self.play(Create(highlight), run_time=0.3)
                self.play(FadeIn(area), run_time=0.3)
                self.play(Create(step))
                self.play(Create(right_dot))
                self.play(FadeOut(highlight, area))
            else:
                floor_graph.add(step, right_dot)

        self.play(Create(floor_graph), run_time=3)
        self.wait(1)

        line2 = axes.plot(lambda x: x - 1, x_range=[-4, 5], color=GREEN_N100)
        line2.z_index = -10
        self.play(Create(line2), run_time=2)

        self.wait(4)


class FloorFunctionIllus(Scene):
    def construct(self):
        number_line = NumberLine(
            x_range=[0, 4, 1],
            length=5,
            color=GRAY_D,
        )
        self.play(Create(number_line))

        x_labels = VGroup()
        for x in range(0, 4):
            if x == 0:
                continue
            label = Text(
                str(x), font_size=18, color=GREY, font="Comic Sans MS"
            ).move_to(number_line.number_to_point(x) + 0.3 * DOWN)
            x_labels.add(label)

        self.play(Create(x_labels))

        # Mark x = 1.8
        x_val = 2.8
        dot = Dot(point=number_line.number_to_point(x_val), color=NUMBRIK_COLOR)
        dot.z_index = 10
        label = MathTex("x = 1.8").next_to(dot, UP)
        self.play(FadeIn(dot), Write(label))
        self.wait(0.5)

        # Create a dot at x = 1.8 that will move to x = 1
        moving_dot = Dot(point=number_line.number_to_point(x_val), color=RED)
        self.play(FadeIn(moving_dot))

        self.play(
            moving_dot.animate.move_to(number_line.number_to_point(2)),
            run_time=2,
            rate_func=smooth,
        )

        self.play(FadeOut(dot, moving_dot))

        x_val = 1.8
        dot = Dot(point=number_line.number_to_point(x_val), color=NUMBRIK_COLOR)
        dot.z_index = 10
        label = MathTex("x = 1.8").next_to(dot, UP)
        self.play(FadeIn(dot), Write(label))
        self.wait(0.5)

        # Create a dot at x = 1.8 that will move to x = 1
        moving_dot = Dot(point=number_line.number_to_point(x_val), color=RED)
        self.play(FadeIn(moving_dot))

        self.play(
            moving_dot.animate.move_to(number_line.number_to_point(1)),
            run_time=2,
            rate_func=smooth,
        )

        self.wait(2)


class GintIntro(Scene):
    def construct(self):
        title = Text(
            "Greatest Integer Function", font_size=42, color=NUMBRIK_COLOR
        ).to_edge(UP)
        self.play(FadeIn(title, shift=UP))

        # Example explanation
        desc = (
            MathTex(
                "\\text{The greatest integer less than or equal to x}",
                color=GREY_D,
            )
            .scale(0.8)
            .arrange(DOWN, buff=0.25)
            .next_to(title, DOWN, buff=1)
        )
        self.play(FadeIn(desc))
        self.wait(1)

        example0 = (
            MathTex(
                r"\lfloor 1.35 \rfloor = 1",
                color=GREY_N400,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(desc, DOWN, buff=0.5)
        )
        example1 = (
            MathTex(
                r"\lfloor -1.35 \rfloor = -2",
                color=GREY_N400,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(example0, DOWN, buff=0.5)
        )

        self.play(FadeIn(example0))
        self.wait(1)
        self.play(FadeIn(example1))
        self.wait(2)


class LimitsIntro(Scene):
    def construct(self):
        title = Text("Understanding Limits", font_size=42, color=NUMBRIK_COLOR).to_edge(
            UP
        )
        self.play(FadeIn(title, shift=UP))
        self.wait(1)

        # Intro explanation
        desc = (
            VGroup(
                MathTex(
                    "\\text{In mathematics, a limit describes the value}",
                    color=GREY_D,
                ),
                MathTex(
                    "\\text{a function or sequence approaches as}",
                    color=GREY_D,
                ),
                MathTex(
                    "\\text{its input approaches a certain value.}",
                    color=GREY_D,
                ),
            )
            .scale(0.8)
            .arrange(DOWN, buff=0.25)
            .next_to(title, DOWN, buff=1)
        )
        self.play(FadeIn(desc))
        self.wait(1)

        # Limit example resolving indeterminate form
        limit_eq = (
            MathTex(
                r"\lim_{x \to 0} \frac{\sin x}{x} = 1",
                color=GREY_N400,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.8)
            .next_to(desc, DOWN, buff=0.5)
        )
        self.play(FadeIn(limit_eq))
        self.wait(2)
