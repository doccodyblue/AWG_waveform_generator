import numpy as np
import sys
import math


# Function to create waveform data

def create_waveform_file(max_samples, freq_factors, filename="waveform.awg"):
	"""
	Generate a waveform file with a base sine wave and additional sine waves modulated on top
	:param max_samples:
	:param freq_factors:
	:param filename:
	:return:
	"""

	# Ensure freq_factors is a list of integers or floats
	if not isinstance(freq_factors, list):
		raise ValueError("freq_factors must be a list of frequency factors.")

	# The base frequency (1 cycle within the sample size)
	base_freq = 1.0 / max_samples

	# Start the waveform with a base sine wave that has exactly max_samples
	time_points = np.arange(max_samples)
	waveform = np.sin(2 * np.pi * base_freq * time_points)

	# Add modulated sine waves on top of the base sine wave
	for factor in freq_factors:
		if factor == 0:
			# skip if factor 0 -> no modulation
			continue

		# Calculate the number of samples per cycle for the modulated wave
		modulated_samples_per_cycle = max_samples / factor
		# Ensure that the modulated wave is zero at the end of the sample set
		modulated_freq = math.floor(factor) / max_samples
		modulated_wave = np.sin(2 * np.pi * modulated_freq * time_points)
		waveform += modulated_wave

	# Normalize the waveform to fit in the range [-32768, 32767]
	waveform = ((waveform - waveform.min()) / (waveform.max() - waveform.min())) * (32767 + 32768) - 32768
	waveform = waveform.astype(np.int16)

	# Save to file, each value on a new line
	with open(filename, 'w') as f:
		for value in waveform:
			f.write(f"{value}\n")

	print(f"Waveform written to {filename}")


if __name__ == "__main__":
	# Parse command line arguments
	if len(sys.argv) < 3:
		print("Usage: python generate_waveform.py <max_samples> <freq_multiplier1,freq_multiplier2,...>")
		sys.exit(1)

	max_samples = int(sys.argv[1])
	freq_multipliers = list(map(float, sys.argv[2].split(',')))

	# Generate waveform file
	create_waveform_file(max_samples, freq_multipliers,
						 f"waveform_{max_samples}_{'_'.join(map(str, freq_multipliers))}.awg")
