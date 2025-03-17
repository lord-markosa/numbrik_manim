# Welcome to Numbrik videos Repository (MANIM)

This project contains various scripts created using the Manim library to visualize mathematical equations and concepts.

## Requirements

-   Python 3.7 or higher
-   Manim library

## Installation

-   Follow the [Manim community guide](https://docs.manim.community/en/stable/installation.html)

## Running Manim Scripts

To render a Manim script, use the `manim` command followed by the script name and the scene class name. You can specify the quality using flags.

### Low Quality

To render in low quality (faster rendering):

```sh
manim -pql script_name.py SceneClassName
```

NOTE: here 'p' is used for preview

### High Quality

To render in high quality (slower rendering):

```sh
manim -qh script_name.py SceneClassName
```

### Example

Assuming you have a script called `example.py` with a scene class named `ExampleScene`, you can render it in low quality with:

```sh
manim -pql example.py ExampleScene
```

And in high quality with:

```sh
manim -pqh example.py ExampleScene
```

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements.

## License

This project is licensed under the MIT License.

## Acknowledgements

This project uses the [Manim](https://www.manim.community/) library created by Grant Sanderson (3Blue1Brown).

## Tutorial

https://github.com/brianamedee/Manim-Tutorials-2021/blob/main/5Tutorial_Adv2D.py
