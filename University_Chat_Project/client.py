import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog

# --- CONFIGURATION ---
SERVER_IP = '127.0.0.1'
PORT = 65432

class UniversityChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("University Unified Chat v2.1")
        self.root.geometry("450x600")
        self.root.configure(bg="#2c3e50")

        # --- ASK FOR USERNAME ON START ---
        self.username = simpledialog.askstring("Username", "Enter your PC Name (e.g., PC-0):", parent=root)
        if not self.username:
            self.username = "Anonymous"

        # Header with Username
        self.label = tk.Label(root, text=f"LOGGED IN AS: {self.username}", font=("Helvetica", 12, "bold"), 
                             bg="#34495e", fg="#27ae60", pady=10)
        self.label.pack(fill=tk.X)

        self.chat_display = scrolledtext.ScrolledText(root, state='disabled', font=("Segoe UI", 10))
        self.chat_display.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        self.chat_display.configure(bg="#ecf0f1", fg="#2c3e50")

        self.entry_frame = tk.Frame(root, bg="#2c3e50")
        self.entry_frame.pack(fill=tk.X, padx=20, pady=20)

        self.msg_entry = tk.Entry(self.entry_frame, font=("Segoe UI", 12), bd=0)
        self.msg_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8)
        self.msg_entry.bind("<Return>", lambda event: self.send_message())

        self.send_btn = tk.Button(self.entry_frame, text="SEND", command=self.send_message,
                                 bg="#27ae60", fg="white", font=("Helvetica", 10, "bold"),
                                 relief=tk.FLAT, padx=15)
        self.send_btn.pack(side=tk.RIGHT, padx=5)

        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((SERVER_IP, PORT))
            threading.Thread(target=self.receive_messages, daemon=True).start()
        except:
            tk.messagebox.showerror("Error", "Server is offline!")

    def send_message(self):
        msg = self.msg_entry.get()
        if msg:
            # SENDS USERNAME + MESSAGE
            full_message = f"{self.username}: {msg}"
            self.s.send(full_message.encode('utf-8'))
            self.update_chat(f"You: {msg}")
            self.msg_entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                msg = self.s.recv(1024).decode('utf-8')
                if msg:
                    self.update_chat(msg)
            except: break

    def update_chat(self, msg):
        self.chat_display.configure(state='normal')
        self.chat_display.insert(tk.END, msg + "\n")
        self.chat_display.configure(state='disabled')
        self.chat_display.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = UniversityChatClient(root)
    root.mainloop()