# PyStanli

Python wrapper for [stanli](https://github.com/hackl/TikZ-StructuralAnalysis) using [PyLaTeX](https://github.com/JelteF/PyLaTeX/).

## Installation

Use `pip` to install `PyStanli`:
```sh
pip install pystanli
```

### Optional: Download a more up-to-date copy of stanli.sty

As of 2023, the version of `stanli` available through [CTAN](https://ctan.org/pkg/stanli) is out of date compared to the version availabe on the [stanli GitHub](https://github.com/hackl/TikZ-StructuralAnalysis).

```sh
wget https://raw.githubusercontent.com/hackl/TikZ-StructuralAnalysis/master/stanli.sty
```

## Usage

TODO: add in documentation

### Optional: Use more up to date stanli.sty

Call `update_stanli_sty` before creating your TikZ diagram, e.g.:
```python
import pystanli
pystanli.update_stanli_sty('./stanli.sty')
```

## Contributing

Any pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
