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
- **Show Answer (Back)**: Anki's native button shows clean text with `[[d1::text]]` syntax stripped
- **Answer**: Natural reading text with answers filled in + optional explanation

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

### Back Template Design Decision (Session 8-10)
**Challenge**: Back template rendering complexity vs. user needs
- **Original Goal**: Process `[[d1::text]]` syntax to show highlighted filled text
- **Technical Issues**: JavaScript processing failures in back template environment
- **Multiple Failed Attempts**: Hidden div, regex replacement, diagnostic approaches all failed
- **Root Cause**: Fundamental execution environment differences between front/back templates
- **Design Decision**: ✅ **Enhanced approach** - Strip `[[dN::]]` syntax while preserving text content
- **New Specification**: Back template shows clean, readable text with answers naturally filled in
- **Benefits**: Natural reading experience, clean presentation, maintains reliability
- **Implementation**: ✅ **Hidden div pattern with regex processing** - Proven approach with secure text manipulation

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
- **Front Template**: Interactive drag-and-drop interface with visual feedback
- **Back Template**: Enhanced design displaying clean text with bracketed syntax stripped
- **Modern UI**: Semantic form-style interface with cohesive blue color scheme
- **Cross-Platform**: Works on Anki Desktop, AnkiWeb, and mobile
- **User Experience**: Streamlined workflow from content creation to study
- **Semantic Validation**: Interchangeable blanks using `@groupX` syntax for semantically equivalent answers
- **Paragraph Break Preservation**: DOM-based processing maintains paragraph structure in multi-paragraph content
- **Direct Inter-Container Movement**: Items can be dragged directly between input containers without intermediate panel return

### 🔄 Current Issues & Future Enhancements

#### 🔮 Future Enhancement Opportunities
- Distractor items functionality
- Advanced formatting options
- Performance optimizations

### ✅ Enhanced Answer Display (Session 12)
**Feature**: Enhanced back template with styled blanked-out terms
- **Goal**: In back template, show complete answer text with original blank items highlighted
- **Visual Effect**: Words/phrases that were `[[d1::text]]` blanks display in **bold dark blue**
- **Example**: "Python is a programming language" (where "Python" and "programming" are bold and dark blue)
- **Purpose**: Provide clear visual feedback showing which terms were the learning targets
- **Implementation**: Modified back template regex processing to wrap identified terms in `<strong style="color: #1565c0;">` tags
- **Technical Details**: 
  - **File**: `back.html:37`
  - **Change**: `innerHTML.replace(/\[\[d\d+::([^\]]+)\]\]/g, '<strong style="color: #1565c0;">$1</strong>')`
  - **Color**: `#1565c0` (matches theme color from `.answer-input.filled`)
  - **Integration**: Seamlessly works with existing dual processing architecture
- **Status**: ✅ **Successfully Implemented**

### ✅ Group Syntax Removal from Back Template (Session 24)
**Feature**: Remove `@groupN` syntax from back template display
- **Goal**: Strip `@groupN` syntax from back template while preserving answer highlighting
- **Problem**: With semantic validation feature, syntax like `[[d::mangoes]]@group1` displayed as "**mangoes@group1**" instead of "**mangoes**"
- **Solution**: Extended regex pattern to match optional `@groupN` syntax but exclude from replacement
- **Implementation**: 
  - **HTML Processing**: `innerHTML.replace(/\[\[d\d*::([^\]]+)\]\](@\w+)?/g, '<strong style="color: #1565c0;">$1</strong>')`
  - **Text Processing**: `textContent.replace(/\[\[d\d*::([^\]]+)\]\](@\w+)?/g, '$1')`
- **Technical Details**:
  - **Files**: `back.html:37, back.html:50`
  - **Pattern**: Added `(@\w+)?` to existing regex to optionally match group syntax
  - **Backward Compatibility**: Works with both `[[d::text]]` and `[[d::text]]@group1` formats
  - **Consistency**: Uses same `@\w+` pattern as front template for validation
- **Result**: Clean answer display with proper highlighting, no visible group syntax
- **Status**: ✅ **Successfully Implemented**

### ❌ Initial Simplified Syntax Implementation Attempt (Session 13)
**Feature Request**: Simplify `[[d1::text]]` syntax to `[[d::text]]` format
- **Goal**: Remove unnecessary numbering since only one card is generated, simplify user experience
- **Rationale**: Numbers (d1, d2, d3) serve no functional purpose in single-card system
- **Approach Chosen**: Approach 1 (Simple Replacement) - Breaking change implementation
- **Implementation Attempt**: 
  - **Add-on**: Removed counter logic, generate `[[d::{selected_text}]]`
  - **Front template**: Updated all regex patterns to `/\[\[d::([^\]]+)\]\]/g` with position-based ID generation
  - **Back template**: Updated regex to `/\[\[d::([^\]]+)\]\]/g`
