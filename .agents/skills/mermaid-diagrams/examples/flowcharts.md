# Esempi Pratici di Flowchart in Mermaid JS

Questa raccolta fornisce modelli pronti all'uso per diverse tipologie di diagrammi di flusso.

---

## Esempio 1: Diagramma Didattico Decisionale (Analisi Logica - Il Soggetto)

Questo diagramma illustra un algoritmo guidato per individuare il soggetto in una frase:

```mermaid
flowchart TD
    classDef startEnd fill:#d4edda,stroke:#28a745,stroke-width:2px,color:#155724;
    classDef decision fill:#fff3cd,stroke:#ffc107,stroke-width:2px,color:#856404;
    classDef action fill:#d1ecf1,stroke:#17a2b8,stroke-width:2px,color:#0c5460;
    classDef result fill:#f8d7da,stroke:#dc3545,stroke-width:2px,color:#721c24;

    Start([Inizio Analisi]) :::startEnd
    FindVerb["1. Trova il Predicato (Verbo)"] :::action
    CheckVerb{Il verbo è alla<br/>forma personale?} :::decision
    AskWho["2. Chiediti:<br/>'Chi compie o subisce l'azione?'"] :::action
    IsExplicit{Il soggetto è<br/>espresso nella frase?} :::decision
    SoggEspresso["Soggetto Espresso<br/>(es. 'Marco corre')"] :::result
    SoggSottinteso["Soggetto Sottinteso<br/>(es. '(Io) ho mangiato')"] :::result
    ModoImpersonale["Verbo Impersonale<br/>(Nessun soggetto, es. 'Piove')"] :::result

    Start --> FindVerb
    FindVerb --> CheckVerb
    CheckVerb -->|Sì| AskWho
    CheckVerb -->|No| ModoImpersonale
    AskWho --> IsExplicit
    IsExplicit -->|Sì| SoggEspresso
    IsExplicit -->|No| SoggSottinteso
```

---

## Esempio 2: Architettura a Fasi con Subgraph (Ciclo di Apprendimento)

Rappresentazione di un ciclo didattico basato sulla metodologia flipped classroom / inquiry:

```mermaid
flowchart LR
    classDef phase fill:#f0f4f8,stroke:#3b82f6,stroke-width:2px;

    subgraph Casa ["Fase 1: Studio Autonomo (A Casa)"]
        A["Visione Video Didattico"] --> B["Lettura Materiale"]
        B --> C["Quiz di Autovalutazione"]
    end

    subgraph Aula ["Fase 2: Applicazione Pratica (In Aula)"]
        D["Discussione Dubbi"] --> E["Lavoro di Gruppo / Laboratorio"]
        E --> F["Presentazione Elaborati"]
    end

    subgraph Verifica ["Fase 3: Valutazione"]
        G["Valutazione Formativa"] --> H{"Competenza Raggiunta?"}
        H -->|Sì| I([Prossimo Modulo])
        H -->|No| J["Attività di Recupero"]
    end

    C --> D
    F --> G
    J --> E
```

---

## Esempio 3: Workflow Sequenziale Orizzontale con Icone e Database

```mermaid
flowchart LR
    User([Studente]) --> Form[/"Compilazione Test Didattico"/]
    Form --> API["Server / API"]
    API --> DB[("Database Risultati")]
    API --> Engine[["Motore di Correzione"]]
    Engine --> Grade{"Esito Superato?"}
    Grade -->|Punteggio >= 60%| Cert[/"Generazione Certificato"/]
    Grade -->|Punteggio < 60%| Feed["Suggerimenti di Ripasso"]
    Cert --> User
    Feed --> User
```
