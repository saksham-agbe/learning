# Networking
* Networking is the process of connecting two or more computers or devices so that they can communicate, share resources, and exchange data with each other.

## Types of Networks
* LAN(Local Area Network)-> Home wifi, office network
* MAN(Metropolitan Area Network)-> tv cables
* WAN(Wide Area Network)-> Internet
* PAN(Personal Area Network)-> Bluetooth
* VPN(Virtual Private Network)-> Secure office network

## Basic Components of Networking
* Node-> Any device connected to a network
* Router-> Connects multiple network
* Switch-> Connects devices in same network
* Access Point-> Connects wireless devices
* Server-> Provides services or data
* Client-> Request data or services
* Cable/Medium-> Path for data transfer

## OSI Model
* The OSI (Open Systems Interconnection) model explains how data travels from one device to another in a network. It has 7 layers, each handling a specific function.

* Physical layer-> Hardware layer, transmission of bits(Cables, Wifi)
* Data-link layer-> MAC addressing, error detection(Ethernet)
* Networking layer-> Logical addressing and routing(IP, ICMP)
* Transport layer-> Ensures reliable data transfer(TCP, UDP)
* Session layer-> Establishes, manages, and terminates session(Session token)
* Presentation layer-> Data formatting, encryption, compression(SSL/TLS, JPEG)
* Application layer-> Interface for end-user applications(HTTP, SSH, FTP)

## TCP/IP Model
* The TCP/IP model is a more practical, real-world version of the OSI model used by the Internet.

* Network Access->  Ethernet, Wi-Fi
* Internet-> IP, ICMP
* Transport-> TCP, UDP
* Application-> HTTP, HTTPS, DNS, SSH

## IP Addressing & Subnetting

### IPv4
* 32-bit address (4 octets)
* Example: 192.168.10.15
* Range: 0.0.0.0 → 255.255.255.255

### IPv6
* 128-bit address, written in hex.
* Example: 2001:0db8:85a3::8a2e:0370:7334

### CIDR (Classless Inter-Domain Routing)
* 


## What is an IP Address?
* An IP Address (Internet Protocol Address) is a unique numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication. It serves two main purposes:

* Identifying a device on the network.
* Locating the device to enable communication with other devices over a network like the Internet.

### Components of an IP Address
* Network Portion: Identifies the network to which the device belongs.
* Host Portion: Identifies the individual device on the network.
* Subnet Mask (for IPv4): Defines which part of the IP is network and which part is host.
* Example: IP 192.168.1.10 with subnet mask 255.255.255.0
* Network ID: 192.168.1.0
* Host ID: 10

* 192.168.1.1
* 192-> First octet
* 168-> Second octet
* 1-> Third octet
* 1-> Fourth octet

### Classes of IPv4 Address
* Class A-> 1-127 
* Class B-> 128-191
* Class C-> 192-223
* Class D-> 224-239
* Class E-> 240-254

## Routing and Switching Basics
### Routers
* Operates at layer 3
* Forward packets between different networks
* Each router interface has an IP address
* Types -> Static routing and Dynamic routing

### Switches
* Operate at layer 2
* Forward data within same network using MAC addresses
* Create a MAC address table

## Protocols
* A protocol is a set of rules that defines how data is transmitted and received between devices in a network. It ensures standardized communication, allowing different systems to understand and interact with each other. Examples include TCP/IP, HTTP, and SMTP.

### Types of protocols
* TCP (Transmission Control Protocol):
* TCP operates at the transport layer of the OSI model. It
establishes a connection between two devices before data exchange, ensuring
reliable and ordered delivery of information.
* Functionality: It breaks data into packets, assigns sequence numbers, and
uses acknowledgment messages to guarantee delivery. It's connection-oriented,
meaning it sets up, maintains, and terminates a connection for data exchange.

*  UDP (User Datagram Protocol):
* Also operating at the transport layer, UDP is a connectionless protocol that offers minimal services. It's like a 'fire and forget'approach for data transmission.
* Functionality: It sends data without establishing a connection, providing lowlatency communication. However, it doesn't guarantee delivery or order, making
it suitable for real-time applications like video streaming or online gaming.

* IP (Internet Protocol):
*  IP functions at the network layer and is a fundamental part of the
TCP/IP protocol suite. It handles addressing and routing to ensure data packets reach their intended destinations.
* Functionality: IP assigns unique IP addresses to devices and uses routing
tables to direct data across networks. It's responsible for the logical connection between different devices on the Internet.

## Ports:
* Ports are communication endpoints that allow different services on a device to send and receive data. 
* 20-> 
* 21-> File transfer protocol(FTP)
* 22-> Secure shell(SSH)
* 23-> Telnet remote login
* 25-> Simple Mail Transfer Protocol(SMTP)
* 53-> Domain Name System(DNS)
* 80-> Hypertext Transfer Protocol(HTTP)
* 110-> Post Office Protocol(POP3)
* 123-> Network Time Protocol(NTP)
* 143-> Internet Message Access Protocol(IMAP)
* 161-> Simple Network Manage Protocol(SNMP)
* 443-> HTTPs
* 3306-> Mysql
* 5432-> Postgress

# Network Interface & IP Commands
* ip a & ipconfig -> check all network interfaces
* ip addr show eth0 -> View ip address odf specific interface
* sudo ip link set eth0 up & sudo ip link set eth0 down -> Bring interface up and down

# Connectivity Testing Commands
* ping google.com -> check connectivity
* traceroute google.com -> Shows path packet
* hostname -i -> Check if hostname resolves

Submited by Saksham
7-11-2025





