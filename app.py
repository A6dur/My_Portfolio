import streamlit as st
from pathlib import Path

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Muhammad Abdur Rafay | Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------
# STATIC DATA
# ---------------------------------------------------------
NAME = "Muhammad Abdur Rafay"
TITLE = "Software Engineer | Backend Developer | AI Enthusiast"
LOCATION = "Karachi, Pakistan"
EMAIL = "rafaabdur9@gmail.com"
PHONE = "+92 317 8397023"
GITHUB = "https://github.com/A6dur"
LINKEDIN = "https://www.linkedin.com/in/abdurrafayds/"

SUMMARY = (
    "Software Engineering student at Karachi University with hands-on experience "
    "building scalable backend systems, AI-powered applications, and data-driven "
    "projects. Skilled in FastAPI, REST APIs, JWT Authentication, MongoDB, "
    "SQLAlchemy, and Streamlit. Passionate about solving real-world problems and "
    "turning ideas into impactful software."
)

SKILLS = [
    "Python Programming", "FastAPI & REST APIs", "SQLAlchemy & Databases",
    "MongoDB Atlas", "JWT Authentication", "Streamlit Development",
    "HTML, CSS, JavaScript", "Machine Learning (scikit-learn)",
    "Deep Learning (PyTorch, Keras)", "Data Analysis (Pandas, NumPy)",
    "Data Visualization (Matplotlib, Seaborn)", "Git & GitHub",
    "Problem Solving", "Teamwork & Collaboration", "Time Management",
    "Effective Communication", "Leadership & Critical Thinking",
]

TOOLS = [
    "Python", "FastAPI", "Streamlit", "MongoDB", "SQLAlchemy",
    "Git", "Docker", "Postman", "VS Code", "FFmpeg",
]

LANGUAGES = [
    ("English", "Fluent"),
    ("Urdu", "Fluent"),
    ("Hindi", "Fluent"),
]

EDUCATION = [
    {
        "degree": "Bachelor of Software Engineering",
        "school": "University of Karachi – UBIT",
        "years": "2023 – 2027",
        "detail": "GPA: 3.0 / 4.0",
    },
    {
        "degree": "Matriculation & Intermediate",
        "school": "AKUEB Board – Nasra School / College",
        "years": "2019 – 2022",
        "detail": "Achieved A+ Grades",
    },
]

