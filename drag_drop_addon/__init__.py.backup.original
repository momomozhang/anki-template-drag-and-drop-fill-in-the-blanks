# Drag-and-Drop Blanks Add-on for Anki
# Adds a toolbar button to create [[dN::text]] syntax for drag-and-drop templates
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
        
        # Find next available counter (existing logic)
        pattern = r'\[\[d(\d+)::[^\]]+\]\]'
        matches = re.findall(pattern, field_content)
        next_counter = max([int(match) for match in matches]) + 1 if matches else 1
        
        # Create the drag-drop syntax
        wrapped_text = f"[[d{next_counter}::{selected_text}]]"
        
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
                tooltip(f"✅ Created d{next_counter}: \"{selected_text[:30]}{'...' if len(selected_text) > 30 else ''}\"", 2000)
                print(f"Drag-Drop: Success - Created d{next_counter} using {method}")
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
    """Minimal button setup with native Qt integration"""
    
    print("Drag-Drop Blanks: Setting up minimal version...")
    
    # Setup keyboard shortcut using native Qt
    setup_keyboard_shortcut_minimal(editor)
    
    # Add optional visual button
    try:
        # Try modern API first
        if hasattr(editor, 'addButton'):
            button = editor.addButton(
                icon=":/icons/cloze.png",
                cmd="drag_drop_minimal",
                tip="Create drag-drop blank [[dN::text]] with Ctrl+Shift+D",
                func=lambda e: create_drag_drop_blank_minimal(e)
            )
            print("Drag-Drop Blanks: Button created with modern API")
            return buttons + [button]
        else:
            # Fallback to legacy API
            editor._links['drag_drop_minimal'] = lambda e: create_drag_drop_blank_minimal(e)
            button = editor._addButton(
                ":/icons/cloze.png",
                "drag_drop_minimal", 
                "Create drag-drop blank [[dN::text]] with Ctrl+Shift+D"
            )
            print("Drag-Drop Blanks: Button created with legacy API")
            return buttons + [button]
            
    except Exception as e:
        print(f"Drag-Drop Blanks: Button creation failed: {e}")
        # Still return buttons even if button creation fails
        return buttons

def show_shortcut_info():
    """Show information about using the keyboard shortcut"""
    showInfo("Drag-Drop Blank Creator\n\nTo create drag-drop blanks:\n\n1. Select text with your mouse\n2. Press Ctrl+Shift+D (or Cmd+Shift+D on Mac)\n\nExample:\nSelect 'Python' → Press Ctrl+Shift+D → Get [[d1::Python]]\n\nThe blanks will be automatically numbered (d1, d2, d3...)")

# Replace existing hook with minimal version
print("Drag-Drop Blanks: Setting up minimal button hook...")
addHook("setupEditorButtons", add_drag_drop_button_minimal)

print("Drag-Drop Blanks: Add-on loaded successfully (Version 1 - Native Qt)")