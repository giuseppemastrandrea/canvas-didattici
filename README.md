# 🎓 Canvas Didattici

Raccolta di strumenti web interattivi progettati per la didattica, l'uso in classe e la fruizione su Lavagna Interattiva Multimediale (LIM).

🌐 **Sito online (GitHub Pages):** [https://giuseppemastrandrea.github.io/canvas-didattici/](https://giuseppemastrandrea.github.io/canvas-didattici/)

---

## 🏛️ Canvas Disponibili

### 1. [Analisi della Frase Latina](./analisi_logica_latino.html)
Un'applicazione web interattiva per l'apprendimento e l'insegnamento della sintassi e della grammatica latina:
- **Analisi Logica e Morfologica:** evidenziazione interattiva per casi e funzioni logiche (soggetto, predicato, complementi).
- **Concordanze con Frecce Dinamiche SVG:** visualizzazione immediata dei legami di concordanza (nome-aggettivo, soggetto-predicato).
- **Riordino Sintattico:** esercizio drag-and-drop / touch con slot per ricostruire l'ordine sintattico secondo la lingua italiana (SVO).
- **3 Livelli di Difficoltà:** selezione di frasi classiche a complessità crescente.
- **Verifica Morfologica:** finestre modali con opzioni randomizzate per verificare desinenze, casi e declinazioni.

### 2. [Risoluzione Equazioni di 2° Grado](./equazioni_secondo_grado.html)
Un canvas didattico interattivo per la visualizzazione dell'algoritmo di risoluzione delle equazioni di secondo grado:
- **Flowchart Mermaid JS con Tracciamento:** diagramma di flusso strutturato con evidenziazione animata del ramo decisionale attivo corrispondente ai coefficienti inseriti.
- **Supporto Completo di Tutti i Casi:** equazioni incomplete (monomie, pure, spurie) ed equazioni complete con discriminante $\Delta > 0$, $\Delta = 0$ e $\Delta < 0$.
- **Risolutore Interattivo Passo-Passo:** calcolo esplicito del discriminante $\Delta$ (con formula ridotta se $b$ pari), radici esatte (frazioni e radicali) e decimali.
- **Interpretazione Geometrica con la Parabola:** grafico SVG interattivo della parabola $y = ax^2 + bx + c$ con evidenziazione del vertice, asse di simmetria e punti di intersezione con l'asse $x$.
- **8 Preset Didattici:** pulsanti rapidi con esempi classici pensati per la spiegazione alla LIM.
- **Controlli LIM Avanzati:** Pan & Zoom (touch, rotella, trascinamento), schermo intero, esportazione diagramma SVG e visualizzazione/copia del codice sorgente Mermaid.

---

## 🚀 Come aggiungere nuovi Canvas

1. Aggiungere il nuovo file HTML (ad es. `nome_modulo.html`) nella root del repository.
2. Inserire una nuova card con il link in `index.html`.
3. Effettuare il commit e il push sul branch `main`: GitHub Pages aggiornerà automaticamente il sito online.

---

## 💻 Tecnologie Utilizzate

- HTML5 standard e Vanilla JavaScript (nessun build step richiesto)
- [Tailwind CSS](https://tailwindcss.com/) via CDN per lo styling responsive
- [Mermaid JS](https://mermaid.js.org/) per il rendering dinamico e reattivo dei diagrammi di flusso
- [KaTeX](https://katex.org/) per il rendering tipografico delle formule matematiche
- SVG per il rendering dinamico delle frecce di concordanza e dei grafici di funzioni (parabole)
- Compatibile con touch screen, LIM e dispositivi desktop / tablet

---

## 👤 Autore

**Giuseppe Mastrandrea**  
- GitHub: [@giuseppemastrandrea](https://github.com/giuseppemastrandrea)
