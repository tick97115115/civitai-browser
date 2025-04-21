import os

# 打印 PYTHONPATH（如果不存在则返回 None 或报错）
pythonpath = os.environ.get("PYTHONPATH")
print("PYTHONPATH:", pythonpath)