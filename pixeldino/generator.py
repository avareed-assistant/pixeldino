"""
Pixel Dinosaur Generator - Cute Front-Facing Style
"""

import random
from PIL import Image, ImageDraw

# Dino base colors (main, light highlight, dark shadow)
DINO_PALETTES = [
    {"main": (219, 112, 219), "light": (255, 182, 255), "dark": (153, 50, 153)},  # Pink/purple like reference
    {"main": (76, 175, 80), "light": (129, 199, 132), "dark": (46, 125, 50)},      # Green
    {"main": (255, 152, 0), "light": (255, 193, 7), "dark": (230, 81, 0)},         # Orange
    {"main": (33, 150, 243), "light": (100, 181, 246), "dark": (21, 101, 192)},    # Blue
    {"main": (156, 39, 176), "light": (186, 104, 200), "dark": (106, 27, 154)},    # Purple
    {"main": (0, 188, 212), "light": (77, 208, 225), "dark": (0, 131, 143)},       # Cyan
    {"main": (244, 67, 54), "light": (229, 115, 115), "dark": (183, 28, 28)},      # Red
    {"main": (255, 235, 59), "light": (255, 245, 157), "dark": (251, 192, 45)},    # Yellow
]

HAT_PALETTES = [
    {"main": (244, 67, 54), "light": (255, 138, 128), "dark": (183, 28, 28)},      # Red
    {"main": (33, 150, 243), "light": (100, 181, 246), "dark": (21, 101, 192)},    # Blue
    {"main": (76, 175, 80), "light": (129, 199, 132), "dark": (46, 125, 50)},      # Green
    {"main": (156, 39, 176), "light": (186, 104, 200), "dark": (106, 27, 154)},    # Purple
    {"main": (255, 193, 7), "light": (255, 224, 130), "dark": (255, 143, 0)},      # Gold
    {"main": (50, 50, 50), "light": (97, 97, 97), "dark": (0, 0, 0)},              # Black
]

# Front-facing cute dino sprite (24x24 grid)
# 0 = transparent, 1 = main color, 2 = light/highlight, 3 = dark/shadow
BASE_DINO_FRONT = [
    # Row 0-3: Top of head with little horns/bumps
    [0,0,0,0,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,1,2,0,0,2,1,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,2,1,1,1,1,1,1,2,2,0,0,0,0,0,0,0],
    # Row 4-7: Head
    [0,0,0,0,0,0,2,2,1,1,1,1,1,1,1,1,2,2,0,0,0,0,0,0],
    [0,0,0,0,0,2,2,1,1,1,1,1,1,1,1,1,1,2,2,0,0,0,0,0],
    [0,0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0,0,0],
    [0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0,0],
    # Row 8-9: Eyes row
    [0,0,0,0,2,1,1,4,4,4,1,1,1,1,4,4,4,1,1,2,0,0,0,0],  # 4 = eye white
    [0,0,0,0,2,1,1,4,5,4,1,1,1,1,4,5,4,1,1,2,0,0,0,0],  # 5 = pupil
    # Row 10-11: Cheeks/lower face
    [0,0,0,0,2,1,1,4,4,4,1,1,1,1,4,4,4,1,1,2,0,0,0,0],
    [0,0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0,0,0],
    # Row 12-13: Snout/mouth
    [0,0,0,0,0,2,1,1,1,1,1,3,3,1,1,1,1,1,2,0,0,0,0,0],
    [0,0,0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,2,0,0,0,0,0,0],
    # Row 14-15: Neck
    [0,0,0,0,0,0,0,2,1,1,1,1,1,1,1,1,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,1,1,1,1,1,1,2,0,0,0,0,0,0,0,0],
    # Row 16-17: Body top with arms
    [0,0,0,0,2,1,1,2,2,1,1,1,1,1,1,2,2,1,1,2,0,0,0,0],
    [0,0,0,2,1,1,3,0,2,1,1,1,1,1,1,2,0,3,1,1,2,0,0,0],
    # Row 18-19: Body middle
    [0,0,0,0,2,3,0,0,0,2,1,1,1,1,2,0,0,0,3,2,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,1,1,1,1,1,1,2,0,0,0,0,0,0,0,0],
    # Row 20-21: Body lower / belly
    [0,0,0,0,0,0,0,2,1,1,1,2,2,1,1,1,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,1,1,2,2,2,2,1,1,2,0,0,0,0,0,0,0],
    # Row 22-23: Feet
    [0,0,0,0,0,0,2,1,1,3,0,0,0,0,3,1,1,2,0,0,0,0,0,0],
    [0,0,0,0,0,0,2,3,3,0,0,0,0,0,0,3,3,2,0,0,0,0,0,0],
]

