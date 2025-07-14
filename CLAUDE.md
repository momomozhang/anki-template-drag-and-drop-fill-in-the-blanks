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
- ❌ **ACTIVE ISSUE**: Front-side template not displaying cloze-style blanks or draggable items
- ❌ **ACTIVE ISSUE**: Template showing literal field references instead of parsed content
- ❌ **ACTIVE ISSUE**: Event handlers not working ("Check Answers" button non-functional)
- ❌ **ACTIVE ISSUE**: Original UI design/styling missing or broken

### Session 5 Failed Debugging Attempt (2025-07-14):

#### **Issue Investigated**: Template showing literal `{{Question}}` instead of parsed content
- **Symptoms**: Front-side card shows no cloze-style blanks, no draggable items, broken event handlers
- **Root Cause Hypothesis**: Field references using quotes `'{{Question}}'` instead of direct `{{Question}}`

#### **What We Tried**:
1. **Systematic Debugging Plan**: Created comprehensive 5-phase debugging approach following Claude Code best practices
2. **File Analysis**: Examined front.html, back.html, diagnostic-test.html, test-template.html
3. **Solution Attempts**: 
   - Changed `'{{Question}}'` to `{{Question}}` (direct field reference)
   - Changed to template literals `` `{{Question}}` ``
   - Updated diagnostic tests to show both old/new methods
4. **Created Test Files**: verify-fix.html, updated diagnostic-test.html

#### **Why It Failed**:
- **Over-engineering**: Applied complex debugging methodology to potentially simple issue
- **Assumption Error**: Assumed templates were already fixed when they weren't
- **UI Regression**: Changes broke original styling and functionality
- **Incomplete Testing**: Didn't verify in actual Anki environment before committing to approach

#### **Lessons Learned**:
- **Test in Real Environment First**: Always test templates in actual Anki before assuming they work
- **Preserve Working State**: Don't modify functional code without backup/verification
- **Incremental Changes**: Make small, testable changes rather than comprehensive rewrites
- **UI Consistency**: Maintain styling and UX during debugging

#### **Session 6 Updates (2025-07-14)**:
- **Template Field Structure**: Updated both front.html and back.html to use only Question and Explain fields
- **Error Handling**: Added validation for empty/missing Question field content
- **Field References**: Fixed template literal syntax to use proper Anki field references
- **Draggable Items**: Updated logic to extract items directly from Question field [[d1::text]] syntax
- **Back Template**: Updated to use {{Explain}} field instead of {{Answer}}

#### **Next Session Should**:
1. **Test in Anki Environment**: Load templates in actual Anki to identify exact failure points
2. **Debug Field Parsing**: Check if Anki is properly substituting field values
3. **Validate JavaScript Execution**: Ensure scripts run properly in Anki's web environment
4. **Fix Content Display**: Resolve why blanks and draggable items aren't showing

### Future Features (Not MVP):
- Distractor items in Items field
- Multiple instance selection  
- Advanced formatting options

# AI Collaboration Methodology Documentation

## About Mengni's_CLAUDE_CODE_JOURNEY.md

This file serves as a professional showcase of sophisticated AI collaboration methodology, demonstrating that effective work with AI coding agents requires strategic thinking, clear communication, and active partnership—not automated "magic button" solutions.

### Core Purpose
Document the end-to-end AI collaboration process across the entire project lifecycle, showcasing:
- Strategic communication skills and effective AI agent guidance
- Active project steering and decision-making capabilities  
- Best practices and techniques for maximizing Claude Code effectiveness
- Real-world examples of sophisticated AI partnership approaches

### Living Documentation Process
This is a work-in-progress document updated each collaboration session to capture:
- **Session-by-Session Learning**: Techniques that worked, challenges faced, solutions discovered
- **Real-Time Methodology Evolution**: How collaboration approaches improve through practice
- **Practical Tips Collection**: Concrete communication patterns and effective prompting strategies
- **Iterative Expertise Development**: Growing sophistication in AI partnership skills

### Update Requirements
During each session, we should:
- Document new learnings in "Project-Specific Insights"
- Add practical tips that prove effective
- Record any pivots, challenges, or breakthrough moments
- Refine methodology based on collaborative discoveries

### Meta-Objective
This document itself demonstrates sophisticated AI collaboration by simultaneously building the Anki template while documenting and refining our partnership methodology in real-time.

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