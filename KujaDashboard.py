import tkinter as tk
from tkinter import ttk
import time
import threading
from playsound import playsound

class MarsDiggingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Mars Digging Robot Dashboard")
        self.root.geometry("400x300")

        # Digging Robot Attributes
        self.depth_dug = 0  # Depth in cm
        self.max_depth = 100  # Set target depth to 100 cm (1 meter)
        self.energy_level = 100  # Energy level in percentage
        self.digging = False  # Digging state

        # Depth Progress Bar
        self.depth_label = tk.Label(root, text="Digging Progress:")
        self.depth_label.pack(pady=5)
        self.depth_progress = ttk.Progressbar(root, length=300, mode='determinate', maximum=self.max_depth)
        self.depth_progress.pack(pady=5)

        # Energy Level Display
        self.energy_label = tk.Label(root, text=f"Energy Level: {self.energy_level}%")
        self.energy_label.pack(pady=5)
        
        # Start and Stop Buttons
        self.start_button = tk.Button(root, text="Start Digging", command=self.start_digging)
        self.start_button.pack(pady=5)
        
        self.stop_button = tk.Button(root, text="Pause", command=self.stop_digging)
        self.stop_button.pack(pady=5)

    def dig(self):
        """Simulates the digging process in a background thread."""
        while self.digging and self.depth_dug < self.max_depth:
            time.sleep(1)  # Simulate digging time
            self.depth_dug += 10  # Increase depth by 10 cm
            self.energy_level -= 5  # Reduce energy level

            # Update GUI
            self.depth_progress["value"] = self.depth_dug
            self.energy_label.config(text=f"Energy Level: {self.energy_level}%")

            # Check if energy is too low
            if self.energy_level <= 10:
                self.digging = False
                self.energy_label.config(text="Energy Low! Recharge Needed.")
                break

        if self.depth_dug >= self.max_depth:
            self.depth_label.config(text="Digging Complete!")
            self.play_sound()  # Play sound on completion

    def play_sound(self):
        """Plays a sound when digging reaches max depth."""
        playsound("alert.mp3")  # Ensure alert.mp3 is in the same directory

    def start_digging(self):
        """Starts the digging process in a separate thread."""
        if not self.digging:
            self.digging = True
            threading.Thread(target=self.dig, daemon=True).start()

    def stop_digging(self):
        """Pauses the digging process."""
        self.digging = False

# Run the GUI
root = tk.Tk()
app = MarsDiggingGUI(root)
root.mainloop()
