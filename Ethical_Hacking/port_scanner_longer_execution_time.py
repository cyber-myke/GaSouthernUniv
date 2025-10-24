import socket
import threading
import time

# Function to perform port scan on a given host and port range
def port_scan(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print("Port {} is open".format(port))
            open_ports.append(port)
        s.close()
    except Exception as e:
        exceptions.append(str(e))

# Function to perform port scan with threading
def threaded_port_scan(host, ports):
    threads = []
    for port in ports:
        t = threading.Thread(target=port_scan, args=(host, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    host = input("Enter the host or IP address to scan: ")
    start_time = time.time()
    start_date = time.strftime("%Y-%m-%d %H:%M:%S")

    open_ports = []
    exceptions = []

    # Define port range
    ports = range(1, 1027)

    # Perform threaded port scan
    threaded_port_scan(host, ports)

    end_time = time.time()
    end_date = time.strftime("%Y-%m-%d %H:%M:%S")

    total_time = end_time - start_time

    # Print open ports
    print("Open ports:", open_ports)

    # Print start and end time and start and end date
    print("Start Time:", start_date)
    print("End Time:", end_date)

    # Print total time of port scan
    print("Total Time:", total_time)

    # Write results to a text file
    with open("port_scan_results.txt", "w") as file:
        file.write("Start Time: {}\n".format(start_date))
        file.write("End Time: {}\n".format(end_date))
        file.write("Total Time: {} seconds\n\n".format(total_time))

        file.write("Open ports:\n")
        for port in open_ports:
            file.write("{}\n".format(port))

        file.write("\nExceptions:\n")
        for exception in exceptions:
            file.write("{}\n".format(exception))

    print("Results saved to port_scan_results.txt")
  
# Output
# Enter the host IP address: 8.8.8.8
# Scan completed. Open ports: [53, 443, 853]
# Total scan time: 0:00:21.178528 seconds

# Process finished with exit code 0
