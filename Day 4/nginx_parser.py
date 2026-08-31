import re
from collections import Counter


LOG_PATTERN = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)'       # capture IP
    r'.*?'                               # skip middle
    r'"(?P<method>\w+)\s+'               # capture method (GET, POST...)
    r'(?P<path>.*?)\s+.*?"\s+'           # capture path
    r'(?P<status>\d{3})'                 # capture status code
)

def analyze_logs(log_lines):
    ips=Counter()
    statuses=Counter()
    paths=Counter()

    for line in log_lines:
        match = LOG_PATTERN.search(line)

        if match:
            data = match.groupdict()
            ips[data['ip']] += 1
            statuses[data['status']] += 1
            paths[data['path']] += 1
        else:
            print(f"Invalid log line: {line}")



    print("\n📊 LOG ANALYSIS REPORT")

    print("─" * 40)
    print("\n🌐 Top 3 IPs:")
    for ip, count in ips.most_common(3):
        print(f"  {ip:15} → {count} requests")
    print("\n📋 Status Code Breakdown:")
    for status, count in statuses.most_common():
        icon = "✅" if status.startswith("2") else "❌"
        print(f"  {icon} {status} → {count} times")
    print("\n🔗 Top 3 Endpoints:")
    for path, count in paths.most_common(3):
        print(f"  {path} → {count} hits")



if __name__ == "__main__":
    sample = [
        '192.168.1.1 - - [25/Jan/2026:10:00:01] "GET /api/users HTTP/1.1" 200 1234',
        '192.168.1.2 - - [25/Jan/2026:10:00:02] "POST /api/login HTTP/1.1" 401 532',
        '192.168.1.1 - - [25/Jan/2026:10:00:03] "GET /api/users HTTP/1.1" 200 1234',
        '10.0.0.5    - - [25/Jan/2026:10:00:04] "GET /admin HTTP/1.1" 404 88',
        '192.168.1.1 - - [25/Jan/2026:10:00:05] "DELETE /api/user/5 HTTP/1.1" 200 0',
        'INVALID LINE WITHOUT LOG FORMAT',
    ]
    analyze_logs(sample)
