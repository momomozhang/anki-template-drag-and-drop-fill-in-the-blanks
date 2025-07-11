# Anki Template Development Research

## Executive Summary

This research document provides comprehensive findings on Anki template development, focusing on drag-and-drop functionality, cross-platform compatibility, and JavaScript context preservation. The research covers current best practices, proven implementations, and critical technical considerations for building interactive Anki flashcards.

## Core Technology Stack

### Template Architecture
- **HTML**: Structure and content layout
- **CSS**: Styling and visual design  
- **Vanilla JavaScript**: Interactive functionality (no frameworks/libraries allowed)

### Field Syntax
- **Basic Fields**: `{{FieldName}}` - wrapped in double curly brackets
- **Special Fields**: `{{Tags}}`, `{{Type}}`, `{{Deck}}`, `{{Card}}`, `{{FrontSide}}`
- **Text Stripping**: `{{text:FieldName}}` - removes formatting
- **Conditional Logic**: `{{#Field}}...{{/Field}}` - conditional replacements

## Cross-Platform Compatibility

### Platform Differences
- **Anki Desktop**: Chromium engine, supports window object persistence
- **AnkiMobile**: Safari engine, limited JavaScript support
- **AnkiDroid**: WebView engine, supports sessionStorage
- **AnkiWeb**: Browser-based, consistent with desktop behavior

### Version Requirements
- **Modern Features**: Anki 2.1.50+, AnkiMobile 2.0.84+, AnkiDroid 2.17+
- **TTS Features**: Same version requirements as above
- **Template Editing**: Anki 2.1.28+ supports Ctrl+1/2/3 shortcuts

### JavaScript Constraints
- **Vanilla JavaScript Only**: No jQuery, React, or other frameworks
- **Variable Declarations**: Use `var` instead of `let` for cross-platform compatibility
- **Platform Detection**: Required for feature adaptation

## Context Preservation & State Management

### The Core Problem
JavaScript variables don't persist between:
- Front and back of same card
- Different cards in review session
- Platform transitions

### Critical Issues
- **Variable Scope**: `var` creates global scope, `let` doesn't work on AnkiMobile
- **Context Reset**: Variables reset across different cards when using `var`
- **Platform Inconsistency**: Works on desktop but not consistently on mobile

### Solution: Anki Persistence Library

**Primary Library**: `SimonLammer/anki-persistence` (GitHub)
- **Purpose**: Persist data between both sides of an Anki flashcard
- **Auto-Detection**: Chooses appropriate storage method per platform
- **Implementation**: 
  - Desktop/AnkiWeb: `Persistence_windowKey` (window object)
  - AnkiDroid: `Persistence_sessionStorage` (sessionStorage API)

**Common Use Cases**:
- Display same random number on both sides
- Transfer state from front to back
- Shuffle answers in multiple choice questions
- Preserve user input between card sides
- Maintain drag-and-drop state

### Technical Patterns

**IIFE Wrapper Pattern**:
```javascript
(function () {
    // Code wrapped in function scope
    var code = document.getElementById('code').innerText;
    eval(code);
})()
```

**Variable Initialization**:
- Always initialize variables to prevent cross-card contamination
- Use `var` for cross-platform compatibility

## Drag-and-Drop Implementation

### Current State (2024-2025)
Multiple production-ready templates exist with proven patterns:

1. **Interactive Flashcard Template with Drag and Drop Feedback** (Sept 2024)
2. **cjdduarte/anki-template-interactive-drag-drop** (GitHub)
3. **New Drag and Drop Interactive Matching Template** (Jan 2025)
4. **momomozhang/anki-template-interactive-drag-drop** (UI Improvements Branch)

### Proven Features
- **HTML5 Drag-and-Drop API**: Standard implementation approach
- **Visual Feedback**: ±1 indicators for correct/incorrect drops
- **Multiple Answers**: Pipe separator (`|`) for multiple correct answers
- **Dynamic Layouts**: Support for up to 9 categories, horizontal/vertical options
- **Randomization**: Shuffled order prevents pattern memorization
- **Markdown Support**: Available in newer templates

### Implementation Patterns
- Category-based drag zones
- Instant visual feedback on drop
- Touch-friendly targets for mobile
- Responsive design for small screens
- Platform-specific CSS classes

### Advanced UI/UX Patterns (from Production Analysis)

