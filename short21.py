from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        S = 4

        stroke_color = GREY_N800

        O = ORIGIN + 2 * DOWN
        A = O + LEFT * S / 2
        B = O + RIGHT * S / 2
        C = B + S * UP
        D = A + S * UP

        X = B + UP * S / 2
        Y = X + RIGHT * S / 2
        Z = B + RIGHT * S / 2

        square1 = Polygon(
            A,
            B,
            C,
            D,
            color=GREEN_N100,
            stroke_color=GREY_N800,
            fill_opacity=1,
        )

        square2 = Polygon(
            B, X, Y, Z, color=YELLOW, stroke_color=GREY_N800, fill_opacity=1
        )

        # Draw circles
        circle = Sector(
            radius=np.sqrt(5 * S**2 / 4),
            arc_center=O,
            start_angle=0,
            angle=PI,
            stroke_width=DEFAULT_STROKE_WIDTH,
            stroke_color=stroke_color,
        )

        labelArea = Text("64", font_size=48, font="Segoe", color=BLACK).move_to(
            square1.get_center()
        )

        # Draw triangle between centers
        self.play(FadeIn(circle, scale=1.2), run_time=1.5)
        self.wait(1)
        self.play(Create(square1))
        self.wait(1)
        self.play(Create(square2))
        self.wait(1)
        self.play(FadeIn(labelArea, scale=1.2))
        self.wait(4)

        centerMarker = CurvedArrow(
            O + LEFT * 2.5 + UP * 2.5,
            O + UP * 0.2,
            color=RED_N,
            angle=-PI / 3,  # Negative angle for opposite curvature
        )

        tempPolygon = Polygon(O, B, C, color=RED_N, stroke_width=6)
        tempPolygon2 = Polygon(O, Y, Z, color=RED_N, stroke_width=6)

        # Solution
        sideLength = lengthMarker(A + 0.4 * DOWN, B + 0.4 * DOWN, "8")
        sideLength2 = lengthMarker(Y + 0.75 * RIGHT, Z + 0.75 * RIGHT, "S")

        self.play(FadeIn(sideLength[1], sideLength[2]))
        self.play(GrowArrow(sideLength[0]))
        self.wait(1)
        self.play(FadeOut(labelArea))
        self.wait(1)
        self.play(Create(Dot(O, radius=0.07, color=GREY_N800)), Create(centerMarker))
        self.wait(1)
        self.play(FadeOut(centerMarker))
        self.play(Create(DashedLine(O, C, color=GREY_N800)))
        self.wait(1)
        self.play(Create(tempPolygon))
        self.wait(1)
        self.play(Uncreate(tempPolygon))
        self.wait(1)
        self.play(Create(DashedLine(O, Y, color=GREY_N800)))
        self.wait(1)
        self.play(FadeIn(sideLength2[1], sideLength2[2]))
        self.play(GrowArrow(sideLength2[0]))
        self.wait(1)
        self.play(Create(tempPolygon2))

        self.wait(10)


class Statements(Scene):
    def construct(self):
        question = (
            VGroup(
                MathTex(
                    "\\text{Given both are squares}",
                    color=BLACK,
                ),
                MathTex(
                    "\\text{Find the area in yellow}",
                    color=BLACK,
                ),
            )
            .arrange(DOWN, buff=0.25)
            .to_edge(UP)
        )

        self.play(FadeIn(question, scale=1.2))
        clearScreen(self, 4)

        step1 = nMath("S^2 = 64").to_edge(UP)
        step2 = nMath("S = 8").next_to(step1, DOWN, buff=0.5)
        self.play(fadeInTex(step1))
        self.wait(1)
        self.play(fadeInTex(step2))
        clearScreen(self, 4)

        step1 = nMath("R^2 = 4^2 + 8^2").to_edge(UP)
        step2 = nMath("(4+s)^2 + s^2 = R^2").next_to(step1, DOWN, buff=0.5)
        self.play(fadeInTex(step1))
        self.wait(1)
        self.play(fadeInTex(step2))
        clearScreen(self, 4)

        step1 = nMath("s^2 + 4s - 32 = 0").to_edge(UP)
        step2 = nMath("s = 4, -8").next_to(step1, DOWN, buff=0.5)
        step3 = nMath("Area = s^2 = 16").next_to(step2, DOWN, buff=0.5)
        self.play(fadeInTex(step1))
        self.wait(1)
        self.play(fadeInTex(step2))
        self.wait(1)
        self.play(fadeInTex(step3))
        highlight(self, step3, buff=0.2, wait_time=4)
        clearScreen(self, 4)

        self.wait(10)


class Options(Scene):
    def construct(self):
        options = (
            VGroup(
                VGroup(
                    MathTex("A) \\ 4", color=BLACK),
                    MathTex("C) \\ 8", color=BLACK),
                ).arrange(DOWN, buff=0.25, aligned_edge=LEFT),
                VGroup(
                    MathTex("B) \\ 16", color=BLACK),
                    MathTex("D) \\ 32", color=BLACK),
                ).arrange(DOWN, buff=0.25, aligned_edge=LEFT),
            )
            .arrange(RIGHT, buff=2)
            .to_edge(UP)
        )

        self.play(FadeIn(options))
        self.wait(5)

        self.wait(1)
        self.play(
            Create(SurroundingRectangle(options[1][0], corner_radius=0.1, buff=0.1))
        )
        self.wait(4)
