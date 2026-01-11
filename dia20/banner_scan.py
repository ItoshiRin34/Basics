#!/usr/bin/env python3
# banner_grab.py
# Uso seguro: por padrão, só permite 127.0.0.1 (localhost).
# Objetivo: aprender banner grabbing em ambiente autorizado.

import socket
import sys
from typing import Optional

TIMEOUT = 2.0
MAX_BYTES = 4096

# TRAVA: só localhost por padrão (evita uso indevido sem querer)
ALLOW_NON_LOCALHOST = False

def is_localhost(host: str) -> bool:
    return host in ("127.0.0.1", "localhost")

def tcp_connect(host: str, port: int) -> socket.socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)
    s.connect((host, port))
    return s

def grab_generic_banner(host: str, port: int) -> str:
    """
    Para serviços que mandam banner ao conectar (ex: SSH, FTP, SMTP em alguns casos).
    """
    s = tcp_connect(host, port)
    try:
        data = s.recv(MAX_BYTES)
        return data.decode("utf-8", errors="replace").strip()
    finally:
        s.close()

def grab_http_banner(host: str, port: int, use_tls: bool = False) -> str:
    """
    Para HTTP: envia HEAD e lê os headers (onde muitas vezes vem Server: ...)
    Obs: aqui é HTTP puro. Para HTTPS de verdade, precisaria de ssl.wrap_socket().
    """
    s = tcp_connect(host, port)
    try:
        req = (
            f"HEAD / HTTP/1.1\r\n"
            f"Host: {host}\r\n"
            f"User-Agent: banner-grab-study\r\n"
            f"Connection: close\r\n\r\n"
        )
        s.sendall(req.encode("ascii", errors="ignore"))
        data = s.recv(MAX_BYTES)
        text = data.decode("utf-8", errors="replace")
        # retorna só headers (até a linha em branco)
        headers = text.split("\r\n\r\n", 1)[0]
        return headers.strip()
    finally:
        s.close()

def main():
    if len(sys.argv) < 3:
        print("Uso:")
        print("  python3 banner_grab.py <host> <porta> [modo]")
        print("Modos:")
        print("  generic  (default)  -> só conecta e lê o banner")
        print("  http               -> envia HEAD e lê headers")
        print("\nExemplos (LOCAL):")
        print("  python3 banner_grab.py 127.0.0.1 22 generic")
        print("  python3 banner_grab.py 127.0.0.1 80 http")
        sys.exit(1)

    host = sys.argv[1].strip()
    port = int(sys.argv[2])
    mode = (sys.argv[3].strip().lower() if len(sys.argv) >= 4 else "generic")

    if not ALLOW_NON_LOCALHOST and not is_localhost(host):
        print("[BLOQUEADO] Por segurança, este script só permite 127.0.0.1/localhost.")
        print("Se você tiver autorização explícita, mude ALLOW_NON_LOCALHOST = True no código.")
        sys.exit(2)

    try:
        if mode == "http":
            out = grab_http_banner(host, port)
        else:
            out = grab_generic_banner(host, port)

        if out:
            print("=== BANNER / RESPOSTA ===")
            print(out)
        else:
            print("(Sem banner/sem resposta imediata — pode ser normal.)")

    except (socket.timeout, ConnectionRefusedError) as e:
        print(f"[ERRO] Não conectou em {host}:{port} -> {e}")
    except Exception as e:
        print(f"[ERRO] {type(e).__name__}: {e}")

if __name__ == "__main__":
    main()
