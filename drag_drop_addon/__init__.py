# Drag-and-Drop Blanks Add-on for Anki
# Adds a toolbar button to create [[dN::text]] syntax for drag-and-drop templates

from anki.hooks import addHook
from aqt.editor import Editor
from aqt import mw
from aqt.utils import showInfo, tooltip
import re
import json
import time

# Try to import gui_hooks, fallback if not available
try:
    from aqt import gui_hooks
    HAS_GUI_HOOKS = True
except ImportError:
    HAS_GUI_HOOKS = False

# Debug: Print when add-on loads
print("Drag-Drop Blanks Add-on: Loading...")

def show_debug_message(message, duration=5000):
    """Show debug message that stays visible for specified duration"""
    tooltip(f"🐛 DEBUG: {message}", duration)
    print(f"Drag-Drop Debug: {message}")

def inject_shortcut_handler(editor):
    """Inject JavaScript that monitors selections and handles Ctrl+Shift+D"""
    
    js_code = """
    (function() {
        // Remove any existing listeners to avoid duplicates
        if (window.dragDropKeyListener) {
            document.removeEventListener('keydown', window.dragDropKeyListener);
        }
        if (window.dragDropMouseListener) {
            document.removeEventListener('mouseup', window.dragDropMouseListener);
        }
        if (window.dragDropKeyUpListener) {
            document.removeEventListener('keyup', window.dragDropKeyUpListener);
        }
        
        // Create debug display function
        window.showDebugMsg = function(msg) {
            // Create or update debug display
            var debugDiv = document.getElementById('drag-drop-debug');
            if (!debugDiv) {
                debugDiv = document.createElement('div');
                debugDiv.id = 'drag-drop-debug';
                debugDiv.style.cssText = `
                    position: fixed;
                    top: 10px;
                    right: 10px;
                    background: #ff4444;
                    color: white;
                    padding: 10px;
                    border-radius: 5px;
                    z-index: 9999;
                    font-family: monospace;
                    font-size: 12px;
                    max-width: 300px;
                    word-wrap: break-word;
                `;
                document.body.appendChild(debugDiv);
            }
            
            var timestamp = new Date().toLocaleTimeString();
            debugDiv.innerHTML = timestamp + '<br>' + msg;
            
            // Auto-remove after 8 seconds
            setTimeout(function() {
                if (debugDiv && debugDiv.parentNode) {
                    debugDiv.parentNode.removeChild(debugDiv);
                }
            }, 8000);
        };
        
        // Selection storage with complete context
        window.dragDropSelection = {
            data: null,
            
            store: function(selection) {
                if (selection.rangeCount === 0 || selection.isCollapsed) return;
                
                var range = selection.getRangeAt(0);
                var activeField = document.activeElement;
                
                // Only store if in a valid editor field
                if (!activeField || (!activeField.isContentEditable && activeField.tagName !== 'DIV')) {
                    window.showDebugMsg('⚠️ Not storing - not in valid field');
                    return;
                }
                
                var selectedText = selection.toString().trim();
                if (selectedText.length === 0) {
                    window.showDebugMsg('⚠️ Not storing - empty selection');
                    return;
                }
                
                this.data = {
                    text: selectedText,
                    range: {
                        startContainer: range.startContainer,
                        startOffset: range.startOffset,
                        endContainer: range.endContainer,
                        endOffset: range.endOffset,
                        commonAncestor: range.commonAncestorContainer
                    },
                    field: activeField,
                    fieldContent: activeField.innerHTML,
                    timestamp: Date.now()
                };
                
                window.showDebugMsg('📝 Stored selection: "' + selectedText + '"');
                console.log('Stored selection:', this.data.text);
            },
            
            isValid: function() {
                if (!this.data) {
                    window.showDebugMsg('❌ No stored selection data');
                    return false;
                }
                
                // Check if too old (10 seconds)
                if (Date.now() - this.data.timestamp > 10000) {
                    window.showDebugMsg('❌ Stored selection too old');
                    this.clear();
                    return false;
                }
                
                // Check if field still exists and has same content
                if (!this.data.field || !document.contains(this.data.field)) {
                    window.showDebugMsg('❌ Field no longer exists');
                    this.clear();
                    return false;
                }
                
                // Check if field content changed significantly
                if (this.data.field.innerHTML !== this.data.fieldContent) {
                    window.showDebugMsg('❌ Field content changed');
                    this.clear();
                    return false;
                }
                
                window.showDebugMsg('✅ Stored selection is valid');
                return true;
            },
            
            restore: function() {
                if (!this.isValid()) return null;
                
                try {
                    var range = document.createRange();
                    range.setStart(this.data.range.startContainer, this.data.range.startOffset);
                    range.setEnd(this.data.range.endContainer, this.data.range.endOffset);
                    
                    var selection = window.getSelection();
                    selection.removeAllRanges();
                    selection.addRange(range);
                    
                    window.showDebugMsg('🔄 Restored selection: "' + this.data.text + '"');
                    return this.data;
                } catch (e) {
                    window.showDebugMsg('❌ Failed to restore selection: ' + e.message);
                    console.log('Failed to restore selection:', e);
                    this.clear();
                    return null;
                }
            },
            
            clear: function() {
                this.data = null;
                window.showDebugMsg('🗑️ Cleared stored selection');
            }
        };
        
        // Monitor mouse selections
        window.dragDropMouseListener = function(e) {
            setTimeout(function() {  // Small delay to let selection settle
                var selection = window.getSelection();
                if (selection.rangeCount > 0 && !selection.isCollapsed) {
                    window.dragDropSelection.store(selection);
                }
            }, 10);
        };
        
        // Monitor keyboard selections (Shift+arrows, Ctrl+A, etc.)
        window.dragDropKeyUpListener = function(e) {
            if (e.shiftKey || e.ctrlKey || e.metaKey) {  // Selection modifiers
                setTimeout(function() {
                    var selection = window.getSelection();
                    if (selection.rangeCount > 0 && !selection.isCollapsed) {
                        window.dragDropSelection.store(selection);
                    }
                }, 10);
            }
        };
        
        // Keyboard handler for Cmd+Shift+D
        window.dragDropKeyListener = function(e) {
            // Debug all key presses to see what we're getting
            if (e.shiftKey && (e.ctrlKey || e.metaKey)) {
                window.showDebugMsg('⌨️ Key: ' + e.key + ' (Ctrl:' + e.ctrlKey + ', Meta:' + e.metaKey + ', Shift:' + e.shiftKey + ')');
            }
            
            // Check for Ctrl+Shift+D (or Cmd+Shift+D on Mac)
            if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key === 'D') {
                e.preventDefault();
                e.stopPropagation();
                
                window.showDebugMsg('✅ Keyboard shortcut detected: Cmd+Shift+D');
                
                // Try to use stored selection
                var selectionData = window.dragDropSelection.data;
                
                if (selectionData && window.dragDropSelection.isValid()) {
                    window.showDebugMsg('🎯 Using stored selection: "' + selectionData.text + '"');
                    
                    // Send data to Python via pycmd
                    var data = {
                        text: selectionData.text,
                        content: selectionData.fieldContent,
                        debug: {
                            timestamp: selectionData.timestamp,
                            age: Date.now() - selectionData.timestamp,
                            fieldTag: selectionData.field.tagName
                        }
                    };
                    
                    pycmd('drag_drop_create:' + JSON.stringify(data));
                } else {
                    window.showDebugMsg('❌ No valid stored selection available');
                    pycmd('drag_drop_error:no_selection');
                }
            }
        };
        
        // Add all event listeners
        document.addEventListener('mouseup', window.dragDropMouseListener, true);
        document.addEventListener('keyup', window.dragDropKeyUpListener, true);
        document.addEventListener('keydown', window.dragDropKeyListener, true);
        
        // Also try adding to window level
        window.addEventListener('mouseup', window.dragDropMouseListener, true);
        window.addEventListener('keyup', window.dragDropKeyUpListener, true);
        window.addEventListener('keydown', window.dragDropKeyListener, true);
        
        // Test selection detection after setup
        setTimeout(function() {
            var testSelection = window.getSelection();
            window.showDebugMsg('🔧 Selection storage system loaded');
            console.log('Selection storage system loaded, current selection:', testSelection.toString());
        }, 100);
        
        return true;
    })();
    """
    
    def injection_callback(result):
        if result:
            show_debug_message("JavaScript selection monitor injected successfully", 3000)
            print("Drag-Drop Blanks: JavaScript selection monitor injected successfully")
        else:
            show_debug_message("FAILED to inject JavaScript selection monitor", 5000)
            print("Drag-Drop Blanks: Failed to inject JavaScript selection monitor")
    
    editor.web.evalWithCallback(js_code, injection_callback)

