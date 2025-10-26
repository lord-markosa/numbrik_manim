from manim import *
from utils import *


class Intro(Scene):
    def construct(self):
        addBackground(self)

        f = 0.8

        a = 2 * f
        b = 3 * f
        c = np.sqrt(a**2 + b**2)

        # Step 1: Right triangle
        C = ORIGIN
        A = RIGHT * b
        B = UP * a

        triangle = (
            Polygon(A, B, C, color=BLUE, fill_opacity=1, stroke_color=BLACK)
            .set_color_by_gradient([BLUE, WHITE])
            .set_stroke(BLACK)
        )

        # Step 2: Construct squares on each side
        square_a = (
            Square(
                a,
                fill_opacity=1,
            )
            .set_color_by_gradient([GREEN_N100, WHITE])
            .set_stroke(BLACK)
            .move_to(Line(B, C).get_center(), aligned_edge=RIGHT)
        )

        square_b = (
            Square(b, fill_opacity=1, stroke_color=BLACK)
            .move_to(Line(A, C).get_center(), aligned_edge=UP)
            .set_color_by_gradient([YELLOW, WHITE])
            .set_stroke(BLACK)
        )

        # Hypotenuse square (rotate to align with side BC)
        hyp_line = Line(A, B)
        square_c = (
            Square(c, fill_opacity=1, stroke_color=BLACK)
            .move_to(Line(A, C).get_center(), aligned_edge=UP)
            .set_color_by_gradient([PURPLE, WHITE])
            .set_stroke(BLACK)
        )

        square_a2 = Square(a, color=BLACK).move_to(
            Line(B, C).get_center(), aligned_edge=RIGHT
        )

        square_b2 = Square(b, color=BLACK).move_to(
            Line(A, C).get_center(), aligned_edge=UP
        )

        square_c.move_to(hyp_line.get_center() + UP * b / 2 + RIGHT * a / 2)
        square_c.rotate(
            hyp_line.get_angle(),
            about_point=hyp_line.get_center() + UP * b / 2 + RIGHT * a / 2,
        )

        # Center the whole thing
        grp = VGroup(square_a, square_b, square_c, triangle, square_a2, square_b2)
        grp.move_to(ORIGIN + 0.5 * UP)

        # Get updated vertices
        A, B, C = triangle.get_vertices()

        labelA = nMath("a", color=BLACK).next_to((B + C) / 2, LEFT)
        labelB = nMath("b", color=BLACK).next_to((A + C) / 2, DOWN)
        labelC = nMath("c", color=BLACK).next_to((A + B) / 2, UP + RIGHT, buff=0.2)

        labelA2 = nMath("a^2", color=BLACK).move_to(square_a.get_center())
        labelB2 = nMath("b^2", color=BLACK).move_to(square_b.get_center())
        labelC2 = nMath("c^2", color=BLACK).move_to(square_c.get_center())

        self.add(triangle, labelA, labelB, labelC)
        self.wait(1)

        # Animation1: Create squares
        self.play(
            LaggedStart(
                FadeOut(labelA, labelB, labelC),
                Create(square_a),
                Create(square_b),
                Create(square_c),
                lag_ratio=0.5,
            ),
            run_time=3,
        )
        self.play(Write(labelA2), Write(labelB2), Write(labelC2))
        self.wait(2)
        self.play(FadeOut(labelA2, labelB2, labelC2))

        # Animation2: Demonstrate the pythagoras theorem
        self.play(
            square_a.animate.scale(0.5).move_to(ORIGIN + 2 * LEFT + DOWN * 2),
        )

        plus = nMath("+", color=BLACK).next_to(square_a, RIGHT, buff=0.3).scale(1.5)

        self.play(square_b.animate.scale(0.5).next_to(plus, RIGHT, buff=0.3))

        equal = nMath("=", color=BLACK).next_to(square_b, RIGHT, buff=0.3).scale(1.2)

        self.play(
            square_c.animate.rotate(
                -hyp_line.get_angle(), about_point=square_c.get_center()
            )
            .scale(0.5)
            .next_to(equal, RIGHT, buff=0.3)
        )

        labelA2.move_to(square_a.get_center())
        labelB2.move_to(square_b.get_center())
        labelC2.move_to(square_c.get_center())

        self.play(FadeIn(labelA2, labelB2, labelC2, plus, equal))

        self.wait(4)


