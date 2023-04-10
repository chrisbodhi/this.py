import subprocess

def get_selected_text():
    script = 'tell application "System Events" to return the value of the attribute "AXSelectedText" of UI element 1 of (window 1 of (process 1 whose frontmost is true))'
    p = subprocess.Popen(['osascript', '-e', script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if stderr:
        print(f"Error executing AppleScript: {stderr}")
        return None
    return stdout.decode('utf-8').strip()

selected_text = get_selected_text()
if selected_text:
    print(f"The selected text is: {selected_text}")
else:
    print("No text is currently selected.")
