from manim import *
from utils import *


class Problem1(Scene):
    def construct(self):
        # Net of a die (unfolded cube)
        face1 = Square(side_length=1, color=WHITE, fill_color=BLUE_E, fill_opacity=0.7)

        face2 = Square(
            side_length=1, color=WHITE, fill_color=BLUE_E, fill_opacity=0.7
        ).next_to(face1, RIGHT, buff=0)

        face3 = Square(
            side_length=1, color=WHITE, fill_color=BLUE_E, fill_opacity=0.7
        ).next_to(face2, RIGHT, buff=0)

        face4 = Square(
            side_length=1, color=WHITE, fill_color=BLUE_E, fill_opacity=0.7
        ).next_to(face3, RIGHT, buff=0)

        face5 = Square(
            side_length=1, color=WHITE, fill_color=BLUE_E, fill_opacity=0.7
        ).next_to(face3, DOWN, buff=0)

        face6 = Square(
            side_length=1, color=WHITE, fill_color=BLUE_E, fill_opacity=0.7
        ).next_to(face2, UP, buff=0)

        net = VGroup([face1, face2, face3, face4, face5, face6]).move_to(
            TITLE_TEXT_POSITION + 0.5 * UP
        )

        # Label faces with numbers (standard die configuration)
        labels = VGroup(
            Text("1").move_to(net[0]),  # Back
            Text("6").move_to(net[1]),  # Right
            Text("3").move_to(net[2]),  # Left
            Text("2").move_to(net[3]),  # Top
            Text("5").move_to(net[4]),  # Bottom
            Text("4").move_to(net[5]),  # Front
        )

        self.play(Create(net), Write(labels))

        lines = animateTextSeq(
            self,
            [
                Text("When folded into a cube,", font_size=30),
                MathTex("\\text{Opposite to } 6 =", "?", color=YELLOW).set_color_by_tex(
                    "?", PURE_RED
                ),
            ],
            wait_time=0.1,
            line_buffer=0.5,
            next_reference=net,
        )

        self.play(
            Write(
                Text("Comment your answer!", color=NUMBRIK_COLOR, font_size=30).next_to(
                    lines[1], DOWN, buff=0.75
                )
            )
        )
        self.wait(4)

        clearScreen(self)
        subscribe(self)


class Problem2(Scene):
    def construct(self):
        lines = animateTextSeq(
            self,
            [
                Text("In a class...", font_size=30, color=NUMBRIK_COLOR),
                MathTex("\\text{History: } 25 \\text{ students}"),
                MathTex("\\text{Maths: } 30 \\text{ students}"),
                MathTex("\\text{Both: } 15 \\text{ students}"),
                MathTex("\\text{Total } = \\ ", "?", color=YELLOW).set_color_by_tex(
                    "?", PURE_RED
                ),
            ],
            wait_time=0.1,
            run_time=1,
        )

        commentYourAns(self, lines[-1])

        subscribe(self)


class Problem3(Scene):
    def construct(self):
        # Define triangle vertices
        A = np.array([-2, 2, 0])
        B = np.array([2, -1, 0])
        C = np.array([-2, -1, 0])

        labelA = Text("A", font_size=34).next_to(A, UP)
        labelB = Text("B", font_size=34).next_to(B, RIGHT)
        labelC = Text("C", font_size=34).next_to(C, LEFT)

        lenAC = Text("3", font_size=34).next_to((A + C) / 2, LEFT)
        lenBC = Text("4", font_size=34).next_to((B + C) / 2, DOWN)

        apx = C + 0.25 * UP
        apy = C + 0.25 * RIGHT
        apEnd = C + 0.25 * (UP + RIGHT)

        rightAngleLine1 = Line(start=apx, end=apEnd)
        rightAngleLine2 = Line(start=apy, end=apEnd)

        # Draw the right-angled triangle
        triangle = Polygon(A, B, C, color=WHITE)

        # Calculate the circumcenter (midpoint of hypotenuse)
        circumcenter = (A + B) / 2

        # Calculate the circumradius (distance from circumcenter to any vertex)
        circumradius = np.linalg.norm(circumcenter - C)

        # Draw the circumcircle
        circumcircle = Circle(radius=circumradius, color=YELLOW).move_to(circumcenter)

        # Draw all elements
        self.play(Create(triangle))
        self.play(
            Write(labelA),
            Write(labelB),
            Write(labelC),
            Write(lenAC),
            Write(lenBC),
            Create(rightAngleLine1),
            Create(rightAngleLine2),
        )
        self.play(Create(circumcircle))

        self.play(
            Write(
                MathTex("Radius=\\ ", "?", color=YELLOW)
                .shift(1.15 * UP + 0.85 * RIGHT)
                .set_color_by_tex("?", PURE_RED)
                .scale(0.8)
            )
        )

        self.wait(1)

        commentYourAns(self, circumcircle)

        subscribe(self)