- **Critical Issue Discovered**: 
  - **Breaking Change Problem**: Existing cards with `[[d1::text]]` syntax became unusable
  - **Template Failure**: Front template shows "No question content found" 
  - **User Impact**: All existing user content would require manual migration
- **Root Cause**: Approach 1 creates breaking change requiring all existing cards to be updated
- **Lesson Learned**: Backward compatibility is essential for existing user content
- **Status**: ❌ **Failed Implementation - Reverted**
- **Resolution**: Successfully implemented in Session 14 with backward compatibility

### ✅ Backward Compatible Syntax Simplification (Session 14)
**Feature**: Implement `[[d::text]]` syntax with full backward compatibility
- **Goal**: Support both `[[d1::text]]` (legacy) and `[[d::text]]` (new) syntax simultaneously
- **Approach**: Version 2 - Smart regex with hybrid ID system
- **Implementation**:
  - **Add-on**: Generate `[[d::text]]` syntax (no numbering)
  - **Smart regex**: Use `(\d*)` pattern to handle both numbered and unnumbered patterns
  - **ID preservation**: Legacy `[[d1::text]]` keeps original ID `d1`, new `[[d::text]]` gets sequential IDs
  - **Backward compatibility**: Existing cards continue working unchanged
- **Technical Details**:
  - **Front template**: `innerHTML.replace(/\[\[d(\d*)::([^\]]+)\]\]/g, function(match, num, text) { ... })`
  - **ID generation**: 
    - Legacy: `if (num && num.length > 0) { blankId = 'd' + num; }`
    - New: `else { blankId = 'd' + nextAutoId; nextAutoId++; }`
  - **Back template**: Updated regex to `/\[\[d\d*::([^\]]+)\]\]/g`
- **Files Modified**:
  - `drag_drop_addon/__init__.py`: Line 46 - Generate `[[d::text]]` syntax
  - `front.html`: Lines 89-101, 132-144 - Smart regex processing
  - `back.html`: Lines 37, 50 - Support both patterns
- **Benefits**:
  - **User Experience**: Simplified syntax for new content
  - **Backward Compatibility**: Existing cards remain functional
  - **Seamless Migration**: No user action required
- **Status**: ✅ **Successfully Implemented**

### ✅ Formatting Preservation Implementation (Session 11)
**Challenge**: Users reported that HTML formatting (bold, italic, colors) applied in the Question field was lost in both front and back templates.

**Root Issue**: Templates used `.textContent` which strips HTML formatting, processing only plain text.

**Initial Failed Approach**: Fragment-based DOM manipulation (TreeWalker + fragment replacement)
- **Problem**: Complex DOM manipulation broke content detection logic
- **Symptom**: Both templates showed "No question content found"
- **Root Cause**: Changed core content access method instead of enhancing it

**Diagnostic Breakthrough**: Used systematic debugging approach
- **Version 1**: Content access comparison revealed HTML formatting was available
- **Key Finding**: `innerHTML` contained 121 more characters than `textContent` (HTML formatting)
- **Critical Insight**: Field validation worked fine - implementation approach was wrong

**Successful Solution**: Minimal HTML Processing (Version 3 refined)
- **Strategy**: Preserve working `.textContent` validation, add `.innerHTML` enhancement layer
- **Implementation**: Dual processing with HTML-first approach and text fallback
- **Front Template**: Enhanced drag-and-drop to transfer HTML content
- **Back Template**: Simple regex replacement preserving HTML structure
- **Safety**: Graceful fallback to text processing if HTML processing fails

**Technical Details**:
- **Content Detection**: Uses `textContent` for validation (preserves working logic)
- **HTML Processing**: Attempts `innerHTML` processing when formatting detected
- **Fallback System**: Falls back to original text processing if HTML fails
- **Drag & Drop**: Transfers both text and HTML content in drag operations
- **Answer Display**: Shows formatted answers in both front and back templates

**Current Status**: ✅ **Feature successfully implemented** - HTML formatting preserved in both templates
**Result**: Bold, italic, colors, and all HTML formatting now maintained throughout the learning experience

