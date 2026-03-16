Fourier Phase Scrambling for Visual Neuroscience
This repository contains a lightweight, interactive Python tool for generating Fourier Phase Scrambled images. It is designed specifically for Jupyter Notebook environments, providing a seamless workflow for researchers in computational vision and neuroscience.
 Developed with the assistance of AI to accelerate implementation and learning. 

 Neuroscience Context
In visual perception studies, it is crucial to control for low-level image properties. Phase scrambling allows researchers to:
• Preserve Amplitude Spectrum: Keep the spatial frequency and contrast energy of the original image.
• Randomize Phase Spectrum: Destroy the structural information (shapes, edges, and semantic meaning).
• Create Control Stimuli: Use scrambled images as a "baseline" to ensure neural responses (e.g., in fMRI or EEG) are due to object recognition rather than just low-level visual features.

Requirements
Ensure you have the following Python libraries installed:
pip install numpy matplotlib pillow

Usage (Jupyter Notebook)
1. Copy the Code: Open jupyter_scrambler.py and copy the entire script.
2. Run in Cell: Paste into a Jupyter cell and press Shift + Enter.
3. Interactive Input:
• A prompt will appear:  Please enter the image path:.
• Type your image name (e.g., 1.png) or drag and drop the file into the input box.
4. Result: A side-by-side comparison will be displayed immediately below the cell.
   
Implementation Details
The script follows a standard 2D Fourier Transform workflow:
1. 2D-FFT: Transition from the spatial domain to the frequency domain.
2. Magnitude Extraction: Capture the "energy" of the original stimulus.
3. Phase Randomization: Generate a noise-based phase matrix.
4. Inverse-FFT: Reconstruct the image into a "cloud-like" texture that is mathematically matched in energy to the original.