def handle_drag_drop_command(editor, cmd, data_str):
    """Handle commands from JavaScript"""
    
    print(f"Drag-Drop: Received command: {cmd}")
    show_debug_message(f"Python received: {cmd}", 3000)
    
    if cmd == 'drag_drop_error':
        error_type = data_str
        show_debug_message(f"Error from JS: {error_type}", 5000)
        
        if error_type == 'no_selection':
            showInfo("Please select some text first.\n\nTo create a drag-drop blank:\n1. Select text with your mouse\n2. Press Ctrl+Shift+D (or Cmd+Shift+D on Mac)")
        elif error_type == 'empty_selection':
            showInfo("Selected text is empty. Please select some text first.")
        elif error_type == 'already_formatted':
            showInfo("Selected text already contains drag-drop blanks.")
        else:
            showInfo(f"Error: {error_type}")
        return
    
    if cmd == 'drag_drop_create':
        try:
            data = json.loads(data_str)
            selected_text = data.get('text', '')
            content = data.get('content', '')
            debug_info = data.get('debug', {})
            
            show_debug_message(f"Processing: '{selected_text}' (len={len(selected_text)})", 3000)
            print(f"Drag-Drop: Processing selection: '{selected_text}'")
            print(f"Drag-Drop: Debug info: {debug_info}")
            
            # Check if selected text already contains drag-drop syntax
            if '[[d' in selected_text and '::' in selected_text and ']]' in selected_text:
                show_debug_message("Text already contains drag-drop syntax", 3000)
                showInfo("Selected text already contains drag-drop blanks.")
                return
            
            # Find the highest existing counter number in the content
            pattern = r'\[\[d(\d+)::[^\]]+\]\]'
            matches = re.findall(pattern, content)
            
            if matches:
                counters = [int(match) for match in matches]
                next_counter = max(counters) + 1
            else:
                next_counter = 1
            
            # Create the drag-drop syntax
            wrapped_text = f"[[d{next_counter}::{selected_text}]]"
            
            show_debug_message(f"Creating d{next_counter}: {wrapped_text}", 3000)
            print(f"Drag-Drop: Creating blank d{next_counter}: {wrapped_text}")
            
            # Replace the selected text in the editor
            replace_selected_text(editor, selected_text, wrapped_text, next_counter)
            
        except json.JSONDecodeError as e:
            show_debug_message(f"JSON decode error: {e}", 5000)
            print(f"Drag-Drop: JSON decode error: {e}")
            showInfo("Error processing selection data.")
        except Exception as e:
            show_debug_message(f"Unexpected error: {e}", 5000)
            print(f"Drag-Drop: Unexpected error: {e}")
            showInfo(f"Unexpected error: {e}")

