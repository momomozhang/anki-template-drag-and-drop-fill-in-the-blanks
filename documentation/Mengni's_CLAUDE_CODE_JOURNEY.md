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

#### Session 7: Strategic Feature Evaluation & Technical Decision-Making

**New Requirement**: Multi-card generation system (like Anki's cloze deletion)
- Each unique dN number generates separate flashcard
- Same-number grouping (multiple blanks with same dN on same card)
- Context preservation (different dN numbers remain visible)

**Strategic Research Process**:
1. **Requirement Clarification**: Used collaborative communication to ensure precise understanding
2. **Technical Research**: Partnered with Zen MCP to study Anki's cloze deletion mechanisms
3. **Solution Analysis**: Comprehensive evaluation of implementation complexity
4. **Strategic Decision**: Feature dropped after thorough analysis

**Key Research Findings**:
- Requires complex add-on preprocessing (`[[dN::text]]` → `{{cN::text}}`)
- Needs dual-field architecture (original + processed content)
- Demands sophisticated JavaScript for context preservation
- Adds significant maintenance overhead and user complexity

**Strategic Decision**: ❌ **Feature Dropped**
**Rationale**: Complexity deemed too high for benefit provided - single-card system already provides excellent functionality with simpler user experience

**Meta-Learning**: This session demonstrated mature technical decision-making - knowing when NOT to implement a feature is as important as knowing how to implement it. The comprehensive research process ensured the decision was based on thorough analysis rather than assumptions.

#### Session 8: Strategic Feature Simplification (July 15, 2025)

**Issue Discovery**: Scoring calculation bug discovered during testing (incorrect percentages displayed)

**Investigation Process**:
1. **Bug Analysis**: Used Zen MCP debug tool for systematic analysis of JavaScript scoring logic
2. **Root Cause**: Complex whitespace handling between stored answers and user input, plus regex parsing limitations
3. **Strategic Evaluation**: Applied same framework as Session 7's multi-card decision

**Strategic Decision Framework**:
- **Complexity vs. Benefit**: Scoring feature debugging revealed intricate edge cases and maintenance burden
- **User Value Assessment**: Core learning happens through drag-and-drop interaction, not percentage calculations
- **UX Simplification**: Removing scoring eliminates user confusion and technical complexity

**Implementation**: ❌ **Feature Removed**
- **Removed**: "Check Answers" button and percentage scoring calculations
- **Kept**: "Show Answers" button with existing color-coded feedback system
- **Result**: Simplified workflow - drag items → show answers → visual feedback through colors

**Methodology Insight**: This session demonstrates evolved AI collaboration methodology:
- **Bug-to-Feature-Decision Pipeline**: Transformed debugging session into strategic product decision
- **Systematic Analysis**: Used Zen MCP tools for evidence-based decision making
- **Strategic Simplification**: Chose feature removal over complex debugging, prioritizing user experience
- **Documentation-Driven**: Updated all project docs to reflect new simplified workflow

**Meta-Learning**: Effective AI collaboration can transform technical problems into strategic product improvements. Sometimes the best solution is strategic simplification rather than complex technical fixes.

**Follow-up Success**: After feature removal, discovered color-coding logic was broken (all answers showing green). Successfully implemented intelligent three-tier feedback system:
- **Green**: User-placed correct answers (learning validation)
- **Red**: User-placed incorrect answers (mistake identification)  
- **Grey**: Auto-filled correct answers (neutral information)

**Technical Achievement**: Version 1 solution with inline comparison logic proved most effective - minimal risk, surgical fix, preserved educational value while maintaining simplified interface.

## Session 9: UI Redesign - Strategic Visual Modernization

### Challenge: Balancing Modern Design with Functional Preservation

**User Request Analysis**: User provided screenshot showing modern UI design with integrated input boxes and bottom panel layout, requesting visual modernization while preserving all existing functionality.

**Strategic Decision Framework**:
- **Visual Modernization**: Replace inline underlined spaces with rectangular bordered input boxes
- **Layout Consolidation**: Move all draggable items to single horizontal bottom panel
- **Functionality Preservation**: Maintain all drag-and-drop interactions, color-coded feedback, and control buttons
- **Design Philosophy**: Create modern, form-like appearance without sacrificing educational effectiveness

**Documentation Strategy**:
- **CLAUDE.md**: Updated project specifications to include new UI design requirements
- **README.md**: Added UI redesign status and modern UI feature highlight
- **SESSION_LOG.md**: Documented decision rationale and implementation specifications

**Key Collaboration Insight**: When users request UI changes, the critical skill is distinguishing between cosmetic preferences and functional requirements. The approach here was to:
1. **Understand the visual goal** through screenshot analysis
2. **Preserve functional elements** that provide educational value
3. **Document the hybrid approach** to ensure nothing is lost during implementation

**Meta-Learning**: Effective AI collaboration requires treating UI redesign as strategic product evolution rather than simple restyling. The ability to maintain functional integrity while modernizing appearance demonstrates mature AI partnership skills.

## Session 11: Diagnostic Debugging Methodology

**Challenge**: Formatting preservation attempt failed catastrophically - both templates showed "No question content found"

**Initial Mistake**: Attempted complex DOM manipulation (TreeWalker + fragment replacement) without understanding why simpler approaches failed

**Breakthrough Learning**: When hitting implementation walls, use systematic diagnostic debugging instead of trying new approaches blindly

**Diagnostic Process**:
1. **Version 1**: Content access comparison - revealed HTML formatting was available (121 character difference)
2. **Key Insight**: Problem wasn't content access but implementation approach
3. **Version 3**: Minimal HTML processing with fallback - successful implementation

**Critical Methodology Insight**: 
- **DON'T**: Try different complex solutions when one fails
- **DO**: Ask Claude to create diagnostic code to pinpoint the root issue
- **Result**: Saved time, avoided frustration, achieved successful implementation

**Technical Success**: HTML formatting preservation implemented with dual processing approach - maintains working logic while adding enhancement layer

**Meta-Learning**: Diagnostic debugging transforms blocked development into systematic problem-solving. When stuck, step back and diagnose rather than trying more complex solutions.

---

*This document serves as both a methodology showcase and a living example of how professional AI collaboration can enhance development outcomes while maintaining human agency and oversight.*