#### Visual Design System
**Color Palette Standards:**
- **Success Green**: `#58cc02` for correct answers and positive actions
- **Interactive Blue**: `#1cb0f6` for buttons and interactive elements
- **Feedback Colors**: Light green (#d7ffb8) for correct, light red (#ffdfe0) for incorrect
- **Neutral Grays**: Subtle backgrounds (#f0f0f0, #f9f9f9) for organization

**Typography & Layout:**
- **Font Stack**: 'Segoe UI' with fallbacks for cross-platform consistency
- **Responsive Design**: Flexbox-based layout with max-width constraints
- **Mobile-First**: Touch-friendly targets and responsive breakpoints

#### Enhanced Interaction Architecture
**Advanced Drag-and-Drop Features:**
- **Position Indicators**: Visual feedback showing where items will be dropped
- **Bidirectional Movement**: Terms can be dragged back to container or between positions
- **Insertion Logic**: Smart placement between existing terms (major UX improvement)
- **Contextual Drop Zones**: Dynamic highlighting during drag operations

**State Management Patterns:**
- **Game State Tracking**: Clear phases (`playing`, `checking`, `review`)
- **Dynamic Event Handling**: Reattaches events after DOM changes
- **Progressive Enhancement**: Works without JavaScript, enhanced with interactions

#### Learning-Centered UX Innovations
**Feedback Systems:**
- **Immediate Visual Response**: Color-coded correct/incorrect states
- **Progressive Disclosure**: Hints appear only after checking answers
- **Score Display**: +1/-1 icons with smooth animations
- **Contextual Hints**: Post-check answer revealing

**Adaptive Interface:**
- **Flexible Content Support**: Handles varying amounts of content
- **Reordering Support**: Drag terms within categories for fine-tuning
- **Extended Category Support**: Up to 9 categories with responsive layouts

#### Technical Architecture Patterns
**Component Design:**
- **Data-Driven Rendering**: Uses hidden Anki fields to populate content
- **Modular Components**: Reusable drag-drop elements
- **Event Delegation**: Efficient handling for dynamic content

**Performance Optimizations:**
- **Cached Selectors**: Minimal DOM queries
- **Hardware-Accelerated Transitions**: Smooth animations without blocking
- **Event Throttling**: Optimized drag event handling

#### Mobile-Specific Enhancements
**Touch Interaction:**
- **Gesture Recognition**: Proper touch event handling
- **Visual Feedback**: Enhanced touch states for mobile
- **Responsive Touch Targets**: Appropriately sized for finger interaction
- **Smooth Animations**: 60fps transitions on mobile devices

## Development Best Practices

### Template Editor Workflow
- **Access**: Click "Cards..." button in editing screen
- **Navigation**: Ctrl+1 (Front), Ctrl+2 (Back), Ctrl+3 (Styling)
- **Preview**: Real-time preview on right side of editor
- **External Editing**: Preferred over built-in editor for complex templates

### External File Integration
- **CSS Import**: `@import url("_filename.css");`
- **JavaScript Libraries**: Can be embedded for advanced users
- **IDE Support**: External editors provide syntax highlighting, linting

### Testing Strategy
- **Cross-Platform**: Test on desktop, mobile, and web
- **Version Compatibility**: Ensure compatibility with minimum required versions
- **State Persistence**: Verify data persists between front/back
- **Mobile Optimization**: Touch-friendly interactions, responsive design

## Platform-Specific Considerations

### Mobile Optimization
- **Automatic Scrolling**: Scroll to answer section on small screens
- **Touch Targets**: Appropriately sized for finger interaction
- **Responsive Design**: Adapts to screen size
- **Performance**: Lightweight JavaScript for mobile constraints

### AnkiWeb Compatibility
- **Cloud Sync**: Templates sync across all devices
- **Consistent Behavior**: No special requirements for web platform
- **Browser Support**: Works in modern browsers

### Styling Considerations
- **Platform-Specific CSS**: Special CSS classes for different platforms
- **Important Declarations**: Use `!important` for platform-specific overrides
- **Responsive Units**: Use relative units for cross-device compatibility

## Historical Context & Evolution

### Version Changes
- **Anki 2.0**: Had `window.py` object for Python-JavaScript interaction
- **Anki 2.1**: Eliminated persistent data storage, breaking old templates
- **Current**: Persistence requires external libraries or add-ons

### Add-on Solutions
- **Cookie Monster**: Restores JavaScript persistence functionality in Anki 2.1
- **JS Booster**: Original solution for Anki 2.0 (deprecated)

## Key Limitations & Warnings

### JavaScript Support
- **No Guarantee**: Anki provides JavaScript "without any support or warranty"
- **Future Compatibility**: No guarantee code will work in future Anki updates
- **Platform Variations**: Feature availability depends on client and OS

### Development Constraints
- **Built-in Editor**: Limited compared to modern IDEs
- **Debugging**: Difficult to debug across platforms
- **Performance**: Mobile devices have limited resources

## Implementation Recommendations

### For Drag-and-Drop Templates
1. **Use Anki Persistence Library**: Essential for state management
2. **Implement Visual Feedback**: Proven to enhance user experience
3. **Support Multiple Answers**: Use pipe separator for flexibility
4. **Test Cross-Platform**: Verify functionality on all target devices
5. **Optimize for Mobile**: Ensure touch-friendly interactions

### Advanced Implementation Recommendations (from Production Analysis)

#### Inline Drag-and-Drop Pattern (Project Requirement)
**Innovation**: Inline blanks within text flow rather than separate drop zones

**Technical Approach**:
- **Syntax**: Use `{{d1::text}}` format (d = drag-and-drop)
- **Editor Integration**: Cloze-style button for text selection and wrapping
- **Auto-population**: Extract selected text to Items and Answers fields
- **Rendering**: Convert `{{d1::text}}` to underlined gaps in study mode
- **Interaction**: Drag items to fill gaps within sentence flow

**User Experience**:
1. **Content Creation**: Copy/paste paragraph → select text → click button
2. **Editor View**: `{{d1::Elastic Beanstalk}}` syntax like Cloze cards
3. **Study View**: Underlined gaps with draggable items below
4. **Natural Flow**: Blanks integrated within text, not separate zones
5. **Answer Feedback**: Complete paragraph with color-coded correct answers
   - Green text for correct user answers
   - Red text for incorrect answers (shows correct word, not user input)
   - Maintains natural reading flow

**Key Benefits**:
- **Familiar UX**: Leverages existing Cloze deletion patterns
- **Inline Integration**: More natural reading experience
- **Auto-generation**: Reduces manual field management
- **Scalable**: Works with any text length or complexity

#### UI/UX Design Patterns
1. **Adopt Proven Color System**: Use established color tokens for consistency
   - Success Green (#58cc02), Interactive Blue (#1cb0f6)
   - Feedback colors for immediate visual response
2. **Implement Position Indicators**: Visual feedback for drop target positioning
3. **Support Bidirectional Movement**: Allow terms to move between containers
4. **Add Game State Management**: Clear phases for playing, checking, reviewing
5. **Progressive Enhancement**: Ensure functionality without JavaScript

#### Technical Architecture
1. **Component-Based Design**: Modular, reusable drag-drop elements
2. **Data-Driven Rendering**: Use hidden Anki fields for content population
3. **Event Delegation**: Efficient handling for dynamic content
4. **Performance Optimization**: Cached selectors and hardware-accelerated transitions
5. **Extended Category Support**: Scale up to 9 categories with responsive layouts

#### Mobile-First Considerations
1. **Touch-Optimized Interactions**: Proper gesture recognition and feedback
2. **Responsive Touch Targets**: Appropriately sized for finger interaction
3. **Smooth Animations**: 60fps transitions optimized for mobile devices
4. **Adaptive Layouts**: Flexible design that works across screen sizes

### Code Quality
- **Vanilla JavaScript**: No external frameworks
- **Proper Scoping**: Use IIFE wrapper for variable isolation
- **Error Handling**: Graceful degradation for unsupported features
- **Documentation**: Clear comments for maintenance

### Performance Optimization
- **Lightweight Code**: Minimize JavaScript for mobile performance
- **Efficient DOM Manipulation**: Avoid frequent DOM queries
- **Event Handling**: Use event delegation where appropriate

## Future Considerations

### Emerging Trends
- **Markdown Integration**: Growing support in newer templates
- **Enhanced Visual Feedback**: More sophisticated animation systems
- **Mobile-First Design**: Increasing focus on mobile experience

### Potential Improvements
- **External Template Support**: Future Anki versions may support external files
- **Better JavaScript Integration**: Enhanced debugging and development tools
- **Standardized Persistence**: Built-in state management solutions

---

## Sources

- **Anki Manual**: Official documentation for templates, styling, and field syntax
- **Anki Forums**: Community discussions and template sharing
- **GitHub Repositories**: Open-source template implementations
- **Stack Overflow**: Technical solutions and troubleshooting
- **AnkiDroid Issues**: Mobile-specific compatibility discussions

## Production Template Analysis

### Analyzed Repository
- **momomozhang/anki-template-interactive-drag-drop** (UI Improvements Branch)
- **Analysis Date**: July 2025
- **Focus**: UI/UX design patterns, interaction architecture, and mobile optimization

### Key Findings Summary
This production template demonstrates sophisticated UI/UX patterns including:
- Advanced drag-and-drop with position indicators and bidirectional movement
- Proven color system and responsive design principles
- Game state management with progressive enhancement
- Mobile-first architecture with touch optimization
- Performance optimizations for cross-platform compatibility

The analysis reveals mature patterns that can be adapted and improved upon for our implementation.

*This research was conducted in July 2025 and reflects the current state of Anki template development practices.*