# Hat patterns (y_offset from top, pixels as (x, y, color_type))
# color_type: 1=main, 2=light, 3=dark
HATS = {
    "none": [],
    "party_hat": {
        "offset": -5,
        "pixels": [
            (11, 0, 2), (12, 0, 2),
            (10, 1, 1), (11, 1, 1), (12, 1, 1), (13, 1, 1),
            (9, 2, 1), (10, 2, 1), (11, 2, 1), (12, 2, 1), (13, 2, 1), (14, 2, 1),
            (8, 3, 3), (9, 3, 1), (10, 3, 1), (11, 3, 1), (12, 3, 1), (13, 3, 1), (14, 3, 1), (15, 3, 3),
            (8, 4, 3), (9, 4, 2), (10, 4, 2), (11, 4, 2), (12, 4, 2), (13, 4, 2), (14, 4, 2), (15, 4, 3),
        ]
    },
    "top_hat": {
        "offset": -6,
        "pixels": [
            (9, 0, 1), (10, 0, 1), (11, 0, 1), (12, 0, 1), (13, 0, 1), (14, 0, 1),
            (9, 1, 1), (10, 1, 2), (11, 1, 2), (12, 1, 2), (13, 1, 2), (14, 1, 1),
            (9, 2, 1), (10, 2, 2), (11, 2, 2), (12, 2, 2), (13, 2, 2), (14, 2, 1),
            (9, 3, 1), (10, 3, 1), (11, 3, 1), (12, 3, 1), (13, 3, 1), (14, 3, 1),
            (9, 4, 3), (10, 4, 3), (11, 4, 3), (12, 4, 3), (13, 4, 3), (14, 4, 3),
            (7, 5, 3), (8, 5, 1), (9, 5, 1), (10, 5, 1), (11, 5, 1), (12, 5, 1), (13, 5, 1), (14, 5, 1), (15, 5, 1), (16, 5, 3),
        ]
    },
    "crown": {
        "offset": -3,
        "pixels": [
            (8, 0, 2), (11, 0, 2), (12, 0, 2), (15, 0, 2),
            (8, 1, 1), (9, 1, 2), (10, 1, 1), (11, 1, 1), (12, 1, 1), (13, 1, 1), (14, 1, 2), (15, 1, 1),
            (8, 2, 3), (9, 2, 1), (10, 2, 1), (11, 2, 1), (12, 2, 1), (13, 2, 1), (14, 2, 1), (15, 2, 3),
        ]
    },
    "beanie": {
        "offset": -3,
        "pixels": [
            (11, 0, 2), (12, 0, 2),
            (9, 1, 2), (10, 1, 1), (11, 1, 1), (12, 1, 1), (13, 1, 1), (14, 1, 2),
            (8, 2, 3), (9, 2, 1), (10, 2, 1), (11, 2, 1), (12, 2, 1), (13, 2, 1), (14, 2, 1), (15, 2, 3),
        ]
    },
    "cap": {
        "offset": -2,
        "pixels": [
            (8, 0, 1), (9, 0, 1), (10, 0, 1), (11, 0, 1), (12, 0, 1), (13, 0, 1), (14, 0, 1), (15, 0, 1),
            (6, 1, 3), (7, 1, 3), (8, 1, 3), (9, 1, 1), (10, 1, 1), (11, 1, 1), (12, 1, 1), (13, 1, 1), (14, 1, 1), (15, 1, 3),
        ]
    },
}

GLASSES = {
    "none": [],
    "sunglasses": {
        "row": 9,
        "pixels": [
            (6, 0, "black"), (7, 0, "black"), (8, 0, "black"), (9, 0, "black"), (10, 0, "black"),
            (11, 0, "frame"), (12, 0, "frame"),
            (13, 0, "black"), (14, 0, "black"), (15, 0, "black"), (16, 0, "black"), (17, 0, "black"),
        ]
    },
    "round_glasses": {
        "row": 9,
        "pixels": [
            (6, 0, "frame"), (7, 0, "lens"), (8, 0, "lens"), (9, 0, "frame"),
            (10, 0, "frame"), (11, 0, "frame"), (12, 0, "frame"), (13, 0, "frame"),
            (14, 0, "lens"), (15, 0, "lens"), (16, 0, "frame"),
        ]
    },
}

