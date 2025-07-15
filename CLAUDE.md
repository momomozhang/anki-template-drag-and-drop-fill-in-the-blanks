# Anki Drag-and-Drop Template Project

## Project Overview

This is an interactive Anki flashcard template that creates drag-and-drop fill-in-the-blank exercises. Built entirely with Claude Code assistance, it demonstrates sophisticated AI collaboration and solves a real need for Anki users seeking more interactive learning experiences.

### Key Features:
- **Interactive Learning**: Drag words/phrases to fill blanks in sentences
- **Cross-Platform**: HTML5 drag-and-drop API works on Anki Desktop, AnkiWeb, and mobile
- **Visual Feedback**: Color-coded answers when revealing solutions
- **Randomization**: Shuffled item order prevents pattern memorization
- **Automation**: One-click blank creation with auto-incrementing
- **Versatile**: Supports language learning, medical terminology, history, coding practice

### Technical Architecture:
- **Frontend**: HTML5 drag-and-drop with JavaScript state management
- **Backend**: Python Anki add-on using native Qt APIs
- **Template**: CSS-styled responsive interface
- **Compatibility**: Cross-platform Anki environment support

## System Specifications

### Field Structure
- **Question Field**: Contains text with `[[d1::selected_text]]` syntax
- **Explain Field**: Optional explanations/context for answers
- **Single-Card System**: One interactive card showing all blanks simultaneously

### User Workflow
1. **Content Creation**: Paste text into Question field
2. **Blank Creation**: Select text → Press `Ctrl+Shift+D` → Creates `[[d1::text]]`
3. **Auto-increment**: Automatically detects existing blanks and increments counter
4. **Study**: Drag items to fill underlined gaps within text
5. **Show Answers**: Click "Show Answers" to see correct answers with color coding

### Study Experience
- **Front**: "You simply upload your code and _________ automatically handles the _________"
- **Interaction**: Drag items to fill underlined gaps
- **Show Answers**: Click button to reveal correct answers with intelligent color coding:
  - **Green**: User-placed correct answers
  - **Red**: User-placed incorrect answers  
  - **Grey**: Auto-filled correct answers for empty blanks
- **Answer**: Complete paragraph with color-coded feedback + optional explanation

## Development Journey

### Add-on Automation (Sessions 1-4)
**Challenge**: Text selection automation in Anki's QtWebEngine editor
- **Problem**: 500+ lines of JavaScript selection monitoring failed
- **Research**: Systematic investigation using Claude Code + Zen MCP tools
- **Solution**: Native Qt APIs (`editor.web.selectedText()`) instead of JavaScript
- **Result**: ✅ **Working automation** with `Ctrl+Shift+D` shortcut

### Template Rendering (Sessions 5-6)
**Challenge**: Complete front-side template rendering failure
- **Problem**: Blank display, no content, JavaScript execution issues
- **Solutions**: Field reference fixes, DOMContentLoaded replacements
- **Breakthrough**: IIFE + conditional rendering + hidden div pattern
- **Result**: ✅ **Fully functional** drag-and-drop template

### Multi-Card Feature Research (Session 7)
**Initial Goal**: Multi-card generation system (like cloze deletion)
- **Research**: Extensive technical analysis using Claude Code + Zen MCP
- **Findings**: Complex add-on preprocessing, dual-field architecture required
- **Decision**: ❌ **Feature dropped** - Complexity too high for benefit
- **Outcome**: Single-card system provides excellent functionality with simpler UX

## Current Status

### ✅ Completed Features
- **Automation**: Fully functional `Ctrl+Shift+D` shortcut for blank creation
- **Templates**: Interactive drag-and-drop interface with visual feedback
- **Cross-Platform**: Works on Anki Desktop, AnkiWeb, and mobile
- **User Experience**: Streamlined workflow from content creation to study

### 🔄 Future Enhancement Opportunities
- Distractor items functionality
- Advanced formatting options
- UI/UX improvements
- Performance optimizations

**Project Status**: Complete and fully functional single-card drag-and-drop system.

# AI Collaboration Methodology Documentation

## About Mengni's_CLAUDE_CODE_JOURNEY.md

This file serves as a professional showcase of sophisticated AI collaboration methodology, demonstrating systematic problem-solving and effective partnership with AI coding agents.

### Core Purpose
Document the end-to-end AI collaboration process, showcasing:
- Strategic communication and systematic debugging approaches
- Real-world problem-solving methodology with AI assistance
- Best practices for maximizing Claude Code effectiveness
- Learning from failed attempts and iterative improvement

### Current Focus
Project demonstrates both successes and challenges:
- **Success**: Complex add-on automation breakthrough (Session 4)
- **Challenge**: Template rendering failure requiring systematic debugging
- **Methodology**: Evolving from assumption-based fixes to evidence-based problem-solving

# Best Practices Reference

## Available Resource
`anthropic_blog_claude_code_best_practices.md` contains comprehensive Claude Code best practices and advanced techniques.

## Collaborative Guidance Protocol
- Reference best practices document when workflows could be optimized
- Suggest specific improvements based on established patterns
- Provide reasoning for recommendations while respecting user decisions
- Proactively guide toward more effective approaches when beneficial

## Application
Use best practices knowledge to:
- Recommend optimal workflows (Explore → Plan → Code → Commit)
- Suggest thinking modes for complex problems
- Improve collaboration efficiency
- Enhance project outcomes through proven techniques

# Permission Management

## Auto-Execute Permissions Granted
Commands approved for automatic execution:
- `git status` - Check repository status
- `ls` - List directory contents
- `cat` - Read file contents
- `mv` - Move/rename files (when explicitly requested)

## Permissions Requiring Approval
Commands that require user confirmation:
- `git commit` - Committing changes
- `git add` - Staging files
- `rm` - Removing files
- File creation/modification operations (except when explicitly requested)