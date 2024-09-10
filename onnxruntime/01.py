import onnxruntime as ort

a  = ort.get_available_providers()

for i in a:
    print(i)