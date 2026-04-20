"""
Author: Hunter Lusk
Vulnerability: Missing Security Headers
Target: blog.0x10.cloud
"""

import urllib.request

url = "http://blog.0x10.cloud"

try:
    response = urllib.request.urlopen(url)

    headers = response.headers

    if "X-Frame-Options" not in headers:
        print("------------------------------------")
        print("VULNERABILITY FOUND")
        print()
        print("Missing X-Frame-Options header (Clickjacking risk)")
        print("------------------------------------")

    if "Content-Security-Policy" not in headers:
        print("------------------------------------")
        print("VULNERABILITY FOUND")
        print()
        print("Missing Content-Security-Policy header (XSS risk)")
        print("------------------------------------")

except Exception as e:
    print("------------------------------------")
    print()
    print("Error:", e)
    print()
    print("------------------------------------")