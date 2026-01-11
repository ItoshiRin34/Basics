#!/usr/bin/env python3
# Banner Grabbing para aplicações WEB (HTTP)
# Uso educacional e em ambientes autorizados

import socket
import sys

TIMEOUT = 3
MAX_BYTES = 8192

def grab_http_banner(host, port=80):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)
    s.connect((host, port))

    request = (
        f"HEAD / HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"User-Agent: banner-grab-study\r\n"
        f"Connection: close\r\n\r\n"
    )

    s.sendall(request.encode())
    response = s.recv(MAX_BYTES).decode(errors="ignore")
    s.close()

    headers = response.split("\r\n\r\n")[0]
    return headers

def main():
    if len(sys.argv) != 2:
        print("Uso:")
        print("  python3 banner_web.py <host>")
        print("Exemplo:")
        print("  python3 banner_web.py 127.0.0.1")
        sys.exit(1)

    host = sys.argv[1]

    try:
        banner = grab_http_banner(host)
        print("=== HEADERS HTTP ===")
        print(banner)

    except Exception as e:
        print(f"[ERRO] {e}")

if __name__ == "__main__":
    main()
