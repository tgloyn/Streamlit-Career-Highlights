from PIL import Image
import base64
from io import BytesIO
import streamlit as st, hmac

def check_password():
    def _enter():
        pw_ok = hmac.compare_digest(st.session_state.get("pw", ""), st.secrets["password"])
        st.session_state["auth"] = pw_ok
        st.session_state.pop("pw", None) # remove password from session state

    if not st.session_state.get("auth", False):
        st.text_input("Enter password to access site:", type="password", key="pw", on_change=_enter)
        if "auth" in st.session_state and not st.session_state["auth"]:
            st.error("Incorrect password")
        st.stop()
        
def load_headshot(path, display_px=150, pixel_ratio=2):
    """
    Load and process the headshot image.
    """
    img = Image.open(path).convert("RGB")
    w, h = img.size
    if w != h:
        side = min(w, h)
        left = (w - side) // 2
        top = (h - side) // 2
        img = img.crop((left, top, left + side, top + side))
    target_px = display_px * pixel_ratio
    if img.width != target_px:
        img = img.resize((target_px, target_px), Image.LANCZOS)
    buf = BytesIO()
    img.save(buf, format="PNG")  # lossless
    b64 = base64.b64encode(buf.getvalue()).decode()
    st.markdown(
        f"""
        <img src="data:image/png;base64,{b64}" 
             style="width:{display_px}px;height:{display_px}px;
                    border-radius:50%;object-fit:cover;
                    border:3px solid #fff;box-shadow:0 4px 8px rgba(0,0,0,0.2);" />
        """,
        unsafe_allow_html=True
    )

def social_links(
    linkedin_url: str,
    github_url: str,
    goodreads_url: str,
    size: int = 26,
    color: str = "#0A66C2",
    opacity: float = 0.70,
    hover_color: str | None = None,
):
    """
    color: base hex (no alpha)
    opacity: 0–1 applied uniformly
    hover_color: optional solid hover color (e.g. '#0A66C2' or '#222')
  All icons inherit currentColor so they share the same base/hover styles.
  Goodreads icon path sourced from Simple Icons (simplified) – brand color typically #382110
    """
    # Normalize
    color = color.strip()
    if hover_color:
        hover_color = hover_color.strip()

    # Build RGBA from hex + opacity
    def hex_to_rgba(hex_color, alpha):
        hex_color = hex_color.lstrip("#")
        if len(hex_color) == 3:
            hex_color = "".join(c*2 for c in hex_color)
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return f"rgba({r},{g},{b},{alpha})"

    rgba = hex_to_rgba(color, opacity)

    hover_css = f"color:{hover_color} !important;" if hover_color else f"color:{hex_to_rgba(color, min(opacity+0.2,1))} !important;"

    return f"""
    <style>
      .social-links a {{
        display:inline-flex;
        align-items:center;
        color:{rgba};
        transition: color .25s ease, transform .25s ease;
      }}
      .social-links a:hover {{
        {hover_css}
        transform: translateY(-2px);
      }}
      .social-links svg {{
        width:{size}px;
        height:{size}px;
      }}
    </style>
    <div class="social-links" style="display:flex;gap:14px;margin-top:6px;">
      <a href="{linkedin_url}" target="_blank" rel="noopener" title="LinkedIn" aria-label="LinkedIn">
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M4.98 3.5a2.5 2.5 0 11.02 5.001A2.5 2.5 0 014.98 3.5zM3 9h4v12H3zM9.5 9h3.8v1.71h.05c.53-.96 1.82-1.97 3.75-1.97 4.01 0 4.75 2.64 4.75 6.07V21h-4v-5.2c0-1.24-.02-2.83-1.73-2.83-1.73 0-1.99 1.35-1.99 2.74V21h-4z"/>
        </svg>
      </a>
      <a href="{github_url}" target="_blank" rel="noopener" title="GitHub" aria-label="GitHub">
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 .5C5.65.5.5 5.65.5 12c0 5.1 3.29 9.4 7.86 10.94.58.11.79-.25.79-.56 0-.27-.01-1.15-.02-2.09-3.2.7-3.88-1.36-3.88-1.36-.53-1.06-1.29-1.35-1.29-1.35-1.06-.73.08-.72.08-.72 1.18.08 1.81 1.21 1.81 1.21 1.04 1.78 2.73 1.27 3.39.97.11-.76.41-1.27.74-1.56-2.56-.29-5.26-1.29-5.26-5.73 0-1.27.46-2.31 1.21-3.12-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.18 1.19a11.07 11.07 0 012.9-.39c.98 0 1.97.13 2.9.39 2.2-1.5 3.17-1.19 3.17-1.19.63 1.59.23 2.76.11 3.05a4.54 4.54 0 011.21 3.12c0 4.45-2.7 5.44-5.28 5.72.42.36.79 1.07.79 2.17 0 1.56-.02 2.81-.02 3.19 0 .31.21.68.8.56A10.52 10.52 0 0023.5 12c0-6.35-5.15-11.5-11.5-11.5z"/>
        </svg>
      </a>
      <a href="{goodreads_url}" target="_blank" rel="noopener" title="Goodreads" aria-label="Goodreads">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true">        <path d="M11.43 23.995c-3.608-.208-6.274-2.077-6.448-5.078.695.007 1.375-.013 2.07-.006.224 1.342 1.065 2.43 2.683 3.026 1.583.496 3.737.46 5.082-.174 1.351-.636 2.145-1.822 2.503-3.577.212-1.042.236-1.734.231-2.92l-.005-1.631h-.059c-1.245 2.564-3.315 3.53-5.59 3.475-5.74-.054-7.68-4.534-7.528-8.606.01-5.241 3.22-8.537 7.557-8.495 2.354-.14 4.605 1.362 5.554 3.37l.059.002.002-2.918 2.099.004-.002 15.717c-.193 7.04-4.376 7.89-8.209 7.811zm6.1-15.633c-.096-3.26-1.601-6.62-5.503-6.645-3.954-.017-5.625 3.592-5.604 6.85-.013 3.439 1.643 6.305 4.703 6.762 4.532.591 6.551-3.411 6.404-6.967z"/>
      </svg>
      </a>
    </div>
    """

def page_title_and_socials(title: str):
    st.title(title)
    st.write(social_links(
        linkedin_url="https://www.linkedin.com/in/troy-gloyn-99b24b131/",
        github_url="https://github.com/troygloyn",
        goodreads_url="https://www.goodreads.com/user/show/130347255-troy-gloyn",
        size=26,
        color="#0A66C2",
        opacity=0.55,
        hover_color="#004182"
    ), unsafe_allow_html=True)

def headshot_and_title(title: str):
    # Create custom header with circular headshot and title
    headshot_col, title_col = st.columns([1, 8])

    with headshot_col:
        # Display the headshot image
        try:
            load_headshot('assets/headshot.png', display_px=120)
        except:
            st.error("Headshot image not found")

    with title_col:
        page_title_and_socials(title)

def ds_project_details(header: str, provenance: str, date: str, description: str, tech_used: str, key_features: str, github_link: str):
    st.header(header)
    
    if github_link.lower() == "nan":
        st.write(f"""
        **Provenance**: {provenance}
                
        **Date**: {date}

        **Description**: {description}

        **Technologies Used**: {tech_used}

        **Key Features**:
        {key_features}""")
        st.info("No public repository available for this project.")
    else:
        st.write(f"""
        **Provenance**: {provenance}
                
        **Date**: {date}

        **Description**: {description}

        **Technologies Used**: {tech_used}

        **Key Features**:
        {key_features}

        **Link to Project**: [GitHub Repository]({github_link})""")



