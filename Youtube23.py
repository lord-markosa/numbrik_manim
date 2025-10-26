from manim import *
from utils import *


class Intro(Scene):
    def construct(self):
        addBackground(self)

        f = 1.2
        b = 3 * f
        c = 4 * f
        A = ORIGIN
        B = A + c * RIGHT
        C = A + b * UP

        triangle = Polygon(A, B, C, stroke_color=BLACK, color=GREEN_N50, fill_opacity=1)

        triangle.move_to(ORIGIN + UP)

        A, B, C = triangle.get_vertices()

        labelA = nMath("a").move_to((A + C) / 2 + LEFT * 0.5)
        labelB = nMath("b").move_to((A + B) / 2 + DOWN * 0.5)

        disp = RIGHT * 0.5 / 1.4 + UP * 0.5 / 1.4
        labelC = nMath("c").move_to((B + C) / 2 + disp)

        labelA = lengthMarkerV2(C, A, "a", LEFT * 0.5)
        labelB = lengthMarkerV2(A, B, "b", DOWN * 0.5).move_to((A + B) / 2 + DOWN * 0.5)

        lengthC_marker1 = Arrow(
            labelC.get_center() + 0.05 * (b * DOWN + c * RIGHT),
            B + disp,
            color=GREY_N400,
            stroke_width=4,
            buff=0,
        )

        # Arrow 2: from label edge in -shift direction to P1+shift
        lengthC_marker2 = Arrow(
            labelC.get_center() + 0.05 * (b * UP + c * LEFT),
            C + disp,
            color=GREY_N400,
            stroke_width=4,
            buff=0,
        )

        labelA_ = nMath("A", color=BLACK).move_to(B + 0.5 * DOWN + 0.5 * RIGHT)
        labelB_ = nMath("B", color=BLACK).move_to(C + 0.5 * UP + 0.5 * LEFT)
        labelC_ = nMath("C", color=BLACK).move_to(A + 0.5 * DOWN + 0.5 * LEFT)

        self.play(
            LaggedStart(
                Create(triangle),
                FadeIn(labelA_, labelB_, labelC_),
                FadeIn(labelA, labelB, labelC, lengthC_marker1, lengthC_marker2),
                lag_ratio=0.8,
            )
        )

        stmt1 = nMath("a^2 + b^2 = c^2").shift(
            2.8 * DOWN,
        )

        hgl1 = solidHighlight(self, stmt1, buff=0.2, corner_radius=0.18, animate=False)
        self.play(fadeInTex(stmt1))
        self.play(FadeIn(*hgl1))
        self.wait(10)


class Intro2(Scene):
    def construct(self):
        addBackground(self)

        f = 1.1
        b = 3 * f
        c = 4 * f
        A = ORIGIN
        B = A + c * RIGHT
        C = A + b * UP

        triangle = Polygon(A, B, C, color=BLACK)

        triangle.move_to(ORIGIN + 2.8 * LEFT)

        A, B, C = triangle.get_vertices()
        D = (B * b + C * c) / (b + c)

        disp = RIGHT * 0.5 / 1.4 + UP * 0.5 / 1.4

        labelA_ = nMath("C", color=BLACK).move_to(B + 0.5 * DOWN + 0.5 * RIGHT)
        labelB_ = nMath("B", color=BLACK).move_to(C + 0.5 * UP + 0.5 * LEFT)
        labelC_ = nMath("A", color=BLACK).move_to(A + 0.5 * DOWN + 0.5 * LEFT)
        labelD_ = nMath("D", color=BLACK).move_to(D + disp)
        perp = Line(A, D, color=BLACK)
        rt = RightAngle(Line(D, A), Line(D, B), color=BLACK)

        stmts = (
            VGroup(
                nMath("AB\\cdot AB = BD\\cdot BC").scale(0.9),
                nMath("AC\\cdot AC = DC\\cdot BC").scale(0.9),
                nMath("AB\\cdot AB + AC \\cdot AC= BC \\cdot BC").scale(0.9),
            )
            .arrange(DOWN, buff=0.5)
            .shift(RIGHT * 3.5)
        )

        self.play(
            LaggedStart(
                Create(triangle),
                FadeIn(labelA_, labelB_, labelC_),
                Create(perp),
                FadeIn(labelD_),
                Create(rt),
                lag_ratio=0.8,
            )
        )

        self.play(fadeInTex(stmts[0]), fadeInTex(stmts[1]), fadeInTex(stmts[2]))

        self.wait(10)


