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
- **Question Field**: Original text with `{{d1::selected_text}}` syntax (d = drag-and-drop)
- **Items Field**: Auto-populated with selected words (become draggable items)
- **Answers Field**: Full original text with selected parts highlighted

#### Editor Interface:
- **Button**: Cloze-style button for creating blanks (integration level flexible)
- **Selection**: Click button wraps selected text with `{{d1::text}}`, `{{d2::text}}`, etc.
- **Auto-increment**: Automatically numbers blanks sequentially
- **Auto-populate**: Updates Items and Answers fields automatically

#### User Workflow Example:
1. Paste: "You simply upload your code and Elastic Beanstalk automatically handles the deployment"
2. Select "Elastic Beanstalk" → click button → becomes `{{d1::Elastic Beanstalk}}`
3. Select "deployment" → click button → becomes `{{d2::deployment}}`
4. System generates:
   - **Items**: "Elastic Beanstalk, deployment"
   - **Answers**: "You simply upload your code and **Elastic Beanstalk** automatically handles the **deployment**"

#### Study Experience:
- **Display**: "You simply upload your code and _________ automatically handles the _________"
- **Interaction**: Drag items to fill underlined gaps within text
- **Appearance**: Blanks show as underlined gaps (like Cloze cards)
- **Answer Section**: Show complete original paragraph with color coding:
  - **Green text**: Correct answers (show actual correct word)
  - **Red text**: Incorrect answers (show what correct answer should be, not user input)
  - **Natural flow**: Full paragraph context, not individual feedback messages

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