# Project Understanding

This is an Anki flashcard template project that creates interactive drag-and-drop fill-in-the-blank exercises. The project serves as a showcase of Claude Code's development capabilities.

## Key Understanding:
- It's a complete educational tool built entirely with Claude Code assistance
- Creates interactive flashcards where users drag words/phrases to fill blanks in sentences
- Uses HTML5 drag-and-drop API for cross-platform compatibility (Anki Desktop, AnkiWeb, mobile)
- Features visual feedback, randomization, and flexible input formatting
- Targets various learning domains (language, medical, history, coding)

## Primary Purpose:
Demonstrate Claude Code's ability to build complete, functional projects while solving a real need for Anki users who want more interactive learning experiences.

The project appears to be a legitimate educational tool focused on enhancing learning through interactive exercises.

## Detailed Requirements (Established Session 2)

### Core User Experience
- **Content Creation**: User copies/pastes a paragraph into Question field
- **Blank Creation**: User selects text portions and clicks a Cloze-style button to create inline blanks
- **Inline Blanks**: Blanks appear within sentence flow (not as separate drop zones)
- **Study Experience**: Draggable items below text for filling blanks

### Technical Specifications

#### Anki Field Structure:
- **Question Field**: Original text with `[[d1::selected_text]]` syntax (d = drag-and-drop)
- **Answer Field**: Simple explanation/notes for the answer
- ~~**Items Field**~~: **REMOVED** - Template automatically extracts items from Question field syntax
- ~~**Notes Field**~~: **REMOVED** - Replaced with simpler Answer field
- ~~**Extra Field**~~: **REMOVED** - Replaced with simpler Answer field
- ~~**Explain Field**~~: **REMOVED** - Replaced with Answer field

#### Editor Interface:
- **Button**: ✅ **WORKING** - Cloze-style button for creating blanks using native Qt APIs
- **Keyboard Shortcut**: `Ctrl+Shift+D` (or `Cmd+Shift+D` on Mac) for quick blank creation
- **Auto-increment**: ✅ **FUNCTIONAL** - Automatically detects existing blanks and increments counter
- **Smart Parsing**: ✅ **AUTOMATIC** - Template extracts draggable items directly from `[[d1::text]]` syntax

#### User Workflow Example (FULLY AUTOMATED PROCESS):
1. Paste: "You simply upload your code and Elastic Beanstalk automatically handles the deployment"
2. **Select text** "Elastic Beanstalk" → **Press Ctrl+Shift+D** → Becomes `[[d1::Elastic Beanstalk]]`
3. **Select text** "deployment" → **Press Ctrl+Shift+D** → Becomes `[[d2::deployment]]`
4. **Add explanation** (optional): Fill Answer field with context or hints
5. **Done**: Template automatically extracts "Elastic Beanstalk" and "deployment" as draggable items

✅ **AUTOMATION RESTORED**: Fixed using native Qt `selectedText()` API approach.

#### Study Experience:
- **Display**: "You simply upload your code and _________ automatically handles the _________"
- **Interaction**: Drag items to fill underlined gaps within text
- **Appearance**: Blanks show as underlined gaps (like Cloze cards)
- **Answer Section**: Show complete original paragraph with color coding:
  - **Green text**: Correct answers (show actual correct word)
  - **Red text**: Incorrect answers (show what correct answer should be, not user input)
  - **Natural flow**: Full paragraph context, not individual feedback messages
- **Answer Section**: Optional explanation/context from Answer field displayed below answer

### Add-on Development Journey (RESOLVED):

#### **Original Challenges (Sessions 1-2):**
- **Automated text selection**: Anki's QtWebEngine editor doesn't expose selections to JavaScript
- **Button automation**: Multiple API approaches failed due to selection clearing behavior  
- **Event monitoring**: Standard web APIs (`selectionchange`, `mouseup`) don't work in Anki context

#### **Research & Analysis (Session 3):**
Using Claude Code with Zen MCP tools, we conducted systematic investigation:
- **Hypothesis**: JavaScript selection detection is fundamentally flawed in QtWebEngine
- **Discovery**: Qt provides native `selectedText()` property that bypasses JavaScript entirely
- **Architecture Analysis**: Other Anki developers successfully use `editor.web.selectedText()`

#### **Solution Implementation (Session 3):**
- **Root Cause**: Wrong architectural approach (JavaScript vs native Qt APIs)
- **Fix**: Replaced 500+ lines of JavaScript with simple `editor.web.selectedText()` calls
- **Result**: ✅ **WORKING AUTOMATION** - reliable text selection and blank creation

### Current Status:
- ✅ Fully automated "select text → press shortcut" workflow
- ✅ Add-on button and keyboard shortcuts functional
- ✅ Cross-platform compatibility maintained
- ✅ Template fields updated to Question and Explain only (Session 6)
- ✅ **RESOLVED**: Front-side template fully functional with drag-and-drop interface
- ✅ **RESOLVED**: JavaScript execution working with IIFE and conditional rendering
- ✅ **RESOLVED**: Field substitution working with hidden div pattern
- ✅ **COMPLETE**: Template displays cloze-style blanks and draggable items correctly

