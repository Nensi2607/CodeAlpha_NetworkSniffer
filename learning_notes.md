
# Day 1 - Networking Basics

## What is a Network
A network is a group of connected devices that can communicate and share data.

Example: Laptop and mobile connected to WiFi.

## What is an IP Address
An IP address is a unique identifier assigned to each device on a network.

Example: 192.168.1.1

## What is a Packet
A packet is a small unit of data sent over a network.

It contains:
- Source IP
- Destination IP
- Data


# Day 2 - Protocols and Ports

## TCP vs UDP

### TCP
- Reliable communication
- Ensures data delivery
- Used in web browsing

### UDP
- Faster but unreliable
- No guarantee of delivery
- Used in streaming and gaming

## Ports

Ports help identify specific services on a device.

Examples:
- 80 → HTTP
- 443 → HTTPS
- 53 → DNS

## Protocol

A protocol is a set of rules for communication.

Examples:
- TCP
- UDP
- HTTP


# Day 3 - Packet Sniffing and Scapy

## What is Packet Sniffing
Packet sniffing is the process of capturing and analyzing network packets traveling through a network.

It is used for:
- Network monitoring
- Security analysis
- Troubleshooting

## Information Captured
A packet sniffer can capture:
- Source IP
- Destination IP
- Protocol
- Ports
- Payload data

## What is Scapy
Scapy is a Python library used for packet manipulation and network analysis.

It helps in:
- Capturing packets
- Analyzing packets
- Creating custom packets


# Day 5 - Extracting Packet Information

## New Concepts Learned
- Accessing packet layers
- Extracting source and destination IP addresses
- Identifying protocol numbers

## Important Functions
- packet.haslayer(IP)
- packet[IP].src
- packet[IP].dst
- packet[IP].proto

## Result
Successfully extracted IP and protocol information from captured packets.