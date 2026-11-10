---
name: mermaid-diagrams
description: >-
  Specialized skill for generating, designing, and validating diagrams with Mermaid JS.
  Focuses on Flowcharts (diagrammi di flusso), Mindmaps (mappe concettuali), and Timelines
  (linee temporali/cronologie). Use this skill whenever the user asks to create, convert,
  or refine diagrams, conceptual maps, algorithmic workflows, or chronological timelines.
---

# Mermaid JS Diagrams: Flowcharts, Mindmaps & Timelines

Questa skill guida l'agente nella progettazione e generazione di diagrammi **Mermaid JS** robusti, privi di errori di parsing e ottimizzati per la leggibilità visiva e didattica.

La skill è specializzata nei tre tipi di diagramma richiesti:
1. **Flowcharts (Diagrammi di flusso)**: Processi, algoritmi, alberi decisionali e pipeline.
2. **Mindmaps (Mappe concettuali e mentali)**: Tassonomie, gerarchie concettuali e schematizzazioni tematiche.
3. **Timelines (Linee temporali e cronologie)**: Sequenze temporali, epoche storiche, evoluzione di idee e roadmap.

---

## 1. Matrice Decisionale: Quale Diagramma Scegliere?

Se l'utente non specifica esplicitamente la sintassi desiderata, seleziona il formato più adatto in base alla natura dei dati:

| Obiettivo dell'Utente | Diagramma Raccomandato | Dichiarazione Chiave |
| :--- | :--- | :--- |
| Processo passo-passo, algoritmo, condizioni IF/ELSE, bivi logici | **Flowchart** | `flowchart TD` (verticale) o `flowchart LR` (orizzontale) |
| Relazioni concettuali attorno a un tema cardine, categorie, anatomia di un argomento | **Mindmap** | `mindmap` con singola radice `root((...))` |
| Eventi ordinati nel tempo, date, secoli, fasi di progetto, evoluzione storica | **Timeline** | `timeline` con `title` e `section` opzionali |

---

## 2. Guida Rapida di Sintassi

### A. Flowcharts (Diagrammi di Flusso)
*Documentazione dettagliata:* [Guida Completa Flowchart](./references/flowchart.md) | [Esempi Pratici Flowchart](./examples/flowcharts.md)

- **Orientamento:** `flowchart TD` (alto-basso) o `flowchart LR` (sinistra-destra).
- **Forme dei nodi principali:**
  - `id["Testo rettangolare"]`: Azione o passaggio standard.
  - `id(["Inizio/Fine"])`: Terminatore a pillola (Stadium).
  - `id{"Condizione logica?"}`: Bivio decisionale (Rombo).
  - `id[("Database / Archivio")]`: Fonte dati (Cilindro).
  - `id[/"Input o Output"/]`: Acquisizione o restituzione dati.
- **Collegamenti:** `A --> B`, con etichetta `A -->|Etichetta| B`, tratteggiato `A -.-> B`, spesso `A ==> B`.
- **Raggruppamenti:** `subgraph NomeGruppo ["Titolo"] ... end`.

### B. Mindmaps (Mappe Concettuali)
*Documentazione dettagliata:* [Guida Completa Mindmap](./references/mindmap.md) | [Esempi Pratici Mindmap](./examples/mindmaps.md)

- **Orientamento:** Centrifugo, gestito puramente dall'**indentazione** (2 o 4 spazi costanti).
- **Forme dei nodi:**
  - `root((Concetto Centrale))`: Cerchio (raccomandato per il nodo radice).
  - `[Testo]`: Rettangolo (definizioni, categorie).
  - `(Testo)`: Arrotondato (argomenti secondari).
  - `))Testo((`: Nuvola/Bang (idee salienti, eccezioni).
  - `{{Testo}}`: Esagono (domande guida).
  - `Testo semplice`: Senza contorno (foglie terminali, dettagli).
- **Importante:** In una mindmap **NON SI USANO FRECCE (`-->`)**.

### C. Timelines (Linee Temporali)
*Documentazione dettagliata:* [Guida Completa Timeline](./references/timeline.md) | [Esempi Pratici Timeline](./examples/timelines.md)

- **Dichiarazione:** `timeline`
- **Titolo:** `title Titolo descrittivo`
- **Sezioni (Epoche / Fasi):** `section Nome della Fase`
- **Formato Periodo ed Evento:**
  ```mermaid
  timeline
      title Titolo Esempio
      section Epoca 1
          Data1 : Evento singolo
          Data2 : Evento A
                : Evento B (stessa data)
  ```

---

## 3. Regole d'Oro per Evitare Errori di Rendering

1. **Racchiudi SEMPRE il testo tra virgolette nei Flowchart se contiene caratteri speciali:**
   - Se il testo include parentesi `()`, quadre `[]`, graffe `{}`, due punti o virgole, usa sempre le virgolette doppie:
     - `A{"Verifica (es. condizione A)"}`
2. **Nelle Mindmap mantieni una sola radice:**
   - La mindmap deve avere un solo elemento al primo livello di indentazione.
   - Non usare frecce o connettori.
3. **Nelle Timeline fai attenzione ai due punti (`:`):**
   - Poiché `:` è il delimitatore sintattico tra Periodo ed Evento, evita di usare `:` sciolti all'interno delle descrizioni testuali.
4. **Nessun ID con parole riservate:**
   - Non usare come identificatori di nodo: `end`, `subgraph`, `graph`, `flowchart`, `style`, `class`, `default`.
5. **Andare a capo nel testo dei nodi:**
   - Usa `<br/>` o `<br>` all'interno delle etichette (es. `node["Prima riga<br/>Seconda riga"]`).

---

## 4. Validazione dei Diagrammi

La skill include uno script Python per verificare che il codice Mermaid generato non contenga violazioni sintattiche comuni:

```bash
python3 .agents/skills/mermaid-diagrams/scripts/validate_mermaid.py percorso/del/file.md
```

Lo script controlla:
- Chiusura corretta dei blocchi `subgraph ... end` nei Flowchart.
- Assenza di frecce `-->` o indentazioni errate nelle Mindmap.
- Presenza corretta dei delimitatori `:` e titoli nelle Timeline.
- Utilizzo sicuro delle virgolette in presenza di parentesi annidate.

---

## 5. Indice delle Risorse

- **Documentazione di Riferimento:**
  - [flowchart.md](./references/flowchart.md): Sintassi, forme, stili e subgraphs.
  - [mindmap.md](./references/mindmap.md): Mappe concettuali, gerarchia e formattazione markdown.
  - [timeline.md](./references/timeline.md): Cronologie, eventi paralleli e sezioni temporali.
- **Esempi Pratici:**
  - [flowcharts.md](./examples/flowcharts.md): Esempi didattici (analisi logica, processi a fasi).
  - [mindmaps.md](./examples/mindmaps.md): Mappe concettuali di grammatica e metodo scientifico.
  - [timelines.md](./examples/timelines.md): Cronologia linguistica (dal latino ai volgari) e storia dell'AI.
- **Script di Utilità:**
  - [validate_mermaid.py](./scripts/validate_mermaid.py): Tool CLI di verifica sintattica.
