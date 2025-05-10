from flask import Flask, jsonify
import time
import numpy as np
import os
from concurrent.futures import ProcessPoolExecutor

app = Flask(__name__)

# 可配置参数（可通过环境变量调整）
MATRIX_SIZE = int(os.getenv('MATRIX_SIZE', 2500))  # 矩阵维度（默认2500x2500）
LOOP_COUNT = int(os.getenv('LOOP_COUNT', 2))       # 计算循环次数

# 创建进程池（每次请求都启动一个新进程来计算）
executor = ProcessPoolExecutor(max_workers=1)

def cpu_intensive_calculation():
    """执行高强度矩阵运算"""
    for _ in range(LOOP_COUNT):
        matrix = np.random.rand(MATRIX_SIZE, MATRIX_SIZE)
        np.linalg.svd(matrix)  # 奇异值分解

@app.route('/')
def cpu_intensive_task():
    start = time.time()

    # 提交任务到进程池，每次请求启动一个新进程
    future = executor.submit(cpu_intensive_calculation)
    
    # 等待进程完成
    future.result()

    duration = time.time() - start

    # 返回 JSON 格式的响应
    response = {
        "time_taken": f"{duration:.2f} seconds",  # 时间部分
        "message": f"CPU intensive task completed (Matrix: {MATRIX_SIZE}x{MATRIX_SIZE}, Loops: {LOOP_COUNT})"  # 消息部分
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)
