# Adaptive Cruise Control Benchmark

## Overview
This repository contains the Adaptive Cruise Control (ACC) benchmark for the Verification of Neural Networks Competition (VNN-COMP). It features safety verification properties for an adaptive cruise control neural network. The properties include non-linear kinematic constraints and are defined using the VNN-LIB 2.0 format to evaluate the safety of the network's predictions.

## Prerequisites
- Python 3.x

## Usage Instructions
To generate the VNN-LIB properties and the benchmark instances CSV file, run the `generate_properties.py` script with a random seed:

```bash
python generate_properties.py <random_seed>
```

**Example:**
```bash
python generate_properties.py 42
```

This command will generate the corresponding VNN-LIB specification files inside the `vnnlib/` directory and update `instances.csv` with the ONNX model, VNN-LIB file path, and the per-instance verification timeout.

## Directory Structure
- `generate_properties.py`: Main script to generate VNN-LIB benchmark instances based on a specified random seed.
- `instances.csv`: A CSV file containing the benchmark instances (ONNX model path, VNN-LIB file path, and verification timeout).
- `onnx/`: Directory containing the pre-trained ONNX neural network models for adaptive cruise control.
- `python_scripts/`: Directory containing helper scripts (e.g., `create_specifications.py` which defines the VNN-LIB 2.0 templates and constraints).
- `vnnlib/`: Directory where the generated VNN-LIB 2.0 specification files are saved.
