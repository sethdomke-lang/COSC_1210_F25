# Pygame → Web (pygbag) Starter

This folder is ready to build & run in a browser using **pygbag**.

## Prereqs
- Python 3.10–3.12
- Install pygbag:  
  ```bash
  python -m pip install pygbag
  ```

## Build
From this folder:
```bash
python -m pygbag --build .
```

## Run locally
```bash
python -m pygbag --serve build/web
```
Then open the printed URL (usually http://127.0.0.1:8000).

## Files
- `main.py` — async game loop for the browser (awaits once per frame)
- `config.py` — settings and colors
- `adventure_functions.py` — drawing & collision helpers
- `assets/goose.png` — 48×48 placeholder sprite (replace with your own)

## Notes
- Keep assets in `assets/` and refer with relative paths (already set in `config.py`).
- In the browser, audio may require a user gesture before playback.
- If controls feel "sticky", check that the `await asyncio.sleep(0)` remains once per frame.
