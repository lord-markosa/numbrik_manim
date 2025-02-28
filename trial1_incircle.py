from manim import *


class RightAngledTriangleWithIncircle(Scene):
    def construct(self):
        # Define points for the right-angled triangle
        A = np.array([-4, -1, 0])  # Vertex A
        B = np.array([4, -1, 0])   # Vertex B (base)
        C = np.array([-4, 3, 0])   # Vertex C (height)

        # Create the triangle using Polygon
        triangle = Polygon(A, B, C, color=WHITE)

        # Find the incenter and inradius (approximated)
        a = np.linalg.norm(B - C)  # Length of side opposite to A
        b = np.linalg.norm(A - C)  # Length of side opposite to B
        c = np.linalg.norm(A - B)  # Length of side opposite to C

        # Incenter calculation (weighted average of triangle vertices)
        incenter = (a * A + b * B + c * C) / (a + b + c)

        # Inradius calculation (area of triangle divided by semiperimeter)
        s = (a + b + c) / 2  # Semi-perimeter
        area = np.abs(np.cross(B - A, C - A)) / 2  # Area of the triangle
        inradius = area / s

        # Draw the incircle
        incircle = Circle(radius=inradius, color=YELLOW).move_to(incenter)

        # Draw everything on the scene
        self.play(Create(triangle))  # Create the triangle
        self.play(Create(incircle))  # Create the incircle

        # Label vertices
        label_A = MathTex("A").next_to(A, LEFT)
        label_B = MathTex("B").next_to(B, DOWN)
        label_C = MathTex("C").next_to(C, UP)
        self.play(Write(label_A), Write(label_B), Write(label_C))

        # Pause to display the scene
        self.wait(2)
