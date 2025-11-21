"""
Create the final statistics meme by assembling all four panels.
Demonstrates selection bias through visual metaphor.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def create_statistics_meme(
    original_img: np.ndarray,
    stipple_img: np.ndarray,
    block_letter_img: np.ndarray,
    masked_stipple_img: np.ndarray,
    output_path: str,
    dpi: int = 150,
    background_color: str = "white"
) -> None:
    """
    Assemble all four panels into a professional-looking statistics meme.
    
    Parameters
    ----------
    original_img : np.ndarray
        Original grayscale image (Reality panel)
    stipple_img : np.ndarray
        Stippled image (Your Model panel)
    block_letter_img : np.ndarray
        Block letter image (Selection Bias panel)
    masked_stipple_img : np.ndarray
        Masked stippled image (Estimate panel)
    output_path : str
        Path to save the output PNG file
    dpi : int
        Resolution in dots per inch (default 150)
    background_color : str
        Background color for the meme (default "white")
    """
    # Ensure all images have the same shape
    shapes = [
        original_img.shape,
        stipple_img.shape,
        block_letter_img.shape,
        masked_stipple_img.shape
    ]
    
    if len(set(shapes)) > 1:
        print(f"Warning: Images have different shapes: {shapes}")
        # Use the first image's shape as reference
        target_shape = shapes[0]
        # Resize other images if needed (simple approach - just use what we have)
    
    # Create figure with 1 row, 4 columns
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    
    # Panel labels
    labels = ["Reality", "Your Model", "Selection Bias", "Estimate"]
    images = [original_img, stipple_img, block_letter_img, masked_stipple_img]
    
    # Plot each panel
    for i, (ax, img, label) in enumerate(zip(axes, images, labels)):
        ax.imshow(img, cmap='gray', vmin=0, vmax=1)
        ax.axis('off')
        ax.set_title(label, fontsize=14, fontweight='bold', pad=10)
    
    # Set background color
    fig.patch.set_facecolor(background_color)
    
    # Adjust layout with minimal spacing between panels
    plt.subplots_adjust(left=0.01, right=0.99, top=0.95, bottom=0.05, wspace=0.02)
    plt.tight_layout(pad=0.5)
    
    # Save the figure
    plt.savefig(output_path, dpi=dpi, bbox_inches='tight', facecolor=background_color)
    print(f"Saved statistics meme to: {output_path}")
    print(f"Image size: {fig.get_size_inches()}, DPI: {dpi}")
    
    # Close the figure to free memory
    plt.close(fig)