class Pythagoras1(Scene):
    def construct(self):
        addBackground(self)

        f = 0.6
        b = 4 * f
        c = 3 * f
        A = ORIGIN + (b + c) / 2 * DOWN + (b + c) / 2 * LEFT
        B = A + c * RIGHT
        C = A + b * UP

        # Draw triangle ABC
        triangle = Polygon(A, B, C, stroke_color=BLACK, color=YELLOW, fill_opacity=1)

        self.play(Create(triangle))

        # 2nd transformation
        triangle2 = triangle.copy()

        self.play(triangle2.animate.shift(UP * b + LEFT * c))
        self.play(Rotate(triangle2, PI / 2, IN, triangle2.get_vertices()[1]))

        # 3rd transformation
        triangle3 = triangle2.copy()

        self.play(triangle3.animate.shift(RIGHT * b + UP * c))
        self.play(Rotate(triangle3, PI / 2, IN, triangle3.get_vertices()[1]))

        # 4th Transformation
        triangle4 = triangle3.copy()

        self.play(triangle4.animate.shift(RIGHT * c + DOWN * b))
        self.play(Rotate(triangle4, PI / 2, IN, triangle4.get_vertices()[1]))

        grp = VGroup(triangle, triangle2, triangle3, triangle4)
        self.play(grp.animate.scale(1.2))

        square = Polygon(
            triangle.get_vertices()[0],
            triangle2.get_vertices()[0],
            triangle3.get_vertices()[0],
            triangle4.get_vertices()[0],
            color=GREEN_N100,
            fill_opacity=1,
            stroke_color=BLACK,
            z_index=-10,
        )
        self.play(FadeIn(square))

        lengthAB = lengthMarkerV2(
            triangle.get_vertices()[0], triangle.get_vertices()[1], "b", DOWN * 0.5
        )
        lengthAC = lengthMarkerV2(
            triangle.get_vertices()[2], triangle.get_vertices()[0], "a", LEFT * 0.5
        )

        areaSqLabel = MathTex("c^2", color=BLACK).scale(1.3)

        self.play(
            LaggedStart(
                FadeIn(lengthAB),
                FadeIn(lengthAC),
                FadeIn(areaSqLabel),
                lag_ratio=0.5,
            )
        )
        self.wait(2)

        c = np.linalg.norm(triangle.get_vertices()[0] - triangle.get_vertices()[1])

        b = np.linalg.norm(triangle.get_vertices()[0] - triangle.get_vertices()[2])

        area1Label = MathTex("b^2", color=BLACK).scale(1.3)
        area2Label = MathTex("a^2", color=BLACK).scale(1.3)

        area1Label.move_to(triangle.get_vertices()[2] + RIGHT * c / 2 + UP * c / 2)
        area2Label.move_to(triangle.get_vertices()[1] + RIGHT * b / 2 + UP * b / 2)

        self.play(FadeOut(areaSqLabel))
        self.wait(1)
        self.play(triangle3.animate.shift(DOWN * c + LEFT * b))
        self.wait(1)
        self.play(triangle2.animate.shift(RIGHT * c), triangle4.animate.shift(UP * b))
        self.wait(1)
        self.play(FadeIn(area1Label, area2Label))
        self.wait(4)


