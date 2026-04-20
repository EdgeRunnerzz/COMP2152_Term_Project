import socket
import ssl

TARGET = "old.0x10.cloud"

print("\n=== Legacy Server Security Analysis ===\n")

# Normal TLS handshake
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

try:
    with socket.create_connection((TARGET, 443), timeout=10) as sock:
        with context.wrap_socket(sock, server_hostname=TARGET) as secure_sock:
            tls_version = secure_sock.version()
            cipher_info = secure_sock.cipher()

            print(f"Target Host      : {TARGET}")
            print(f"Negotiated TLS   : {tls_version}")
            print(f"Cipher Suite     : {cipher_info[0]}")
            print(f"Key Strength     : {cipher_info[2]} bits")

            print("\n--- Vulnerability Assessment ---")

            if tls_version in ["SSLv3", "TLSv1", "TLSv1.1"]:
                print("STATUS: CRITICAL")
                print("Reason: Server negotiated an outdated and insecure TLS protocol.")
                print("Risk  : Susceptible to downgrade attacks (POODLE/BEAST) that can expose cookies and session data.")
            elif tls_version == "TLSv1.2":
                print("STATUS: MODERATE RISK")
                print("Reason: TLS 1.2 is in use, but the server is described as running legacy software.")
            else:
                print("STATUS: SECURE TLS VERSION")
                print(f"Negotiated: {tls_version}")

except Exception as e:
    print(f"Connection failed: {e}")
    print("Unable to analyze TLS configuration.")

print("\nAdditional Context:")
print("• The server is documented as Apache 2.2.22 (unsupported since 2017)")
print("• Old Apache versions contain multiple known unpatched vulnerabilities")
print("• Even with modern TLS, the outdated web server remains a high-risk target.")

print("\n=== Analysis Complete ===")