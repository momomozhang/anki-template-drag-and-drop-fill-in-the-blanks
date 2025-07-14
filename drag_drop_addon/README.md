# Drag-and-Drop Blanks Creator Add-on

This Anki add-on adds a toolbar button to create `[[dN::text]]` syntax for drag-and-drop fill-in-the-blank templates.

## Features

- **Smart Counter Detection**: Automatically detects existing `[[d1::text]]`, `[[d2::text]]`, etc. and uses the next available number
- **Keyboard Shortcut**: Use `Ctrl+Shift+D` to quickly create blanks
- **Error Handling**: Provides helpful feedback when text selection is invalid
- **Per-Card Intelligence**: Scans each card individually to determine the correct counter number

## How to Use

1. **Select Text**: Highlight the text you want to turn into a drag-drop blank
2. **Click Button**: Click the `[...]` button in the editor toolbar (or use `Ctrl+Shift+D`)
3. **Result**: Selected text becomes `[[dN::text]]` where N is automatically determined

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

## Template Compatibility

This add-on is designed to work with drag-and-drop fill-in-the-blank templates that use the `[[dN::text]]` syntax. It will work with any note type, but is specifically designed for:

- Drag-and-Drop Fill Blanks templates
- Custom templates using square bracket syntax
- Any template that parses `[[d1::text]]` patterns

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

- **Smart Counter Logic**: Scans current field content using regex `/\\[\\[d(\\d+)::[^\\]]+\\]\\]/g`
- **Cross-Platform**: Works on Anki Desktop (Windows, Mac, Linux)
- **Version Compatibility**: Requires Anki 2.1.45+

## Current Status: NON-FUNCTIONAL

⚠️ **This add-on does not work due to Anki editor limitations**

### Issue Summary
The add-on button appears but cannot detect text selections due to Anki's editor architecture. Extensive debugging revealed:

### Failed Approaches Tried
1. **Standard JavaScript `window.getSelection()`** - Returns empty in Anki's editor
2. **Anki's `editor.web.selectedText()`** - Deprecated/unreliable in modern versions
3. **Event-based selection capture** - `selectionchange` events don't fire in Anki
4. **Mouse/keyboard event monitoring** - Events fire but selection data unavailable
5. **Multiple API compatibility layers** - All selection detection methods failed

### Root Cause
Anki's QtWebEngine editor uses a custom selection system that doesn't expose selections to JavaScript add-ons. The selection is cleared when keyboard shortcuts are triggered, making automation impossible.

## Version History

- **1.0.0**: Initial release attempt - non-functional due to selection detection issues