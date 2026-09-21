# Design

## Principles
Clarity over decoration, source visibility, predictable states, keyboard-friendly controls, and an artifact workspace that never hides the conversation.

## Layout
Desktop uses a three-column layout: sessions, chat, artifact viewer. At narrower widths the artifact panel hides first, then the session list becomes hidden so the chat remains usable.

## Chat
User messages are visually distinct from assistant messages. Sources appear directly below grounded assistant responses. Enter sends; Shift+Enter creates a new line.

## Artifact viewer
Markdown is rendered as sanitized HTML. HTML artifacts are displayed inside a sandboxed iframe. Empty/loading/error states are explicit.

## Accessibility
Semantic buttons, visible focus via browser defaults, labels/placeholders, readable contrast, and keyboard submission are included. A future iteration should add formal automated a11y testing.
