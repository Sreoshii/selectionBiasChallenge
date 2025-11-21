"""
Step 4: Create a block letter matching image dimensions.
Generates a block letter (default "S") that can be used as a mask for selection bias.
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os


def create_block_letter_s(
    height: int,
    width: int,
    letter: str = "S",
    font_size_ratio: float = 0.9
) -> np.ndarray:
    """
    Create a block letter matching the image dimensions.
    
    Parameters
    ----------
    height : int
        Height of the output image in pixels
    width : int
        Width of the output image in pixels
    letter : str
        Letter to draw (default "S")
    font_size_ratio : float
        Ratio of font size to image size (default 0.9)
    
    Returns
    -------
    block_letter : np.ndarray
        2D numpy array (height, width) with values in [0, 1]
        where 0.0 = black (letter) and 1.0 = white (background)
    """
    # Create a white image
    img = Image.new('L', (width, height), color=255)
    draw = ImageDraw.Draw(img)
    
    # Calculate font size based on image dimensions
    # Use the smaller dimension to ensure the letter fits
    font_size = int(min(height, width) * font_size_ratio)
    
    # Try to find a suitable font
    font = None
    font_paths = [
        # Windows fonts
        "C:/Windows/Fonts/arialbd.ttf",  # Arial Bold
        "C:/Windows/Fonts/calibrib.ttf",  # Calibri Bold
        "C:/Windows/Fonts/impact.ttf",    # Impact
        "C:/Windows/Fonts/timesbd.ttf",   # Times Bold
        # macOS fonts
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/Library/Fonts/Arial Bold.ttf",
        # Linux fonts
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    
    # Try to load a font
    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                font = ImageFont.truetype(font_path, font_size)
                break
            except:
                continue
    
    # If no font found, use default font
    if font is None:
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            try:
                font = ImageFont.load_default()
            except:
                font = None
    
    # Get text bounding box to center it
    if font:
        bbox = draw.textbbox((0, 0), letter, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
    else:
        # Fallback: estimate text size
        text_width = font_size * 0.6
        text_height = font_size * 0.8
    
    # Center the text
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    
    # Draw the letter in black
    draw.text((x, y), letter, fill=0, font=font)
    
    # Convert to numpy array and normalize to [0, 1]
    # PIL uses 0-255, we want 0-1 where 0 = black, 1 = white
    block_letter = np.array(img, dtype=np.float32) / 255.0
    
    # Invert so that 0.0 = black (letter), 1.0 = white (background)
    # Actually, we want 0.0 for letter, 1.0 for background
    # PIL already has 0 for black, 255 for white, so after /255.0:
    # 0.0 = black (letter), 1.0 = white (background) - this is correct!
    
    print(f"Created block letter '{letter}' with size {block_letter.shape}")
    print(f"Letter pixels (black): {np.sum(block_letter < 0.5)}")
    print(f"Background pixels (white): {np.sum(block_letter >= 0.5)}")
    
    return block_letter