def replace_selected_text(editor, original_text, wrapped_text, counter):
    """Replace selected text with drag-drop syntax using stored selection"""
    
    # Escape special characters for JavaScript
    original_escaped = original_text.replace("'", "\\'").replace('"', '\\"').replace('\n', '\\n')
    wrapped_escaped = wrapped_text.replace("'", "\\'").replace('"', '\\"').replace('\n', '\\n')
    
    js_code = f"""
    (function() {{
        window.showDebugMsg('🔄 Starting text replacement');
        
        // Try to restore the stored selection first
        var selectionData = window.dragDropSelection.restore();
        
        if (selectionData) {{
            var selection = window.getSelection();
            
            if (selection.rangeCount > 0 && !selection.isCollapsed) {{
                var range = selection.getRangeAt(0);
                var selectedText = selection.toString().trim();
                
                window.showDebugMsg('🔍 Current selection: "' + selectedText + '"');
                window.showDebugMsg('🎯 Target text: "{original_escaped}"');
                
                // Verify we have the right selection
                if (selectedText === '{original_escaped}') {{
                    // Replace selection with wrapped text
                    range.deleteContents();
                    range.insertNode(document.createTextNode('{wrapped_escaped}'));
                    
                    // Clear selection
                    selection.removeAllRanges();
                    
                    // Trigger Anki's change detection
                    var event = new Event('input', {{bubbles: true}});
                    document.activeElement.dispatchEvent(event);
                    
                    // Clear stored selection since we used it
                    window.dragDropSelection.clear();
                    
                    window.showDebugMsg('✅ Successfully replaced text');
                    return {{success: true, counter: {counter}, text: '{original_escaped}'}};
                }}
            }}
        }}
        
        // Fallback: replace in content directly using stored field
        if (window.dragDropSelection.data && window.dragDropSelection.data.field) {{
            var field = window.dragDropSelection.data.field;
            if (field && (field.tagName === 'DIV' || field.isContentEditable)) {{
                var content = field.innerHTML;
                var newContent = content.replace('{original_escaped}', '{wrapped_escaped}');
                
                if (newContent !== content) {{
                    field.innerHTML = newContent;
                    
                    // Trigger Anki's change detection
                    var event = new Event('input', {{bubbles: true}});
                    field.dispatchEvent(event);
                    
                    // Clear stored selection since we used it
                    window.dragDropSelection.clear();
                    
                    window.showDebugMsg('✅ Fallback replacement successful');
                    return {{success: true, counter: {counter}, text: '{original_escaped}'}};
                }}
            }}
        }}
        
        window.showDebugMsg('❌ Replacement failed - no valid selection or field');
        return {{success: false, error: 'Could not replace text'}};
    }})();
    """
    
    def replacement_callback(result):
        if result and result.get('success'):
            counter = result.get('counter')
            text = result.get('text')
            show_debug_message(f"SUCCESS: Created d{counter}", 3000)
            tooltip(f"Created drag-drop blank d{counter}: \"{text}\"", 2000)
            print(f"Drag-Drop: Success - Created d{counter}")
        else:
            error = result.get('error', 'Unknown error') if result else 'Replacement failed'
            show_debug_message(f"REPLACEMENT FAILED: {error}", 5000)
            showInfo(f"Could not create drag-drop blank: {error}")
            print(f"Drag-Drop: Replacement failed: {error}")
    
    editor.web.evalWithCallback(js_code, replacement_callback)

