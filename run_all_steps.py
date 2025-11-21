"""
Run all steps of the selection bias challenge to generate the final meme.
"""

import numpy as np
import matplotlib.pyplot as plt
from step1_prepare_image import prepare_image
from step2_create_stipple import create_stipple
from step3_create_tonal import create_tonal
from step4_create_block_letter import create_block_letter_s
from step5_create_masked import create_masked_stipple
from create_meme import create_statistics_meme

print("=" * 60)
print("Selection Bias Challenge - Running All Steps")
print("=" * 60)

# Step 1: Prepare Image
print("\n[Step 1] Preparing image...")
img_path = 'My_Image.jpg'
gray_image = prepare_image(img_path, max_size=512)
print(f"[OK] Step 1 complete. Image shape: {gray_image.shape}")

# Step 2: Create Stippled Image
print("\n[Step 2] Creating stippled image...")
stipple_pattern, samples = create_stipple(
    gray_image,
    percentage=0.08,
    sigma=0.9,
    content_bias=0.9,
    noise_scale_factor=0.1,
    extreme_downweight=0.5,
    extreme_threshold_low=0.2,
    extreme_threshold_high=0.8,
    extreme_sigma=0.1
)
print(f"[OK] Step 2 complete. Generated {len(samples)} stipple points")

# Step 3: Create Tonal Analysis (Optional but recommended)
print("\n[Step 3] Creating tonal analysis...")
grid_rows = 16
grid_cols = 12
tonal_image, average_tones, tonal_stats = create_tonal(
    gray_image,
    grid_rows=grid_rows,
    grid_cols=grid_cols,
    return_full_image=True
)
print(f"[OK] Step 3 complete. Mean brightness: {tonal_stats['mean']:.3f}")

# Step 4: Create Block Letter
print("\n[Step 4] Creating block letter S...")
h, w = gray_image.shape
block_letter = create_block_letter_s(h, w, letter="S", font_size_ratio=0.9)
print(f"[OK] Step 4 complete. Block letter shape: {block_letter.shape}")

# Step 5: Create Masked Image
print("\n[Step 5] Creating masked stippled image...")
masked_stipple = create_masked_stipple(
    stipple_pattern,
    block_letter,
    threshold=0.5
)
print(f"[OK] Step 5 complete. Masked image shape: {masked_stipple.shape}")

# Final: Create Meme
print("\n[Final] Creating statistics meme...")
create_statistics_meme(
    original_img=gray_image,
    stipple_img=stipple_pattern,
    block_letter_img=block_letter,
    masked_stipple_img=masked_stipple,
    output_path="my_statistics_meme.png",
    dpi=150,
    background_color="white"
)
print(f"[OK] Final meme created: my_statistics_meme.png")

print("\n" + "=" * 60)
print("All steps completed successfully!")
print("=" * 60)

