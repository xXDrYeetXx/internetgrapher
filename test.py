import speedtest

# Initialize Speedtest
s = speedtest.Speedtest()

# Fetch all servers
s.get_servers()

# Pick your specific server by host
server_host = "speedtest-florida.hyperfiber.com"
server_list = s.servers  # dictionary of servers keyed by server ID
matching_servers = []

# Find servers that match the host
for servers in server_list.values():
    for server in servers:
        if server['host'].startswith(server_host):
            matching_servers.append(server)

if not matching_servers:
    print("Server not found. Using default best server.")
    best_server = s.get_best_server()
else:
    best_server = matching_servers[0]  # pick first matching server

print(f"Using server: {best_server['host']} ({best_server['sponsor']}, {best_server['country']})")

# Perform download test
try:
    download_speed = s.download(threads=1) / 1e6  # Convert to Mbps
    print(f"Download speed: {download_speed:.2f} Mbps")
except Exception as e:
    print("Speedtest failed:", e)
