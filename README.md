# 🎨 Elite Graphic Designer - Multi-Agent Swarm

> **"Design is not just what it looks like and feels like. Design is how it works."**

A production-grade **Multi-Agent Orchestration Swarm** operating at the highest attainable level of human graphic design mastery. Using the official `claude-agent-sdk`, this package delegates to specialist subagents for typography, color, brand systems, layouts, and QA.

## 🏛️ Swarm Architecture
- **Master Orchestrator**: `elite-graphic-designer` (Opus)
- **Specialist Subagent**: `typography-master` (Sonnet)
- **Specialist Subagent**: `color-architect` (Sonnet)
- **Specialist Subagent**: `brand-system-builder` (Sonnet)
- **Specialist Subagent**: `ux-layout-engineer` (Sonnet)
- **QA Sentinel**: `design-qa-sentinel` (Haiku)

## 🚀 Quick Start

### 1. Install the SDK
```bash
pip install claude-agent-sdk
export ANTHROPIC_API_KEY=your-api-key-here
```

### 2. Run the Swarm
```bash
cd factory/production/agents/elite-graphic-designer
python main.py
```

## 🧠 Persistent Memory
This agent utilizes `memory: project` to persist brand patterns, client knowledge, and design decisions across sessions inside `.claude/agent-memory/elite-graphic-designer/MEMORY.md`.

## 📄 License
MIT License - Construct visually. 🎨