class Proof(Scene):
    def construct(self):
        # Step 1: Define right triangle with hypotenuse horizontal
        addBackground(self)

        f = 0.5
        a = 3 * f
        b = 4 * f
        c = 5 * f

        theta = np.arctan(b / a)

        A = ORIGIN
        B = ORIGIN + c * RIGHT
        C = ORIGIN + a * np.sin(theta) * UP + a * np.cos(theta) * RIGHT
        triangle = Polygon(A, B, C, color=BLACK, z_index=2)

        # Step 2: Build squares outward on each side
        def square_on_side(p1, p2, outward=1, color=BLUE, fill=True):
            """Return a square on side p1-p2 built outward."""
            side = Line(p1, p2)
            vec = side.get_unit_vector()
            normal = np.array([-vec[1], vec[0], 0]) * outward
            square = Polygon(
                p1,
                p2,
                p2 + normal * side.get_length(),
                p1 + normal * side.get_length(),
                color=color,
                fill_opacity=1 if fill else 0,
                stroke_color=BLACK,
            )
            return square

        sq_ab = square_on_side(A, B, outward=-1, fill=False)  # hypotenuse
        sq_ac = square_on_side(A, C, outward=1, color=GREEN_N100)
        sq_bc = square_on_side(B, C, outward=-1, color=YELLOW)  # slanted side

        grp = VGroup(triangle, sq_ab, sq_bc, sq_ac)
        grp.move_to(ORIGIN)

        labelA2 = nMath("a^2", color=BLACK).move_to(sq_ac.get_center())
        labelB2 = nMath("b^2", color=BLACK).move_to(sq_bc.get_center())
        labelC2 = nMath("c^2", color=BLACK).move_to(sq_ab.get_center())

        self.play(
            LaggedStart(
                Create(triangle),
                Create(sq_ac),
                Create(sq_bc),
                Create(sq_ab),
                FadeIn(labelA2, labelB2, labelC2),
                lag_ratio=0.5,
            ),
            run_time=3,
        )
        self.wait(0.5)
        self.play(FadeOut(labelA2, labelB2, labelC2))

        A, B, C = triangle.get_vertices()

        P = A + a / np.sin(theta) * UP
        Q = B + b / np.sin(theta) * UP

        # Step 3: Drop perpendiculars

        S1 = sq_ac.get_vertices()
        S2 = sq_bc.get_vertices()

        p1 = Polygon(A, C, P, color=GREEN_N100, stroke_color=BLACK, fill_opacity=1)
        p2 = Polygon(
            A, P, S1[2], S1[3], color=GREEN_N100, stroke_color=BLACK, fill_opacity=1
        )

        self.play(FadeIn(p1, p2))

        self.remove(sq_ac)
        sq_ac = Polygon(*sq_ac.get_vertices(), color=BLACK)
        self.add(sq_ac)

        self.play(p2.animate.shift(C - A))

        P1 = Q + LEFT * c

        p21 = Polygon(
            P, P1, S1[2], color=GREEN_N100, stroke_color=BLACK, fill_opacity=1
        )
        p22 = Polygon(
            P,
            P1,
            p2.get_vertices()[2],
            p2.get_vertices()[1],
            C,
            color=GREEN_N100,
            stroke_color=BLACK,
            fill_opacity=1,
        )

        self.play(FadeIn(p22, p21))
        self.remove(p2)
        self.play(p21.animate.shift(p22.get_vertices()[2] - S1[2]))

        p3 = Polygon(B, Q, S2[3], color=YELLOW, stroke_color=BLACK, fill_opacity=1)
        p4 = Polygon(
            B, Q, S2[2], S2[1], C, color=YELLOW, stroke_color=BLACK, fill_opacity=1
        )

        self.play(FadeIn(p4, p3))

        self.remove(sq_bc)
        sq_bc = Polygon(*sq_bc.get_vertices(), color=BLACK)
        self.add(sq_bc)

        self.play(p3.animate.shift(C - B))

        grp2 = VGroup(p22, p21, p1, p4, p3)
        grp2.z_index = -1

        self.play(grp2.animate.shift(DOWN * c))

        # self.add(p1, p2, p3, p4, p21, p22)

        triangle2 = Polygon(
            *triangle.get_vertices(),
            color=BLUE,
            stroke_color=BLACK,
            fill_opacity=1,
            z_index=2,
        )

        self.play(FadeIn(triangle2))
        self.remove(triangle)
        triangle = Polygon(
            *triangle.get_vertices(),
            color=WHITE,
            stroke_color=BLACK,
            fill_opacity=1,
            z_index=1,
        )
        self.add(triangle)

        self.play(triangle2.animate.shift(DOWN * c))

        final = (
            sq_ab.copy()
            .set_z_index(10)
            .set_opacity(1)
            .set_color_by_gradient([PURPLE, WHITE])
            .set_stroke(BLACK)
        )

        self.play(FadeIn(final))

        self.wait(10)
