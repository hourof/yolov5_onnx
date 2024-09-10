import onnxruntime as ort

#查看有什么可以用得推理框架
#一般是没有dml推理得,要是下载可以采用 pip install onnxruntime-directml  命令
a  = ort.get_available_providers()

for i in a:
    print(i)
