import csv
import sys

class Request:
    def __init__(self, timestamp, file, processing_time):
        self.timestamp = timestamp
        self.file = file
        self.processing_time = processing_time
        self.start_time = None

class Server:
    def __init__(self):
        self.queue = []
        self.current_request = None

    def tick(self, current_time):
        if not self.current_request and self.queue:
            self.current_request = self.queue.pop(0)
            self.current_request.start_time = current_time
        if self.current_request:
            self.current_request.processing_time -= 1
            if self.current_request.processing_time <= 0:
                self.current_request = None

def read_requests(filename):
    requests = []
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            timestamp, file, processing_time = int(row[0]), row[1], int(row[2])
            requests.append(Request(timestamp, file, processing_time))
    return requests

def simulateOneServer(filename):
    requests = read_requests(filename)
    server = Server()
    time = 0
    wait_times = []

    while requests or server.queue or server.current_request:
        for r in requests[:]:
            if r.timestamp == time:
                server.queue.append(r)
                requests.remove(r)
        server.tick(time)
        if server.current_request and server.current_request.start_time == time:
            wait_times.append(time - server.current_request.timestamp)
        time += 1

    avg_wait = sum(wait_times) / len(wait_times) if wait_times else 0
    print(f"Average wait time (1 server): {avg_wait:.2f} seconds")
    return avg_wait

def simulateManyServers(filename, n_servers):
    requests = read_requests(filename)
    servers = [Server() for _ in range(n_servers)]
    time = 0
    wait_times = []
    server_index = 0

    while requests or any(s.queue or s.current_request for s in servers):
        for r in requests[:]:
            if r.timestamp == time:
                servers[server_index].queue.append(r)
                server_index = (server_index + 1) % n_servers
                requests.remove(r)
        for s in servers:
            s.tick(time)
            if s.current_request and s.current_request.start_time == time:
                wait_times.append(time - s.current_request.timestamp)
        time += 1

    avg_wait = sum(wait_times) / len(wait_times) if wait_times else 0
    print(f"Average wait time ({n_servers} servers): {avg_wait:.2f} seconds")
    return avg_wait

def main():
    if len(sys.argv) < 2:
        print("Usage: python simulation.py <file> [servers]")
        return
    filename = sys.argv[1]
    if len(sys.argv) == 3:
        servers = int(sys.argv[2])
        simulateManyServers(filename, servers)
    else:
        simulateOneServer(filename)

if __name__ == "__main__":
    main()
