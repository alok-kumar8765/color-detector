import cv2
import numpy as np
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class ColorDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Detector")
        self.root.geometry("850x550")
        self.root.configure(bg="#0b0b0f")

        # Initialize Webcam
        self.cap = cv2.VideoCapture(0)
        self.current_rgb = (0, 0, 0)
        self.current_hex = "#000000"
        self.current_color_name = "Unknown"

        # --- Title ---
        title_label = tk.Label(root, text="Webcam Color Detector", font=("Helvetica", 16, "bold"), fg="#00ff88", bg="#0b0b0f")
        title_label.pack(pady=10)

        # --- Main Layout Frame ---
        main_frame = tk.Frame(root, bg="#0b0b0f")
        main_frame.pack(fill="both", expand=True, padx=15, pady=5)

        # Video Display Canvas/Label on Left
        self.video_label = tk.Label(main_frame, bg="#1e1e1e", relief="solid", bd=1)
        self.video_label.pack(side="left", padx=10, pady=10)
        # Bind mouse click on video feed to sample color
        self.video_label.bind("<Button-1>", self.pick_color_on_click)

        # Info & Controls Panel on Right
        info_frame = tk.Frame(main_frame, bg="#0b0b0f")
        info_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Instruction note
        tk.Label(info_frame, text="💡 Click anywhere on the video feed\nto sample that pixel's color!", fg="#aaaaaa", bg="#0b0b0f", font=("Helvetica", 9), justify="left").pack(anchor="w", pady=(0, 10))

        # HEX Display
        tk.Label(info_frame, text="HEX:", fg="#00ff88", bg="#0b0b0f", font=("Helvetica", 11, "bold")).pack(anchor="w")
        self.hex_var = tk.StringVar(value="#------")
        self.hex_entry = tk.Entry(info_frame, textvariable=self.hex_var, font=("Helvetica", 12), width=15, state="readonly")
        self.hex_entry.pack(anchor="w", pady=(0, 10))

        # RGB Display
        tk.Label(info_frame, text="RGB:", fg="#00ff88", bg="#0b0b0f", font=("Helvetica", 11, "bold")).pack(anchor="w")
        self.rgb_var = tk.StringVar(value="---, ---, ---")
        self.rgb_entry = tk.Entry(info_frame, textvariable=self.rgb_var, font=("Helvetica", 12), width=15, state="readonly")
        self.rgb_entry.pack(anchor="w", pady=(0, 10))

        # Color Name Display
        tk.Label(info_frame, text="Color Name:", fg="#00ff88", bg="#0b0b0f", font=("Helvetica", 11, "bold")).pack(anchor="w")
        self.name_var = tk.StringVar(value="---")
        self.name_entry = tk.Entry(info_frame, textvariable=self.name_var, font=("Helvetica", 12), width=18, state="readonly")
        self.name_entry.pack(anchor="w", pady=(0, 15))

        # Color Visual Box Preview
        self.color_preview = tk.Label(info_frame, text="Preview", bg="black", fg="white", font=("Helvetica", 10, "bold"), width=18, height=3, relief="solid", bd=1)
        self.color_preview.pack(anchor="w", pady=(0, 15))

        # Buttons
        copy_btn = tk.Button(info_frame, text="Copy HEX", command=self.copy_hex, bg="#0088ff", fg="#ffffff", font=("Helvetica", 10, "bold"), relief="flat", padx=10, pady=5)
        copy_btn.pack(anchor="w", fill="x", pady=5)

        # Store last captured frame for pixel color picking
        self.latest_frame = None

        # Start the video loop
        self.update_frame()

    def get_color_name(self, r, g, b):
        # Cast to standard int to prevent uint8 overflow warnings during subtraction
        r, g, b = int(r), int(g), int(b)
        
        # Expanded basic color classification based on RGB values
        if r > 220 and g > 220 and b > 220: return "White"
        if r < 40 and g < 40 and b < 40: return "Black"
        if abs(r - g) < 15 and abs(g - b) < 15: return "Gray"
        
        if r > g and r > b:
            if g > 150 and b < 100: return "Yellow"
            if g > 100 and b > 100: return "Pink / Light Red"
            return "Red"
        elif g > r and g > b:
            if r > 150: return "Yellow / Lime"
            if b > 150: return "Cyan / Teal"
            return "Green"
        elif b > r and b > g:
            if r > 120: return "Purple / Magenta"
            if g > 150: return "Cyan / Turquoise"
            return "Blue"
        return "Custom"

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # Flip frame horizontally for natural mirror effect and convert BGR to RGB
            frame = cv2.flip(frame, 1)
            self.latest_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Resize frame for GUI display container (e.g., 480x360)
            display_frame = cv2.resize(self.latest_frame, (480, 360))
            
            # Draw a small crosshair target in the center as a default reference
            h, w, _ = display_frame.shape
            cv2.drawMarker(display_frame, (w // 2, h // 2), (0, 255, 0), markerType=cv2.MARKER_CROSS, markerSize=15, thickness=2)

            # Convert to ImageTk format for Tkinter
            img = Image.fromarray(display_frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        # Loop frame updates every 15 ms
        self.root.after(15, self.update_frame)

    def pick_color_on_click(self, event):
        if self.latest_frame is not None:
            # Map widget click coordinates to the resized display frame dimensions (480x360)
            click_x = event.x
            click_y = event.y
            
            h_orig, w_orig, _ = self.latest_frame.shape
            # Scale coordinates back to original camera resolution
            orig_x = int(click_x * (w_orig / 480))
            orig_y = int(click_y * (h_orig / 360))

            if 0 <= orig_x < w_orig and 0 <= orig_y < h_orig:
                # Extract RGB tuple from clicked pixel
                r, g, b = self.latest_frame[orig_y, orig_x]
                self.current_rgb = (int(r), int(g), int(b))
                self.current_hex = f"#{r:02x}{g:02x}{b:02x}".upper()
                self.current_color_name = self.get_color_name(r, g, b)

                # Update UI elements
                self.hex_var.set(self.current_hex)
                self.rgb_var.set(f"{r}, {g}, {b}")
                self.name_var.set(self.current_color_name)
                self.color_preview.config(bg=self.current_hex, fg="black" if (r*0.299 + g*0.587 + b*0.114) > 150 else "white")

    def copy_hex(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.current_hex)
        messagebox.showinfo("Copied", f"Copied {self.current_hex} to clipboard!")

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorDetectorApp(root)
    root.mainloop()