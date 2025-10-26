from manim import *
from utils import *


class Sierpinski(MovingCameraScene):
    def create_sierpinski(self, vertices, depth):
        if depth == 0:
            return

        # Get the vertices of the triangle
        a, b, c = vertices

        # Find midpoints
        ab_mid = (a + b) / 2
        bc_mid = (b + c) / 2
        ca_mid = (c + a) / 2

        # Create inverted triangle in the middle
        inner_triangle = Polygon(
            ab_mid,
            bc_mid,
            ca_mid,
            stroke_color=BLACK,
            color=BLUE,
            stroke_width=0,
            fill_opacity=1,
        )

        self.add(inner_triangle)

        # Recursively apply to the 3 outer triangles
        self.create_sierpinski([a, ab_mid, ca_mid], depth - 1)
        self.create_sierpinski([ab_mid, b, bc_mid], depth - 1)
        self.create_sierpinski([ca_mid, bc_mid, c], depth - 1)

    def construct(self):
        n = 9

        # Initial large triangle

        a = 6
        rt3 = np.sqrt(3)
        r = a / rt3

        triangle = Polygon(
            LEFT * a / 2 + DOWN * a / 2 / rt3,
            RIGHT * a / 2 + DOWN * a / 2 / rt3,
            UP * r,
            color=BLACK,
            fill_opacity=1,
            stroke_width=0,
        )

        self.add(triangle)

        self.camera.frame.set_height(triangle.get_height())
        self.camera.frame.move_to(triangle.get_center())

        self.create_sierpinski(triangle.get_vertices(), n)

        self.play(
            self.camera.frame.animate.scale(0.1).move_to(triangle.get_vertices()[2]),
            run_time=10,
            rate_func=linear,
        )  # Zoom in
        self.wait(1)
        # self.play(self.camera.frame.animate.scale(5))  # Zoom out


class TriangleSimpleFractal(MovingCameraScene):
    def simpleFractal(self, line, depth=12):
        if depth == 0:
            return

        s = line.get_center()
        d = line.get_length() / 2

        A = (line.get_start() + s) / 2
        B = (line.get_end() + s) / 2

        C = s + d * perpendicular_unit_vector(A, B, IN)

        stroke_width = (DEFAULT_STROKE_WIDTH - 0.1) / (12 - 1) * (depth - 1) + 0.1

        line1 = Line(C, B, color=BLUE, stroke_width=stroke_width)
        line2 = Line(A, C, color=GREEN, stroke_width=stroke_width)

        self.add(line1, line2)
        self.simpleFractal(line1, depth - 1)
        self.simpleFractal(line2, depth - 1)

    def construct(self):
        d = 5
        line = Line(ORIGIN + 3 * DOWN + d * LEFT, ORIGIN + 3 * DOWN + d * RIGHT)
        self.add(line)
        self.simpleFractal(line)

        # self.play(self.camera.frame.animate.scale(0.01).shift(UP + RIGHT), run_time=10)
        self.wait(10)


from manim import *
from manim.utils.unit import Percent, Pixels


class DoorWithForce(ThreeDScene):
    def construct(self):
        # Set camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Create axes for reference (optional)
        axes = ThreeDAxes()

        # Create a 3D door
        door = Rectangle(
            height=3,
            width=1.5,
            fill_color=BLUE_E,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=2,
        )

        # Position the door
        door.move_to(LEFT * 2)

        # Add door frame
        frame = Rectangle(
            height=3.2,
            width=1.7,
            fill_color=BLACK,
            fill_opacity=0.3,
            stroke_color=GRAY,
            stroke_width=3,
        )
        frame.move_to(LEFT * 2)

        # Create hinge point (left side of door)
        hinge = Dot3D(point=door.get_left(), color=RED, radius=0.05)

        # Create force arrows pushing the door
        # Multiple arrows to show distributed force
        arrow_positions = [
            door.get_corner(UR) + DOWN * 0.3 + RIGHT * 0.1,
            door.get_center() + RIGHT * 0.1,
            door.get_corner(DR) + UP * 0.3 + RIGHT * 0.1,
        ]

        force_arrows = VGroup()
        for pos in arrow_positions:
            arrow = Arrow(
                start=pos + RIGHT * 0.5,
                end=pos,
                buff=0,
                color=RED,
                stroke_width=8,
                max_tip_length_to_length_ratio=0.3,
            )
            force_arrows.add(arrow)

        # Add force label
        force_label = Text("Force", color=RED).scale(0.5)
        force_label.next_to(force_arrows[1], RIGHT, buff=0.2)

        # Animation sequence
        self.begin_ambient_camera_rotation(rate=0.1)

        # Show door and frame
        self.play(Create(frame), run_time=1)
        self.play(Create(door), run_time=1)
        self.play(Create(hinge), run_time=0.5)

        self.wait(1)

        # Show force arrows
        self.play(
            LaggedStartMap(GrowArrow, force_arrows, lag_ratio=0.3),
            Write(force_label),
            run_time=2,
        )

        self.wait(1)

        # Animate door opening
        door_copy = door.copy()
        self.play(
            Rotate(
                door_copy,
                angle=-60 * DEGREES,
                about_point=hinge.get_center(),
                rate_func=smooth,
                run_time=3,
            )
        )

        self.wait(2)

        # Stop camera rotation for final view
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75 * DEGREES, theta=45 * DEGREES, run_time=2)

        self.wait(2)