class Problem4(Scene):
    def construct(self):
        lines = animateTextSeq(
            self,
            [
                Text("What's next?", font_size=30, color=NUMBRIK_COLOR),
                MathTex("5, 12, 23, 50, 141,", "?", color=YELLOW).set_color_by_tex(
                    "?", PURE_RED
                ),
            ],
            wait_time=0.1,
            run_time=1,
        )

        commentYourAns(self, lines[-1])

        subscribe(self)


class Problem5(ThreeDScene):
    def construct(self):
        # Set up 3D camera orientation
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)

        group = VGroup(
            self.createCube("2", "5", "1"), self.createCube("4", "2", "1")
        ).arrange(UP + LEFT)

        self.play(Create(group))

        self.wait(3)

    def createCube(self, x, y, z):
        cube = Cube(
            side_length=2,
            fill_opacity=1,
            fill_color=BLUE,
            stroke_color=WHITE,
            stroke_width=2,
        )

        # Add numbers on three visible faces
        one = (
            Text(x, color=BLACK, font="Arial")
            .move_to(cube.get_center() + OUT * 1.01)
            .rotate(PI)
        )
        two = (
            Text(y, color=BLACK, font="Arial")
            .move_to(cube.get_center() + RIGHT * 1.01)
            .rotate(PI / 2)
            .rotate(PI / 2, UP)
        )
        three = (
            Text(z, color=BLACK, font="Arial")
            .move_to(cube.get_center() + UP * 1.01)
            .rotate(PI)
            .rotate(PI / 2, LEFT)
        )

        return VGroup(cube, one, two, three)


class Problem6(Scene):
    def construct(self):
        animateTextSeq(
            self,
            [
                MathTex("2xm-ym+yn-2xn = 0"),
                MathTex(
                    "\\text{if } m \\ne n \\text{ and } y = kx\\text{, find }k",
                    color=YELLOW,
                ),
                MathTex("m(2x-y)+n(y-2x) = 0"),
                MathTex("(m-n)(2x-y) = 0"),
                MathTex("\\Rightarrow y = 2x \\Rightarrow k = 2", color=GREEN_N100),
            ],
        )

        self.wait(2)

        subscribe(self)


class Problem7(Scene):
    def construct(self):
        lines = animateTextSeq(
            self,
            [
                MathTex("3^{81}").scale(2.5),
            ],
        )

        commentYourAns(self, lines[-1])
        subscribe(self)


class Problem8(Scene):
    def construct(self):
        # Create two squares with the same center
        outer_square = Square(side_length=4, color=BLUE)
        inner_square = Square(side_length=2, color=GREEN).move_to(
            outer_square.get_center()
        )

        # Create two lines dissecting the squares horizontally and vertically
        horizontal_line = Line(
            start=outer_square.get_left(), end=outer_square.get_right(), color=RED
        )
        vertical_line = Line(
            start=outer_square.get_top(), end=outer_square.get_bottom(), color=RED
        )

        # Group and display the elements
        group = VGroup(outer_square, inner_square, horizontal_line, vertical_line)
        self.play(Create(group), run_time=2)
        self.wait(2)


class Temp(Scene):
    def construct(self):
        lines = animateTextSeq(
            self,
            [
                MathTex("3^x = x^9").scale(2.2),
                Text("Is this solvable?", font_size=36, color=YELLOW),
            ],
            line_buffer=1,
        )
        commentYourAns(self, lines[-1])
        subscribe(self)


def subscribe(self):
    clearScreen(self, 1)

    youtubeIcon = ImageMobject("assets/Youtube.png").scale(0.25).shift(UP)
    self.play(FadeIn(youtubeIcon))
    animateTextSeq(
        self,
        [
            Text("SUBSCRIBE", color=ManimColor("#FF0000"), font_size=36),
            Text("for more...", font_size=30, color=NUMBRIK_COLOR),
        ],
        next_reference=youtubeIcon,
        next_buff=0,
        wait_time=0.2,
    )

    self.wait(2)


def commentYourAns(self, next_ref):
    self.play(
        Write(
            Text("Comment your ans!", color=NUMBRIK_COLOR, font_size=30).next_to(
                next_ref, DOWN, buff=1
            )
        )
    )
