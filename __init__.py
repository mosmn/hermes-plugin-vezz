"""
vezz-me - Webpage reading assistant and prompt-preset plugin for Hermes Agent.

Exposes model-callable tools for:
- vezz_extract_reading_context: Extracts dense semantic markdown and paragraphs from webpage excerpts.
- vezz_format_prompt_preset: Formats highlighted text with Vezz reading assistant prompt templates.
"""

from __future__ import annotations

import logging
import re
from typing import Any

from tools.registry import tool_error, tool_result

logger = logging.getLogger(__name__)

READING_CONTEXT_SCHEMA = {
    "description": (
        "Extract clean, dense reading context from raw webpage text or highlighted excerpts, "
        "removing boilerplate and identifying key topics for Hermes LLM reasoning."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "raw_content": {
                "type": "string",
                "description": "Webpage text, markdown, or highlighted selection.",
            },
            "focus_query": {
                "type": "string",
                "description": "Optional search term or question to extract relevant passages for.",
            },
        },
        "required": ["raw_content"],
        "additionalProperties": False,
    },
}

PROMPT_PRESET_SCHEMA = {
    "description": (
        "Retrieve a Vezz-optimized prompt structure for explaining, summarizing, or analyzing text."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "preset": {
                "type": "string",
                "enum": ["concise", "technical", "study", "rephrase"],
                "description": "The prompt style preset to apply.",
            },
            "selected_text": {
                "type": "string",
                "description": "The target text passage to format.",
            },
        },
        "required": ["preset", "selected_text"],
        "additionalProperties": False,
    },
}


def _handle_extract_context(args: dict, **kwargs: Any) -> str:
    del kwargs
    content = str(args.get("raw_content", "")).strip()
    if not content:
        return tool_error("raw_content cannot be empty")

    query = str(args.get("focus_query", "")).strip().lower()

    # Clean redundant whitespace
    cleaned = re.sub(r"\n{3,}", "\n\n", content)
    words = cleaned.split()
    word_count = len(words)

    extracted = cleaned
    if query:
        paragraphs = cleaned.split("\n\n")
        matching = [p for p in paragraphs if query in p.lower()]
        if matching:
            extracted = "\n\n".join(matching)

    return tool_result({
        "success": True,
        "word_count": word_count,
        "extracted_context": extracted,
        "has_focused_passages": bool(query),
    })


def _handle_format_prompt(args: dict, **kwargs: Any) -> str:
    del kwargs
    preset = args.get("preset", "concise")
    text = str(args.get("selected_text", "")).strip()

    prompts = {
        "concise": f"Explain this clearly in 2-3 bullet points:\n\n{text}",
        "technical": f"Break down the technical mechanics, assumptions, and edge cases:\n\n{text}",
        "study": f"Explain this concept step-by-step with a real-world analogy and key definitions:\n\n{text}",
        "rephrase": f"Rephrase this in clear, natural prose while preserving all key facts:\n\n{text}",
    }

    return tool_result({
        "success": True,
        "preset": preset,
        "formatted_prompt": prompts.get(preset, prompts["concise"]),
    })


def register(ctx: Any) -> None:
    """Register Vezz reading context and prompt tools."""
    ctx.register_tool(
        name="vezz_extract_reading_context",
        toolset="vezz_me",
        schema=READING_CONTEXT_SCHEMA,
        handler=_handle_extract_context,
        description="Clean and structure webpage text context for LLM analysis.",
    )
    ctx.register_tool(
        name="vezz_format_prompt_preset",
        toolset="vezz_me",
        schema=PROMPT_PRESET_SCHEMA,
        handler=_handle_format_prompt,
        description="Format highlighted text with Vezz reading assistant prompt templates.",
    )
    logger.debug("Registered vezz-me tools")
