import time
import win32gui
import win32con
import win32clipboard as clipboard

def get_mt4_journal_entries():
    hwnd = win32gui.FindWindow(None, "22665629: Forex.comJP-Demo 104 - StoneX Financial Co., Ltd. - USDZAR,M1")  # Adjust this if your MT4 window has a different title
    if hwnd == 0:
        print("MetaTrader 4 window not found!")
        return ""

    # Set the MT4 window to the foreground
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(1)  # Wait for the window to come to the foreground

    # Open the Terminal window with Ctrl + T
    win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_CONTROL, 0)
    win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, ord('T'), 0)
    time.sleep(1)

    # Send Ctrl + A to select all text in the Journal
    win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_CONTROL, 0)
    win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, ord('A'), 0)
    time.sleep(1)

    # Send Ctrl + C to copy the selected text
    win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, ord('C'), 0)
    win32gui.SendMessage(hwnd, win32con.WM_KEYUP, ord('C'), 0)
    time.sleep(1)

    # Retrieve the copied text from the clipboard
    clipboard.OpenClipboard()
    journal_text = clipboard.GetClipboardData(win32con.CF_TEXT).decode('utf-8')
    clipboard.CloseClipboard()

    return journal_text

def main():
    last_entry = ""
    while True:
        journal_text = get_mt4_journal_entries()
        if journal_text:
            lines = journal_text.strip().split("\r\n")
            new_entry = lines[-1]
            if new_entry != last_entry:
                print(new_entry)
                last_entry = new_entry
        time.sleep(5)

if __name__ == "__main__":
    main()
