# build_index_once.py  (run locally)
import os
from dotenv import load_dotenv
import faiss, numpy as np, pickle, json
from openai import OpenAI

load_dotenv()
VECTORIZE_PATH = "assets/vectorize"
docs = json.load(open("assets/cv_docs.json"))  # [{"text": ..., "meta": {...}}, ...]
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

emb = client.embeddings.create(model="text-embedding-3-large",
                               input=[d["text"] for d in docs]).data
X = np.vstack([np.array(e.embedding, dtype="float32") for e in emb]).astype("float32")
faiss.normalize_L2(X)
index = faiss.IndexFlatIP(X.shape[1]); index.add(X)

faiss.write_index(index, f"{VECTORIZE_PATH}/cv.index")
with open(f"{VECTORIZE_PATH}/cv_docs.pkl","wb") as f: pickle.dump(docs, f)
with open(f"{VECTORIZE_PATH}/embedding_spec.json","w") as f: json.dump({"model":"text-embedding-3-large"}, f)
