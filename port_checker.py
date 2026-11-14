
import socket

print("=" * 40)
print("       PORT STATUS CHECKER")
print("=" * 40)

try:
    host = input("Enter hostname or IP address: ")
    port = int(input("Enter port number: "))

    if port < 1 or port > 65535:
        print("\nInvalid port number!")

    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)

        result = s.connect_ex((host, port))

        print("\n" + "-" * 40)
        print("Host:", host)
        print("Port:", port)

        if result == 0:
            print("Status: OPEN")
        else:
            print("Status: CLOSED")

        print("-" * 40)

        s.close()

except ValueError:
    print("Please enter a valid port number!")

except socket.gaierror:
    print("Invalid hostname or IP address!")

except socket.error:
    print("Network error occurred!")
