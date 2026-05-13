from scapy.all import sniff
from scapy.layers.inet import IP

packet_count = 0

log_file = open("packet_logs.txt", "a")

def packet_callback(packet):

    global packet_count
    packet_count += 1

    if packet.haslayer(IP):

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol_num = packet[IP].proto
        packet_size = len(packet)

        protocol_name = "OTHER"

        if protocol_num == 6:
            protocol_name = "TCP"

        elif protocol_num == 17:
            protocol_name = "UDP"

        elif protocol_num == 1:
            protocol_name = "ICMP"

        output = f"""
====================================
Packet Number   : {packet_count}
Source IP       : {source_ip}
Destination IP  : {destination_ip}
Protocol        : {protocol_name}
Packet Size     : {packet_size} bytes
====================================
"""

        print(output)

        log_file.write(output)
        log_file.flush()

sniff(prn=packet_callback, filter="tcp", count=10)

log_file.close()