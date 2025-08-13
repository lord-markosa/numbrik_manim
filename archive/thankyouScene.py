from manim import *
from utils import *


class SubscribeEndScreen(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Subscribe button
        button = RoundedRectangle(
            corner_radius=0.2, height=1, width=3.25, color=RED_N100, fill_opacity=1
        ).move_to(TITLE_TEXT_POSITION)
        sub_text = Text("SUBSCRIBE", font="Georgia", font_size=32, color=WHITE).next_to(
            button, 0
        )
        subscribe_button = VGroup(button, sub_text)

        # Subtitle: new videos every week
        subtitle = Text("for more", font="Verdana", font_size=26, color=RED_N100)
        subtitle.next_to(subscribe_button, DOWN, buff=0.3)

        # Curved arrow from button's right edge to bottom right corner
        button_right = button.get_right()
        arrow = CurvedArrow(
            start_point=button_right + 0.5 * RIGHT,
            end_point=DOWN + 2 * RIGHT,
            angle=-PI / 2,
            color=RED_N100,
            stroke_width=6,
            tip_length=0.3,
        )

        # Animate everything

        self.play(FadeIn(subscribe_button, scale=0.8))
        self.play(Create(arrow))
        self.play(FadeIn(subtitle, shift=0.5 * UP))
        self.wait(4)


class SubscribeEndSceneShorts(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Subscribe button
        button = RoundedRectangle(
            corner_radius=0.2, height=1, width=3.25, color=RED_N100, fill_opacity=1
        ).move_to(TITLE_TEXT_POSITION)
        sub_text = Text("SUBSCRIBE", font="Georgia", font_size=32, color=WHITE).next_to(
            button, 0
        )
        subscribe_button = VGroup(button, sub_text)

        # Subtitle: new videos every week
        subtitle = Text("for more", font="Verdana", font_size=26, color=RED_N100)
        subtitle.next_to(subscribe_button, DOWN, buff=0.3)

        # Curved arrow from button's right edge to bottom right corner
        button_right = button.get_right()
        arrow = CurvedArrow(
            start_point=button_right + DOWN + 0.2 * RIGHT,
            end_point=3 * DOWN + RIGHT,
            angle=-PI / 2,
            color=RED_N100,
            stroke_width=6,
            tip_length=0.3,
        )

        # Animate everything

        self.play(FadeIn(subscribe_button, scale=0.8))
        self.play(Create(arrow))
        self.play(FadeIn(subtitle, shift=0.5 * UP))
        self.wait(4)
