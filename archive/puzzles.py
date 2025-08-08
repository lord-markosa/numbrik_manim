from manim import *
from utils import *


class Problem(Scene):
    def construct(self):
        animateTextSeq(
            self,
            [
                Text(
                    "Is this too complicated?",
                    font_size=30,
                    font="Arial",
                ),
                MathTex("1, 2, 3, 5, 8,", "?", color=YELLOW).set_color_by_tex(
                    "?", ORANGE
                ),
                Text("Comment your answer", font_size=30, color=NUMBRIK_COLOR),
            ],
            shift_val=DOWN,
            wait_time=0.2,
            run_time=0.75,
        )

        self.wait(4)

        clearScreen(self)

        subscribe = Text("Subscribe for more", color=GREEN_N100).move_to(
            TITLE_TEXT_POSITION
        )

        self.play(Write(subscribe))

        self.wait(2)


class Problem2(Scene):
    def construct(self):
        title = Text("Count the number of triangles", font_size=30).to_edge(UP)
        self.play(Write(title))

        # Define main triangle vertices
        A = np.array([-2, -1, 0])  # Bottom left
        B = np.array([2, -1, 0])  # Bottom right
        C = np.array([0, 2, 0])  # Top vertex

        # Draw the outer large triangle
        main_triangle = Polygon(A, B, C, color=WHITE)

        # Midpoints of sides
        AB_mid = (A + B) / 2
        AC_mid = (A + C) / 2
        BC_mid = (B + C) / 2

        # Additional dividing lines
        line1 = Line(AC_mid, B, color=BLUE)
        line2 = Line(BC_mid, A, color=BLUE)
        line3 = Line(AB_mid, C, color=BLUE)

        # Draw all elements
        self.play(Create(main_triangle))
        self.play(Create(line1), Create(line2), Create(line3))

        comment = Text(
            "Comment your answer", color=NUMBRIK_COLOR, font_size=30
        ).next_to(main_triangle, DOWN, buff=1)

        self.play(Write(comment))

        self.wait(8)

        clearScreen(self)

        subscribe = Text("Subscribe for more", color=GREEN_N100).move_to(
            TITLE_TEXT_POSITION
        )
        self.play(Write(subscribe))

        self.wait(2)


def subscribe(self):
    youtubeIcon = ImageMobject("assets/Youtube.png").scale(0.25).shift(UP)
    self.play(FadeIn(youtubeIcon))
    animateTextSeq(
        self,
        [
            Text("SUBSCRIBE", color=ManimColor("#FF0000"), font_size=36).move_to(
                TITLE_TEXT_POSITION
            ),
            Text("for more...", font_size=30, color=NUMBRIK_COLOR),
        ],
        next_reference=youtubeIcon,
        wait_time=0.2,
    )

    self.wait(2)


class Problem3(Scene):
    def construct(self):
        animateTextSeq(
            self,
            [
                Text(
                    "In a language...",
                    font_size=30,
                ),
                MathTex("DUCK \\Rightarrow FXGP", color=YELLOW),
                MathTex("MIKE \\Rightarrow \\ ", "?").set_color_by_tex("?", ORANGE),
                Text("Comment your answer", font_size=30, color=NUMBRIK_COLOR),
            ],
            wait_time=0.2,
            run_time=0.75,
        )

        self.wait(4)
        clearScreen(self)
        subscribe(self)


class Problem4(Scene):
    def construct(self):
        title = Text("Count the number of triangles", font_size=30).to_edge(UP)
        self.play(Write(title))

        # Define main triangle vertices
        A = np.array([-2, -1, 0])  # Bottom left
        B = np.array([2, -1, 0])  # Bottom right
        C = np.array([0, 2, 0])  # Top vertex

        # Draw the outer large triangle
        main_triangle = Polygon(A, B, C, color=WHITE)

        # Midpoints of sides
        AB_1 = (2 * A + B) / 3
        AB_2 = (2 * B + A) / 3
        AC_mid = (A + C) / 2
        BC_mid = (B + C) / 2

        # Additional dividing lines
        line1 = Line(AB_1, C, color=BLUE)
        line2 = Line(AB_2, C, color=BLUE)
        line3 = Line(AC_mid, BC_mid, color=BLUE)

        # Draw all elements
        self.play(Create(main_triangle))
        self.play(Create(line1), Create(line2), Create(line3))

        comment = Text(
            "Comment your answer", color=NUMBRIK_COLOR, font_size=30
        ).next_to(main_triangle, DOWN, buff=1)

        self.play(Write(comment))

        self.wait(8)

        clearScreen(self)

        subscribe(self)


class Subscribe(Scene):
    def construct(self):
        subscribe(self)
