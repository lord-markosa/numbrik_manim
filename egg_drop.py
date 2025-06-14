from manim import *


class EggDroppingIntro(Scene):
    def construct(self):
        title = Text("Egg Dropping Problem", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        building = Rectangle(height=5, width=2, color=BLUE).shift(LEFT * 3)
        floors = VGroup()
        for i in range(10):
            y = -2.5 + i * 0.5
            line = Line(start=[-4, y, 0], end=[-2, y, 0], stroke_width=1.5)
            floor_label = Text(str(i + 1), font_size=20).next_to(line, RIGHT, buff=0.1)
            floors.add(line, floor_label)

        egg = ImageMobject("assets/brown-egg.png").scale(0.09).shift(RIGHT * 3 + UP * 2)

        self.play(Create(building), Create(floors))
        self.play(FadeIn(egg))
        self.wait(1)

        # Drop animation
        drop_path = Line(egg.get_center(), [-3, 0, 0])
        self.play(MoveAlongPath(egg, drop_path), run_time=2)

        # Break animation
        crack = Text("💥", font_size=48).move_to([-3, 0, 0])
        self.play(FadeIn(crack))
        self.wait(1)

        self.play(
            FadeOut(egg),
            FadeOut(crack),
            FadeOut(building),
            FadeOut(floors),
            FadeOut(title),
        )


class RecursiveIdea(Scene):
    def construct(self):
        title = Text("Recursive Idea", font_size=48).to_edge(UP)
        self.play(Write(title))

        eq = MathTex(
            r"dp(k, n) = 1 + \min_{1 \le x \le n}(\max(dp(k{-}1,x{-}1), dp(k,n{-}x)))"
        )
        eq.scale(0.7).next_to(title, DOWN)
        self.play(Write(eq))
        self.wait(1)

        # Build a tree for decision from floor x
        node1 = Text("Drop from floor x").shift(UP * 1.5)
        egg_breaks = Text("Egg breaks → dp(k-1, x-1)").shift(LEFT * 3)
        egg_not_break = Text("Egg doesn't break → dp(k, n-x)").shift(RIGHT * 3)

        self.play(FadeIn(node1))
        self.wait(0.5)
        self.play(GrowArrow(Arrow(node1.get_bottom(), egg_breaks.get_top(), buff=0.1)))
        self.play(
            GrowArrow(Arrow(node1.get_bottom(), egg_not_break.get_top(), buff=0.1))
        )
        self.play(FadeIn(egg_breaks), FadeIn(egg_not_break))
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])


class DPTable(Scene):
    def construct(self):
        title = Text("DP Table Filling", font_size=48).to_edge(UP)
        self.play(Write(title))

        table = (
            Table(
                [[f"{i * j}" for j in range(1, 6)] for i in range(1, 6)],
                row_labels=[Text(f"{i} eggs") for i in range(1, 6)],
                col_labels=[Text(f"{i} flr") for i in range(1, 6)],
                top_left_entry=Text(""),
                include_outer_lines=True,
            )
            .scale(0.7)
            .shift(DOWN * 0.5)
        )

        self.play(Create(table))
        self.wait(1)

        highlight = SurroundingRectangle(table.get_cell((2, 3)))
        self.play(Create(highlight))
        self.wait(1)

        update = Text("Min trials = 3", font_size=24).next_to(table, RIGHT)
        self.play(FadeIn(update))
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])
