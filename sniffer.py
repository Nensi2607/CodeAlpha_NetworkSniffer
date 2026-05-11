from scapy.all import sniff
from scapy.layers.inet import IP

packet_count = 0

def packet_callback(packet):

    global packet_count
    packet_count += 1

    if packet.haslayer(IP):

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol_num = packet[IP].proto

        protocol_name = "OTHER"

        if protocol_num == 6:
            protocol_name = "TCP"

        elif protocol_num == 17:
            protocol_name = "UDP"

        elif protocol_num == 1:
            protocol_name = "ICMP"

        print("\n==============================")
        print(f"Packet Number   : {packet_count}")
        print(f"Source IP       : {source_ip}")
        print(f"Destination IP  : {destination_ip}")
        print(f"Protocol        : {protocol_name}")

sniff(prn=packet_callback, filter="tcp", count=10)