PROJECTS = [
    {
        "name": "SnapSphere – Social Media Backend",
        "years": "2024 – Present",
        "stack": "FastAPI, SQLAlchemy, JWT, SQLite, Python",
        "desc": (
            "A Facebook/Instagram-inspired social media backend supporting photo "
            "and video posts with captions, a viewable feed, and the ability to "
            "delete one's own posts. JWT-based authentication secures every "
            "endpoint."
        ),
        "github": "https://github.com/A6dur/SnapSphere",
        "demo": None,
        "emoji": "📱",
    },
    {
        "name": "ProjectVidSnapAI – AI Reel Generator",
        "years": "2024 – Present",
        "stack": "Python, ElevenLabs API, FFmpeg, HTML, CSS",
        "desc": (
            "An AI SaaS platform that converts user-provided images and captions "
            "into narrated reels. Captions are converted to voice using the "
            "ElevenLabs API and reels are rendered with FFmpeg, wrapped in a "
            "polished custom UI."
        ),
        "github": "https://github.com/A6dur/ProjectVidSnapAI",
        "demo": None,
        "emoji": "🎬",
    },
    {
        "name": "Notepad – CRUD Web App",
        "years": "2024",
        "stack": "FastAPI, MongoDB Atlas, Jinja2, HTML, CSS",
        "desc": (
            "A full CRUD application for creating, viewing, editing, and "
            "deleting notes, built with FastAPI and MongoDB Atlas with a simple "
            "functional HTML frontend."
        ),
        "github": "https://github.com/A6dur/notepad",
        "demo": None,
        "emoji": "📝",
    },
    {
        "name": "News App",
        "years": "2024",
        "stack": "Python, Streamlit, NewsAPI",
        "desc": (
            "A real-time news application with category-based filtering and an "
            "interactive Streamlit UI, pulling live articles via the NewsAPI."
        ),
        "github": "https://github.com/A6dur/NewsApp",
        "demo": "https://a6dur-newsapp.streamlit.app/",
        "emoji": "📰",
    },
    {
        "name": "PDF Toolkit",
        "years": "2024",
        "stack": "Python, Streamlit, PyPDF2",
        "desc": (
            "A toolkit to merge PDFs, extract text and images, and export "
            "results as a ZIP file. More features are planned."
        ),
        "github": "https://github.com/A6dur/PDF-Toolkit",
        "demo": "https://a6dur-pdf-toolkit.streamlit.app/",
        "emoji": "📄",
    },
    {
        "name": "Pocket Calculator",
        "years": "2024",
        "stack": "Python, Streamlit",
        "desc": (
            "An interactive calculator with a clean, modern UI covering all "
            "essential arithmetic operations."
        ),
        "github": "https://github.com/A6dur/Pocket-Calculator",
        "demo": "https://akbmfflbc5gn26m9y7h7nk.streamlit.app/",
        "emoji": "🧮",
    },
    {
        "name": "Millionaire Game",
        "years": "2024",
        "stack": "Python, Streamlit",
        "desc": (
            "A quiz game with a per-question timer, live countdown indicator, "
            "multiple-choice questions, and a reward system based on correct "
            "answers."
        ),
        "github": "https://github.com/A6dur/Millionaire-Game-",
        "demo": "https://mdaw82kcuf7xf2xbtsmzk9.streamlit.app/",
        "emoji": "🎯",
    },
]

ACHIEVEMENTS = [
    ("⭐", "Built and deployed multiple Streamlit applications."),
    ("🚀", "Hands-on experience building AI-powered applications."),
    ("🎯", "Strong problem solver with a passion for clean code."),
]

