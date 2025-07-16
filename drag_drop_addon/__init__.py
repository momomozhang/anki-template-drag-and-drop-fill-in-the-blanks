# Drag-and-Drop Blanks Add-on for Anki
# Adds a toolbar button to create [[d::text]] syntax for drag-and-drop templates
# Version 1: Minimal Refactor using native Qt APIs

from anki.hooks import addHook
from aqt.editor import Editor
from aqt import mw
from aqt.utils import showInfo, tooltip
from aqt.qt import QShortcut, QKeySequence
import re
import json

# Debug: Print when add-on loads
print("Drag-Drop Blanks Add-on: Loading (Version 1 - Native Qt)...")

def create_drag_drop_blank_minimal(editor):
    """Minimal refactor: Replace JS selection with native Qt API"""
    
    try:
        # Use native Qt API instead of JavaScript
        selected_text = editor.web.selectedText().strip()
        
        if not selected_text:
            showInfo("Please select some text first.\n\nTo create a drag-drop blank:\n1. Select text with your mouse\n2. Press Ctrl+Shift+D (or Cmd+Shift+D on Mac)")
            return
        
        # Existing validation logic (unchanged)
        if '[[d' in selected_text and '::' in selected_text and ']]' in selected_text:
            showInfo("Selected text already contains drag-drop blanks.")
            return
        
        # Basic length validation
        if len(selected_text) > 200:
            showInfo("Selected text is too long (max 200 characters).")
            return
        
        # Get current field content for counter detection
        current_field = editor.currentField
        if current_field is None:
            showInfo("Please click in a field first.")
            return
        
        field_content = editor.note.fields[current_field]
        
        # Create the simplified drag-drop syntax (no numbering needed)
        wrapped_text = f"[[d::{selected_text}]]"
        
        # Replace selected text using reliable insertText
        js_code = f"""
        (function() {{
            try {{
                // Modern approach: use execCommand if supported
                if (document.queryCommandSupported && document.queryCommandSupported('insertText')) {{
                    var success = document.execCommand('insertText', false, {json.dumps(wrapped_text)});
                    if (success) {{
                        return {{success: true, method: 'execCommand'}};
                    }}
                }}
                
                // Fallback: manual range replacement if there's a selection
                var selection = window.getSelection();
                if (selection.rangeCount > 0) {{
                    var range = selection.getRangeAt(0);
                    range.deleteContents();
                    var textNode = document.createTextNode({json.dumps(wrapped_text)});
                    range.insertNode(textNode);
                    
                    // Clear selection
                    selection.removeAllRanges();
                    
                    // Trigger Anki's change detection
                    var event = new Event('input', {{bubbles: true}});
                    if (document.activeElement) {{
                        document.activeElement.dispatchEvent(event);
                    }}
                    
                    return {{success: true, method: 'range'}};
                }}
                
                return {{success: false, error: 'No selection available'}};
                
            }} catch (e) {{
                return {{success: false, error: e.message}};
            }}
        }})();
        """
        
        def replacement_callback(result):
            if result and result.get('success'):
                method = result.get('method', 'unknown')
                tooltip(f"✅ Created blank: \"{selected_text[:30]}{'...' if len(selected_text) > 30 else ''}\"", 2000)
                print(f"Drag-Drop: Success - Created blank using {method}")
            else:
                error = result.get('error', 'Unknown error') if result else 'Replacement failed'
                showInfo(f"Could not create drag-drop blank: {error}\n\nPlease try selecting the text again.")
                print(f"Drag-Drop: Replacement failed: {error}")
        
        editor.web.evalWithCallback(js_code, replacement_callback)
        
    except Exception as e:
        showInfo(f"Error creating drag-drop blank: {str(e)}")
        print(f"Drag-Drop: Unexpected error: {e}")

def setup_keyboard_shortcut_minimal(editor):
    """Setup Ctrl+Shift+D shortcut with native Qt API"""
    
    try:
        # Create shortcut for this editor
        shortcut = QShortcut(QKeySequence("Ctrl+Shift+D"), editor.widget)
        shortcut.activated.connect(lambda: create_drag_drop_blank_minimal(editor))
        
        # Store reference to prevent garbage collection
        if not hasattr(editor, '_drag_drop_shortcuts'):
            editor._drag_drop_shortcuts = []
        editor._drag_drop_shortcuts.append(shortcut)
        
        print("Drag-Drop: Keyboard shortcut Ctrl+Shift+D setup successful")
        
    except Exception as e:
        print(f"Drag-Drop: Shortcut setup failed: {e}")

