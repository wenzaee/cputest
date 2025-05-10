import requests
import time
import argparse

# 配置参数
URL = "http://10.96.124.15:9001/"  # 要访问的URL

def get_average_response_time(url, interval, num_requests):
    times = []

    for i in range(num_requests):
        print(f"Sending request {i + 1} to {url}...")  # 输出请求提示信息
        start_time = time.time()  # 记录请求前的时间
        try:
            response = requests.get(url)  # 发送HTTP GET请求
            # 确保请求成功
            if response.status_code == 200:
                end_time = time.time()  # 记录请求后的时间
                elapsed_time = end_time - start_time  # 计算请求时间
                times.append(elapsed_time)
                print(f"Request {i + 1} completed in {elapsed_time:.2f} seconds")
            else:
                print(f"Request {i + 1} failed with status code {response.status_code}")
        except Exception as e:
            print(f"Request {i + 1} failed: {e}")
        
        time.sleep(interval)  # 等待下一次请求

    # 计算平均响应时间
    if times:
        avg_time = sum(times) / len(times)
        print(f"\nAverage Response Time: {avg_time:.2f} seconds")
    else:
        print("No valid requests to calculate average time.")

def main():
    # 设置命令行参数解析器
    parser = argparse.ArgumentParser(description="Get average response time from the URL.")
    
    # 添加 INTERVAL 和 NUM_REQUESTS 的命令行参数
    parser.add_argument("--interval", type=int, default=2, help="Interval between requests in seconds (default is 2s)")
    parser.add_argument("--num_requests", type=int, default=10, help="Number of requests to make (default is 10)")

    # 解析命令行参数
    args = parser.parse_args()

    # 调用函数获取平均响应时间
    get_average_response_time(URL, args.interval, args.num_requests)

if __name__ == "__main__":
    main()
