import datetime

def log_keystrokes_simulated():
    print("🔐 Simulated Keylogger Started (Educational Purpose Only)")
    print("Type your text below. Type 'EXIT' to stop.\n")

    keys_logged = []

    while True:
        key = input("Type: ")
        if key.upper() == "EXIT":
            break
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        keys_logged.append(f"[{timestamp}] {key}\n")

    # Save to log file
    with open("simulated_keylog.txt", "w") as file:
        file.writelines(keys_logged)

    print("\n✅ Logging complete. Data saved to 'simulated_keylog.txt'.")

if __name__ == "__main__":
    log_keystrokes_simulated()