class Pythagoras2(Scene):
    def construct(self):
        addBackground(self)

        f = 0.8
        a = 3.5
        b = 1.8
        A = ORIGIN + 2.5 * DOWN + 2 * LEFT
        B = A + RIGHT * a
        C = B + UP * a
        D = A + UP * a

        P = B
        Q = P + b * RIGHT
        R = Q + UP * b
        S = P + UP * b

        square1 = Polygon(A, B, C, D, color=YELLOW, stroke_color=BLACK, fill_opacity=1)
        square2 = Polygon(
            P, Q, R, S, color=GREEN_N100, stroke_color=BLACK, fill_opacity=1
        )

        N = A + b * RIGHT
        M = (b * N + (a - b) * R) / a

        p1 = Polygon(A, D, N, color=YELLOW, stroke_color=BLACK, fill_opacity=1)
        p2 = Polygon(D, N, M, C, color=YELLOW, stroke_color=BLACK, fill_opacity=1)
        p3 = Polygon(N, B, M, color=YELLOW, stroke_color=BLACK, fill_opacity=1)
        p4 = Polygon(M, R, S, color=GREEN_N100, stroke_color=BLACK, fill_opacity=1)
        p5 = Polygon(M, B, Q, R, color=GREEN_N100, stroke_color=BLACK, fill_opacity=1)

        grp0 = VGroup(p1, p2, p3, p4, p5)
        grp = VGroup(square1, square2, grp0)

        grp.move_to(ORIGIN)

        # self.add(square1, square2, p1, p2, p3, p4, p5)
        # self.remove(square1, square2)

        c = np.sqrt(a * a + b * b)

        displacement = p1.get_vertices()[0] - A

        A = A + displacement
        B = B + displacement
        C = C + displacement
        D = D + displacement
        P = P + displacement
        Q = Q + displacement
        R = R + displacement
        S = S + displacement
        N = N + displacement
        M = M + displacement

        lengthA = lengthMarkerV2(D, A, "a", 0.5 * LEFT)
        lengthB = lengthMarkerV2(Q, R, "b", RIGHT * 0.5)
        lengthB2 = lengthMarkerV2(A, N, "b", DOWN * 0.5)

        tmp_reg = Polygon(*p1.get_vertices(), color=BLACK)

        tmp_grp = VGroup(tmp_reg, lengthA[2], lengthB2[2])

        self.play(
            LaggedStart(Create(square1), Create(square2), lag_ratio=0.7), run_time=2
        )
        self.play(FadeIn(lengthA[2], lengthB[2]))
        self.wait(1)

        self.play(FadeIn(p1, p2, p3, p4, p5), run_time=1)
        self.remove(square1, square2)

        self.play(FadeIn(lengthB2[2]))
        self.wait(1)
        self.play(FadeOut(lengthB[2]))

        self.play(tmp_grp.animate.shift(1.2 * LEFT), grp0.animate.shift(1.2 * RIGHT))
        self.wait(1)

        self.play(grp0.animate.shift(0.5 * DOWN), tmp_grp.animate.shift(0.5 * DOWN))

        displacement = p4.get_vertices()[0] - M

        p1.z_index = 1
        self.play(Rotate(p1, PI / 2, OUT, p1.get_vertices()[1]))
        p1.z_index = 0

        lengthC = (
            lengthMarkerV2((N + UP * a + D) / 2, (N + A) / 2, "c", LEFT * 0.5)
            .shift(displacement)
            .scale(c / a)
        )

        self.play(Rotate(VGroup(p3, p5), PI / 2, IN, p5.get_vertices()[3]))
        self.play(FadeIn(lengthC[2]))

        self.wait(10)


