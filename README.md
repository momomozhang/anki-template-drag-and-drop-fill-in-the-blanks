## 🤖 Claude Code Development Showcase

**A complete project built entirely with Claude Code - from concept to deployment**

In this repo, every line of code, documentation, feature, as well as git & Github actions was created through collaborative programming with Claude Code agent. What's my point? Claude Code is no magic, you still need to learn & practice how to use it!

Check `documentation` folder for the learnings! 

### ✨ Features
Transform any text into an engaging learning exercise where words or phrases are removed from sentences and become draggable items that students must place back in the correct positions.

### Installation & Usage

**Initial Setup:**
1. **Install Add-on**: 
   - Find your Anki add-ons directory:
     - **Windows**: `%APPDATA%\Anki2\addons21\`
     - **Mac**: `~/Library/Application Support/Anki2/addons21/`
     - **Linux**: `~/.local/share/Anki2/addons21/`
     - **Alternative**: Tools → Add-ons → View Files (opens the directory)
   - Copy the `drag_drop_addon` folder to this directory
   - Restart Anki to load the add-on
2. **Configure Note Type**:
   - Tools → Manage Note Types → Add (or select existing)
   - Add fields: Question, Explain (optional)
   - Click "Cards..." to edit templates

**Template Configuration:**
1. **Front Template**: Clear existing content, paste `front.html`
2. **Back Template**: Clear existing content, paste `back.html`  
3. **Styling**: Clear existing styles, paste `style.css`
4. Save and close

**Content Creation Workflow:**
1. **Add Note**: Browse → Add (or press 'A')
2. **Enter Text**: Type or paste content in Question field
3. **Create Blanks**: 
   - Select text you want as draggable item
   - Press `Ctrl+Shift+D` or click ❤️ button
   - Text becomes `[[d1::word]]` format
   - Repeat for additional blanks (auto-increments)
4. **Add Explanation** (optional): Use Explain field for context

**Study Experience:**
1. **Front Side**: See text with input boxes and draggable items below
2. **Interact**: Drag items to correct positions in text
3. **Check**: Click "Show Answers" for color-coded feedback:
   - Green: Correct placement
   - Red: Incorrect placement  
   - Grey: Auto-filled correct answers
4. **Reset**: Click "Reset" to try again or continue to back
5. **Back Side**: See clean text with answers filled in

**Tips:**
- Supports HTML formatting (bold, italic, colors)
- Works on desktop, web, and mobile
- Items are shuffled to prevent memorization
- Click filled blanks to remove items
