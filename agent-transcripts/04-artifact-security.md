# Artifact security
Added server-side HTML sanitization for scripts, event handlers, dangerous URL schemes, and untrusted iframes. The frontend additionally uses DOMPurify and a sandboxed iframe with scripts disabled.
