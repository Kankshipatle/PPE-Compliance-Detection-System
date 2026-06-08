# import streamlit as st
# import cv2
# import numpy as np
# from ultralytics import YOLO
# from PIL import Image

# # Page config
# st.set_page_config(
#     page_title="PPE Compliance Detection",
#     page_icon="🦺",
#     layout="wide"
# )

# # Dark theme styling
# st.markdown("""
#     <style>
#     .stApp { background-color: #0e1117; }
#     .title { text-align: center; color: #00d4ff; font-size: 2.5em; font-weight: bold; }
#     .subtitle { text-align: center; color: #888; margin-bottom: 30px; }
#     .allowed { background-color: #1a4a1a; border: 2px solid #00ff00;
#                border-radius: 10px; padding: 20px; text-align: center; }
#     .denied { background-color: #4a1a1a; border: 2px solid #ff0000;
#               border-radius: 10px; padding: 20px; text-align: center; }
#     .status-text { font-size: 2em; font-weight: bold; }
#     .ppe-item { padding: 8px; border-radius: 5px; margin: 5px 0; font-size: 1.1em; }
#     </style>
# """, unsafe_allow_html=True)

# # Load model
# @st.cache_resource
# def load_model():
#     return YOLO("ppe_best_v2.pt")

# model = load_model()
# classes = {0: "gloves", 1: "mask", 2: "hairnet"}
# required = {"gloves", "mask", "hairnet"}

# # Header
# st.markdown('<div class="title">🦺 PPE Compliance Detection System</div>', unsafe_allow_html=True)
# st.markdown('<div class="subtitle">AI-Based Smart Access Control for Food Processing Environments</div>', unsafe_allow_html=True)
# st.divider()

# # Mode selection
# mode = st.radio("Select Mode", ["📷 Webcam", "🖼️ Upload Image"], horizontal=True)

# def run_detection(image_np):
#     results = model(image_np, conf=0.2)
#     detected = set()
#     for r in results:
#         for box in r.boxes:
#             cls_id = int(box.cls[0])
#             detected.add(classes[cls_id])
#     annotated = results[0].plot()
#     annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
#     return annotated_rgb, detected

# def show_result(detected):
#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown("### PPE Status")
#         for item in ["gloves", "mask", "hairnet"]:
#             if item in detected:
#                 st.markdown(f'<div class="ppe-item" style="background:#1a3a1a; color:#00ff00;">✅ {item.upper()}</div>', unsafe_allow_html=True)
#             else:
#                 st.markdown(f'<div class="ppe-item" style="background:#3a1a1a; color:#ff4444;">❌ {item.upper()}</div>', unsafe_allow_html=True)
#     with col2:
#         st.markdown("### Access Decision")
#         if len(detected) >= 2:
#             st.markdown('<div class="allowed"><span class="status-text" style="color:#00ff00;">✅ ACCESS ALLOWED</span></div>', unsafe_allow_html=True)
#         else:
#             missing = required - detected
#             st.markdown(f'<div class="denied"><span class="status-text" style="color:#ff0000;">❌ ACCESS DENIED</span><br><span style="color:#ff8888;">Missing: {", ".join(missing)}</span></div>', unsafe_allow_html=True)

# # Webcam mode
# if mode == "📷 Webcam":
#     img_file = st.camera_input("Show your PPE to the camera")
#     if img_file:
#         image = Image.open(img_file)
#         image_np = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
#         annotated, detected = run_detection(image_np)
#         st.image(annotated, caption="Detection Result", use_column_width=True)
#         show_result(detected)

# # Image upload mode
# elif mode == "🖼️ Upload Image":
#     uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
#     if uploaded:
#         image = Image.open(uploaded)
#         image_np = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
#         annotated, detected = run_detection(image_np)
#         st.image(annotated, caption="Detection Result", use_column_width=True)
#         show_result(detected)







import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image
from datetime import datetime

