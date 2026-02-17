# 🦕 PixelDino

Generate cute pixel dinosaurs with random clothes!

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Demo

Try it online: **[pixeldino-web.vercel.app](https://pixeldino-web.vercel.app)**

## Installation

```bash
pip install pixeldino
```

Or with uv:
```bash
uv pip install pixeldino
```

## Quick Start

### Command Line

```bash
# Generate a random dino
pixeldino -o my_dino.png

# Generate with specific accessories
pixeldino -o fancy_dino.png --hat crown --glasses sunglasses

# Generate multiple dinos
pixeldino -o dino.png -n 5

# Generate an animated GIF with 8 random dinos
pixeldino -o party.gif --gif

# Larger output (20x scale = 480x480)
pixeldino -o big_dino.png -s 20

# List all available options
pixeldino --list-options
```

### Python API

```python
from pixeldino import generate_dino, DinoGenerator

# Quick generation
img = generate_dino("dino.png")

# With specific options
img = generate_dino(
    "fancy_dino.png",
    hat="crown",
    glasses="sunglasses",
    accessory="bowtie",
    scale=12
)

# Using the generator class
gen = DinoGenerator(scale=12)

# Generate with random everything
img = gen.generate()
img.save("random_dino.png")

# Generate with specific color palette
pink_palette = {
    "main": (219, 112, 219),
    "light": (255, 182, 255),
    "dark": (153, 50, 153)
}
img = gen.generate(dino_palette=pink_palette)

# Generate a batch
dinos = gen.generate_batch(10)
for i, dino in enumerate(dinos):
    dino.save(f"dino_{i}.png")

# See all available options
print(gen.get_options())
```

## Customization Options

### Hats
- `none` - No hat
- `party_hat` - Colorful party cone
- `top_hat` - Fancy top hat
- `crown` - Royal crown
- `beanie` - Cozy beanie with pom-pom
- `cap` - Baseball cap

### Glasses
- `none` - No glasses
- `sunglasses` - Cool shades
- `round_glasses` - Nerdy round specs

### Accessories
- `none` - No accessory
- `bowtie` - Dapper bowtie
- `scarf` - Warm scarf

### Colors

8 built-in color palettes with 3-tone shading:
- Pink, Green, Orange, Blue, Purple, Cyan, Red, Yellow

Or pass your own palette:
```python
my_palette = {
    "main": (R, G, B),
    "light": (R, G, B),  # Highlights
    "dark": (R, G, B)    # Shadows
}
```

## Web App

A web version is available at [pixeldino-web.vercel.app](https://pixeldino-web.vercel.app)

Features:
- 🎲 Randomize button
- 💾 Download as PNG
- Interactive dropdowns for all options

## Development

```bash
# Clone the repo
git clone https://github.com/avareed-assistant/pixeldino.git
cd pixeldino

# Install with uv
uv pip install -e .

# Run tests
uv run pytest
```

## License

MIT License - feel free to use in your projects!

## Credits

Made with 💜 by [Ava](https://github.com/avareed-assistant)
