# Prodigy_CS_04
# **Python Keylogger**

A simple Python-based keylogger that logs keystrokes to a text file. This tool is intended strictly for ethical use, such as personal system monitoring or approved security research.

---

## **⚠️ Disclaimer**

This tool is designed for **legal and ethical use only**. Ensure you have explicit permission from the system owner before deploying or using this keylogger. Unauthorized use may violate privacy laws and lead to severe consequences.

---

## **Features**
- Logs all printable characters entered on the keyboard.  
- Records special keys (e.g., `Enter`, `Shift`, `Esc`) in a readable format.  
- Automatically writes captured keystrokes to a log file (`key_log.txt`).  
- Stops logging when the `Esc` key is pressed.  

---

## **How It Works**
1. Captures keystrokes using the `pynput` library.  
2. Records printable characters directly and formats special keys for clarity.  
3. Writes all logs to a file (`key_log.txt`) in the script's directory.  

---

## **Usage Instructions**
1. **Clone the repository**:  
   ```bash
   git clone https://github.com/yourusername/python-keylogger.git
   cd python-keylogger
   ```

2. **Install dependencies**:  
   Install the `pynput` library:  
   ```bash
   pip install pynput
   ```

3. **Run the keylogger**:  
   Execute the script:  
   ```bash
   python keylogger.py
   ```

4. **View logs**:  
   Check the `key_log.txt` file in the same directory for logged keystrokes.  

5. **Stop the keylogger**:  
   Press the `Esc` key to stop logging and terminate the program.  

---

## **Requirements**
- Python 3.6 or later.  
- `pynput` library (install with `pip install pynput`).  

---

## **Security and Ethical Usage**
- Use this tool **only** on systems you own or have explicit permission to monitor.  
- Be transparent about its use if conducting security research or testing.  
- Avoid storing sensitive data or using this tool in environments with confidential information.  

---

## **Example Log**
Sample output in `key_log.txt`:  
```plaintext
Hello [space] World [enter]
[shift] This is a test. [esc]
```

---

## **License**
This project is licensed under the **MIT License**. Use and modify responsibly.  

---

## **Contributions**
Contributions and feedback are welcome! Open an issue or submit a pull request for suggestions or improvements.  
