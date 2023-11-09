import numpy as np
import argparse


def create_waveform_file(max_samples, freq_factors, filename="waveform.awg", amplitude=32767, normalize=True, dc_mode=False):
	"""
	Generate a waveform file with a base sine wave, additional sine waves modulated on top, or a DC waveform.
	:param max_samples: Number of samples in the waveform
	:param freq_factors: List of frequency factors for modulation
	:param filename: Name of the output file
	:param amplitude: Peak value of the waveform (default: 32767)
	:param normalize: Flag to normalize the waveform (default: True)
	:param dc_mode: Flag to generate a DC waveform (default: False)
	:return: None
	"""

	if dc_mode:
		waveform = np.full(max_samples, amplitude, dtype=np.int16)
	else:
		base_freq = 1.0 / max_samples
		time_points = np.arange(max_samples)
		waveform = np.sin(2 * np.pi * base_freq * time_points)

		for factor in freq_factors:
			modulated_freq = factor / max_samples
			modulated_wave = np.sin(2 * np.pi * modulated_freq * time_points)
			waveform += modulated_wave

		if normalize:
			waveform = ((waveform - waveform.min()) / (waveform.max() - waveform.min())) * (2 * amplitude) - amplitude
		else:
			waveform = waveform * amplitude / max(waveform.max(), -waveform.min())

		waveform = waveform.astype(np.int16)

	with open(filename, 'wb' if filename.endswith('.bin') else 'w') as f:
		if filename.endswith('.bin'):
			f.write(waveform.tobytes())
		else:
			for value in waveform:
				f.write(f"{value}\n")

	print(f"Waveform written to {filename}")


def main():
	parser = argparse.ArgumentParser(description="Generate a waveform file.")
	parser.add_argument('max_samples', type=int, help='Number of samples in the waveform')
	parser.add_argument('freq_multipliers', type=lambda s: [float(item) for item in s.split(',')],
						help='List of frequency multipliers')
	parser.add_argument('--amplitude', type=int, default=32767, help='Peak value of the waveform (default: 32767)')
	parser.add_argument('-n', '--normalize', action='store_true', help='Normalize the waveform')
	parser.add_argument('--dc', action='store_true', help='Generate a DC waveform')

	args = parser.parse_args()

	filename = f"waveform_{args.max_samples}_{'_'.join(map(str, args.freq_multipliers))}.awg" if not args.dc else f"dc_waveform_{args.max_samples}.awg"
	create_waveform_file(args.max_samples, args.freq_multipliers, filename, args.amplitude, args.normalize, args.dc)


if __name__ == "__main__":
	main()
