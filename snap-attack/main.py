import argparse
import threading
from scapy.all import sniff, IP
import paramiko
import time

def scan_network(interface: str) -> None:
    """Capture packets on the specified network interface."""
    print(f"[*] Sniffing on {interface}...")
    sniff(iface=interface, prn=lambda pkt: print(f"Captured: {pkt.summary()}"), store=False)

def ssh_attack(target: str, username: str, password: str) -> None:
    """Attempt SSH login to simulate brute-force testing."""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(target, username=username, password=password, timeout=5)
        print(f"[+] SUCCESS: Logged into {target} as {username}")
    except paramiko.AuthenticationException:
        print(f"[-] FAILED: Invalid credentials for {target}")
    except Exception as e:
        print(f"[!] ERROR: {e}")
    finally:
        client.close()