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

        sub_text2 = Text(
            "SUBSCRIBED", font="Georgia", font_size=32, color=WHITE
        ).next_to(button, 0)

        # Subtitle: new videos every week
        subtitle = Text("for more", font="Verdana", font_size=24, color=RED_N100)
        subtitle.next_to(subscribe_button, DOWN, buff=0.4)

        # Animate everything

        self.play(FadeIn(subscribe_button, scale=0.8), run_time=1.2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1)
        self.wait(1)
        self.play(Transform(sub_text, sub_text2), button.animate.set_color(RED_N900))

        self.wait(2)
