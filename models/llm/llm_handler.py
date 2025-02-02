from llama_cpp import Llama
import os

MODEL_PATH = os.path.join("models", "llm", "llama-2-7b.Q4_K_M.gguf")

# Load the model
llm = Llama(model_path=MODEL_PATH, n_ctx=2048)

def generate_story_prompt(prompt):
    response = llm(f"Tell me a detailed and engaging story about {prompt}.", max_tokens=500)
    return response["choices"][0]["text"].strip()

if __name__ == "__main__":
    print(generate_story_prompt("a boy who found a magic book"))
