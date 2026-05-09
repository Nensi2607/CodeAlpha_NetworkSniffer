from scapy.all import sniff
from scapy.layers.inet import IP

def packet_callback(packet):

    if packet.haslayer(IP):

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol = packet[IP].proto

        print("\n--- Packet Captured ---")
        print(f"Source IP      : {source_ip}")
        print(f"Destination IP : {destination_ip}")
        print(f"Protocol Number: {protocol}")

sniff(prn=packet_callback, store=False)