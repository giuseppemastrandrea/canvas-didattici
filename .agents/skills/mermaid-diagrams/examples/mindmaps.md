# Esempi Pratici di Mappe Concettuali (Mindmap) in Mermaid JS

Questa raccolta fornisce modelli di mappe concettuali e mentali didattiche e tassonomiche.

---

## Esempio 1: Mappa Didattica di Grammatica (La Struttura del Periodo)

Questo esempio dimostra come schematizzare le relazioni tra proposizioni nella grammatica italiana:

```mermaid
mindmap
  root(("**La Struttura del Periodo**"))
    Proposizione Principale["**Proposizione Principale**<br/>(Autonoma di senso compiuto)"]
      Informativa["Enunciativa: 'Il sole splende'"]
      Interrogativa["Interrogativa: 'Che ora è?'"]
      Esclamativa["Esclamativa: 'Che bella sorpresa!'"]
      Volitiva["Esortativa / Imperativa"]
    Proposizioni Coordinate["**Proposizioni Coordinate**<br/>(Stesso livello sintattico)"]
      Copulative["Copulative (e, né)"]
      Disgiuntive["Disgiuntive (o, oppure)"]
      Avversative["Avversative (ma, tuttavia)"]
      Conclusive["Conclusive (dunque, perciò)"]
      Correlative["Correlative (sia... sia, non solo... ma anche)"]
    Proposizioni Subordinate["**Proposizioni Subordinate**<br/>(Dipendenti dalla reggente)"]
      Forma
        Esplicita["Esplicita (Modi finiti: indicativo, congiuntivo)"]
        Implicita["Implicita (Modi indefiniti: infinito, gerundio, participio)"]
      Funzione Logica
        Soggettive_Oggettive["Sostantive (Soggettive, Oggettive, Dichiarative)"]
        Relative["Attributive (Relative proprie e improprie)"]
        Complementari["Circostanziali (Causali, Finali, Temporali, Concessive, Ipotesi)"]
```

---

## Esempio 2: Mappa Concettuale Scientifica (Il Metodo Scientifico Sperimentale)

Questo esempio sfrutta diverse forme per distinguere i momenti dell'indagine scientifica:

```mermaid
mindmap
  root((Metodo Scientifico))
    Osservazione["1. Osservazione del Fenomeno"]
      Raccolta Dati
      Identificazione delle Variabili
    Ipotesi{{2. Formulazione dell'Ipotesi}}
      Domanda Guida
      Relazione Causa-Effetto
    Esperimento["3. Verifica Sperimentale"]
      Gruppo di Controllo
      Gruppo Sperimentale
      Misurazione Ripetibile
    Analisi Dati["4. Elaborazione Risultati"]
      Conferma Ipotesi
        ))Legge o Teoria((
      Smentita Ipotesi
        ))Riformulazione Ipotesi((
```

---

## Esempio 3: Architettura Concettuale (I Pilastri del Web Moderno)

```mermaid
mindmap
  root(("Ecosistema Web"))
    HTML["**Struttura (HTML5)**"]
      Tag Semantici
        header, nav, main, article, footer
      Accessibilità (ARIA)
    CSS["**Stile (CSS3)**"]
      Layout
        Flexbox
        CSS Grid
      Design Responsivo
        Media Queries
        Unità Relative (rem, vw)
    JavaScript["**Comportamento (JS)**"]
      DOM Manipulation
      Eventi Utente
      Chiamate Asincrone (Fetch / Async-Await)
```
