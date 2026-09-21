# Manual UI Test Plan

1. Start Postgres, Ollama, backend, and frontend.
2. Check `/health` and `/api/settings/model`.
3. Create New Chat.
4. Ask a grounded product question and verify source cards.
5. Ask a follow-up and verify it uses the same session context.
6. Create a second chat and verify its message history starts empty.
7. Generate a Ship 30 for 30 essay and verify ~1,250-word output plus sources.
8. Request a Markdown artifact and verify the viewer.
9. Request an HTML artifact and verify sandboxed rendering.
10. Try HTML containing `<script>`, `onclick`, `javascript:` and an untrusted iframe; verify payloads do not execute/render.
11. Stop Ollama; verify the UI reports local model unavailability while the API remains alive.
12. Restart Ollama and verify requests work again.
13. Restart Postgres; verify persisted sessions/messages remain after reconnect.
