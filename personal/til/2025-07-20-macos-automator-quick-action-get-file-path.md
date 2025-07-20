
# TIL: Mac OS Automator Quick Action – Copy File Path in Finder (2025-07-20)

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> **Copy file paths instantly from Finder** – Create a Quick Action in Automator to copy the POSIX path of selected files or folders to your clipboard.

---

## The Pain Point

Getting the full file path of selected items in Finder is a common need, but macOS doesn’t provide a built-in shortcut. Automator lets you create a Quick Action to copy paths with a right-click or keyboard shortcut.

---

## Step-by-Step Guide

### 1. Open Automator

Press `Cmd + Space` and type Automator, then hit Return.

### 2. Create a New Quick Action

Select "New Document".
Choose "Quick Action" (or "Service" in older macOS versions).

### 3. Configure Workflow Settings

At the top of the workflow area, set:
- Workflow receives current: **files or folders**
- in: **Finder**

### 4. Add an Action: "Run AppleScript" (Recommended)

In the left pane, search for **Run AppleScript**.
Drag it to the workflow area.
Replace the default script with:

```applescript
on run {input, parameters}
    set output to ""
    repeat with anItem in input
        set output to output & (POSIX path of anItem) & linefeed
    end repeat
    set the clipboard to output
    return input
end run
```

This script:
- Collects the POSIX (Unix) path(s) of each selected file/folder
- Copies them (each on a new line) to the clipboard

### 5. Save the Quick Action

Press `Cmd + S`.
Enter a name, e.g., **Copy Path to Clipboard**.
Click Save.

### 6. Use Your Quick Action in Finder

In Finder, right-click (or Control-click) a file or folder.
Go to **Quick Actions** (or **Services**), and choose your action (e.g., Copy Path to Clipboard).
The POSIX path(s) will now be on your clipboard.

### 7. (Optional) Add a Keyboard Shortcut

Open **System Settings > Keyboard > Keyboard Shortcuts > Services**.
Find your Quick Action and assign a shortcut.

---

## Troubleshooting

- If the Quick Action doesn’t appear, check that it’s set to receive files/folders in Finder.
- If paths aren’t copied, ensure the AppleScript is entered correctly.
- Assign a keyboard shortcut for even faster access.

---

## Related Resources

- [Automator User Guide (Apple)](https://support.apple.com/guide/automator/welcome/mac)
- [AppleScript Overview](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)

---

*Let me know if you want to do something more advanced or need screenshots!*
