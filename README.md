# ACC Non-Linear Properties Benchmark

This repository contains the **ACC (Adaptive Cruise Control) Non-Linear Properties Benchmark**, developed to serve as a verification benchmark for **VNN-COMP 2026**.

## Overview

This benchmark evaluates the safety verification of an Adaptive Cruise Control neural network against non-linear properties. It provides verification instances formulated in the **VNN-LIB 2.0** format, challenging verifiers to prove bounds on the output (relative acceleration) given constraints on the inputs (relative position and relative velocity).

The neural network under verification is `acc-2000000-64-64-64-64-retrain-100000-200000-0.9.onnx`, which processes the following:
- **Input (`X`):** `[1, 2]` - Contains the relative position (`rPos`) and relative velocity (`rVel`).
- **Output (`Y`):** `[1, 1]` - Contains the target relative acceleration (`rAccpost`).

## Verification Properties

The verification properties test whether the network's predicted acceleration is physically safe, utilizing complex non-linear SMT assertions. 
- **Input Constraints:** Defined by specific $\epsilon$-boxes of `rPos` and `rVel`, ensuring that it is physically possible to brake before a collision.
- **Output Constraints:** Verifies the predicted acceleration output `rAccpost` against non-linear safety limits.
- **VNN-COMP Timeout:** 100 seconds per instance.

## Project Structure

- `generate_properties.py`: The main script used to sample property boxes, generate VNN-LIB specifications, and output the `instances.csv` index file.
- `python_scripts/`: Contains the specific VNN-LIB 2.0 templates and logic.
- `onnx/`: Contains the ONNX model to be verified.
- `vnnlib/`: The target directory for the generated `.vnnlib` specifications.
- `instances.csv`: The required index of verification targets mapping the ONNX model and VNN-LIB spec with the standard timeout for VNN-COMP execution.

## Requirements

To run the instance generation script, you need a basic Python environment (no heavy dependencies are required for the script itself):
- `python >= 3.8`

To generate the instances, run:
```bash
python generate_properties.py <random_seed>
```

## Author

**Author:** Lukas Rohwer
