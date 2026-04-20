# 🤠 FoodsUp

> **Collect group orders in seconds — no internet required.**

RoundUp is a single-file offline HTML app built for group travel. Each round, everyone taps their name, picks their order, and the app tallies the totals instantly. Built for 18 people across 4 families on a trek through Nepal.

---

## Features

**Ordering**
- Tile-based voter grid — tap any name in any order, checkmark appears when done
- Multi-select — pick multiple items per person (e.g. Tea + a biscuit)
- Custom write-in option — type anything not on the list; it becomes a button for everyone after
- Sub-options — attach choice groups to any option (e.g. "Breakfast set → Coffee or Tea → Jam or Honey")
- Temporary guests — add porters, guides or anyone else per round without touching the permanent list

**Themes**
- 5 built-in themes: Tea time, Lunch, Dinner, Drinks, Snacks
- Fully editable — add, rename, delete themes and their default options
- Round-specific tweaks — adjust options for a single round without changing the defaults
- Save round options back to the theme permanently with one tap

**Results & History**
- Live totals with bar chart and voter names per option
- Full history of every saved round with date and time
- Per-person breakdown — who ordered what
- Share button — sends a formatted summary via WhatsApp, Signal, or any app (falls back to clipboard)

**Multilingual**
- Dutch / English / Nepali (Devanagari) — switch instantly via header toggle
- Language preference is remembered across sessions
- Theme names and UI are fully translated in all three languages

**Reliability**
- Votes are auto-saved to localStorage after every tap — reloading mid-round loses nothing
- Works fully offline — no internet, no server, no installation
- Single `.html` file — copy it anywhere, open it in Chrome

---

## How to Use

### Setup (once)
1. Open `groepsbestelling.html` in **Chrome** on Android or desktop
2. Tap **👥 Namen** to enter the names of all participants
3. Tap **✎** on any theme to set the default options for that theme

### Each round
1. Pick a theme on the home screen
2. Tap **Start order** — optionally adjust options for this round only
3. The voter grid appears — tap a name to open their order screen
4. They pick one or more items (sub-options expand automatically if configured)
5. Tap **Confirm ✓** — they get a checkmark, you're back at the grid
6. When everyone is done, tap **📤 Share** to send the summary, then **Close round & save**

### Sharing the result
The share button sends a plain-text summary like this:

```
🍽️ Dinner
08/04/2026 · 19:45

6× Dal Bhat
5× Momos
3× Thukpa

---
Dries: Dal Bhat
Hendrik: Momos · Vegetarian
Juno: Dal Bhat + Biscuit
...
```

Works with WhatsApp, Signal, email, or any share target on Android.

---

## Tips

| Situation | What to do |
|---|---|
| Porter wants to order too | Tap **+ Guest** on the voter grid |
| Someone wants two things | Tap both options — both stay selected |
| Breakfast set with choices | Edit the theme → **+ Sub-group** on the set option |
| Wrong order after confirming | Tap the name again — choices are still editable |
| App looks broken | Use **Chrome**, not Brave or Firefox |
| Lost all data after reload | This shouldn't happen — votes auto-save. If it does, check Chrome's site settings |

---

## Browser Compatibility

| Browser | Works? | Notes |
|---|---|---|
| Chrome (Android / Desktop) | ✅ | Recommended |
| Samsung Internet | ✅ | Works |
| Firefox (Android) | ⚠️ | May block localStorage on `file://` |
| Brave | ❌ | Blocks localStorage — use Chrome instead |
| Safari (iOS) | ⚠️ | Works but localStorage may be restricted |

---

## Technical Notes

- **Single file** — all HTML, CSS and JavaScript in one `.html` file, no dependencies
- **No internet required** — Google Fonts removed, system fonts used (`Georgia`, `Segoe UI`)
- **Storage** — `localStorage` key `gb6`, falls back to in-memory if blocked
- **Data model** — votes stored as arrays per voter key to support multi-select
- **Options** — plain strings or `{ label, subs: [{ group, values[] }] }` objects for sub-option trees
- **Languages** — i18n via a `LANGS` constant object, switched at runtime via `setLang()`

---

## Context

Built for a group trip to Nepal (April 2026) — 18 people, 4 families, many tea stops and dinner orders to coordinate. Designed to work without WiFi, survive a phone reload mid-trek, and be handed to a Nepali guide who can read the Devanagari UI.

---

*Made with Claude · Nepal 2026*