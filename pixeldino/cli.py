"""
Command-line interface for PixelDino
"""

import argparse
import sys
from pathlib import Path
from .generator import DinoGenerator, generate_dino


def main():
    parser = argparse.ArgumentParser(
        description="Generate pixelated dinosaurs with random clothes"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="dino.png",
        help="Output file path (default: dino.png)"
    )
    parser.add_argument(
        "-n", "--count",
        type=int,
        default=1,
        help="Number of dinos to generate (default: 1)"
    )
    parser.add_argument(
        "-s", "--scale",
        type=int,
        default=16,
        help="Pixel scale multiplier (default: 16 = 256x256)"
    )
    parser.add_argument(
        "--hat",
        type=str,
        choices=["none", "top_hat", "cap", "crown", "beanie", "party_hat"],
        help="Specific hat type"
    )
    parser.add_argument(
        "--glasses",
        type=str,
        choices=["none", "sunglasses", "monocle", "nerd_glasses"],
        help="Specific glasses type"
    )
    parser.add_argument(
        "--shirt",
        type=str,
        choices=["none", "tshirt", "vest", "hoodie"],
        help="Specific shirt type"
    )
    parser.add_argument(
        "--accessory",
        type=str,
        choices=["none", "bowtie", "necklace", "scarf"],
        help="Specific accessory type"
    )
    parser.add_argument(
        "--list-options",
        action="store_true",
        help="List all available options and exit"
    )
    parser.add_argument(
        "--gif",
        action="store_true",
        help="Generate an animated GIF with multiple dinos"
    )
    
    args = parser.parse_args()
    
    gen = DinoGenerator(scale=args.scale)
    
    if args.list_options:
        print("Available options:")
        for key, values in gen.get_options().items():
            if key != "dino_colors":
                print(f"  {key}: {', '.join(values)}")
            else:
                print(f"  {key}: {len(values)} colors available")
        return 0
    
    kwargs = {}
    if args.hat:
        kwargs["hat"] = args.hat
    if args.glasses:
        kwargs["glasses"] = args.glasses
    if args.shirt:
        kwargs["shirt"] = args.shirt
    if args.accessory:
        kwargs["accessory"] = args.accessory
    
    if args.gif:
        # Generate animated GIF
        frames = [gen.generate(**kwargs) for _ in range(8)]
        output = Path(args.output).with_suffix('.gif')
        frames[0].save(
            output,
            save_all=True,
            append_images=frames[1:],
            duration=200,
            loop=0
        )
        print(f"Generated animated GIF: {output}")
    elif args.count > 1:
        # Generate multiple images
        base = Path(args.output).stem
        ext = Path(args.output).suffix or ".png"
        for i in range(args.count):
            img = gen.generate(**kwargs)
            out_path = f"{base}_{i+1}{ext}"
            img.save(out_path)
            print(f"Generated: {out_path}")
    else:
        # Generate single image
        img = gen.generate(**kwargs)
        img.save(args.output)
        print(f"Generated: {args.output}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
