import tkinter as tk
from tkinter import ttk

class CaesarCipherApp:
    def __init__(self, root):  # Perbaikan di sini
        self.root = root
        self.root.title("Program Enkripsi & Dekripsi - Caesar Cipher")
        self.root.geometry("600x400")
        
        # Nilai pergeseran default
        self.shift_value = tk.IntVar(value=3)  # default shift 3
        
        # Create tabs
        self.tab_control = ttk.Notebook(root)
        
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        
        self.tab_control.add(self.tab1, text='Enkripsi')
        self.tab_control.add(self.tab2, text='Dekripsi')
        self.tab_control.pack(expand=1, fill="both")
        
        # Enkripsi tab
        self.setup_enkripsi_tab()
        
        # Dekripsi tab
        self.setup_dekripsi_tab()
    
    def setup_enkripsi_tab(self):
        # Frame untuk nilai pergeseran
        shift_frame = ttk.Frame(self.tab1)
        shift_frame.pack(pady=10)
        
        tk.Label(shift_frame, text="Jumlah Pergeseran:").pack(side=tk.LEFT)
        shift_spinbox = ttk.Spinbox(
            shift_frame, 
            from_=1, 
            to=25, 
            width=5,
            textvariable=self.shift_value
        )
        shift_spinbox.pack(side=tk.LEFT, padx=5)
        
        # Label dan input untuk plainteks
        tk.Label(self.tab1, text="Masukkan Plainteks:").pack(pady=5)
        self.plaintext_input = tk.Text(self.tab1, height=5, width=50)
        self.plaintext_input.pack(pady=5)
        
        # Button enkripsi
        tk.Button(self.tab1, text="Enkripsi", command=self.encrypt).pack(pady=10)
        
        # Label dan output untuk cipherteks
        tk.Label(self.tab1, text="Hasil Enkripsi (Cipherteks):").pack(pady=5)
        self.cipher_output = tk.Text(self.tab1, height=5, width=50)
        self.cipher_output.pack(pady=5)
    
    def setup_dekripsi_tab(self):
        # Frame untuk nilai pergeseran
        shift_frame = ttk.Frame(self.tab2)
        shift_frame.pack(pady=10)
        
        tk.Label(shift_frame, text="Jumlah Pergeseran:").pack(side=tk.LEFT)
        shift_spinbox = ttk.Spinbox(
            shift_frame, 
            from_=1, 
            to=25, 
            width=5,
            textvariable=self.shift_value
        )
        shift_spinbox.pack(side=tk.LEFT, padx=5)
        
        # Label dan input untuk cipherteks
        tk.Label(self.tab2, text="Masukkan Cipherteks:").pack(pady=2)
        self.cipher_input = tk.Text(self.tab2, height=2, width=50)
        self.cipher_input.pack(pady=5)
        
        # Button dekripsi
        tk.Button(self.tab2, text="Dekripsi", command=self.decrypt).pack(pady=10)
        
        # Label dan output untuk plainteks
        tk.Label(self.tab2, text="Hasil Dekripsi (Plainteks):").pack(pady=2)
        self.plain_output = tk.Text(self.tab2, height=2, width=50)
        self.plain_output.pack(pady=5)
    
    def shift_character(self, char, shift, encrypt=True):
        if not char.isalpha():
            return char
            
        # Menentukan ASCII base (97 untuk lowercase, 65 untuk uppercase)
        ascii_base = 97 if char.islower() else 65
        
        # Jika dekripsi, balik arah pergeseran
        if not encrypt:
            shift = -shift
            
        # Lakukan pergeseran dan pastikan tetap dalam range alfabet (0-25)
        shifted = (ord(char) - ascii_base + shift) % 26
        
        # Kembalikan ke bentuk karakter
        return chr(shifted + ascii_base)
    
    def process_text(self, text, encrypt=True):
        shift = self.shift_value.get()
        result = ''
        
        for char in text:
            result += self.shift_character(char, shift, encrypt)
            
        return result
    
    def encrypt(self):
        # Ambil teks dari input
        plaintext = self.plaintext_input.get("1.0", tk.END).strip()
        
        # Proses enkripsi
        ciphertext = self.process_text(plaintext, encrypt=True)
        
        # Tampilkan hasil
        self.cipher_output.delete("1.0", tk.END)
        self.cipher_output.insert("1.0", ciphertext)
    
    def decrypt(self):
        # Ambil teks dari input
        ciphertext = self.cipher_input.get("1.0", tk.END).strip()
        
        # Proses dekripsi
        plaintext = self.process_text(ciphertext, encrypt=False)
        
        # Tampilkan hasil
        self.plain_output.delete("1.0", tk.END)
        self.plain_output.insert("1.0", plaintext)

if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()
