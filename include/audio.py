import os
import sys

# Cross-platform sound handling
if sys.platform == "win32":
    import winsound
else:
    # For macOS/Linux, we can use system commands as a fallback if no extra libs are installed
    pass

class AudioEngine:
    def __init__(self):
        self.current_type = ".wav"  # Default fallback

    def GetType(self, file_type):
        """Sets the active audio file extension type (e.g., '.wav')."""
        # Ensure it has the leading dot
        if not file_type.startswith("."):
            file_type = "." + file_type
        self.current_type = file_type
        print(f"[Audio] Format set to: {self.current_type}")

    def PlayFile(self, file_name, file_type=None):
        """Plays the specified file name with the given or default extension."""
        # Use the passed file_type, or fallback to the one set by GetType
        ext = file_type if file_type else self.current_type
        
        # Ensure extension format is clean
        if not ext.startswith("."):
            ext = "." + ext

        full_filename = f"{file_name}{ext}"

        # Check if file exists before trying to play it
        if not os.path.exists(full_filename):
            print(f"[Audio Error] Could not find file: {full_filename}")
            return

        print(f"[Audio] Playing: {full_filename}...")

        # Native Playback Logic
        if sys.platform == "win32":
            # SND_FILENAME plays the file, SND_ASYNC lets the code keep running without freezing
            winsound.PlaySound(full_filename, winsound.SND_FILENAME | winsound.SND_ASYNC)
        elif sys.platform == "darwin":  # macOS
            os.system(f"afplay {full_filename} &")
        else:  # Linux
            os.system(f"aplay {full_filename} &")

# Instantiate the library object for the import
audio = AudioEngine()