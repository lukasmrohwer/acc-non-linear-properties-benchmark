import csv
from python_scripts.create_specifications import vnnlib_template_2

# create VNN-LIB 2.0 files given the following:
VNN_COMP_TIMEOUT = 100  # per-instance verification timeout
ONNX_MODEL_PATH = "onnx/acc-2000000-64-64-64-64-retrain-100000-200000-0.9.onnx"

instance_data = []

lines = vnnlib_template_2()

vnnlib_filename = "vnnlib/instance_1.vnnlib2"
with open(vnnlib_filename, "w") as f:
    f.writelines(line + "\n" for line in lines)

instance = [ONNX_MODEL_PATH, vnnlib_filename, VNN_COMP_TIMEOUT]
instance_data.append(instance)

# save the ONNX/VNN-LIB instance pairs in the required CSV
with open(f"instances.csv", 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(instance_data)