class Pythagoras3(Scene):
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

        triangle = Polygon(A, B, C, color=BLUE, fill_opacity=1, stroke_color=BLACK)

        # Step 2: Construct squares on each side
        square_a = Square(a, color=YELLOW, fill_opacity=1, stroke_color=BLACK).move_to(
            Line(B, C).get_center(), aligned_edge=RIGHT
        )
        square_b = Square(b, color=YELLOW, fill_opacity=1, stroke_color=BLACK).move_to(
            Line(A, C).get_center(), aligned_edge=UP
        )

        # Hypotenuse square (rotate to align with side BC)
        hyp_line = Line(A, B)
        square_c = Square(c, color=GREEN_N100, fill_opacity=1, stroke_color=BLACK)

        square_c.move_to(hyp_line.get_center() + UP * b / 2 + RIGHT * a / 2)
        square_c.rotate(
            hyp_line.get_angle(),
            about_point=hyp_line.get_center() + UP * b / 2 + RIGHT * a / 2,
        )

        grp = VGroup(square_a, square_b, square_c, triangle)
        grp.move_to(ORIGIN)

        self.play(Create(triangle))
        self.play(
            LaggedStart(
                Create(square_a), Create(square_b), Create(square_c), lag_ratio=0.5
            ),
            run_time=3,
        )
        self.wait(1)

        C = triangle.get_vertices()[2]
        triangle2 = Polygon(
            C,
            C + LEFT * a,
            C + DOWN * b + LEFT * a,
            fill_opacity=1,
            stroke_color=BLACK,
            color=BLUE,
        )
        triangle3 = Polygon(
            C,
            C + DOWN * b,
            C + DOWN * b + LEFT * a,
            fill_opacity=1,
            stroke_color=BLACK,
            color=BLUE,
        )

        triangle_copy = triangle.copy()

        self.play(
            Rotate(
                triangle_copy,
                PI,
                OUT,
                UP * b / 2 + RIGHT * a / 2,
            )
        )

        triangle2_copy = triangle2.copy()
        triangle3_copy = triangle3.copy()
        self.play(
            LaggedStart(Create(triangle2), Create(triangle3), lag_ratio=0.8), run_time=3
        )
        self.play(triangle2_copy.animate.shift(UP * (a + b) + RIGHT * a))
        self.play(triangle3_copy.animate.shift(RIGHT * (a + b) + UP * b))
        self.wait(1)

        A = triangle.get_vertices()[0]
        B = triangle.get_vertices()[1]
        pent1 = Polygon(
            A,
            B,
            B + LEFT * a,
            C + LEFT * a + DOWN * b,
            A + DOWN * b,
            stroke_color=RED_N100,
            stroke_width=8,
            fill_opacity=0.3,
            color=GREY,
        )

        pent2 = pent1.copy()

        self.play(Create(pent1))
        self.wait(1)
        self.play(Rotate(pent2, PI, OUT, (A + B) / 2))
        self.wait(1)

        pent1Outline = Polygon(
            A,
            B,
            B + LEFT * a,
            C + LEFT * a + DOWN * b,
            A + DOWN * b,
            stroke_color=RED_N100,
            stroke_width=8,
        )

        pent2Outline = pent1Outline.copy().rotate(PI, OUT, (A + B) / 2)

        self.add(pent1Outline, pent2Outline)
        self.play(pent1.animate.set_opacity(0), pent2.animate.set_opacity(0))
        self.play(triangle.animate.set_opacity(0), triangle_copy.animate.set_opacity(0))
        self.wait(1)
        self.play(
            triangle2.animate.set_opacity(0), triangle2_copy.animate.set_opacity(0)
        )
        self.wait(1)
        self.play(
            triangle3.animate.set_opacity(0), triangle3_copy.animate.set_opacity(0)
        )
        self.wait(1)

        self.wait(10)


