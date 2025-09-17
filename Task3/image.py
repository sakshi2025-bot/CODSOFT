import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from transformers import BlipProcessor, BlipForConditionalGeneration
import os
import random

# Load the BLIP processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

# --- MODIFICATION: Set the path to your image dataset folder ---
# Replace this with the absolute path to the folder containing your images.
DATASET_PATH = "C:/Users/nmpra/OneDrive/Desktop/imagecaption/Flickr8k_Dataset/Flicker8k_Dataset"

# --- MODIFICATION: Set slideshow interval in milliseconds ---
# This is how long each image will be displayed (e.g., 5000ms = 5 seconds)
SLIDESHOW_INTERVAL = 5000


class ImageCaptioningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Captioning Slideshow")
        self.root.geometry("600x600")

        self.image_label = tk.Label(root, text="Starting slideshow...")
        self.image_label.pack(pady=10)

        # --- MODIFICATION: New buttons for slideshow control ---
        self.start_button = tk.Button(root, text="Start Slideshow", command=self.start_slideshow)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop Slideshow", command=self.stop_slideshow)
        self.stop_button.pack(pady=5)

        # Label to display the caption
        self.caption_label = tk.Label(root, text="", wraplength=400)
        self.caption_label.pack(pady=10)

        self.image_display = None
        self.slideshow_job = None  # Stores the ID of the scheduled job

    def start_slideshow(self):
        """Starts the automatic image cycling."""
        self.stop_slideshow()  # Ensure no previous slideshow is running
        self.load_and_caption_random_image()

    def stop_slideshow(self):
        """Stops the automatic image cycling."""
        if self.slideshow_job:
            self.root.after_cancel(self.slideshow_job)
            self.slideshow_job = None
            self.image_label.config(text="Slideshow stopped.")

    def load_and_caption_random_image(self):
        """Loads a random image, captions it, and schedules the next one."""
        try:
            files = os.listdir(DATASET_PATH)
            image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

            if not image_files:
                self.caption_label.config(text="Error: No images found in the specified folder.")
                self.stop_slideshow()
                return

            random_filename = random.choice(image_files)
            image_path = os.path.join(DATASET_PATH, random_filename)

            # Load and display the image
            image = Image.open(image_path)
            image = image.resize((400, 400))
            self.image_display = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.image_display, text="")
            self.image_label.image = self.image_display

            # Generate the caption
            inputs = processor(images=image, return_tensors="pt")
            out = model.generate(**inputs)
            caption = processor.decode(out[0], skip_special_tokens=True)
            self.caption_label.config(text="Generated Caption: " + caption)

            # Schedule the next image to be loaded
            self.slideshow_job = self.root.after(SLIDESHOW_INTERVAL, self.load_and_caption_random_image)

        except FileNotFoundError:
            self.caption_label.config(text="Error: The dataset path was not found.")
            self.stop_slideshow()
        except Exception as e:
            self.caption_label.config(text=f"An error occurred: {e}")
            self.stop_slideshow()


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageCaptioningApp(root)
    root.mainloop()