class DoorWithDistributedForce(ThreeDScene):
    def construct(self):
        # Alternative version with more detailed force visualization
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Create door
        door = Prism(dimensions=[0.1, 1.5, 3], fill_color=BLUE_E, fill_opacity=0.8)
        door.move_to(LEFT * 2 + OUT * 0.05)

        # Door frame
        frame = Prism(dimensions=[0.2, 1.7, 3.2], fill_color=GRAY, fill_opacity=0.3)
        frame.move_to(LEFT * 2)

        # Hinge
        hinge = Dot3D(point=door.get_left() + OUT * 0.05, color=RED, radius=0.05)

        # Distributed force arrows with varying intensities
        force_arrows = VGroup()
        force_intensities = [1.0, 1.2, 0.8]  # Different arrow sizes

        positions = [
            door.get_top() + DOWN * 0.5 + RIGHT * 0.1,
            door.get_center() + RIGHT * 0.1,
            door.get_bottom() + UP * 0.5 + RIGHT * 0.1,
        ]

        for i, pos in enumerate(positions):
            arrow_length = 0.8 * force_intensities[i]
            arrow = Arrow3D(
                start=pos + RIGHT * arrow_length,
                end=pos,
                color=color_gradient([RED, YELLOW], force_intensities[i]),
                thickness=0.05,
                tip_length=0.2,
            )
            force_arrows.add(arrow)

        # Force distribution label
        force_text = Text("Distributed Force", color=RED).scale(0.4)
        force_text.to_corner(UR)

        # Animation
        self.play(Create(frame), Create(door), run_time=2)
        self.play(Create(hinge), run_time=0.5)

        self.wait(1)

        # Show force development
        for arrow in force_arrows:
            self.play(GrowArrow(arrow), run_time=0.7)

        self.play(Write(force_text))

        self.wait(1)

        # Show door opening under force
        door_group = VGroup(door, force_arrows)
        self.play(
            Rotate(
                door_group,
                angle=-45 * DEGREES,
                about_point=hinge.get_center(),
                run_time=3,
            )
        )

        self.wait(2)


# Simple 2D version for quick rendering
class SimpleDoorForce(Scene):
    def construct(self):
        # Create door
        door = Rectangle(height=3, width=1.5, fill_color=BLUE_E, fill_opacity=0.8)
        door.move_to(LEFT * 3)

        # Hinge point
        hinge = Dot(point=door.get_left(), color=RED)

        # Force arrows
        arrow1 = Arrow(
            start=door.get_top() + DOWN * 0.5 + RIGHT,
            end=door.get_top() + DOWN * 0.5,
            color=RED,
            buff=0,
        )

        arrow2 = Arrow(
            start=door.get_center() + RIGHT, end=door.get_center(), color=RED, buff=0
        )

        arrow3 = Arrow(
            start=door.get_bottom() + UP * 0.5 + RIGHT,
            end=door.get_bottom() + UP * 0.5,
            color=RED,
            buff=0,
        )

        force_arrows = VGroup(arrow1, arrow2, arrow3)

        # Force label
        force_label = Text("Applied Force", color=RED).next_to(arrow2, RIGHT)

        # Animation
        self.play(Create(door), Create(hinge))
        self.wait(1)
        self.play(LaggedStartMap(GrowArrow, force_arrows), Write(force_label))
        self.wait(1)

        # Door opening animation
        door_group = VGroup(door, force_arrows, force_label)
        self.play(
            Rotate(
                door_group,
                angle=-60 * DEGREES,
                about_point=hinge.get_center(),
                run_time=3,
            )
        )

        self.wait(2)
