import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def run_elite_design_session(brief: str) -> None:
    """
    Run the Elite Graphic Design multi-agent system.
    Loads all agents from .claude/agents/ via setting_sources=["project"].
    The Task tool enables the orchestrator to delegate to specialist subagents.
    """
    print(f"🎨 Activating Elite Graphic Design System...")
    print(f"📋 Brief: {brief}\n")
    print("─" * 60)

    async for message in query(
        prompt=brief,
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Write", "Bash", "Agent"],
            setting_sources=["project"],  # Loads .claude/agents/ files
        ),
    ):
        # Stream assistant thinking and tool use
        if hasattr(message, "content") and message.content:
            for block in message.content:
                # Detect subagent delegation
                if getattr(block, "type", None) == "tool_use" and block.name == "Task":
                    agent_type = block.input.get("subagent_type", "unknown")
                    print(f"\n🤖 Delegating to specialist: [{agent_type}]")

        # Print the final synthesized result
        if hasattr(message, "result"):
            print("\n" + "═" * 60)
            print("✅ DESIGN SYSTEM COMPLETE")
            print("═" * 60)
            print(message.result)

# ── Example briefs ──────────────────────────────────────────────

LUXURY_SKINCARE = """
A luxury skincare brand called 'Lumière' targeting affluent women 35–55 
needs a complete brand identity system. The brand values: scientific precision, 
natural elegance, and timeless sophistication. Build the full creative direction 
including color architecture, typography system, layout principles, and brand 
guidelines. Run specialist subagents for typography, color, and layout in parallel, 
then synthesize into a complete Brand Identity Specification. Run QA before delivering.
"""

SUSTAINABLE_TECH = """
A sustainable technology startup called 'Verde' building carbon tracking software
needs a complete design system. Values: clarity, optimism, environmental urgency.
Target audience: enterprise sustainability officers aged 28–45. Build the complete
UI design system with component specifications, color system, and typography stack.
"""

if __name__ == "__main__":
    asyncio.run(run_elite_design_session(LUXURY_SKINCARE))
