import json
data = '[{"host": "web1", "os": "ubuntu", "active": true}, {"host": "db1", "os": "centos", "active": false}]'

def process(json_data):
    servers = json.loads(json_data)

    active_ubuntu = [s["host"] for s in servers if s["os"] == "ubuntu" and s["active"]]

    print("Active Ubuntu Servers:", active_ubuntu)
if __name__ == "__main__":
    process(data)
    