class Pythagoras4(Scene):
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

        triangle = Polygon(A, B, C, color=BLUE, fill_opacity=1, stroke_color=BLACK)

        # Step 2: Construct squares on each side
        square_a = Square(
            a, color=GREEN_N100, fill_opacity=1, stroke_color=BLACK
        ).move_to(Line(B, C).get_center(), aligned_edge=RIGHT)

        square_b = Square(b, color=YELLOW, fill_opacity=1, stroke_color=BLACK).move_to(
            Line(A, C).get_center(), aligned_edge=UP
        )

        # Hypotenuse square (rotate to align with side BC)
        hyp_line = Line(A, B)
        square_c = Square(c, color=BLACK)

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

        grp = VGroup(square_a, square_b, square_c, triangle, square_a2, square_b2)
        grp.move_to(ORIGIN)

        self.play(Create(triangle))
        self.wait(1)
        self.play(
            LaggedStart(
                Create(square_a), Create(square_b), Create(square_c), lag_ratio=0.5
            ),
            run_time=3,
        )
        self.wait(2)

        A = triangle.get_vertices()[0]
        B = triangle.get_vertices()[1]
        C = triangle.get_vertices()[2]

        P = square_b.get_vertices()[3]
        Q = square_b.get_vertices()[2]

        N = C + a * DOWN
        M = P + a * LEFT

        O = N + (b - a) * RIGHT

        p4 = Polygon(A, N, O, color=YELLOW, stroke_color=BLACK, fill_opacity=1)
        p5 = Polygon(A, M, O, color=YELLOW, stroke_color=BLACK, fill_opacity=1)

        p3 = Polygon(M, O, N, Q, color=YELLOW, stroke_color=BLACK, fill_opacity=1)

        p2 = Polygon(A, P, M, color=YELLOW, stroke_color=BLACK, fill_opacity=1)
        p1 = Polygon(A, C, N, color=YELLOW, stroke_color=BLACK, fill_opacity=1)

        self.play(FadeIn(p2, p1, p3, p4, p5), run_time=2)
        self.wait(1)

        self.remove(square_b)
        square_b = Polygon(*square_b.get_vertices(), color=BLACK)
        self.add(square_b)

        p2.z_index = 1
        self.play(p2.animate.shift((a + b) * UP + (b - a) * LEFT))
        p2.z_index = 0

        p3.z_index = 1
        self.play(p3.animate.move_to(square_c.get_center()))
        p3.z_index = 0

        p1.z_index = 10
        self.play(Rotate(p1, PI, axis=(A - O), about_point=O))
        self.play(Rotate(p1, -PI, OUT, A))
        p1.z_index = 0

        self.play(Rotate(p5, PI / 2, OUT, A))
        p5.z_index = 1
        self.play(p5.animate.shift(UP * (a + b) + LEFT * (b - a)))
        p5.z_index = 0

        self.play(Rotate(p4, PI, (A - O), O))
        self.play(Rotate(p4, PI / 2, IN, A))

        p6 = Polygon(
            C, B, B + LEFT * a, color=GREEN_N100, stroke_color=BLACK, fill_opacity=1
        )
        p7 = Polygon(
            C,
            C + LEFT * a,
            B + LEFT * a,
            color=GREEN_N100,
            stroke_color=BLACK,
            fill_opacity=1,
        )

        self.remove(square_a)
        square_a = Polygon(*square_a.get_vertices(), color=BLACK)
        self.add(square_a)

        self.add(p6, p7)

        self.play(p6.animate.shift(RIGHT * b))
        self.play(p7.animate.shift(2 * a * RIGHT + UP * b))
        self.wait(10)


class Pythagoras5(Scene):
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

        self.play(Create(triangle))
        self.play(
            LaggedStart(
                Create(sq_ac), Create(sq_bc), Create(sq_ab), lag_ratio=0.5, run_time=3
            )
        )
        self.wait(1)

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
        self.wait(1)

        self.remove(sq_ac)
        sq_ac = Polygon(*sq_ac.get_vertices(), color=BLACK)
        self.add(sq_ac)

        self.play(p2.animate.shift(C - A))
        self.wait(1)

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

        self.wait(1)

        p3 = Polygon(B, Q, S2[3], color=YELLOW, stroke_color=BLACK, fill_opacity=1)
        p4 = Polygon(
            B, Q, S2[2], S2[1], C, color=YELLOW, stroke_color=BLACK, fill_opacity=1
        )

        self.play(FadeIn(p4, p3))
        self.wait(1)

        self.remove(sq_bc)
        sq_bc = Polygon(*sq_bc.get_vertices(), color=BLACK)
        self.add(sq_bc)

        self.play(p3.animate.shift(C - B))
        self.wait(1)

        grp2 = VGroup(p22, p21, p1, p4, p3)
        grp2.z_index = -1

        self.play(grp2.animate.shift(DOWN * c))
        self.wait(1)

        # self.add(p1, p2, p3, p4, p21, p22)

        triangle2 = Polygon(
            *triangle.get_vertices(),
            color=BLUE,
            stroke_color=BLACK,
            fill_opacity=1,
            z_index=2,
        )

        self.play(FadeIn(triangle2))
        self.wait(1)
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

        self.wait(1)


