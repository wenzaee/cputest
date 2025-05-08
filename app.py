# app.py
from flask import Flask
import time
import numpy as np
import os

app = Flask(__name__)

# 可配置参数（可通过环境变量调整）
MATRIX_SIZE = int(os.getenv('MATRIX_SIZE', 2500))  # 矩阵维度（默认1500x1500）
LOOP_COUNT = int(os.getenv('LOOP_COUNT', 8))       # 计算循环次数

@app.route('/')
def cpu_intensive_task():
    start = time.time()
    
    # 高强度矩阵运算（可根据需要调整参数）
    for _ in range(LOOP_COUNT):
        matrix = np.random.rand(MATRIX_SIZE, MATRIX_SIZE)
        np.linalg.svd(matrix)  # 奇异值分解
    
    duration = time.time() - start
    return f"CPU intensive task completed in {duration:.2f} seconds (Matrix: {MATRIX_SIZE}x{MATRIX_SIZE}, Loops: {LOOP_COUNT})\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)