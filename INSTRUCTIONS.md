# Daily German news sheet

You make a **sheet**: five current Swiss news stories in German, each rewritten at the learner's reading **step** and followed by its own **word list**. A sheet is reading material: it holds stories, word lists and sources. Grammar explanations go in chat, when the learner asks.

The second aim is silent: the **ladder** below raises the reading level step by step, and the sheet never mentions it.

## Steps

1. **Read `learner.md`** (glossary language, home country, current step, grammar file) and the **grammar file** it names. That file is the **base**: the structures the learner already knows from class.
2. **Open https://www.srf.ch/news** and collect today's headlines. Use today's date; if you are unsure of it, take it from the news page.
3. **Pick 5 stories**, one per role: world politics · economy, interest rates or energy · Swiss daily life · Swiss news · a light or seasonal closer.
4. **Open each story's own page and take its text.** Every name, number, place and reason in a story comes from that page. A short article makes a short story.
5. **Rewrite** each story at the current step and build its word list (rules below).
6. **Deliver.**
   - *You can edit files:* save `sheets/YYYY-MM-DD.md` (a second sheet on the same day: `YYYY-MM-DD-2.md`), add a row to the log in `learner.md`, then show the sheet. In a git repository, commit both files; in a temporary cloud environment, push too, or the sheet is lost.
   - *Chat only:* reply with the sheet itself and nothing before it.

Done when: five stories, each with its word list; every word the learner may not know is in a list; five links under `## Quellen`.

**No article text?** If you cannot open web pages, or your tool gives back only a summary of a page instead of its text, say so and ask the learner to paste the articles. Stories come only from article text.

## Moving on the ladder

- **`harder`** → one step up. **`too hard`** → one step down; step 0 is the floor.
- With a log: when the latest unbroken run of log rows at the current step reaches **8–10 sheets**, move up one step.
- Every change goes into the `Current step:` line of `learner.md`. That line is the ladder's only memory. *Chat only:* tell the learner, in one line after the sheet, to change it.

## The ladder

Each story stands on the **base**. On top, the current step brings in **one new structure**, a little at a time. The new structure is never explained: its unknown words are in the list, so the sentence resolves from context.

| Step | New structure | Sentence length |
|---|---|---|
| 0 | None: main clauses and the base's connectors (`weil`, `dass`, `wenn`, `aber`, `deshalb`). Relative clauses are split into two sentences. | ~12 words |
| 1 | **Relativsatz**, Nominativ / Akkusativ only (`der/die/das`), 2–4 per sheet | ~18 |
| 2 | Relativsatz in Dativ and after a preposition (`dem`, `denen`, `mit dem`) · **Präteritum** of frequent verbs (`gab`, `kam`, `ging`, `sagte`, `wurde`) | ~20 |
| 3 | **Passiv in the past** (`wurde beschlossen`, `ist freigegeben worden`) · **Genitive prepositions** (`wegen`, `trotz`, `während`, `aufgrund`) | ~22 |
| 4 | **Participles as adjectives** (`die steigenden Preise`, `das geplante Gesetz`) · long noun phrases · `sowohl … als auch` | ~25 |
| 5 | **Konjunktiv I**, the reporting mood of news (`Er sagte, die Lage sei ernst`) · extended adjective phrases (`die vom Bund freigegebenen Reserven`) · Nominalstil | free |

Steps are cumulative: step 3 keeps what steps 1 and 2 brought in.

**The base is free.** Anything the grammar file lists as seen may appear at every step and costs nothing. The one-new-structure limit is only for structures outside the base.

**Rewriting.** The base and the current step's structures stay as they are; everything else is simplified. The usual move is to split the sentence:

```
Source:   Der Käse, der zurückgerufen wurde, ist in vielen Läden.
Step 0:   Der Käse wird zurückgerufen. Er ist in vielen Läden.
```

The order follows news German: a relative clause is in almost every paragraph, and Konjunktiv I is in every reported sentence. These structures, more than vocabulary, are what make news hard to read.

## Stories

- **Rewrite, don't summarize:** keep the story, retell it at the step.
- **5–7 lines, ~80 words at most.** Length makes a text harder without teaching anything.
- **One main point.** When the source lists six states, nine names or five numbers, keep at most two and group the rest (`in zwei weiteren Bundesstaaten`, `mehrere Kantone`).
- **~15–20 new words per story in the text.** More means the story is too long or too technical: cut it, or pick another story.
- **Home country** (if `learner.md` names one): a story linked to it gets one extra short paragraph, with its own source.
- **Swiss spelling: `ss`, never `ß`.** Convert every `ß` from German sources.
- Plain text in the stories: no bold, no italics.
- **Heavy topics** (illness, war, death, accidents): a flat, informative tone.

## Word lists

The word list carries the difficulty. It sits right under its story: one bullet per entry, German and gloss separated by ` – ` (an en dash with spaces). Glosses are in the learner's **glossary language**. A word that appears in several stories is listed again under each one.

**Default: add.** There is no upper limit. A known word in the list costs half a second; an unknown word missing from it breaks the sentence. When in doubt, add it.

The 15–20 budget above limits the *text*. The list stays complete: every word the learner may not know is in it. To make a story easier, shorten the text.

| What | How |
|---|---|
| **Every noun**, even familiar ones | article + plural: `der Engpass, Engpässe` |
| Every **verb** beyond core A1 | with its Perfekt: `prüfen (hat geprüft)` · separable verbs with a middle dot: `frei·geben (hat freigegeben)` · a fixed preposition with its case: `warnen vor + Dat. (hat gewarnt)` (class teaches them as one unit) |
| Non-basic **adjectives and adverbs** | `ungefähr – approximately` |
| **Connectors** (`deshalb`, `ausserdem`, `zuerst`, `dagegen`) | a short gloss |
| **Compounds**, split into parts | `der Engpass, Engpässe – bottleneck (eng "narrow" + Pass "pass")` |
| **Proper names** | what it is, and the name in the glossary language if it differs: `Jambol – Yambol (a town in Bulgaria)` · `Genf – Geneva` |
| **Set phrases** | `noch nie – never (so far)` |

A word used in an unusual sense here: `langsam – slow; here: gradually`.
A word with a second common meaning: `der Ausgang – outcome (≠ also "exit")`.

## Format

```
# Nachrichten — 11. November 2026

## 1 · 🌫️ {headline in German, written at the step}

{German text}
[SRF]({article url})

* der Unfall, Unfälle – accident
* …

---

## 2 · …

---

## Quellen
* [{article title}]({article url})
```

The date in the title is in German. A complete sheet: `examples/2026-11-11.md`.
