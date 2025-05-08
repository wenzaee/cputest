# 使用 Python 3.9 slim 镜像
FROM python:3.9-slim

# 安装 Flask 和 NumPy
RUN pip install flask
RUN pip install numpy

# 将应用程序代码复制到容器中
COPY app.py /app.py

# 开放端口 9001，以便外部可以访问 Flask 应用
EXPOSE 9001

# 设置容器启动时执行的命令
CMD ["python", "/app.py"]
