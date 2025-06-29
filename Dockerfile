FROM ubuntu:latest
LABEL authors="26021"

# 使用官方的 Python 基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到容器的工作目录中
COPY . .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt \
    -i https://pypi.tuna.tsinghua.edu.cn/simple \
    --trusted-host pypi.tuna.tsinghua.edu.cn

# 暴露端口（假设你的 Flask 应用运行在 5000 端口）
EXPOSE 5000

# 运行应用程序
CMD ["python", "app.py"]