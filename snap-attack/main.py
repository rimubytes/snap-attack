import argparse
import threading
from scapy.all import sniff, IP
import paramiko
import time

def scan_network(interface: str) -> None:
    """Capture packets on the specified network interface."""
    print(f"[*] Sniffing on {interface}...")
    sniff(iface=interface, prn=lambda pkt: print(f"Captured: {pkt.summary()}"), store=False)