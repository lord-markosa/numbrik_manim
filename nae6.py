from manim import *
from utils import *


class NavierStokesEquation(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        # Title
        title = Tex("Navier--Stokes Equation", color=YELLOW).scale(1.4).to_edge(UP)

        # Main Navier-Stokes equation
        ns_eq = (
            MathTex(
                r"\rho \, \frac{D\vec{v}}{Dt}\;=\; -\nabla p \;+\; \mu \, \nabla^2 \vec{v} \;+\; \vec{f}",
            )
            .scale(1.3)
            .shift(UP)
        )

        # Material derivative expansion
        material_derivative = (
            MathTex(
                r"\frac{D\vec{v}}{Dt} \;=\; \frac{\partial \vec{v}}{\partial t} \;+\; (\vec{v} \cdot \nabla)\vec{v}",
                # tex_to_color_map={
                #     r"\vec{v}": GREEN,
                #     r"t": YELLOW,
                #     r"\nabla": PURPLE
                # }
            )
            .scale(1.3)
            .next_to(ns_eq, DOWN, buff=1)
        )

        # Animations
        self.add(title)
        self.play(fadeInTex(ns_eq))
        self.play(fadeInTex(material_derivative))
        self.wait(3)


import numpy as np


class SchrodingerWave(Scene):
    def construct(self):
        # Title
        self.camera.background_color = BLACK

        # Schrödinger equation
        schrodinger_eq = MathTex(
            r"i\hbar \frac{\partial}{\partial t}\Psi(x,t) \;=\; "
            r"-\frac{\hbar^2}{2m} \nabla^2 \Psi(x,t) \;+\; V(x)\,\Psi(x,t)",
        ).scale(1.1)

        # Display equation first
        self.play(Write(schrodinger_eq), run_time=3)
        clearScreen(self, 2)

        # Axes for plotting
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-3, 3, 1],
            x_length=9,
            y_length=6,
            axis_config={"color": WHITE},
        )

        label = (
            MathTex("\\psi(x)", color=BLUE)
            .scale(1.2)
            .next_to(
                axes.get_axis(1),
                LEFT,
            )
        )

        # Define wave function ψ = sin(k1 x) + sin(k2 x + φ)
        k1, k2, phi = 1, 2, np.pi / 4
        psi_func = lambda x: np.sin(k1 * x) + np.sin(k2 * x + phi)

        # Original wave plot
        wave_plot = axes.plot(psi_func, color=BLUE)

        # Show the wave plot
        self.play(Create(axes), Write(label))
        self.play(Create(wave_plot), run_time=3)
        self.wait(2)

        # Define squared function |ψ|^2
        psi_squared = lambda x: (np.sin(k1 * x) + np.sin(k2 * x + phi)) ** 2
        squared_plot = axes.plot(psi_squared, color=YELLOW)
        label2 = (
            MathTex("\\psi(x)^2", color=YELLOW)
            .scale(1.2)
            .next_to(axes.get_axis(1), LEFT)
        )

        # Transform ψ to |ψ|²
        self.play(Transform(wave_plot, squared_plot), Transform(label, label2))
        self.wait(2)
