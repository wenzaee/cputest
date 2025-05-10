import requests
import time
import argparse
from concurrent.futures import ThreadPoolExecutor

URL = "http://10.96.124.15:12345/"

def send_request(url, request_id):
    """发送单个请求并返回响应时间"""
    print(f"[Request {request_id}] Sending request to {url}...")
    
    start_time = time.time()
    try:
        response = requests.get(url)
        if response.status_code == 200:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"[Request {request_id}] Completed in {elapsed_time:.2f} seconds")
            return elapsed_time
        else:
            print(f"[Request {request_id}] Failed with status code {response.status_code}")
            return None
    except Exception as e:
        print(f"[Request {request_id}] Failed: {e}")
        return None

def get_average_response_time(url, interval, num_requests):
    """使用并发处理请求并计算平均响应时间"""
    times = []

    # 使用 ThreadPoolExecutor 来并发发送请求
    with ThreadPoolExecutor() as executor:
        # 提交任务到线程池
        futures = []
        for i in range(num_requests):
            # 等待 interval 秒再提交下一个请求
            time.sleep(interval)
            future = executor.submit(send_request, url, i+1)  # 提交任务
            futures.append(future)

        # 收集所有任务的结果
        for future in futures:
            result = future.result()  # 阻塞等待每个请求的结果
            if result is not None:
                times.append(result)

    # 计算平均响应时间
    if times:
        avg_time = sum(times) / len(times)
        print(f"\nAverage Response Time: {avg_time:.2f} seconds")
    else:
        print("No valid requests to calculate average time.")

def main():
    parser = argparse.ArgumentParser(description="Send HTTP requests with interval control.")
    parser.add_argument("--interval", type=int, default=10, help="Interval between requests in seconds (default is 2s)")
    parser.add_argument("--num_requests", type=int, default=10, help="Number of requests to make (default is 10)")
    args = parser.parse_args()
    get_average_response_time(URL, args.interval, args.num_requests)

if __name__ == "__main__":
    main()
