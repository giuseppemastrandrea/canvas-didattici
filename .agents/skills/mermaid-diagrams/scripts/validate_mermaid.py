#!/usr/bin/env python3
"""
validate_mermaid.py
Utility per validare e rilevare errori comuni nei diagrammi Mermaid JS
(specializzata per Flowchart, Mindmap e Timeline).
"""

import sys
import re
from typing import List, Tuple

def extract_mermaid_blocks(content: str) -> List[Tuple[int, str]]:
    """Estrae i blocchi mermaid markdown con il numero di riga di inizio."""
    blocks = []
    lines = content.splitlines()
    in_block = False
    current_block = []
    start_line = 0

    for idx, line in enumerate(lines, 1):
        if line.strip().startswith("```mermaid"):
            in_block = True
            current_block = []
            start_line = idx
            continue
        elif in_block and line.strip().startswith("```"):
            in_block = False
            blocks.append((start_line, "\n".join(current_block)))
            continue
        
        if in_block:
            current_block.append(line)

    # Se l'intero file è codice mermaid senza triple backtick
    if not blocks and content.strip():
        first_line = content.strip().splitlines()[0].strip()
        if any(first_line.startswith(prefix) for prefix in ["flowchart", "graph", "mindmap", "timeline"]):
            blocks.append((1, content))

    return blocks

def validate_flowchart(code: str) -> List[str]:
    errors = []
    lines = [l.strip() for l in code.splitlines() if l.strip()]
    subgraph_count = 0

    reserved_ids = {"end", "subgraph", "graph", "flowchart", "style", "class", "default"}

    for line_idx, line in enumerate(lines, 1):
        # Ignora commenti
        if line.startswith("%%"):
            continue

        if line.startswith("subgraph"):
            subgraph_count += 1
        elif line == "end":
            subgraph_count -= 1
            if subgraph_count < 0:
                errors.append(f"Riga {line_idx}: blocco 'end' senza un 'subgraph' aperto.")

        # Rileva ID riservati usati come nodi
        for word in reserved_ids:
            if re.search(rf"\b{word}\s*-->", line) or re.search(rf"-->\s*{word}\b", line):
                errors.append(f"Riga {line_idx}: Uso di parola riservata '{word}' come identificatore di nodo.")

        # Rileva parentesi non quotate dentro definizioni nodi: es. A(Testo (con parentesi))
        nested_parens = re.findall(r'\w+\([^\"]*?\([^\"]*?\)[^\"]*?\)', line)
        if nested_parens:
            errors.append(f"Riga {line_idx}: Parentesi annidate non racchiuse tra virgolette: {nested_parens[0]}. Usa nodi quotati come `id[\"Testo (info)\"]`.")

    if subgraph_count > 0:
        errors.append(f"Mancano {subgraph_count} blocchi 'end' di chiusura per i subgraph aperti.")

    return errors

def validate_mindmap(code: str) -> List[str]:
    errors = []
    lines = [l for l in code.splitlines() if l.strip()]
    
    # Controllo frecce illegali in mindmap
    for line_idx, line in enumerate(lines, 1):
        if "-->" in line or "---" in line or "==>" in line:
            errors.append(f"Riga {line_idx}: Trovata freccia ('-->'). Le Mindmap usano solo indentazione, non connettori.")

    # Controllo unicità della radice
    indent_levels = []
    for line in lines[1:]:  # salta riga "mindmap"
        stripped = line.strip()
        if stripped.startswith("%%") or stripped.startswith("classDef"):
            continue
        indent = len(line) - len(line.lstrip(" "))
        if "\t" in line:
            errors.append("Rilevata tabulazione: usa spazi invece di tab per l'indentazione della mindmap.")
        indent_levels.append((indent, stripped))

    root_candidates = [text for indent, text in indent_levels if indent == 2 or indent == 4]
    # Se il primo livello ha più nodi alla radice primaria
    if indent_levels:
        min_indent = min(indent for indent, _ in indent_levels)
        min_nodes = [text for indent, text in indent_levels if indent == min_indent]
        if len(min_nodes) > 1:
            errors.append(f"Rilevati più nodi radice al livello base ({len(min_nodes)} trovati: {min_nodes[:2]}...). Una mindmap richiede una singola radice.")

    return errors

def validate_timeline(code: str) -> List[str]:
    errors = []
    lines = [l.strip() for l in code.splitlines() if l.strip()]

    for line_idx, line in enumerate(lines, 1):
        if line.startswith("%%") or line.startswith("timeline") or line.startswith("title") or line.startswith("section"):
            continue
        if ":" not in line:
            errors.append(f"Riga {line_idx}: Riga dell'evento senza separatore ':' -> '{line}'")

    return errors

def validate_block(start_line: int, code: str) -> List[str]:
    errors = []
    first_non_empty = next((l.strip() for l in code.splitlines() if l.strip() and not l.strip().startswith("%%")), "")
    
    if first_non_empty.startswith("flowchart") or first_non_empty.startswith("graph"):
        sub_errs = validate_flowchart(code)
    elif first_non_empty.startswith("mindmap"):
        sub_errs = validate_mindmap(code)
    elif first_non_empty.startswith("timeline"):
        sub_errs = validate_timeline(code)
    else:
        sub_errs = [f"Tipo di diagramma non riconosciuto o non supportato per questa skill: '{first_non_empty}'"]

    for err in sub_errs:
        errors.append(f"[Linea {start_line}] {err}")

    return errors

def main():
    if len(sys.argv) < 2:
        print("Uso: python validate_mermaid.py <file.md>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Errore lettura file: {e}")
        sys.exit(1)

    blocks = extract_mermaid_blocks(content)
    if not blocks:
        print(f"Nessun blocco Mermaid trovato in {file_path}.")
        sys.exit(0)

    total_errors = []
    for start_line, block in blocks:
        errs = validate_block(start_line, block)
        total_errors.extend(errs)

    if total_errors:
        print(f"Rilevati {len(total_errors)} problemi:")
        for err in total_errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print(f"Tutti i {len(blocks)} diagrammi Mermaid in {file_path} sono validi!")
        sys.exit(0)

if __name__ == "__main__":
    main()