def setup_command_handler(editor):
    """Setup the command handler for pycmd communication"""
    
    # Store original onBridgeCmd if it exists
    original_handler = getattr(editor.web, 'onBridgeCmd', None)
    
    def bridge_cmd_handler(cmd):
        """Handle bridge commands from JavaScript"""
        
        if cmd.startswith('drag_drop_'):
            # Extract command and data
            if ':' in cmd:
                command, data = cmd.split(':', 1)
            else:
                command, data = cmd, ''
            
            handle_drag_drop_command(editor, command, data)
            return
        
        # Pass through to original handler if it exists
        if original_handler:
            original_handler(cmd)
    
    # Replace the bridge command handler
    editor.web.onBridgeCmd = bridge_cmd_handler
    show_debug_message("Bridge command handler setup", 2000)
    print("Drag-Drop: Bridge command handler setup complete")

def add_smart_drag_button(buttons, editor):
    """Add smart drag-drop button to editor toolbar"""
    
    print("Drag-Drop Blanks: Adding button to toolbar...")
    show_debug_message("Setting up add-on button", 2000)
    
    # Setup command handler for this editor instance
    setup_command_handler(editor)
    
    # Inject JavaScript handler when editor is ready
    def inject_when_ready():
        show_debug_message("Injecting JavaScript selection monitor", 2000)
        inject_shortcut_handler(editor)
    
    # Inject after a short delay to ensure editor is fully loaded
    mw.progress.timer(100, inject_when_ready, False)
    
    # Add visible button as indicator/help
    try:
        # Try modern API first
        if hasattr(editor, 'addButton'):
            button = editor.addButton(
                icon=":/icons/cloze.png",
                cmd="smart_drag_blank_info",
                tip="Create drag-drop blank [[dN::text]] with Ctrl+Shift+D",
                func=lambda e: show_shortcut_info()
            )
            show_debug_message("Button created with modern API", 2000)
            print("Drag-Drop Blanks: Button created with modern API")
        else:
            # Fallback to legacy API
            editor._links['smart_drag_blank_info'] = show_shortcut_info
            button = editor._addButton(
                ":/icons/cloze.png",
                "smart_drag_blank_info",
                "Create drag-drop blank [[dN::text]] with Ctrl+Shift+D"
            )
            show_debug_message("Button created with legacy API", 2000)
            print("Drag-Drop Blanks: Button created with legacy API")
        
        return buttons + [button]
    except Exception as e:
        show_debug_message(f"Button creation failed: {e}", 5000)
        print(f"Drag-Drop Blanks: Error creating button: {e}")
        return buttons

def show_shortcut_info():
    """Show information about using the keyboard shortcut"""
    showInfo("To create drag-drop blanks:\n\n1. Select text with your mouse\n2. Press Ctrl+Shift+D (or Cmd+Shift+D on Mac)\n\nExample:\nSelect 'Python' → Press Ctrl+Shift+D → Get [[d1::Python]]")

# Hook into Anki's editor button setup
print("Drag-Drop Blanks: Setting up button hook...")
addHook("setupEditorButtons", add_smart_drag_button)

print("Drag-Drop Blanks: Add-on loaded successfully")