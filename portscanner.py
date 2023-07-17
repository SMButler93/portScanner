from IPy import IP
import socket
import time


def check_ip(target):
    try:
        IP(target)
    except ValueError:
        return socket.gethostbyname(target)
    return target


def get_banner(s):
    return s.recv(1024).decode("utf-8").strip()


def port_scan(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        s.connect((target, port))

        try:
            banner = get_banner(s)
            print(f"[+] Open Port: {port} - {banner}")
        except:
            print(f"[+] Open Port: {port}")
    except:
        pass


def scan(target):
    converted_ip = check_ip(target)
    print(f"\nSCANNING TARGET: {target}")
    for port in range(1000):
        port_scan(converted_ip, port)


if __name__ == "__main__":
    target = input("[+] Please enter the target(s) you would like to scan: ")

    if "," in target:
        for ip in target.split(","):
            scan(ip.strip())

    else:
        scan(target.strip())