### Current Template Issue (Sessions 5-6):

#### **Actual Problem**: Complete front-side rendering failure
- **Symptoms**: 
  - Front-side Anki card completely blank/empty
  - No question text displayed (not even raw field content)
  - No cloze-style blanks or underlined gaps
  - Draggable items section completely empty
  - Only basic HTML structure/CSS loads, no dynamic content
- **Root Cause**: JavaScript parsing functions not executing in Anki environment

#### **Previous Incorrect Assumptions**:
- **Session 5**: Thought issue was field reference syntax (`'{{Question}}'` vs `{{Question}}`)
- **Session 6**: Assumed field structure was the problem
- **Reality**: Template isn't rendering any content at all, indicating JavaScript execution failure

#### **What We've Tried**:
1. **Field Reference Changes**: Multiple attempts to fix field syntax
2. **Field Structure Updates**: Reduced to Question and Explain fields only
3. **Template Validation**: Added error handling for empty fields
4. **Diagnostic Files**: Created test files (not tested in actual Anki)

#### **What We Haven't Tried**:
- **Testing in actual Anki environment** to confirm JavaScript execution
- **Debugging JavaScript failures** in Anki's web environment
- **Checking if field values are being substituted at all**
- **Validating basic HTML/CSS rendering** separately from JavaScript

#### **Session 6 Updates (2025-07-14)**:
- **Template Field Structure**: Updated both front.html and back.html to use only Question and Explain fields
- **Error Handling**: Added validation for empty/missing Question field content
- **Field References**: Fixed template literal syntax to use proper Anki field references
- **Issue Clarification**: Discovered template is completely blank, not showing field reference issues
- **DOMContentLoaded Fix**: Implemented IIFE with conditional rendering and immediate execution

#### **Session 6 Test Results**:
**Fix Applied**: Version 2 - Conditional field rendering with immediate execution
- Wrapped JavaScript in `{{#Question}}...{{/Question}}` conditional
- Replaced `DOMContentLoaded` with immediate `initializeStudyMode()` call
- Used IIFE pattern `(function() {...})()` to avoid variable declaration issues

**Test Results**:
- ✅ **JavaScript Execution**: Fixed - script now runs (draggable items section appears)
- ✅ **Variable Declaration**: Fixed - IIFE pattern prevents scope issues
- ✅ **Conditional Rendering**: Works - template only renders when Question field has content
- ✅ **Field Substitution**: Fixed - hidden div pattern enables reliable field access
- ✅ **Content Display**: Working - displays cloze-style blanks and draggable items correctly

**Key Discovery**: Template-level conditionals (`{{#Question}}`) work, but JavaScript-level field substitution (`'{{Question}}'`) doesn't work within conditional blocks. **Solution**: Use hidden div for field storage.

#### **Final Working Solution**:
**Pattern**: Hidden div + IIFE + conditional rendering + immediate execution
```html
{{#Question}}
<div id="question-data" style="display: none;">{{Question}}</div>
<script>
(function() {
    var questionField = document.getElementById('question-data').textContent;
    // JavaScript processes actual field content successfully
})();
</script>
{{/Question}}
```

**Why This Works**:
- **Template Engine**: Substitutes `{{Question}}` in hidden div before JavaScript runs
- **JavaScript Access**: Reads actual field content via `textContent` DOM property
- **Clean Separation**: Template engine handles substitution, JavaScript handles processing
- **Proven Pattern**: Hidden div approach is standard in successful Anki templates

#### **Session 6 - BREAKTHROUGH SUCCESS**:

**Problem Solved**: Complete template rendering failure (blank front-side)
**Root Causes Identified**:
1. **DOMContentLoaded not firing**: Anki's long-running webpage breaks traditional DOM events
2. **Field substitution timing**: JavaScript-level field references don't work in conditional blocks
3. **Variable declaration issues**: Global scope variables need IIFE wrapping

**Solution Implemented**: Multi-part fix addressing all root causes
1. **IIFE Pattern**: `(function() {...})()` for proper variable scoping
2. **Conditional Rendering**: `{{#Question}}...{{/Question}}` ensures content exists
3. **Immediate Execution**: Removed `DOMContentLoaded`, called `initializeStudyMode()` directly
4. **Hidden Div Pattern**: `<div id="question-data" style="display: none;">{{Question}}</div>` for reliable field access

**Result**: ✅ **FULLY FUNCTIONAL** drag-and-drop template with:
- Cloze-style blanks displaying correctly
- Draggable items extracted from Question field
- Working event handlers and interactive functionality
- Cross-platform compatibility maintained

**Next Phase**: Template is now complete and ready for real-world use and testing

### Future Features (Ready for development):
- Distractor items functionality
- Multiple instance selection  
- Advanced formatting options
- UI/UX improvements
- Performance optimizations

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