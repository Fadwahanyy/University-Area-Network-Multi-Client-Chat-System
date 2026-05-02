# University Area Network (UAN) & Multi-Client Chat System

A full-stack implementation of a **University Area Network (UAN)** combined with a **real-time multi-client communication system** built using Python.

This project integrates **network engineering (Cisco Packet Tracer)** with **distributed systems programming (Python sockets & multithreading)** to simulate a scalable and efficient campus network environment.

---

## 🚀 Overview

This project demonstrates the design and implementation of a **complete offline university network**, including:

* Structured network topology (core + distribution)
* VLAN segmentation for departmental isolation
* Inter-VLAN routing for controlled communication
* A real-time chat system enabling communication between clients across the network

The system supports both **wired and wireless connectivity** and operates without external internet access.

---

## 🏗️ Network Architecture

### 🔹 Physical Design

* **Topology:** Hybrid Star–Bus architecture
* **Core Layer:** Central switch managing distribution switches
* **Devices:** 21 workstations across multiple departments
* **Connectivity:**

  * Copper cables (wired)
  * Wireless Access Points (mobile devices)

### 🔹 Logical Design

* **VLAN Segmentation**

  * VLAN 10 → Academic Department
  * VLAN 20 → Administrative Department

* **Trunking**

  * IEEE 802.1Q trunking enabled on core links

* **Routing**

  * Inter-VLAN routing configured via router

### 🔹 Key Features

* Department isolation with secure communication
* Scalable network structure
* Efficient traffic segmentation

---

## 💬 Multi-Client Chat System

### 🔹 Features

* TCP/IP socket communication
* Multi-threaded server handling multiple clients simultaneously
* Real-time message broadcasting
* Username-based client identification
* Persistent logging of messages

### 🔹 Technologies Used

* Python `socket` module
* Python `threading`
* Tkinter (GUI for client interface)

### 🔹 How it Works

* Server listens for incoming connections
* Each client connects and sends messages
* Server broadcasts messages to all connected clients

---

## 📁 Project Structure

```text
.
├── University_Chat_Project/
│   ├── server.py
│   ├── client.py
│   └── chat_log.txt
│
├── Final Network Project.pkt   # Packet Tracer design (external link below)
├── University Area Network Documentation.docx
├── README.md
```

---

## 📥 Large Files (Important)

Due to GitHub file size limits, large files are hosted externally:

👉 **Packet Tracer File (.pkt)**
[Download here]([PASTE_YOUR_GOOGLE_DRIVE_LINK](https://drive.google.com/file/d/1oldDaMaCxN86EcqfmNDtY0oG6C1FMsS4/view?usp=drive_link))

👉 **Project Documentation (.docx)**
[Download here]([PASTE_YOUR_GOOGLE_DRIVE_LINK](https://docs.google.com/document/d/1P2V9IyCppWIP45LBSE6bFlgJMRjClOfh/edit?usp=drive_link&ouid=101793766684269348666&rtpof=true&sd=true))

---

## ▶️ How to Run

### 1. Start the Server

```bash
python University_Chat_Project/server.py
```

### 2. Start the Client

```bash
python University_Chat_Project/client.py
```

### 3. Connect Multiple Clients

Run multiple client instances to simulate different workstations.

---

## 🧪 Testing & Validation

* ✅ Verified connectivity using ICMP (0% packet loss)
* ✅ Confirmed VLAN segmentation and isolation
* ✅ Tested inter-VLAN communication
* ✅ Validated real-time chat broadcasting across multiple clients

---

## ⚙️ Technologies

* Cisco Packet Tracer
* Python
* Socket Programming
* Multithreading
* Tkinter GUI

---

## 🧠 Key Learning Outcomes

* Network design and segmentation (VLANs)
* Inter-VLAN routing and trunking (802.1Q)
* Client-server architecture
* Real-time communication systems
* Multithreaded programming

---

## ⚠️ Disclaimer

This project is intended for:

* Educational purposes
* Network simulation and software demonstration

---

## 👤 Author

**Fadwa Hany**

---

## ⭐ If you find this project useful

Give it a ⭐ on GitHub!
