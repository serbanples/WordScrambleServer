import socket
import sys

def run_client(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_ip, server_port))
        print(f"Connected to server {server_ip}:{server_port}")

        scrambled_word = client_socket.recv(1024).decode()
        
        while True:
            print("Scrambled word received from server:", scrambled_word)

            response = input("Enter your guess: ")

            client_socket.send(response.encode())

            message = client_socket.recv(1024).decode()
            print("Server response:", message)

            if message == "Correct guess!":
                break
        
        client_socket.close()

    except KeyboardInterrupt:
        print("\nCTRL+C detected, closing the client...")
        client_socket.close()
    
    except socket.error as e:
        print("Connection error: %s" % e)
        sys.exit(1)

def main():
    server_ip = '127.0.0.1'
    server_port = 8080
    run_client(server_ip, server_port)

if __name__ == "__main__":
    main()
