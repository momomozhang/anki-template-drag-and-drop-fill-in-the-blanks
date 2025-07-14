## 🤖 Claude Code Development Showcase

**A complete project built entirely with Claude Code - from concept to deployment**

This interactive fill-in-the-blank flashcard system for Anki demonstrates the power of AI-assisted development using Claude Code. Every line of code, documentation, feature, as well as git & Github actions was created through collaborative programming with Claude Code agent.

### 🎯 Project Goals
- **Primary**: Showcase Claude Code's capability to build complete, functional projects ✅
- **Secondary**: Solve real Anki users' need for interactive drag-and-drop flashcards ✅

### ✨ Features
Transform any text into an engaging learning exercise where words or phrases are removed from sentences and become draggable items that students must place back in the correct positions.

- **Drag & Drop Interface**: HTML5 native drag-and-drop API
- **Visual Feedback**: Instant success/error indicators  
- **Cross-Platform**: Works on Anki Desktop, AnkiWeb, and mobile apps
- **Randomization**: Shuffled item order prevents pattern memorization
- **Smart Parsing**: Automatically extracts draggable items from `[[d1::text]]` syntax
- **Streamlined Workflow**: No manual field population required

### 💡 Use Cases
- Language learning (vocabulary, grammar)
- Medical terminology
- Historical facts and dates
- Code syntax practice

### 📋 Project Status
- ✅ **Templates**: Fully functional drag-and-drop interface
- ✅ **Cross-platform**: Works on all Anki platforms
- ✅ **Add-on automation**: **FIXED** - Working automation using native Qt APIs

**The project is now complete** - both interactive templates and automation work perfectly.

### 🔧 **Automation Fix Summary**
**Issue Solved**: The original add-on failed because it used JavaScript selection detection in QtWebEngine, which has fundamental limitations. Through systematic analysis using Claude Code and Zen MCP tools, we discovered that Qt provides native `selectedText()` APIs that completely bypass JavaScript limitations.

**Solution**: Replaced 500+ lines of complex JavaScript selection monitoring with simple native Qt API calls:
```python
selected_text = editor.web.selectedText()  # Works reliably
```