class Statements1(Scene):
    def construct(self):
        addBackground(self)

        prologue = MathTex(
            '\\text{"Imagination is more important than knowledge"}',
            tex_template=TexFontTemplates.droid_serif,
            color=BLACK,
        ).shift(UP * 0.5)
        prologueBy = nMath("\\text{- Albert Einstein}", color=NUMBRIK_COLOR).shift(
            DOWN * 0.5
        )
        self.play(
            LaggedStart(
                fadeInTex(prologue),
                AnimationGroup(Write(prologueBy), run_time=3),
                lag_ratio=0.8,
            )
        )

        clearScreen(self, 4)

        stmt1 = nMath("\\text{Green Area}", "= c^2")
        hgl1 = solidHighlight(self, stmt1[0], color=GREEN_N50, buff=0.12, animate=False)

        self.play(fadeInTex(stmt1))
        self.play(FadeIn(*hgl1))
        self.wait(2)

        stmt2 = nMath("\\text{Green Area}", "= c^2", "= a^2+b^2")
        hgl2 = solidHighlight(self, stmt2[0], color=GREEN_N50, buff=0.12, animate=False)

        self.play(TransformMatchingTex(stmt1, stmt2), Transform(*hgl1, *hgl2))

        clearScreen(self, 4)

        stmt1 = nMath("\\text{Total Area} = a^2 + b^2")

        self.play(fadeInTex(stmt1))
        self.wait(2)

        stmt2 = nMath("\\text{Total Area} = a^2 + b^2", "=c^2")

        self.play(TransformMatchingTex(stmt1, stmt2))

        clearScreen(self, 4)

        stmt1 = nMath("\\text{The two pentagons are equal!}")

        self.play(fadeInTex(stmt1))
        self.wait(2)
        self.play(FadeOut(stmt1))
        self.wait(0.5)

        stmt2 = nMath("\\text{Area in }", "YELLOW", "=", "\\text{Area in }", "GREEN")

        hgl1 = solidHighlight(self, stmt2[1], buff=0.12, animate=False)
        hgl2 = solidHighlight(self, stmt2[4], color=GREEN_N50, buff=0.12, animate=False)

        self.play(
            LaggedStart(Transform(stmt1, stmt2), FadeIn(*hgl1, *hgl2), lag_ratio=0.8)
        )

        clearScreen(self, 4)

        stmt1 = nMath("\\text{These need no explanation!}")
        self.play(fadeInTex(stmt1))
        self.wait(10)


class Thumbnail(Scene):
    def construct(self):
        eqn = MathTex(
            "a^2 + b^2 = c^2",
            color=BLACK,
            tex_template=TexFontTemplates.comic_sans,
        ).scale(3)
        hgl = solidHighlight(self, eqn, buff=0.7, corner_radius=0.4, animate=False)

        self.add(eqn, *hgl)
        self.wait(10)


