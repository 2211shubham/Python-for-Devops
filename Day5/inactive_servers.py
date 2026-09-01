# inactive_servers.py
import json

data = '''[
    {"host": "web1",   "os": "ubuntu", "active": true},
    {"host": "web2",   "os": "ubuntu", "active": false},
    {"host": "db1",    "os": "centos", "active": true},
    {"host": "db2",    "os": "centos", "active": false},
    {"host": "cache1", "os": "debian", "active": false}
]'''

def get_inactive_servers(json_data):
    """Return list of hostnames where active is False."""
    servers = json.loads(json_data)

    # List comprehension: keep only inactive servers
    inactive = [s['host'] for s in servers if not s['active']]

    return inactive


if __name__ == "__main__":
    result = get_inactive_servers(data)
    print("Inactive Servers:", result)
    # Inactive Servers: ['web2', 'db2', 'cache1']