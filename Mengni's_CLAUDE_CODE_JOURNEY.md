# Anki Project: Claude Code Collaboration Journey

## Executive Summary

This document showcases the sophisticated methodology and strategic approach required for effective AI-assisted development. Working with Claude Code isn't about "pressing a button and magic happens" - it's a skilled collaboration that demands strategic thinking, clear communication, and active project steering.

## Core Methodology: AI Partnership as a Professional Skill

### The Partnership Principle
Effective AI collaboration requires treating the AI agent as a skilled partner rather than an automated tool. This means:
- **Strategic Communication**: Learning to frame problems, provide context, and guide the conversation
- **Active Steering**: Understanding when to redirect, refine, or pivot approaches
- **Collaborative Problem-Solving**: Leveraging AI strengths while maintaining human oversight and decision-making

## Project-Specific Application: Anki Drag-and-Drop Template

### Phase 1: Project Initiation & Strategic Planning
**Strategic Innovation:**
- Built multi-layer guidance framework: best practices documentation feeds into project instructions, enabling AI to provide collaborative guidance back to the user
- Transformed project from simple coding task into professional showcase of sophisticated AI partnership skills
- Created methodology for continuous improvement through session-by-session documentation

**Meta-Achievement:** Developed system where AI becomes an active partner in optimizing the human-AI collaboration process, using established best practices to guide both parties toward better outcomes.


## Proven Collaboration Techniques

### Planning Phase
- "Please do not generate any code yet."
- "Please rephrase my requirements to demonstrate your understanding."
- "Please create 3 versions. Which do you think is best? Why?"

### Problem-Solving Phase
- **Isolate issues**: "Focus only on [specific component] first"
- **Define precisely**: Provide screenshots, exact error messages, specific symptoms
- **Confirm understanding**: "Rephrase this issue to show you understand"
- **Document attempts**: "What have we tried? What worked/failed?"

### Communication Techniques
- Press *Esc* twice to edit questions when answers aren't satisfactory
- Provide links, documents, images for context
- Use visual evidence (screenshots) alongside text descriptions
- Correct AI assumptions immediately when they diverge from reality

### Project-Specific Insights

#### Session 2: Requirements Discovery & Implementation

**Key Learning**: The importance of the **Explore → Plan → Code** workflow when requirements seemed unclear initially.

**Challenge**: I jumped to coding without fully understanding the user's mental model of "Cloze-style UI for drag-and-drop."

**Breakthrough Moment**: When user said "discard all coding work" and referenced the best practices document, it demonstrated the power of following structured AI collaboration workflows.

**Technical Insights**:
- Successfully implemented inline drag-and-drop (innovation over existing separate drop-zone patterns)
- Combined editor and study modes in single template
- Requirement refinement through iterative clarification (answer section color coding)

#### Session 6: Systematic Debugging Methodology

**Challenge**: Complete template rendering failure - front-side showing blank screen instead of interactive content.

**Critical Methodology Learnings**:

1. **Issue Isolation**: Break complex problems into small, testable components
   - Separated JavaScript execution from field substitution from UI rendering
   - Identified DOMContentLoaded as isolated failure point vs field access vs variable scope

2. **Precise Issue Definition**: Use detailed descriptions with visual evidence
   - User provided screenshot showing empty template
   - Corrected my assumptions: "not showing parsed content" → "completely blank front-side"
   - Specific symptoms: no cloze blanks, no draggable items, empty sections

3. **Confirmation Through Rephrasing**: Ensure shared understanding before solutions
   - Asked Claude to rephrase issue understanding
   - Prevented solution attempts based on incorrect problem diagnosis
   - "Template showing literal {{Question}}" → "Template completely empty"

4. **Document Failed Attempts**: Record what didn't work and why
   - **Session 5 Failure**: Field reference syntax changes (wrong root cause)
   - **Session 6 Partial**: DOMContentLoaded fix worked for JavaScript execution, revealed field substitution issue
   - **Learning**: Each "failure" provided crucial diagnostic information for final solution

**Breakthrough Pattern**: Problem → Isolate → Define → Confirm → Test → Document → Iterate

**Methodology Win**: Using documentation-first approach (CLAUDE.md updates) to capture requirements before implementation prevented future misunderstandings.

#### Session 4: Complex Problem Solving & Research-Driven Solutions

**Major Challenge**: Add-on automation completely non-functional despite extensive previous attempts

**Strategic Approach**: after multiple failed debugging sessions, I connect Claude Code with Zen MCP to research online the root cause. Together the AI studied multiple working anki template and found the solution.

**Technical Breakthrough**: 
- **Root Cause**: Wrong architectural approach (JavaScript vs native Qt APIs)
- **Solution**: Simple `editor.web.selectedText()` property access
- **Result**: Replaced 500+ lines of failed code with ~20 lines of working automation

**Meta-Learning**: This session demonstrated sophisticated problem-solving methodologies available when combining Claude Code with advanced tools (Zen MCP). The systematic research and analysis capabilities enabled solving a problem that seemed impossible through traditional approaches.

---

*This document serves as both a methodology showcase and a living example of how professional AI collaboration can enhance development outcomes while maintaining human agency and oversight.*