from manim import *
from utils import *


class JapaneseMultiplication(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Colors
        color_3 = BLUE
        color_1 = GREEN
        color_2 = ORANGE
        color_multiplier = RED_N100

        gap = 0.4
        length = 2

        # Horizontal lines for multiplier (3)
        horizontal_lines = VGroup(
            *[
                Line(
                    LEFT * length,
                    RIGHT * length,
                    color=color_multiplier,
                    stroke_width=4,
                ).shift(DOWN * (i - 1) * gap * 2)
                for i in range(3)
            ]
        )

        brace1 = Brace(horizontal_lines, LEFT, color=GREY_N400)
        label1 = nMath("3", color=GREY_N800).next_to(brace1, LEFT)

        self.play(
            LaggedStart(
                Create(horizontal_lines), Write(brace1), Create(label1), lag_ratio=0.3
            )
        )

        # Vertical groups for 312
        group3 = VGroup(
            *[
                Line(UP * length, DOWN * length, color=color_3, stroke_width=4).shift(
                    LEFT * (3 + i * gap)
                )
                for i in range(3)
            ]
        )

        # Tens: 1 line
        group1 = VGroup(
            Line(UP * length, DOWN * length, color=color_1, stroke_width=4).shift(
                RIGHT * 0
            )
        )

        # Ones: 2 lines
        group2 = VGroup(
            *[
                Line(UP * length, DOWN * length, color=color_2, stroke_width=4).shift(
                    RIGHT * (2 + i * gap)
                )
                for i in range(2)
            ]
        )
        vertical_groups = VGroup(group3, group1, group2).arrange(RIGHT, buff=1.0)

        brace2 = Brace(group3, UP, color=GREY_N400)
        label2 = nMath("3", color=GREY_N800).next_to(brace2, UP)

        brace3 = Brace(group1, UP, color=GREY_N400)
        label3 = nMath("1", color=GREY_N800).next_to(brace3, UP)

        brace4 = Brace(group2, UP, color=GREY_N400)
        label4 = nMath("2", color=GREY_N800).next_to(brace4, UP)

        self.play(
            LaggedStart(
                Create(vertical_groups, run_time=2),
                Write(brace2),
                Write(brace4),
                FadeIn(label2, label3, label4),
                lag_ratio=0.2,
            )
        )

        # --- Intersection points ---
        dots = VGroup()

        dotGroups = VGroup()

        for group in vertical_groups:
            tmpGroup = VGroup()
            for h in horizontal_lines:
                for v in group:
                    # Use line_intersection to get intersection point
                    p = line_intersection(
                        [h.get_start(), h.get_end()], [v.get_start(), v.get_end()]
                    )
                    dot = Dot(p, color=GREY_N800, radius=0.1)
                    dots.add(dot)
                    tmpGroup.add(dot)

            dotGroups.add(tmpGroup)

        self.play(
            LaggedStart(*[FadeIn(dot, scale=0.3) for dot in dots], lag_ratio=0.03)
        )

        final = nMath("312 \\times 3 = ", "9", "3", "6", color=GREY_N800).next_to(
            vertical_groups, DOWN, buff=0.75
        )

        self.play(FadeIn(final[0], shift=UP))
        self.play(TransformFromCopy(dotGroups[0], final[1]))
        self.play(TransformFromCopy(dotGroups[1], final[2]))
        self.play(TransformFromCopy(dotGroups[2], final[3]))

        # --- Counting groups visually ---

        self.wait(40)


class Chat(Scene):
    def chatBubble(self, message, sender, time):
        main = VGroup()
        # message = nMath("Hello")
        l = np.linalg.norm(message.get_right() - message.get_left()) + 0.75
        h = np.linalg.norm(message.get_top() - message.get_bottom()) + 1

        body = Rectangle(GREY_N300, h, l).round_corners(radius=0.2)
        message.move_to(body.get_left() + 0.3 * RIGHT, aligned_edge=LEFT).shift(
            UP * 0.1
        )
        sentBy = (
            nText(sender, color=GREY_N200)
            .scale(0.9)
            .move_to(body.get_corner(UL) + 0.2 * UP, aligned_edge=LEFT + DOWN)
        )
        timeStamp = (
            nText(time, color=GREY_N200)
            .scale(0.7)
            .move_to(
                body.get_corner(DR) + 0.1 * UP + 0.2 * LEFT, aligned_edge=RIGHT + DOWN
            )
        )
        main.add(body, message, sentBy, timeStamp)

        return main

    def construct(self):
        def waitBubble(obj):
            dots = VGroup(*[Dot(radius=0.1, color=GREY_N200) for _ in range(3)])
            dots.arrange(RIGHT, buff=0.2)

            rect = SurroundingRectangle(
                dots, color=GREY_N300, corner_radius=0.2, buff=0.18
            )

            bubble = VGroup(dots, rect).to_corner(DL)

            self.wait(1)
            self.play(
                LaggedStart(obj.animate.shift(UP), FadeIn(bubble), lag_ratio=0.4),
                run_time=0.5,
            )

            # Animate each dot sequentially

            for _ in range(3):  # repeat animation a few times
                for i, dot in enumerate(dots):
                    self.play(
                        dot.animate.set_color(GREY_N400).scale(1.5),
                        run_time=0.2,
                    )
                    self.play(
                        dot.animate.set_color(GREY_N200).scale(2 / 3),
                        run_time=0.2,
                    )
            self.play(FadeOut(rect, dots), obj.animate.shift(DOWN), run_time=0.2)

        messages = VGroup()

        chat1 = (
            self.chatBubble(
                VGroup(
                    nMath("\\text{How do you multiply this?}"),
                    nMath("312 \\times 3"),
                )
                .arrange(DOWN, buff=0.2, aligned_edge=LEFT)
                .scale(0.9),
                "Me:",
                "9:18pm",
            )
            .to_edge(DOWN)
            .to_edge(LEFT)
        )

        messages.add(chat1)

        chat2 = (
            self.chatBubble(
                Rectangle(WHITE, height=4, width=5),
                "Random.animations (100k):",
                "9:30pm",
            )
            .to_edge(DOWN)
            .to_edge(LEFT)
        )

        chat3 = (
            self.chatBubble(Rectangle(WHITE, height=3.5, width=5), "K.Lame", "9:31pm")
            .to_edge(DOWN)
            .to_edge(LEFT)
        )

        chat4 = (
            (
                self.chatBubble(
                    VGroup(
                        nMath("\\text{@Random.animations try this:}"),
                        nMath("989 \\times 998"),
                    )
                    .arrange(DOWN, buff=0.2, aligned_edge=LEFT)
                    .scale(0.9),
                    "Random.comments",
                    "9:31pm",
                )
            )
            .to_edge(DOWN)
            .to_edge(LEFT)
        )

        self.play(FadeIn(chat1, shift=UP))
        waitBubble(messages)
        self.play(
            LaggedStart(
                messages.animate.next_to(chat2, UP, buff=0.7, aligned_edge=LEFT),
                FadeIn(chat2),
                lag_ratio=0.3,
            )
        )
        self.wait(15)

        messages.add(chat2)
        waitBubble(messages)
        self.play(
            LaggedStart(
                messages.animate.next_to(chat3, UP, buff=0.7, aligned_edge=LEFT),
                FadeIn(chat3),
                lag_ratio=0.3,
            )
        )
        self.wait(15)

        messages.add(chat3)
        self.wait(1)
        waitBubble(messages)
        self.play(
            LaggedStart(
                messages.animate.next_to(chat4, UP, buff=0.7, aligned_edge=LEFT),
                FadeIn(chat4),
                lag_ratio=0.3,
            )
        )

        self.wait(5)