# ---------------------------------------------------------
# STYLES
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }

    :root {
        --navy: #10233f;
        --navy-light: #16304f;
        --accent: #2b6cb0;
        --accent-light: #7fa8d9;
        --bg: #f5f7fa;
    }

    .stApp, .main, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: var(--bg) !important;
    }

    #MainMenu, header, footer {visibility: hidden;}

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1100px;
    }

    /* HERO */
    .hero-card {
        background: linear-gradient(135deg, #10233f 0%, #1c3a63 100%);
        border-radius: 18px;
        padding: 2.6rem 2.8rem;
        color: white;
        margin-bottom: 1.8rem;
    }
    .hero-name {
        font-size: 2.6rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
        line-height: 1.15;
    }
    .hero-title {
        font-size: 1.15rem;
        color: #cfe0f5;
        font-weight: 500;
        margin-bottom: 0.9rem;
    }
    .hero-summary {
        font-size: 0.98rem;
        color: #e3ecf7;
        line-height: 1.6;
        max-width: 720px;
    }
    .badge-row { margin-top: 1.1rem; }
    .badge {
        display: inline-block;
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.25);
        border-radius: 20px;
        padding: 4px 14px;
        font-size: 0.78rem;
        margin-right: 8px;
        margin-bottom: 8px;
        color: #ffffff;
    }

    /* SECTION HEADERS */
    .section-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: var(--navy);
        margin: 1.6rem 0 1rem 0;
        padding-bottom: 6px;
        border-bottom: 3px solid var(--navy);
        display: inline-block;
    }

    /* PROJECT CARD */
    .proj-card {
        background: white;
        border-radius: 14px;
        padding: 1.3rem 1.5rem;
        box-shadow: 0 2px 10px rgba(16,35,63,0.07);
        border: 1px solid #e7ebf1;
        margin-bottom: 1.1rem;
        height: 100%;
    }
    .proj-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
    }
    .proj-name {
        font-size: 1.05rem;
        font-weight: 700;
        color: var(--navy);
    }
    .proj-years {
        font-size: 0.75rem;
        color: #888;
        white-space: nowrap;
        margin-left: 8px;
    }
    .proj-stack {
        font-size: 0.82rem;
        color: var(--accent);
        font-weight: 600;
        margin: 4px 0 8px 0;
    }
    .proj-desc {
        font-size: 0.87rem;
        color: #444;
        line-height: 1.5;
        min-height: 78px;
    }

    /* SIDEBAR-LIKE INFO CARDS */
    .info-card {
        background: white;
        border-radius: 14px;
        padding: 1.3rem 1.4rem;
        box-shadow: 0 2px 10px rgba(16,35,63,0.07);
        border: 1px solid #e7ebf1;
        margin-bottom: 1.1rem;
    }
    .skill-pill {
        display: inline-block;
        background: #eef3fb;
        color: var(--navy);
        border-radius: 8px;
        padding: 5px 11px;
        font-size: 0.78rem;
        margin: 0 6px 6px 0;
        font-weight: 500;
    }
    .tool-pill {
        display: inline-block;
        background: var(--navy);
        color: white;
        border-radius: 8px;
        padding: 5px 12px;
        font-size: 0.78rem;
        margin: 0 6px 6px 0;
        font-weight: 600;
    }

    .edu-item { margin-bottom: 1rem; }
    .edu-degree { font-weight: 700; color: var(--navy); font-size: 0.95rem; }
    .edu-school { color: var(--accent); font-size: 0.85rem; font-weight: 600; }
    .edu-years { color: #888; font-size: 0.78rem; }
    .edu-detail { color: #555; font-size: 0.83rem; margin-top: 2px; }

    .ach-card {
        background: white;
        border-radius: 14px;
        padding: 1.1rem 1.2rem;
        box-shadow: 0 2px 10px rgba(16,35,63,0.07);
        border: 1px solid #e7ebf1;
        text-align: center;
        height: 100%;
    }
    .ach-emoji { font-size: 1.6rem; margin-bottom: 6px; }
    .ach-text { font-size: 0.85rem; color: #444; line-height: 1.4; }

    a.link-btn {
        display: inline-block;
        text-decoration: none;
        font-size: 0.82rem;
        font-weight: 600;
        padding: 5px 12px;
        border-radius: 7px;
        margin-top: 8px;
        margin-right: 8px;
    }
    a.gh-btn {
        background: var(--navy);
        color: white !important;
    }
    a.demo-btn {
        background: #eef3fb;
        color: var(--navy) !important;
        border: 1px solid #c9d9ec;
    }

    .contact-line {
        font-size: 0.88rem;
        color: #333;
        margin-bottom: 8px;
    }
    .contact-line b { color: var(--navy); }
    .contact-line a { color: var(--accent); text-decoration: none; font-weight: 600; }

    footer-note {
        text-align: center;
        color: #999;
        font-size: 0.8rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------
hero_col1, hero_col2 = st.columns([1, 3], gap="large")

with hero_col1:
    img_path = Path(__file__).parent / "profile.png"
    if img_path.exists():
        st.image(str(img_path), use_container_width=True)
    st.markdown(
        f"""
        <div class="info-card" style="margin-top:1rem;">
            <div class="contact-line">📍 <b>Location:</b> {LOCATION}</div>
            <div class="contact-line">📞 <b>Phone:</b> {PHONE}</div>
            <div class="contact-line">✉️ <b>Email:</b> <a href="mailto:{EMAIL}">{EMAIL}</a></div>
            <div class="contact-line">🔗 <b>GitHub:</b> <a href="{GITHUB}" target="_blank">github.com/A6dur</a></div>
            <div class="contact-line">🔗 <b>LinkedIn:</b> <a href="{LINKEDIN}" target="_blank">in/abdurrafayds</a></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with hero_col2:
    st.markdown(
        f"""
        <div class="hero-card">
            <div class="hero-name">{NAME}</div>
            <div class="hero-title">{TITLE}</div>
            <div class="hero-summary">{SUMMARY}</div>
            <div class="badge-row">
                <span class="badge">⚡ FastAPI</span>
                <span class="badge">🐍 Python</span>
                <span class="badge">🤖 AI / ML</span>
                <span class="badge">🔴 Streamlit</span>
                <span class="badge">🟢 MongoDB</span>
                <span class="badge">📚 SQLAlchemy</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    btn_col1, btn_col2, btn_col3 = st.columns(3)
    with btn_col1:
        st.link_button("💻 View GitHub", GITHUB, use_container_width=True)
    with btn_col2:
        st.link_button("🔗 Connect on LinkedIn", LINKEDIN, use_container_width=True)
    with btn_col3:
        st.link_button("✉️ Send an Email", f"mailto:{EMAIL}", use_container_width=True)

# ---------------------------------------------------------
# PROJECTS
# ---------------------------------------------------------
st.markdown('<div class="section-title">🚀 Projects</div>', unsafe_allow_html=True)

proj_cols = st.columns(2, gap="medium")
for i, proj in enumerate(PROJECTS):
    with proj_cols[i % 2]:
        links_html = f'<a class="link-btn gh-btn" href="{proj["github"]}" target="_blank">GitHub Repo</a>'
        if proj["demo"]:
            links_html += f'<a class="link-btn demo-btn" href="{proj["demo"]}" target="_blank">Live Demo</a>'
        st.markdown(
            f"""
            <div class="proj-card">
                <div class="proj-header">
                    <div class="proj-name">{proj['emoji']} {proj['name']}</div>
                    <div class="proj-years">{proj['years']}</div>
                </div>
                <div class="proj-stack">{proj['stack']}</div>
                <div class="proj-desc">{proj['desc']}</div>
                {links_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

# ---------------------------------------------------------
# SKILLS & TOOLS
# ---------------------------------------------------------
st.markdown('<div class="section-title">🛠 Skills & Tools</div>', unsafe_allow_html=True)

skill_col, tool_col = st.columns(2, gap="medium")

with skill_col:
    pills = "".join(f'<span class="skill-pill">{s}</span>' for s in SKILLS)
    st.markdown(
        f'<div class="info-card"><b style="color:#10233f;">Skills</b><br><br>{pills}</div>',
        unsafe_allow_html=True,
    )

with tool_col:
    pills = "".join(f'<span class="tool-pill">{t}</span>' for t in TOOLS)
    lang_html = "".join(
        f'<div class="contact-line">🌐 {lang} — <i>{level}</i></div>'
        for lang, level in LANGUAGES
    )
    st.markdown(
        f"""
        <div class="info-card">
            <b style="color:#10233f;">Tools & Technologies</b><br><br>{pills}
            <br><br><b style="color:#10233f;">Languages</b><br><br>{lang_html}
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------
# EDUCATION
# ---------------------------------------------------------
st.markdown('<div class="section-title">🎓 Education</div>', unsafe_allow_html=True)

edu_html = ""
for e in EDUCATION:
    edu_html += (
        f'<div class="edu-item">'
        f'<div class="edu-degree">{e["degree"]}</div>'
        f'<div class="edu-school">{e["school"]}</div>'
        f'<div class="edu-years">{e["years"]} &nbsp;•&nbsp; {e["detail"]}</div>'
        f'</div>'
    )
st.markdown(f'<div class="info-card">{edu_html}</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# ACHIEVEMENTS
# ---------------------------------------------------------
st.markdown('<div class="section-title">🏆 Achievements</div>', unsafe_allow_html=True)

ach_cols = st.columns(3, gap="medium")
for i, (emoji, text) in enumerate(ACHIEVEMENTS):
    with ach_cols[i]:
        st.markdown(
            f"""
            <div class="ach-card">
                <div class="ach-emoji">{emoji}</div>
                <div class="ach-text">{text}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown(
    f"""
    <p style="text-align:center; color:#999; font-size:0.85rem;">
        Built with Streamlit · {NAME} © 2026
    </p>
    """,
    unsafe_allow_html=True,
)