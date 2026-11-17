# daily-german-news

A daily German reading sheet made from Swiss news. Your AI assistant picks five current stories from [SRF](https://www.srf.ch/news), rewrites them at your reading level and puts a full word list under each one.

Made for the AK90 A2 class. It works with any AI assistant that can open web pages: ChatGPT, Gemini, Claude, Le Chat, Copilot, or a coding agent.

## What a sheet looks like

> **2 · 🛣️ Die Autobahnen sind in gutem Zustand**
>
> Das Bundesamt für Strassen (Astra) hat die Schweizer Nationalstrassen geprüft. Das Resultat ist die Note 1.81. Die Skala geht von 1 (gut) bis 5 (alarmierend). …
>
> * der Zustand, Zustände – condition, state
> * prüfen (hat geprüft) – to check, to inspect
> * die Note, -n – grade, mark (≠ also "musical note")
> * …

A full sheet: [examples/2026-11-11.md](examples/2026-11-11.md).

It is reading, not a lesson: no grammar boxes, no exercises. Every word you might not know is in the list, so you never need a dictionary. Over the weeks the texts get a little harder (see [The ladder](#the-ladder)).

## Setup

### A · In a chat app (ChatGPT, Gemini, Claude, Le Chat, …)

1. Download three files: [`INSTRUCTIONS.md`](INSTRUCTIONS.md), [`learner.md`](learner.md), [`grammar/ak90-a2.md`](grammar/ak90-a2.md).
2. Open `learner.md` and set your glossary language (see [Settings](#settings)).
3. Create a space that keeps files and instructions together: a **Project** in ChatGPT or Claude, a **Gem** in Gemini. Upload the three files.
4. Paste this as the project's instructions:

   ```
   Make my daily German news sheet. Follow INSTRUCTIONS.md exactly. My settings are in learner.md.
   ```

5. Make sure web search is on, then type **news sheet**.

A chat app can't edit your files. When your step changes, the assistant tells you: change the `Current step` line in `learner.md` and upload it again.

### B · With a coding agent (Claude Code, Codex, Gemini CLI, Cursor, OpenCode, …)

1. Click **Use this template** to create your own copy of the repository (private is fine), then clone it.
2. Edit `learner.md`.
3. Open the folder in your agent and type **news sheet**.

The agent finds its instructions through `AGENTS.md`; `CLAUDE.md` and `GEMINI.md` point to the same file. It saves each sheet in `sheets/`, keeps a log in `learner.md` and moves you up the ladder by itself.

## Using it

| Type | What happens |
|---|---|
| `news sheet` | today's sheet |
| `harder` | one step up |
| `too hard` | one step down |
| a question about a sentence | an answer in chat; the sheet stays as it is |

## Settings

`learner.md` has four lines you may change:

| Line | Meaning |
|---|---|
| `Glossary language` | the language of the word lists. Any language works. |
| `Home country` | a story connected to this country gets one extra paragraph. `none` to skip. |
| `Grammar file` | what your class has covered. The texts stay inside it. |
| `Current step` | your place on the ladder, 0–5. Start at 0. |

## The ladder

Six steps. Step 0 uses only what you have seen in class. Each step after it adds one structure that news German is full of: relative clauses (1), Präteritum (2), past passive (3), participles as adjectives (4), Konjunktiv I (5). Nothing is explained; the word lists carry you through. A step lasts 8–10 sheets. Details are in [`INSTRUCTIONS.md`](INSTRUCTIONS.md#the-ladder).

If a sheet feels too hard, look at its length first. Long stories and long lists of names and numbers make a text harder than a new structure does, so each story is kept to about 80 words. If your assistant writes more, remind it of that rule.

## Another course or level

The ladder is built for A2. For another course, copy `grammar/ak90-a2.md`, list what your class has covered, and point `Grammar file` in `learner.md` to your copy.

## Daily delivery (optional)

If your assistant can run a prompt on a schedule, schedule `news sheet` for the morning. To send a sheet by email, `tools/md-to-html.py` turns it into an HTML email body (Python 3, no installs needed):

```bash
python3 tools/md-to-html.py sheets/2026-11-17.md > sheet.html
```

## Content and license

The instructions and code are under the [MIT license](LICENSE). The stories are simplified rewrites of SRF articles for personal study; each one links to its source, and the articles belong to SRF.
