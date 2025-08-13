from manim import *


class TransformByParts(Scene):
    def construct(self):
        start = MathTex("a", "+", "b")
        start.set_color_by_tex_to_color_map({"a": BLUE, "+": BLACK, "b": GREEN})
        end = MathTex("b", "-", "a", color=BLACK).next_to(start, DOWN)

        self.play(Write(start))
        self.wait(1)

        # WAY ONE
        self.play(TransformFromCopy(start[0], end[2]))  # 'a' to 'a'
        self.play(TransformFromCopy(start[2], end[0]))  # 'b' to 'b'
        self.play(TransformFromCopy(start[1], end[1]))  # '+' to '-'

        # WAY TWO
        self.play(TransformMatchingTex(start, end))
        self.wait(1)