class Pythagoras4Mod(Scene):
    def construct(self):
        f = 0.8

        a = 2.5 * f
        b = 3.5 * f
        c = np.sqrt(a**2 + b**2)

        # Step 1: Right triangle
        C = ORIGIN
        A = RIGHT * b
        B = UP * a

        triangle = (
            Polygon(A, B, C, fill_opacity=1)
            .set_color_by_gradient([BLUE_B, VIOLET_N100])
            .set_stroke(color=GREY_N400, width=4)
        )

        # Step 2: Construct squares on each side
        square_a = (
            Square(
                a,
                fill_opacity=1,
            )
            .set_color_by_gradient([WHITE, GREEN_N100])
            .set_stroke(color=GREY_N400, width=4)
            .move_to(Line(B, C).get_center(), aligned_edge=RIGHT)
        )

        square_b = (
            Square(b, color=YELLOW, fill_opacity=1, stroke_color=BLACK)
            .set_color_by_gradient([WHITE, YELLOW])
            .set_stroke(color=GREY_N400, width=4)
            .move_to(Line(A, C).get_center(), aligned_edge=UP)
        )

        # Hypotenuse square (rotate to align with side BC)
        hyp_line = Line(A, B)
        square_c = Square(c).set_stroke(color=GREY_N400, width=4)

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

        grp = VGroup(square_a, square_b, square_c, triangle, square_a2, square_b2)
        grp.move_to(ORIGIN)

        A = triangle.get_vertices()[0]
        B = triangle.get_vertices()[1]
        C = triangle.get_vertices()[2]

        # Length Markers
        AB_perp = perpendicular_unit_vector(A, B, OUT)

        lengthAB = lengthMarkerV3(
            A,
            B,
            "c",
            0.4 * AB_perp,
            centerDist=0.3,
            tip_length=0.2,
            labelColor=GREY_N500,
        )

        lengthAC = lengthMarkerV3(
            C, A, "b", DOWN * 0.4, tip_length=0.2, labelColor=GREY_N500
        )

        lengthBC = lengthMarkerV3(
            B, C, "a", LEFT * 0.4, tip_length=0.2, labelColor=GREY_N500
        )

        # Square labels
        square_a_label = nMath("a^2", color=GREY_N500).move_to(square_a.get_center())
        square_b_label = nMath("b^2", color=GREY_N500).move_to(square_b.get_center())
        square_c_label = nMath("c^2", color=GREY_N500).move_to(square_c.get_center())

        self.play(
            LaggedStart(
                DrawBorderThenFill(triangle, stroke_width=5),
                AnimationGroup(GrowArrow(lengthBC[0]), GrowArrow(lengthBC[1])),
                FadeIn(lengthBC[2]),
                AnimationGroup(GrowArrow(lengthAC[0]), GrowArrow(lengthAC[1])),
                FadeIn(lengthAC[2]),
                AnimationGroup(GrowArrow(lengthAB[0]), GrowArrow(lengthAB[1])),
                FadeIn(lengthAB[2]),
                lag_ratio=0.2,
            )
        )

        self.play(
            LaggedStart(
                FadeOut(lengthAB, lengthBC, lengthAC),
                Create(square_a),
                Create(square_b),
                Create(square_c),
                lag_ratio=0.4,
            )
        )
        self.play(
            LaggedStart(
                FadeIn(square_a_label),
                FadeIn(square_b_label),
                FadeIn(square_c_label),
                lag_ratio=0.3,
            )
        )

        self.play(FadeOut(square_a_label, square_b_label, square_c_label))

        P = square_b.get_vertices()[3]
        Q = square_b.get_vertices()[2]

        N = C + a * DOWN
        M = P + a * LEFT

        O = N + (b - a) * RIGHT

        p4 = (
            Polygon(A, O, M, color=YELLOW, stroke_color=BLACK, fill_opacity=1)
            .set_color_by_gradient([WHITE, YELLOW])
            .set_stroke(color=GREY_N400, width=4)
        )
        p5 = (
            Polygon(A, O, N, color=YELLOW, stroke_color=BLACK, fill_opacity=1)
            .set_color_by_gradient([WHITE, YELLOW])
            .set_stroke(color=GREY_N400, width=4)
        )

        p3 = (
            Polygon(N, O, M, Q, color=YELLOW, stroke_color=BLACK, fill_opacity=1)
            .set_color_by_gradient([WHITE, YELLOW])
            .set_stroke(color=GREY_N400, width=4)
        )

        p2 = (
            Polygon(A, M, P, color=YELLOW, stroke_color=BLACK, fill_opacity=1)
            .set_color_by_gradient([WHITE, YELLOW])
            .set_stroke(color=GREY_N400, width=4)
        )
        p1 = (
            Polygon(A, N, C, color=YELLOW, stroke_color=BLACK, fill_opacity=1)
            .set_color_by_gradient([WHITE, YELLOW])
            .set_stroke(color=GREY_N400, width=4)
        )

        helper1 = Line(C, square_a.get_corner(DL), color=RED_N50, stroke_width=5)
        path = TracedPath(
            helper1.get_end,
            color=GREY_N200,
            dissipating_time=0.1,
            stroke_width=4,
            stroke_color=GREY_N100,
        )

        self.play(Create(helper1))
        self.add(path)

        self.play(Rotate(helper1, PI / 2, OUT, C))
        self.play(Create(p3))
        self.play(
            LaggedStart(
                FadeOut(helper1),
                Create(p1),
                Create(p2),
                AnimationGroup(Create(p4), Create(p5)),
                lag_ratio=0.5,
            )
        )

        self.remove(square_b)
        square_b = Polygon(*square_b.get_vertices()).set_stroke(
            color=GREY_N400, width=4
        )

        self.add(square_b)

        p2.z_index = 1
        self.play(p2.animate.shift((a + b) * UP + (b - a) * LEFT))
        p2.z_index = 0

        p3.z_index = 1
        self.play(p3.animate.move_to(square_c.get_center()))
        p3.z_index = 0

        p1.z_index = 10
        self.play(Rotate(p1, PI, axis=(A - O), about_point=O))
        self.play(Rotate(p1, -PI, OUT, A))

        p1.z_index = 0

        self.play(Rotate(p4, PI / 2, OUT, A))

        p4.z_index = 1
        self.play(p4.animate.shift(UP * (a + b) + LEFT * (b - a)))

        p4.z_index = 0

        self.play(Rotate(p5, PI, (A - O), O))

        self.play(Rotate(p5, PI / 2, IN, A))

        p6 = (
            Polygon(
                C, B + LEFT * a, B, color=GREEN_N100, stroke_color=BLACK, fill_opacity=1
            )
            .set_color_by_gradient([WHITE, GREEN_N100])
            .set_stroke(color=GREY_N400, width=4)
        )
        p7 = (
            Polygon(
                C,
                B + LEFT * a,
                C + LEFT * a,
                color=GREEN_N100,
                stroke_color=BLACK,
                fill_opacity=1,
            )
            .set_color_by_gradient([WHITE, GREEN_N100])
            .set_stroke(color=GREY_N400, width=4)
        )

        self.play(Create(p6), Create(p7))

        self.remove(square_a)
        square_a = Polygon(
            *square_a.get_vertices(), color=BLACK, z_index=-0.1
        ).set_stroke(color=GREY_N400, width=4)
        self.add(square_a)

        self.play(p6.animate.shift(RIGHT * b))
        self.play(p7.animate.shift(2 * a * RIGHT + UP * b))

        square_c2 = square_c.copy()
        square_c2.set_color_by_gradient([WHITE, ORANGE]).set_stroke(
            GREY_N100, 4
        ).set_opacity(0.5)
        self.play(FadeIn(square_c2))
        self.play(
            LaggedStart(
                FadeIn(square_a_label),
                FadeIn(square_b_label),
                FadeIn(square_c_label),
                lag_ratio=0.4,
            )
        )
        self.wait(2)


class PythagorasStatement(Scene):
    def construct(self):
        pyth = nMath("a^2 + b^2 = c^2", color=GREY_N500)
        self.play(fadeInTex(pyth))
        highlight(self, pyth, buff=0.2, unhighlight=False)
        self.wait(10)
