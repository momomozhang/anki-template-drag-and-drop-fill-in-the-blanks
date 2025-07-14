# Drag-and-Drop Blanks Creator Add-on

This Anki add-on adds a toolbar button to create `[[dN::text]]` syntax for drag-and-drop fill-in-the-blank templates.

## ✅ **WORKING VERSION - Native Qt Implementation**

**Version 1.0.1** - Fixed automation using native Qt APIs instead of JavaScript selection detection.

## Features

- **✅ FUNCTIONAL AUTOMATION**: Uses native Qt `selectedText()` API - **actually works**
- **Smart Counter Detection**: Automatically detects existing `[[d1::text]]`, `[[d2::text]]`, etc. and uses the next available number
- **Keyboard Shortcut**: Use `Ctrl+Shift+D` to quickly create blanks
- **Error Handling**: Comprehensive validation and helpful feedback
- **Cross-Platform**: Works on Windows, Mac, and Linux
- **Per-Card Intelligence**: Scans each card individually to determine the correct counter number

## How to Use

1. **Create Content**: Paste your text into the Question field
2. **Select Text**: Highlight the text you want to turn into a drag-drop blank
3. **Press Shortcut**: Use `Ctrl+Shift+D` (or `Cmd+Shift+D` on Mac) OR click the toolbar button
4. **Result**: Selected text becomes `[[dN::text]]` where N is automatically determined
5. **Done**: Template automatically extracts draggable items - no manual field population needed

## Example

**Before:**
```
You simply upload your code and Elastic Beanstalk automatically handles the deployment.
```

**After selecting "Elastic Beanstalk" and clicking the button:**
```
You simply upload your code and [[d1::Elastic Beanstalk]] automatically handles the deployment.
```

**After selecting "deployment" and clicking the button again:**
```
You simply upload your code and [[d1::Elastic Beanstalk]] automatically handles the [[d2::deployment]].
```

**Result**: Template automatically creates draggable items "Elastic Beanstalk" and "deployment" without manual field setup.

## Template Compatibility

This add-on is designed to work with drag-and-drop fill-in-the-blank templates that use the `[[dN::text]]` syntax. The templates automatically extract draggable items from this syntax, requiring only:

- **Question Field**: Contains text with `[[d1::text]]` syntax (created by this add-on)
- **Explain Field**: Optional explanation/notes field
- **Smart Template**: Automatically parses `[[d1::text]]` patterns and generates draggable items

**No manual field population required** - the template handles everything automatically.

## Installation

1. Copy the `drag_drop_addon` folder to your Anki add-ons directory
2. Restart Anki
3. The `[...]` button will appear in the editor toolbar

## Keyboard Shortcuts

- **Ctrl+Shift+D** (Windows/Linux) or **Cmd+Shift+D** (Mac): Create drag-drop blank

## Error Messages

- **"Please select some text first"**: You need to highlight text before clicking the button
- **"Selected text is empty"**: The highlighted text contains only whitespace
- **"Selected text already contains drag-drop blanks"**: The selection already has `[[dN::text]]` syntax

## Configuration

The add-on includes a `config.json` file where you can customize:
- Keyboard shortcut
- Success tooltip visibility
- Button tooltip text

## Technical Details

- **Native Qt Integration**: Uses `editor.web.selectedText()` property directly from Qt
- **Smart Counter Logic**: Scans current field content using regex `\[\[d(\d+)::[^\]]+\]\]`
- **Robust Text Replacement**: Uses `document.execCommand('insertText')` with range fallback
- **Cross-Platform**: Works on Anki Desktop (Windows, Mac, Linux)
- **Version Compatibility**: Requires Anki 2.1.45+

## Implementation Notes

### ✅ **Fixed Architecture (Version 1.0.1)**
- **Selection Detection**: Native Qt `editor.web.selectedText()` API (bypasses JavaScript issues)
- **Keyboard Shortcuts**: Qt `QShortcut` with `QKeySequence` (reliable cross-platform)
- **Text Replacement**: Modern `execCommand('insertText')` with manual range fallback
- **Error Handling**: Comprehensive validation with user-friendly messages

### 🚫 **Previous Issues (Version 1.0.0)**
The original implementation failed because it attempted JavaScript-based selection detection in QtWebEngine, which has fundamental limitations. The fix was to use Qt's native APIs instead.

## Version History

- **1.0.1**: ✅ **WORKING** - Native Qt implementation with `selectedText()` API
- **1.0.0**: ❌ Non-functional - JavaScript selection detection approach failed