st.set_page_config(
    page_title="PPE Compliance System",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Syne:wght@600;800&display=swap');

:root {
    --bg: #0f1117;
    --surface: #161b25;
    --surface2: #1d2433;
    --border: #252d3d;
    --accent: #4f9cf9;
    --green: #22c55e;
    --red: #ef4444;
    --text: #e2e8f0;
    --muted: #64748b;
}

* { box-sizing: border-box; }
.stApp { background: var(--bg) !important; }

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem !important; max-width: 1400px !important; }

/* Header */
.sys-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 18px 28px;
    margin-bottom: 24px;
}
.sys-header-left h1 {
    font-family: 'Syne', sans-serif;
    font-size: 1.6em;
    font-weight: 800;
    color: var(--text);
    margin: 0;
    letter-spacing: 1px;
}
.sys-header-left p {
    font-family: 'DM Mono', monospace;
    font-size: 0.72em;
    color: var(--muted);
    margin: 4px 0 0 0;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}
.sys-badge {
    background: #1a2a1a;
    border: 1px solid #22c55e44;
    color: var(--green);
    font-family: 'DM Mono', monospace;
    font-size: 0.72em;
    padding: 6px 14px;
    border-radius: 2px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

/* Panel */
.panel {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 20px;
    margin-bottom: 16px;
}
.panel-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.68em;
    color: var(--muted);
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-bottom: 14px;
    padding-bottom: 10px;
    border-bottom: 1px solid var(--border);
}

/* Access Decision */
.decision-allowed {
    background: #0d1f12;
    border: 1px solid #22c55e55;
    border-left: 4px solid var(--green);
    border-radius: 4px;
    padding: 20px 24px;
    margin-bottom: 16px;
}
.decision-denied {
    background: #1f0d0d;
    border: 1px solid #ef444455;
    border-left: 4px solid var(--red);
    border-radius: 4px;
    padding: 20px 24px;
    margin-bottom: 16px;
}
.decision-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.8em;
    font-weight: 800;
    letter-spacing: 3px;
    text-transform: uppercase;
}
.decision-sub {
    font-family: 'DM Mono', monospace;
    font-size: 0.72em;
    letter-spacing: 1.5px;
    margin-top: 6px;
    opacity: 0.7;
}

/* PPE Items */
.ppe-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 14px;
    margin: 6px 0;
    border-radius: 3px;
    font-family: 'DM Mono', monospace;
    font-size: 0.82em;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}
.ppe-detected {
    background: #0d1f12;
    border: 1px solid #22c55e33;
    color: var(--green);
}
.ppe-missing {
    background: #1f0d0d;
    border: 1px solid #ef444433;
    color: var(--red);
}
.conf-pill {
    background: #ffffff11;
    padding: 2px 10px;
    border-radius: 20px;
    font-size: 0.85em;
}
.conf-bar {
    height: 3px;
    background: #ffffff0a;
    border-radius: 2px;
    margin-top: 6px;
    overflow: hidden;
}
.conf-fill-green { background: var(--green); height: 3px; border-radius: 2px; }
.conf-fill-red { background: var(--red); height: 3px; border-radius: 2px; }

