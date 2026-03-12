import os
import argparse
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def fourier_phase_scramble(img_array: np.ndarray) -> np.ndarray:
    """
    Performs Fourier Phase Scrambling on a 2D image array.
    This preserves the amplitude spectrum (spatial frequency energy) 
    while randomizing the phase spectrum (structural information).
    
    Args:
        img_array (np.ndarray): 2D numpy array representing a grayscale image.
        
    Returns:
        np.ndarray: The phase-scrambled image array (uint8).
    """
    # 1. Perform 2D Fast Fourier Transform (FFT)
    fft_img = np.fft.fft2(img_array)

    # 2. Extract the magnitude spectrum
    magnitude = np.abs(fft_img)

    # 3. Generate random phase using white noise
    # Generating a random noise image and taking its phase ensures 
    # the proper symmetry required for the inverse FFT to yield real numbers.
    noise = np.random.rand(*img_array.shape)
    noise_fft = np.fft.fft2(noise)
    random_phase = np.angle(noise_fft)

    # 4. Combine original magnitude with the new random phase
    scrambled_fft = magnitude * np.exp(1j * random_phase)

    # 5. Perform Inverse 2D FFT to convert back to spatial domain
    scrambled_img = np.fft.ifft2(scrambled_fft)
    
    # Take the real part to eliminate negligible imaginary floating-point errors
    scrambled_img = np.real(scrambled_img) 

    # 6. Normalize pixel values to 0-255 range
    img_min = np.min(scrambled_img)
    img_max = np.max(scrambled_img)
    if img_max > img_min:
        scrambled_img = (scrambled_img - img_min) / (img_max - img_min) * 255.0
        
    return scrambled_img.astype(np.uint8)


def main():
    # Setup command-line arguments
    parser = argparse.ArgumentParser(description="Fourier Phase Scrambling Tool (SHINE-like)")
    parser.add_argument('-i', '--input', type=str, required=True, 
                        help="Path to the input image file")
    parser.add_argument('-o', '--output', type=str, default='scrambled_output.png', 
                        help="Path to save the scrambled image (default: scrambled_output.png)")
    parser.add_argument('--show', action='store_true', 
                        help="Display a side-by-side before/after comparison")
    
    args = parser.parse_args()

    # Check if input file exists
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' not found.")
        return

    # Load image and convert to grayscale (Standard procedure for phase scrambling)
    try:
        img = Image.open(args.input).convert('L')
    except Exception as e:
        print(f"Error loading image: {e}")
        return

    img_array = np.array(img)
    
    print("Scrambling image phase...")
    scrambled_array = fourier_phase_scramble(img_array)
    
    # Save the scrambled image
    out_img = Image.fromarray(scrambled_array)
    out_img.save(args.output)
    print(f"Success! Scrambled image saved to '{args.output}'")

    # Display comparison if requested
    if args.show:
        plt.figure(figsize=(10, 5))
        
        plt.subplot(1, 2, 1)
        plt.title("Original Image")
        plt.imshow(img_array, cmap='gray')
        plt.axis('off')
        
        plt.subplot(1, 2, 2)
        plt.title("Phase Scrambled")
        plt.imshow(scrambled_array, cmap='gray')
        plt.axis('off')
        
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    main()
