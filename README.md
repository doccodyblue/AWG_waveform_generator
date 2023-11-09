# AWG Waveform Generator for Picoscope 2000a and Other AWGs

## Overview
This AWG Waveform Generator is a Python tool designed to create waveform files specifically tailored for Arbitrary Waveform Generators (AWGs), including but not limited to the Picoscope 2000a series. It enables users to generate custom waveform files with a base sine wave and additional sine waves modulated on top, which can be used for a variety of signal generation purposes.

## Features
- Generate a waveform file containing a base sine wave with modulated sine waves on top.
- Customizable frequency factors to create complex signal patterns.
- Waveform normalization to fit the data within the 16-bit integer range used by most AWGs.
- Command-line interface for easy integration with scripts and automated processes.

## Requirements
- Python 3.x
- NumPy library

## Installation
No installation is needed. Simply clone the repository or download the `generate_waveform.py` script.


## Usage
Run the script from the command line. You can specify the number of samples, frequency multipliers, and whether to normalize the waveform or generate a DC waveform.

### Command Line Syntax:
*python generate_waveform.py <max_samples> <freq_multiplier1,freq_multiplier2,...> [--normalize] [--dc]*

### Examples:
- Generate a modulated waveform:
  *python generate_waveform.py 32000 2.5,3.75*
  This command creates a waveform file with 32000 samples with frequency factors of 2.5 and 3.75.

- Generate a DC waveform:
  *python generate_waveform.py 32000 --dc*
  This command creates a DC waveform with 32000 samples.

- Generate a normalized waveform:
  *python generate_waveform.py 32000 2.5,3.75 --normalize*
  This generates a normalized waveform with the specified frequency factors.

## Output
The script generates a waveform file named following the pattern `waveform_<max_samples>_<freq_multiplier1>_<freq_multiplier2>... .awg` for modulated waveforms or `dc_waveform_<max_samples>.awg` for DC waveforms. Each sample is a 16-bit integer value, either on a new line or as binary data.

## Contributing
Contributions to improve the AWG Waveform Generator are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

