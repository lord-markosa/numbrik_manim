from manim import *
from utils import *


class SubscribeEndScreen(Scene):
    def construct(self):
        # Thank You text
        thank_you = (
            Text("Thank you for watching", font="Georgia", font_size=60)
            .set_color_by_gradient(TEAL, GREEN_N100)
            .move_to(TITLE_TEXT_POSITION)
        )

        self.play(FadeIn(thank_you, shift=UP), run_time=1.5)

        clearScreen(self, 0.1)

        # Subscribe button
        button = RoundedRectangle(
            corner_radius=0.2, height=1, width=4, color=RED_N100, fill_opacity=1
        ).move_to(TITLE_TEXT_POSITION)
        sub_text = Text("SUBSCRIBE", font="Arial", font_size=36, color=WHITE).next_to(
            button, 0
        )
        subscribe_button = VGroup(button, sub_text)

        # Subtitle: new videos every week
        subtitle = Text(
            "New videos every week",
            font="Verdana",
            font_size=24,
        )
        subtitle.next_to(subscribe_button, DOWN, buff=0.4)

        # Animate everything

        self.play(FadeIn(subscribe_button, scale=0.8), run_time=1.2)

        self.play(FadeIn(subtitle, shift=UP), run_time=1)

        self.wait(2)
