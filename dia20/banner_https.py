#!/usr/bin/env python3
# Banner grabbing WEB via HTTPS (TLS) — educacional
# Por padrão: só localhost. Libere manualmente se você tiver permissão.

import socket
import ssl
import sys

TIMEOUT = 4
MAX_BYTES = 16384
ALLOW_NON_LOCALHOST = True  # mude para False se quiser travar só local

def is_localhost(host: str) -> bool:
    return host in ("127.0.0.1", "localhost")

def grab_https_headers(host: str, port: int = 443, path: str = "/") -> str:
    # 1) Socket TCP
    raw = socket.create_connection((host, port), timeout=TIMEOUT)

    # 2) TLS (importante: SNI = server_hostname)
    ctx = ssl.create_default_context()
    tls = ctx.wrap_socket(raw, server_hostname=host)

    # 3) Requisição HEAD (só headers)
    req = (
        f"HEAD {path} HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"User-Agent: banner-grab-study\r\n"
        f"Connection: close\r\n\r\n"
    )
    tls.sendall(req.encode("ascii", errors="ignore"))

    # 4) Ler resposta (headers costumam caber em 16KB)
    data = tls.recv(MAX_BYTES)
    tls.close()

    text = data.decode("utf-8", errors="replace")
    headers = text.split("\r\n\r\n", 1)[0]
    return headers.strip()

def main():
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python3 banner_https.py <host> [path]")
        print("Exemplos:")
        print("  python3 banner_https.py 127.0.0.1 /")
        print("  python3 banner_https.py youtube.com /")
        sys.exit(1)

    host = sys.argv[1].strip()
    path = sys.argv[2].strip() if len(sys.argv) >= 3 else "/"

    if (not ALLOW_NON_LOCALHOST) and (not is_localhost(host)):
        print("[BLOQUEADO] Por segurança, este script só permite 127.0.0.1/localhost.")
        sys.exit(2)

    try:
        headers = grab_https_headers(host, 443, path)
        print("=== HEADERS HTTPS ===")
        print(headers)
    except ssl.SSLError as e:
        print(f"[SSL] Falha TLS: {e}")
    except Exception as e:
        print(f"[ERRO] {type(e).__name__}: {e}")

if __name__ == "__main__":
    main()
