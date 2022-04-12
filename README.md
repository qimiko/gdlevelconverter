# 2.0+ to 1.9 Geometry Dash Level Converter

A rewrite of my [original level conversion tool](https://github.com/qimiko/gd-level-scripts). Fixes colors and objects when loading a level created in 2.0+ on 1.9.

See [this document](docs/why.md) for the reason for the rewrite, as well as the new features provided.

## Requirements

* Python 3

## Installation

In the root directory of this project, run `pip install .` using Python. This will add `gd-level-converter` to your PATH.

## Usage

`gd-level-converter input [-g groups...] [-o output]`

See `gd-level-converter --help` for more information.

### Groups

Groups define lists of object id conversions. For example, the `slopes` group will convert any object with id 1743 to id 289. This is necessary as some objects have been modified by RobTop and given new ids. By default, all non-hitbox changing groups are enabled.

To enable all conversions that modify hitboxes, use `all` as the argument for groups when running the converter.

The converter uses these groups to categorize the converted objects in the final report, and will warn if a group may heavily modify visuals or hitboxes.

## License

This project is licensed under the [MIT license](LICENSE).
