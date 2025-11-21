"""
Step 5: Create a masked stippled image by applying the block letter mask.
This demonstrates selection bias by systematically removing data points.
"""

import numpy as np


def create_masked_stipple(
    stipple_img: np.ndarray,
    mask_img: np.ndarray,
    threshold: float = 0.5
) -> np.ndarray:
    """
    Apply the block letter mask to the stippled image.
    Where the mask is dark (below threshold), remove stipples (set to white).
    Where the mask is light (above threshold), keep the stipples as they are.
    
    Parameters
    ----------
    stipple_img : np.ndarray
        Stippled image as 2D array (height, width) with values in [0, 1]
        where 0.0 = black dot, 1.0 = white background
    mask_img : np.ndarray
        Mask image as 2D array (height, width) with values in [0, 1]
        where 0.0 = black (mask area), 1.0 = white (keep area)
    threshold : float
        Threshold value. Pixels in mask_img below this value are considered
        part of the mask (will remove stipples). Default 0.5.
    
    Returns
    -------
    masked_stipple : np.ndarray
        2D numpy array with the same shape as input images
        Stipples are removed (set to white) where mask is dark
    """
    # Ensure images have the same shape
    if stipple_img.shape != mask_img.shape:
        raise ValueError(
            f"Image shapes must match: stipple_img {stipple_img.shape} != mask_img {mask_img.shape}"
        )
    
    # Create a copy of the stippled image
    masked_stipple = stipple_img.copy()
    
    # Where mask is dark (below threshold), remove stipples (set to white/1.0)
    # Where mask is light (above threshold), keep stipples as they are
    mask_region = mask_img < threshold
    masked_stipple[mask_region] = 1.0  # Set to white (remove stipples)
    
    # Count statistics
    removed_pixels = np.sum(mask_region)
    removed_stipples = np.sum(mask_region & (stipple_img < 0.5))  # Were black dots
    
    print(f"Applied mask with threshold {threshold}")
    print(f"Mask region pixels: {removed_pixels} ({100*removed_pixels/mask_img.size:.1f}%)")
    print(f"Stipples removed: {removed_stipples}")
    print(f"Remaining stipples: {np.sum(masked_stipple < 0.5)}")
    
    return masked_stipple

