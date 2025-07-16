# Anki Drag-and-Drop Template Project

## Project Overview

This is an interactive Anki flashcard template that creates drag-and-drop fill-in-the-blank exercises. Built entirely with Claude Code assistance, it demonstrates sophisticated AI collaboration and solves a real need for Anki users seeking more interactive learning experiences.

### Key Features:
- **Interactive Learning**: Drag words/phrases to fill blanks in sentences
- **Modern UI**: Integrated input boxes with bottom panel for draggable items
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
4. **Study**: Drag items from bottom panel to fill input boxes within text
5. **Show Answers**: Click "Show Answers" to see correct answers with color coding

### Study Experience
- **Front**: "You simply upload your code and _________ automatically handles the _________"
- **UI Design**: 
  - **Drop zones**: Rectangular bordered input boxes integrated naturally into text flow
  - **Item panel**: All draggable items displayed in horizontal bottom panel with button/tag styling
  - **Controls**: "Show Answers" and "Reset" buttons preserved
- **Interaction**: Drag items from bottom panel to fill input boxes within text
- **Show Answers (Front)**: Click button to reveal correct answers with intelligent color coding:
  - **Green**: User-placed correct answers
  - **Red**: User-placed incorrect answers  
  - **Grey**: Auto-filled correct answers for empty blanks
- **Show Answer (Back)**: Anki's native button shows complete original text with answers naturally filled in
- **Answer**: Complete readable paragraph with all blanks filled + optional explanation

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

### Back Template Rendering Issue (Session 8)
**Issue**: Back template shows empty content instead of filled text
- **Attempted Solution 1**: Hidden div approach (same as front template)
- **Result**: ❌ **Failed** - Issue persisted despite field access fix
- **Attempted Solution 3**: Diagnostic investigation approach
- **Result**: ✅ **Revealed field access works** - Both direct and hidden div methods return content
- **Attempted Solution 2**: Regex replacement to strip [[d1::text]] syntax  
- **Result**: ❌ **Failed** - Issue persisted despite confirmed field access
- **Attempted Solution 4**: Hidden div + original highlighting (corrected approach)
- **Result**: ❌ **Failed** - Issue persisted despite using working front template pattern
- **Analysis**: Field access AND CSS confirmed working, but implementation still fails
- **Status**: Investigating fundamental difference between front/back template execution

### UI Redesign Decision (Session 9)
**New Requirement**: Modernize interface design while preserving functionality
- **Visual Changes**: 
  - Replace inline underlined spaces with rectangular bordered input boxes
  - Consolidate draggable items into horizontal bottom panel with button styling
  - Maintain natural text flow with integrated input boxes
- **Preserved Features**: 
  - "Show Answers" and "Reset" buttons
  - Color-coded feedback system (green/red/grey)
  - All drag-and-drop functionality and interactions
- **Goal**: Modern, form-like appearance with robust interactive features
- **Status**: ✅ **Successfully Implemented**

### UI Redesign Implementation (Session 9)
**Implementation**: Version 2 (Semantic Form-Style) successfully deployed
- **HTML Structure**: 
  - Semantic layout with `<main>`, `<aside>`, `<header>` elements
  - Item bank repositioned below buttons (not at bottom of interface)
  - Clean content flow: Exercise → Controls → Available Items
- **CSS Styling**: 
  - Rectangular bordered input boxes replacing underlined spaces
  - Light blue item bank background (`#c8d6e5`) with white bordered items
  - Cohesive blue color scheme (`#5a9fd4`) replacing bright green
  - Responsive design with mobile-friendly adjustments
- **JavaScript**: 
  - Updated selectors: `.inline-drop-zone` → `.answer-input`
  - Preserved all drag-and-drop logic and state management
  - Maintained color-coded feedback system
- **Result**: ✅ **Modern, cohesive UI with full functionality preserved**

## Current Status

### ✅ Completed Features
- **Automation**: Fully functional `Ctrl+Shift+D` shortcut for blank creation
- **Templates**: Interactive drag-and-drop interface with visual feedback
- **Modern UI**: Semantic form-style interface with cohesive blue color scheme
- **Cross-Platform**: Works on Anki Desktop, AnkiWeb, and mobile
- **User Experience**: Streamlined workflow from content creation to study

### 🔄 Current Development
- **Back Template**: Ongoing investigation of rendering issue

### 🔄 Future Enhancement Opportunities
- Distractor items functionality
- Advanced formatting options
- Performance optimizations

**Project Status**: Core functionality and modern UI complete - production ready.

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