ACCESSORIES = {
    "none": [],
    "bowtie": {
        "row": 15,
        "pixels": [
            (9, 0, 1), (10, 0, 2), (11, 0, 1), (12, 0, 1), (13, 0, 2), (14, 0, 1),
            (10, 1, 1), (11, 1, 3), (12, 1, 3), (13, 1, 1),
        ]
    },
    "scarf": {
        "row": 14,
        "pixels": [
            (7, 0, 1), (8, 0, 2), (9, 0, 1), (10, 0, 1), (11, 0, 1), (12, 0, 1), (13, 0, 1), (14, 0, 2), (15, 0, 1), (16, 0, 1),
            (7, 1, 3), (8, 1, 1), (15, 1, 1), (16, 1, 3),
            (7, 2, 1), (8, 2, 3),
        ]
    },
}


class DinoGenerator:
    """Generate cute front-facing pixel dinosaurs"""
    
    def __init__(self, scale: int = 10):
        self.scale = scale
        self.grid_size = 24
        
    def generate(
        self,
        dino_palette: dict = None,
        hat: str = None,
        glasses: str = None,
        accessory: str = None,
        background_color: tuple = None,
    ) -> Image.Image:
        
        if dino_palette is None:
            dino_palette = random.choice(DINO_PALETTES)
        if hat is None:
            hat = random.choice(list(HATS.keys()))
        if glasses is None:
            glasses = random.choice(list(GLASSES.keys()))
        if accessory is None:
            accessory = random.choice(list(ACCESSORIES.keys()))
            
        hat_palette = random.choice(HAT_PALETTES)
        accessory_palette = random.choice(HAT_PALETTES)
        
        # Create image
        size = self.grid_size * self.scale
        if background_color:
            img = Image.new('RGBA', (size, size), background_color + (255,))
        else:
            img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        
        draw = ImageDraw.Draw(img)
        
        # Color mapping for dino
        color_map = {
            1: dino_palette["main"],
            2: dino_palette["light"],
            3: dino_palette["dark"],
            4: (255, 255, 255),  # Eye white
            5: (20, 20, 20),     # Pupil
        }
        
        # Draw base dinosaur
        for y, row in enumerate(BASE_DINO_FRONT):
            for x, pixel in enumerate(row):
                if pixel != 0:
                    color = color_map.get(pixel, dino_palette["main"])
                    self._draw_pixel(draw, x, y, color)
        
        # Draw hat
        if hat != "none" and hat in HATS:
            hat_data = HATS[hat]
            hat_colors = {
                1: hat_palette["main"],
                2: hat_palette["light"],
                3: hat_palette["dark"],
            }
            y_off = hat_data["offset"]
            for px, py, ct in hat_data["pixels"]:
                self._draw_pixel(draw, px, py + 3 + y_off, hat_colors.get(ct, hat_palette["main"]))
        
        # Draw glasses
        if glasses != "none" and glasses in GLASSES:
            glass_data = GLASSES[glasses]
            base_row = glass_data["row"]
            for px, py, ct in glass_data["pixels"]:
                if ct == "black":
                    color = (20, 20, 20)
                elif ct == "frame":
                    color = (60, 60, 60)
                elif ct == "lens":
                    color = (180, 220, 255)
                else:
                    color = (20, 20, 20)
                self._draw_pixel(draw, px, base_row + py, color)
        
        # Draw accessory
        if accessory != "none" and accessory in ACCESSORIES:
            acc_data = ACCESSORIES[accessory]
            acc_colors = {
                1: accessory_palette["main"],
                2: accessory_palette["light"],
                3: accessory_palette["dark"],
            }
            base_row = acc_data["row"]
            for px, py, ct in acc_data["pixels"]:
                self._draw_pixel(draw, px, base_row + py, acc_colors.get(ct, accessory_palette["main"]))
        
        return img
    
    def _draw_pixel(self, draw: ImageDraw, x: int, y: int, color: tuple):
        if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
            px = x * self.scale
            py = y * self.scale
            draw.rectangle([px, py, px + self.scale - 1, py + self.scale - 1], fill=color)
    
    def generate_batch(self, count: int) -> list:
        return [self.generate() for _ in range(count)]
    
    def get_options(self) -> dict:
        return {
            "hats": list(HATS.keys()),
            "glasses": list(GLASSES.keys()),
            "accessories": list(ACCESSORIES.keys()),
            "palettes": len(DINO_PALETTES),
        }


def generate_dino(output_path: str = None, scale: int = 10, **kwargs) -> Image.Image:
    gen = DinoGenerator(scale=scale)
    img = gen.generate(**kwargs)
    if output_path:
        img.save(output_path)
    return img


if __name__ == "__main__":
    img = generate_dino("sample_dino.png", scale=10)
    print("Generated sample_dino.png")
