# 🦕 PixelDino

Generate pixelated dinosaurs with random clothes!

## Installation

```bash
pip install pixeldino
# or
uv pip install pixeldino
```

## Usage

### Command Line

```bash
# Generate a random dino
pixeldino -o my_dino.png

# Generate with specific accessories
pixeldino -o fancy_dino.png --hat top_hat --glasses sunglasses

# Generate multiple dinos
pixeldino -o dino.png -n 5

# Generate an animated GIF
pixeldino -o party.gif --gif

# Larger output (32x scale = 512x512)
pixeldino -o big_dino.png -s 32

# List all options
pixeldino --list-options
```

### Python API

```python
from pixeldino import generate_dino, DinoGenerator

# Quick generation
img = generate_dino("dino.png")

# With options
img = generate_dino(
    "fancy_dino.png",
    hat="crown",
    glasses="sunglasses",
    shirt="hoodie",
    accessory="necklace",
    scale=16
)

# Using the generator class
gen = DinoGenerator(scale=16)

# Generate with random everything
img = gen.generate()

# Generate with specific color
img = gen.generate(dino_color=(255, 100, 100))

# Generate a batch
dinos = gen.generate_batch(10)

# See all options
print(gen.get_options())
```

## Available Options

### Hats
- `none`, `top_hat`, `cap`, `crown`, `beanie`, `party_hat`

### Glasses
- `none`, `sunglasses`, `monocle`, `nerd_glasses`

### Shirts
- `none`, `tshirt`, `vest`, `hoodie`

### Accessories
- `none`, `bowtie`, `necklace`, `scarf`

## Dino Colors

10 built-in colors: green, light green, orange, yellow, purple, pink, blue, cyan, red, brown.

Or pass any RGB tuple!

## License

MIT
