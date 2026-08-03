# Muhammad Abdur Rafay — Portfolio (Streamlit App)

A single-page portfolio built with Streamlit, showcasing your profile, skills,
tools, education, and all 7 projects with live GitHub/demo links.

## Files
- `app.py` — the full app (single file, no extra setup needed)
- `requirements.txt` — dependencies
- `profile.png` — your profile photo, loaded locally by the app
- `.streamlit/config.toml` — locks the app to light theme so headings stay
  readable even if a visitor's browser/system is set to dark mode

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud
1. Create a new GitHub repo (e.g. `portfolio`) and push these 3 files to it
   (keep `profile.png` in the same folder as `app.py`).
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **"New app"**, select your repo/branch, and set the main file path
   to `app.py`.
4. Click **Deploy** — you'll get a live URL like
   `https://your-app-name.streamlit.app/`.

## Customizing
All your content (bio, skills, projects, links) lives as plain Python data
near the top of `app.py` — edit those lists/dicts directly to update text,
add new projects, or change links. No HTML/CSS knowledge needed for basic
edits.