def add_drag_drop_button_minimal(buttons, editor):
    """Robust button setup with emoji fallback strategies"""
    
    print("Drag-Drop Blanks: Setting up robust version...")
    
    # Setup keyboard shortcut using native Qt
    setup_keyboard_shortcut_minimal(editor)
    
    # Progressive enhancement for emoji support
    def attempt_emoji_button(emoji_text):
        """Try to create button with emoji text"""
        try:
            if hasattr(editor, 'addButton'):
                # Modern API attempts
                try:
                    # Method 1: Direct text parameter
                    return editor.addButton(
                        text=emoji_text,
                        cmd="drag_drop_minimal",
                        tip=f"Create drag-drop blank [[d::text]] with Ctrl+Shift+D {emoji_text}",
                        func=lambda e: create_drag_drop_blank_minimal(e)
                    )
                except (TypeError, AttributeError):
                    # Method 2: No icon + JS injection
                    button = editor.addButton(
                        icon=None,
                        cmd="drag_drop_minimal",
                        tip=f"Create drag-drop blank [[d::text]] with Ctrl+Shift+D {emoji_text}",
                        func=lambda e: create_drag_drop_blank_minimal(e)
                    )
                    # Inject emoji via JavaScript
                    emoji_js = f"""
                    setTimeout(function() {{
                        var btn = document.querySelector('[title*="drag-drop blank"]');
                        if (btn) btn.innerHTML = '{emoji_text}';
                    }}, 100);
                    """
                    editor.web.eval(emoji_js)
                    return button
            else:
                # Legacy API
                editor._links['drag_drop_minimal'] = lambda e: create_drag_drop_blank_minimal(e)
                return editor._addButton(
                    emoji_text,
                    "drag_drop_minimal", 
                    f"Create drag-drop blank [[d::text]] with Ctrl+Shift+D {emoji_text}"
                )
        except Exception as e:
            print(f"Drag-Drop Blanks: Failed to create button with '{emoji_text}': {e}")
            return None

    def attempt_icon_fallback():
        """Fallback to original icon"""
        try:
            if hasattr(editor, 'addButton'):
                return editor.addButton(
                    icon=":/icons/cloze.png",
                    cmd="drag_drop_minimal",
                    tip="Create drag-drop blank [[d::text]] with Ctrl+Shift+D",
                    func=lambda e: create_drag_drop_blank_minimal(e)
                )
            editor._links['drag_drop_minimal'] = lambda e: create_drag_drop_blank_minimal(e)
            return editor._addButton(
                ":/icons/cloze.png",
                "drag_drop_minimal",
                "Create drag-drop blank [[d::text]] with Ctrl+Shift+D"
            )
        except Exception as e:
            print(f"Drag-Drop Blanks: Icon fallback failed: {e}")
            return None

    # Try emoji options in order of preference
    emoji_options = ["❤️", "♥️", "💙", "♡"]

    for emoji in emoji_options:
        button = attempt_emoji_button(emoji)
        if button:
            print(f"Drag-Drop Blanks: Successfully created button with emoji: {emoji}")
            return buttons + [button]

    # Final fallback to original icon
    button = attempt_icon_fallback()
    if button:
        print("Drag-Drop Blanks: Using original icon as fallback")
        return buttons + [button]

    print("Drag-Drop Blanks: All button creation attempts failed")
    return buttons

def show_shortcut_info():
    """Show information about using the keyboard shortcut"""
    info_text = (
        "Drag-Drop Blank Creator\n\n"
        "To create drag-drop blanks:\n\n"
        "1. Select text with your mouse\n"
        "2. Press Ctrl+Shift+D (or Cmd+Shift+D on Mac)\n\n"
        "Example:\n"
        "Select 'Python' → Press Ctrl+Shift+D → Get [[d::Python]]\n\n"
        "The template will handle numbering automatically for compatibility."
    )
    showInfo(info_text)

# Replace existing hook with minimal version
print("Drag-Drop Blanks: Setting up minimal button hook...")
addHook("setupEditorButtons", add_drag_drop_button_minimal)

print("Drag-Drop Blanks: Add-on loaded successfully (Version 3 - Robust Emoji)")