### ✅ Successful Implementation: Semantic Validation for Interchangeable Blanks (Session 19)
**Feature**: User-defined groups for interchangeable blanks using `@groupX` syntax
- **GitHub Issue**: [Feature: Semantic validation for interchangeable blanks](https://github.com/momomozhang/anki-template-drag-and-drop-fill-in-the-blanks/issues/4)
- **Goal**: Allow semantically equivalent answers to be interchangeable regardless of position
- **Syntax**: `[[d::answer]]@group1` to mark blanks as belonging to the same semantic group
- **Example**: `"I love both [[d::mangoes]]@group1 and [[d::pineapples]]@group1."` - either answer works in either blank

**Implementation**: Version 3 Production-Ready Fix
- **Architecture**: Clean separation of semantic vs positional validation modes
- **Enhanced State Management**: 
  - `answerGroups`: Map of groupId → Set of acceptable answers
  - `blankGroupMapping`: Map of blankId → groupId
  - `validationMode`: 'positional' or 'semantic'
- **Core Functions**:
  - `parseSemanticQuestion()`: Handles `@groupX` syntax parsing
  - `parsePositionalQuestion()`: Backward compatibility for existing syntax
  - `validateUserAnswer()`: Group-aware validation with positional fallback
- **Security**: Enhanced with HTML sanitization to prevent XSS attacks

**Key Features**:
- **Automatic Mode Detection**: Detects `@groupX` syntax and switches to semantic mode
- **Group-Aware Validation**: Checks if answer is acceptable for blank's group before positional fallback
- **Backward Compatibility**: Existing `[[d::text]]` syntax continues to work unchanged
- **Security Hardening**: All user input sanitized to prevent XSS vulnerabilities
- **Clean Item Display**: `@groupX` syntax stripped from draggable items

**Files Modified**:
- `front.html`: Complete semantic validation system with security fixes
- `documentation/CLAUDE.md`: Updated documentation

**Status**: ✅ **Successfully Implemented** - Semantic validation working correctly

### ✅ Successful Implementation: Paragraph Break Preservation (Session 20)
**Feature**: DOM-based paragraph break preservation for multi-paragraph content
- **Goal**: Preserve paragraph breaks when content spans multiple paragraphs
- **Problem**: Multi-paragraph content lost line breaks during processing
- **Solution**: Enhanced DOM parsing with `preserveParagraphBreaks()` function

**Implementation**: Version 1 (DOM-Based) 
- **Architecture**: DOM-based HTML parsing that preserves paragraph structure
- **Core Function**: `preserveParagraphBreaks()` - Processes HTML to maintain paragraph boundaries
- **Processing Logic**: 
  - Analyzes HTML structure to identify paragraph breaks (`<p>`, `<div>`, `<br>`)
  - Converts paragraph boundaries to `\n\n` for proper spacing
  - Converts `<br>` tags to single `\n` for line breaks
  - Graceful fallback to original text if processing fails
- **Integration**: Seamlessly integrated into existing `parseQuestion()` workflow

**Key Features**:
- **Structure-Aware Processing**: Recognizes paragraph and block elements
- **Fallback Safety**: Returns original text if DOM processing fails
- **Backward Compatibility**: Works with existing single-paragraph content
- **Security**: Processes content safely without introducing vulnerabilities

**Files Modified**:
- `front.html`: Added `preserveParagraphBreaks()` function and integration
- `documentation/CLAUDE.md`: Updated documentation

**Status**: ✅ **Successfully Implemented** - Paragraph breaks preserved correctly

### ✅ Successful Implementation: Direct Inter-Container Movement (Session 25)
**Feature**: Container-to-container drag-and-drop functionality using event delegation pattern
- **GitHub Issue**: Users can now drag items directly between input containers
- **Goal**: Eliminate the need for intermediate panel return when moving items between containers
- **Problem**: Original implementation created event handler timing issues and conflicts

**Implementation**: Version 1C - Event Delegation Pattern
- **Architecture**: Centralized event management with single delegation handler
- **Enhanced Event Handling**: 
  - `handleDelegatedDragStart()`: Validates targets and routes to appropriate handlers
  - `handlePanelDrag()`: Handles drag operations from item panel
  - `handleContainerDrag()`: Handles drag operations from filled containers
  - `handleDelegatedDragEnd()`: Centralized cleanup
- **Performance Optimizations**: Single event listener eliminates timing issues and memory leaks
- **Error Handling**: Comprehensive validation and error logging

**Key Features**:
- **Event Delegation**: Single `document.addEventListener()` handles all drag events
- **Robust Validation**: Comprehensive checks for event targets and data transfer
- **Error Handling**: Proper try-catch blocks with console warnings
- **Performance**: Eliminates repeated event listener attachment/removal
- **Security**: Maintains all existing HTML sanitization
- **Backward Compatibility**: Preserves existing click-to-return functionality

**Files Modified**:
- `front.html`: Complete event delegation system implementation
- `documentation/CLAUDE.md`: Updated documentation

**Status**: ✅ **Successfully Implemented** - Direct inter-container movement working correctly

## Deep Analysis: Parsing-Validation Gap Investigation (Session 19)

### Investigation Summary
**Objective**: Understand the gap between "parsing success" and "validation failure" claims in semantic validation implementation.

**Key Finding**: The gap is a **technical integration failure** between working parsing components and broken validation logic, not a fundamental design flaw.

### The Real Implementation Story

**Final Implementation Status**:
- ✅ **Parsing Success**: `@groupX` syntax correctly detected and parsed
- ✅ **UI Generation Success**: Input blanks properly created with group metadata  
- ✅ **Item Extraction Success**: All draggable items correctly generated
- ✅ **Validation Success**: Group validation logic successfully implemented and working correctly

**Implementation Journey**: Initial attempts documented implementation challenges, but through systematic debugging and code review, semantic validation was successfully implemented in Session 19 with production-ready code.

### Technical Analysis

**Root Cause**: Classic integration problem where individual components work but don't connect properly:
1. **Data Flow Breakdown**: Group information parsed successfully but not passed to validation
2. **Validation Routing**: System defaults to positional validation instead of group validation  
3. **State Management**: Parsed group data may not be accessible to validation functions

### Complete User Interaction Flow Mapping

**Current Flow**: Drag → Drop → Validate → Feedback

#### 1. DRAG Phase
- **Event**: `handleDragStart()` (line 318)
- **Data Transfer**: Sets plain text, HTML content, and item index
- **Visual Feedback**: Item becomes semi-transparent with rotation/scale

#### 2. DROP Phase  
- **Event**: `handleDrop()` (line 342)
- **Critical Steps**:
  1. Extract item data from `dataTransfer`
  2. Get `data-blank-id` from target drop zone
  3. Update drop zone with item content + `filled` class
  4. Mark dragged item as `used` (disabled)
  5. **Store answer**: `studyState.userAnswers.set(blankId, itemText)`

#### 3. VALIDATE Phase
- **Event**: `showAnswers()` (line 396)
- **Current Logic**: Simple positional validation
  ```javascript
  if (userAnswer === correctAnswer) {
      // Correct - green
  } else {
      // Incorrect - red
  }
  ```

#### 4. FEEDBACK Phase
- **Visual Output**: Color-coded styling applied to drop zones
- **Correct**: Green background + pulse animation
- **Incorrect**: Red background + shake animation  
- **Empty**: Grey background + auto-filled correct answer

### Critical Integration Breakpoints for Group Logic

#### Breakpoint 1: Enhanced Regex Detection
**Location**: `parseQuestion()` line 89, 132
- **Current**: `/\[\[d(\d*)::([^\]]+)\]\]/g`
- **Required**: `/\[\[d(\d*)::([^\]]+)\]\](@\w+)?/g`
- **Purpose**: Detect and capture `@groupX` syntax

#### Breakpoint 2: Enhanced State Management
**Location**: `studyState` object definition (line 29)
- **Current**: Simple key-value maps for positional validation
- **Required**: Add group relationship tracking
- **Purpose**: Store which blanks belong to which groups and acceptable answers

#### Breakpoint 3: Group-Aware Validation
**Location**: `showAnswers()` validation loop (line 415-421)
- **Current**: `userAnswer === correctAnswer` (exact positional match)
- **Required**: Group-aware validation before positional fallback
- **Purpose**: Enable semantic answer acceptance

#### Breakpoint 4: Clean Item Display
**Location**: `createDraggableItems()` (line 200)
- **Current**: Extract items using same regex as parsing
- **Required**: Strip `@groupX` syntax from display items
- **Purpose**: Clean presentation while preserving metadata

### Key Insights

1. **Integration Not Implementation**: The problem is connecting working components, not building new ones
2. **Validation Layer Focus**: Core issue is in the validation logic, not parsing or UI generation
3. **State Management Critical**: Group data must be accessible to validation functions
4. **Backward Compatibility**: Positional validation must remain default for non-grouped content

### Next Steps for Resolution

1. **Debug Runtime Execution**: Add console logging to identify actual failure point
2. **Verify Data Flow**: Ensure group information flows from parsing to validation
3. **Test Components Isolated**: Validate individual pieces before end-to-end integration
4. **Focus on Validation Logic**: Prioritize fixing validation routing over parsing enhancements

**Conclusion**: This is a technical debugging problem requiring systematic component integration analysis, not a fundamental design flaw requiring complete reimplementation.

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