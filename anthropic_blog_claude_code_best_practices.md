# Claude Code Best Practices

**Source**: [https://www.anthropic.com/engineering/claude-code-best-practices](https://www.anthropic.com/engineering/claude-code-best-practices)

*This document is based on the official Anthropic blog post "Claude Code Best Practices" with additional insights from the broader Claude Code community and documentation.*

---

A comprehensive guide to effective patterns and workflows for using Claude Code across various codebases, languages, and environments.

## Introduction

Claude Code is intentionally low-level and unopinionated, providing close to raw model access without forcing specific workflows. This design philosophy creates a flexible, customizable, scriptable, and safe power tool. While powerful, this flexibility presents a learning curve for engineers new to agentic coding tools—at least until they develop their own best practices.

## Core Principles

### Think of Claude as a Fast Intern with Great Memory

Claude Code works best when you treat it like a very capable but inexperienced team member:
- It has perfect memory of your entire codebase
- It needs clear instructions and context
- It benefits from planning before implementation
- It learns from feedback and corrections

### Be Explicit and Direct

Claude 4 models respond well to clear, explicit instructions. Being specific about your desired output enhances results:
- Provide clear, step-by-step instructions
- Specify the exact behavior you want
- Include context about why something is important
- Use examples to clarify expectations

## Memory Management with CLAUDE.md

Claude Code automatically maintains a `CLAUDE.md` file in your project root that serves as its memory system:

### Best Practices for CLAUDE.md
- **Keep it updated**: When Claude makes mistakes, ask it to update CLAUDE.md to avoid repeating them
- **Document patterns**: Include coding standards, architectural decisions, and team preferences
- **Set expectations**: Define how Claude should handle commits, testing, and documentation
- **Include context**: Add project-specific information that helps Claude understand your codebase

### Managing Long Context
For complex tasks that might fill the context window, use these techniques:

**Reference Quotes**: Ask Claude to find and extract relevant quotes before answering:
```xml
<instructions>
Answer the user's question based on the provided document. 
Before you write the final answer, use a <scratchpad> to write down 
the exact quotes from the document that are most relevant to the question.
</instructions>
```

**In-Context Examples**: Provide examples of correctly answered questions about other parts of the document.

## Core Workflows

### 1. Explore, Plan, Code, Commit (The Foundation)

This is the most versatile workflow for tackling any new feature or bug fix:

**Explore**: Ask Claude to read relevant files, images (like UI mockups), or URLs. Crucially, instruct it not to write any code yet. The goal is information gathering.

**Plan**: Ask Claude to create a detailed, step-by-step plan. Use trigger words like "think" to encourage deeper consideration.

**Code**: Ask Claude to implement its solution in code. This is also a good place to ask it to explicitly verify the reasonableness of its solution.

**Commit**: Ask Claude to commit the result and create a pull request. If relevant, have Claude update any READMEs or changelogs.

### 2. Test-Driven Development (TDD)

TDD becomes even more powerful with agentic coding:

1. **Write Tests**: Ask Claude to write tests based on expected input/output pairs
2. **Confirm Failure**: Tell Claude to run the tests and confirm they fail (explicitly tell it not to write implementation code yet)
3. **Commit Tests**: Ask Claude to commit the tests when you're satisfied
4. **Write Code**: Instruct Claude to write code that passes the tests, without modifying the tests
5. **Iterate**: Tell Claude to keep going until all tests pass
6. **Commit Code**: Have Claude commit the final implementation

### 3. Codebase Q&A (Onboarding)

Use Claude as your personal tour guide when joining new projects:
- Ask questions as you would a senior developer
- No special prompting required—just ask
- Claude will agentically search the codebase and synthesize answers
- This dramatically speeds up ramp-up time

## Advanced Features and Tips

### Thinking Modes

Use specific trigger words to activate extended thinking modes with progressively more computation budget:
- `"think"` → 4,000 tokens
- `"think hard"` or `"megathink"` → 10,000 tokens  
- `"think harder"` or `"ultrathink"` → 31,999 tokens

### Custom Slash Commands

Create reusable prompt templates in the `.claude/commands` folder:

**Example**: Create `.claude/commands/issue.md`:
```markdown
Please analyze and fix the GitHub issue: $ARGUMENTS. Follow these steps:
1. Use `gh issue view` to get the issue details
2. Understand the problem described in the issue
3. Search the codebase for relevant files
4. Implement the necessary changes to fix the issue
5. Write and run tests to verify the fix
6. Ensure code passes linting and type checking
7. Create a descriptive commit message
8. Push and create a PR
```

Use with: `/issue #123`

### Git and GitHub Integration

Claude is fluent with git and GitHub CLI:
- **Commit messages**: Claude creates better commit messages than most humans due to "perfect memory"
- **Pull requests**: Use shorthand "pr" to generate appropriate PR descriptions
- **Code review**: Tell Claude to fix comments on your PR and push back to the branch
- **Merge conflicts**: Claude can resolve complex merge conflicts

### Command Line Integration

**Headless Mode**: Use `-p` flag for non-interactive mode:
```bash
claude -p "analyze this error log and suggest fixes"
```

**Piping**: Chain with other CLI tools:
```bash
cat data.csv | claude -p "Who won the most games?"
tail -f app.log | claude -p "Slack me if you see any anomalies"
```

## Safety and Best Practices

### Permission Management
- Only grant "auto execute" permission for read-only commands
- Say "Yes" to: `git status`, `ls`, `cat`
- Say "No" to: `git commit`, `rm`, `git add`

### Version Control Safety
- Commit frequently after significant changes
- Don't be afraid to use `git revert` or `git reset`
- Sometimes it's faster to revert and try a more specific prompt

### Cost Management
- Monitor token usage, especially with thinking modes
- Consider upgrading to Claude Max plans for heavy usage
- Use shorter, more focused prompts when possible

## Advanced Workflows

### Jupyter Notebook Integration
- Keep Claude Code and `.ipynb` files open side-by-side in VS Code
- Claude can interpret outputs, including images
- Ask Claude to clean up notebooks before sharing with colleagues

### Multi-Claude Workflows
- Run multiple instances of Claude for maximum efficiency
- Use different instances for different aspects of a project
- Coordinate between instances using shared files

### CI/CD Integration
- Use headless mode (`-p` flag) in GitHub Actions
- Automate issue triage with label assignment
- Generate release notes automatically

## Quality Improvements

### Documentation and Communication
- Ask Claude to write clear PR descriptions and commit messages
- Use Claude for generating diagrams (GraphViz, Mermaid)
- Have Claude update documentation and changelogs

### Code Quality
- Implement comprehensive unit tests
- Add inline documentation and comments
- Fix linting issues and formatting
- Set up pre-commit hooks for quality checks

### Architecture and Design
- Use Claude for code reviews and architectural analysis
- Generate design documents with diagrams
- Analyze and improve code structure

## Common Pitfalls to Avoid

1. **Skipping the planning phase**: Always have Claude read and plan before coding
2. **Giving too broad permissions**: Be selective about what commands Claude can auto-execute
3. **Not updating CLAUDE.md**: Failing to document lessons learned and preferences
4. **Overthinking prompts**: Simple, clear instructions often work best
5. **Not using version control**: Commit frequently to enable easy rollbacks

## Getting Started Checklist

- [ ] Install Claude Code: `npm install -g @anthropic-ai/claude-code`
- [ ] Set up GitHub CLI: `gh auth login`
- [ ] Navigate to your project: `cd your-project`
- [ ] Start Claude: `claude`
- [ ] Create initial CLAUDE.md with project context
- [ ] Set up custom slash commands in `.claude/commands/`
- [ ] Configure pre-commit hooks for quality checks
- [ ] Practice with the Explore → Plan → Code → Commit workflow

## Conclusion

Claude Code represents a new paradigm in software development where AI becomes a true collaborative partner. The key to success is treating it as a capable but junior team member that needs clear direction, learns from feedback, and excels when given structured workflows.

Remember: these are starting points, not rigid rules. Experiment with different approaches and develop patterns that work best for your specific use cases and team dynamics.

---

## Sources and Attribution

**Primary Source**: [Claude Code Best Practices - Anthropic Engineering Blog](https://www.anthropic.com/engineering/claude-code-best-practices)

**Additional Sources**:
- [Claude Code Documentation - Anthropic](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude 4 Prompt Engineering Best Practices - Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices)
- Community insights and practical experiences from Claude Code users

*This guide synthesizes best practices from Anthropic's engineering teams and the broader Claude Code user community. Continue experimenting and sharing your discoveries to help advance the field of agentic coding.*