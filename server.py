import random
import socket

words = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'car', 'telephone', 'laptop', 'house', 'lemon']

def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

def run_server(set_server_ip, set_server_port, backlog):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((set_server_ip, set_server_port))

    server_socket.listen(backlog)

    print("Server listening on {}:{}".format(set_server_ip, set_server_port))

    while True:
        
        client_socket, addr = server_socket.accept()
        print('Got connection from', addr)

        random_word = random.choice(words)
        scrambled_word = scramble_word(random_word)

        client_socket.send(scrambled_word.encode())

        while True:
            response = client_socket.recv(1024).decode()

            if response == random_word:
                client_socket.send("Correct guess!".encode())
                break
            else:
                client_socket.send("Incorrect guess! Try again.".encode())

        client_socket.close()

def main():
    server_ip = '127.0.0.1'
    server_port = 8080
    backlog = 5
    run_server(server_ip, server_port, backlog)

if __name__ == "__main__":
    main()
