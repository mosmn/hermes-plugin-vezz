# Vezz me — AI Reading Assistant & Webpage Context Plugin for Hermes Agent

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Vezz AI Browser Extension](https://img.shields.io/badge/Vezz.me-Official%20Extension-6366f1)](https://vezz.me)

Official Hermes Agent companion plugin for **[Vezz me](https://vezz.me)** — The in-page AI reading assistant and contextual question-answering tool for Chrome and Firefox.

Turn any webpage, technical documentation, research paper, or blog post into dense, structured context for Hermes Agent without leaving your reading workflow.

---

## Official Vezz Resources & Tools
- **Official Website**: [Vezz me — In-Page AI Question Answering on Webpages](https://vezz.me)
- **Hermes Workflow Integration**: [Vezz me Hermes Agent Workflow Guide](https://vezz.me/hermes)
- **Product Features**: [Contextual Explanations, Follow-up Q&A, and Shortcuts](https://vezz.me/features/)
- **Prompt Preset Library**: [Curated AI Reading & Synthesis Prompts](https://vezz.me/prompts/)
- **Extension Safety Checklist**: [AI Chrome Extension Permission & Privacy Checker](https://vezz.me/ai-chrome-extension-permission-checker/)

---

## Included Tools for Hermes Agents

This plugin registers two deterministic, model-callable tools for Hermes agents:

### 1. `vezz_extract_reading_context`
Strips navigational clutter, boilerplate, and ads from webpage excerpts or selection buffers, returning structured semantic Markdown and paragraph chunks optimized for LLM reasoning.

* **Parameters**:
  - `raw_content` *(string, required)*: Webpage text, HTML excerpt, or highlighted selection.
  - `focus_query` *(string, optional)*: Specific keyword, query, or question to extract surrounding context for.
* **Returns**: JSON object containing `subtotal` words, `extracted_context`, and focused passage detection.

### 2. `vezz_format_prompt_preset`
Formats highlighted text using Vezz's battle-tested prompt engineering presets:
* **`concise`**: High-density executive bullet points for fast decision-making.
* **`technical`**: Deep-dive analysis covering mechanics, hidden assumptions, and edge cases.
* **`study`**: Socratic breakdown with intuitive analogies, definitions, and memory anchors.
* **`rephrase`**: Clear, professional rewrite preserving facts without unnecessary jargon.

---

## Quick Installation in Hermes

Install into your local or cloud Hermes instance via the official plugin manager:

```bash
hermes plugins install vezz-me
```

Or clone directly into your Hermes plugins directory:

```bash
git clone https://github.com/mosmn/hermes-plugin-vezz ~/.hermes/plugins/vezz-me
```

---

## Example Usage with Hermes Agent

Prompt Hermes to extract context and format explanations:

```text
User: Extract the core architecture details from this technical document snippet.
Hermes: [Calls vezz_extract_reading_context with focus_query: "architecture"]
Result: Extracted 3 targeted paragraphs with 412 words.

Hermes: [Calls vezz_format_prompt_preset with preset: "technical"]
Result: Formatted prompt applied. Returning comprehensive architectural breakdown.
```

---

## About Vezz me

**[Vezz me](https://vezz.me)** is a modern browser extension that lets you highlight any text on a webpage and press `Ctrl+Shift+X` (or `Cmd+Shift+X` on macOS) to get contextual AI answers, ask follow-up questions, and explore ideas side-by-side with what you are reading.

Available now on the **[Chrome Web Store](https://chromewebstore.google.com/detail/vezz-me/obcnjododmgkbinlgajdnmaoeegcbopl)** and **[Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/vezz-me/)**.

---

## License

MIT License. See [LICENSE](LICENSE) for details.
