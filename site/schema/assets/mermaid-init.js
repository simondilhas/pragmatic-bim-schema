import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs";

mermaid.initialize({ startOnLoad: false, securityLevel: "loose" });
await mermaid.run({ querySelector: ".mermaid" });
