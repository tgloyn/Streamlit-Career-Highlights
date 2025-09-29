import streamlit as st
from helpers import *
from dotenv import load_dotenv 
import faiss, pickle
import numpy as np
from openai import OpenAI

load_dotenv()
check_password()

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
VECTORIZE_PATH = "assets/vectorize"
SYSTEM_PROMPT = (
  "You are the candidate’s advocate. Answer only from provided context. "
  "If unsure, say so. Keep answers concise. When possible, cite source titles."
)
MAX_QUERIES = 5

st.set_page_config(page_title="Chat", page_icon=":speech_balloon:", layout="wide")
headshot_and_title("Ask Away!")
st.write('---')
st.write('')
st.write('')

@st.cache_resource
def load_assets():
    index = faiss.read_index(f"{VECTORIZE_PATH}/cv.index")
    with open(f"{VECTORIZE_PATH}/cv_docs.pkl","rb") as f: docs = pickle.load(f)
    return index, docs

index, docs = load_assets()

def retrieve(q, k=6):
    v = client.embeddings.create(model="text-embedding-3-large", input=q).data[0].embedding
    v = np.array(v, dtype="float32"); v /= np.linalg.norm(v)
    D, I = index.search(v.reshape(1,-1), k)
    return [docs[i] for i in I[0]]

def answer(prompt: str, k: int = 6):
    # 1) Retrieve context for the latest prompt
    ctx_docs = retrieve(prompt, k=k)  # returns list of {"text": ..., "meta": {...}}
    if ctx_docs:
        ctx_block = "\n\n".join(
            f"[{i+1}] {d['meta'].get('title','doc')}: {d['text']}"
            for i, d in enumerate(ctx_docs)
        )
        augmented_user = {
            "role": "user",
            "content": (
                f"Question: {prompt}\n\n"
                f"{SYSTEM_PROMPT}\n\n"
                f"Context:\n{ctx_block}"
            ),
        }
    else:
        augmented_user = {"role": "user", "content": prompt}

    # 2) Build messages: keep history except the just-added raw user turn
    history = st.session_state.messages[:-1]  # everything before this prompt
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history + [augmented_user]

    # 3) Stream completion
    stream = client.chat.completions.create(
        model=st.session_state["openai_model"],
        messages=messages,
        stream=True,
    )
    return st.write_stream(stream)

if "max_queries" not in st.session_state:
    st.session_state["max_queries"] = 0

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter text"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = answer(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.session_state["max_queries"] += 1
    if st.session_state["max_queries"] >= MAX_QUERIES:
        st.warning("You have reached the maximum number of queries for this session. Please refresh the page to start a new session.")
        st.stop()

st.info(f'You have used {st.session_state["max_queries"]} out of {MAX_QUERIES} allowed queries in this session.')