/* Log */
.log-box {
    background: #0a0d12;
    border: 1px solid var(--border);
    border-radius: 3px;
    padding: 12px 16px;
    font-family: 'DM Mono', monospace;
    font-size: 0.72em;
    max-height: 160px;
    overflow-y: auto;
    color: var(--muted);
}
.log-allow { color: var(--green); }
.log-deny { color: var(--red); }
.log-time { color: #334155; margin-right: 8px; }

/* Streamlit radio fix */
div[data-testid="stRadio"] > label {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.8em !important;
    color: var(--muted) !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
}
div[data-testid="stRadio"] div[role="radiogroup"] label {
    color: var(--text) !important;
}

.stFileUploader label { color: var(--muted) !important; font-family: 'DM Mono', monospace !important; font-size: 0.8em !important; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="sys-header">
    <div class="sys-header-left">
        <h1>🛡️ PPE Compliance Detection System</h1>
        <p>AI-Based Smart Access Control &nbsp;·&nbsp; Food Processing Unit</p>
    </div>
    <div class="sys-badge">● System Online</div>
</div>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return YOLO("ppe_best_v2.pt")

model = load_model()
classes = {0: "gloves", 1: "mask", 2: "hairnet"}

if "access_log" not in st.session_state:
    st.session_state.access_log = []

col_left, col_right = st.columns([1, 1.4])

with col_left:
    st.markdown('<div class="panel"><div class="panel-label">Input Source</div>', unsafe_allow_html=True)
    mode = st.radio("", ["📷 Webcam Capture", "🖼️ Upload Image"], label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    img_input = None
    if mode == "📷 Webcam Capture":
        img_input = st.camera_input("", label_visibility="collapsed")
    else:
        img_input = st.file_uploader("Drop image here", type=["jpg", "jpeg", "png"])

with col_right:
    if img_input:
        image = Image.open(img_input)
        image_np = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        results = model(image_np, conf=0.2)

        detected = {}
        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])
                name = classes[cls_id]
                if name not in detected or conf > detected[name]:
                    detected[name] = conf

        detected_names = set(detected.keys())
        allowed = len(detected_names) >= 2
        timestamp = datetime.now().strftime("%H:%M:%S")

        # 1. Access Decision
        if allowed:
            st.markdown(f'''
            <div class="decision-allowed">
                <div class="decision-title" style="color:#22c55e;">✔ ACCESS ALLOWED</div>
                <div class="decision-sub" style="color:#22c55e;">{len(detected_names)} / 3 PPE Items Detected &nbsp;·&nbsp; {timestamp}</div>
            </div>''', unsafe_allow_html=True)
            st.session_state.access_log.append(f'<span class="log-time">[{timestamp}]</span><span class="log-allow"> ALLOWED — {", ".join(detected_names).upper()}</span>')
        else:
            missing = set(classes.values()) - detected_names
            st.markdown(f'''
            <div class="decision-denied">
                <div class="decision-title" style="color:#ef4444;">✘ ACCESS DENIED</div>
                <div class="decision-sub" style="color:#ef4444;">Missing: {", ".join(missing).upper()} &nbsp;·&nbsp; {timestamp}</div>
            </div>''', unsafe_allow_html=True)
            st.session_state.access_log.append(f'<span class="log-time">[{timestamp}]</span><span class="log-deny"> DENIED — MISSING: {", ".join(missing).upper()}</span>')

        # 2. Annotated Image
        annotated = results[0].plot()
        annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
        st.image(annotated_rgb, use_container_width=True)

        # 3. PPE Detection Details
        st.markdown('<div class="panel"><div class="panel-label">Detection Results</div>', unsafe_allow_html=True)
        for item in ["gloves", "mask", "hairnet"]:
            if item in detected:
                conf_pct = int(detected[item] * 100)
                st.markdown(f'''
                <div class="ppe-row ppe-detected">
                    <span>✔ {item}</span>
                    <span class="conf-pill">{conf_pct}%</span>
                </div>
                <div class="conf-bar"><div class="conf-fill-green" style="width:{conf_pct}%"></div></div>
                ''', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="ppe-row ppe-missing"><span>✘ {item}</span><span class="conf-pill">—</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.markdown("""
        <div style="border:1px dashed #1d2433; border-radius:4px; padding:80px 40px; text-align:center; color:#2d3748; margin-top:10px;">
            <div style="font-size:2.5em; margin-bottom:12px;">🛡️</div>
            <div style="font-family:'DM Mono',monospace; font-size:0.8em; letter-spacing:2px; text-transform:uppercase;">
                Awaiting Input
            </div>
        </div>
        """, unsafe_allow_html=True)

# Access Log
st.markdown('<div class="panel"><div class="panel-label">Access Log</div>', unsafe_allow_html=True)
if st.session_state.access_log:
    log_html = "<br>".join(reversed(st.session_state.access_log[-10:]))
    st.markdown(f'<div class="log-box">{log_html}</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="log-box">No entries yet — awaiting first scan...</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)