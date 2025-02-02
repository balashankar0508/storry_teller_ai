from llama_cpp import Llama
import os

MODEL_PATH = os.path.join("models", "llm", "llama-2-7b.Q4_K_M.gguf")

# Load the model
llm = Llama(model_path=MODEL_PATH, n_ctx=2048)

def generate_story_from_text(text):
    """
    Uses an LLM (LLaMA 2) to rewrite the extracted text into a structured story.
    :param text: Extracted text from the PDF.
    :return: Processed story in natural storytelling format.
    """
    try:
        response = llm(
            f"Rewrite the following text into a well-structured short story:\n\n"
            f"{text[:1500]}\n\n"  # Limit input to 1500 characters for efficiency
            f"Make sure the story has a clear beginning, middle, and end. "
            f"Use engaging and natural storytelling language. "
            f"Do not include instructions or metadata, just the story.",
            max_tokens=800
        )

        if "choices" in response and len(response["choices"]) > 0:
            story_text = response["choices"][0]["text"].strip()

            # Clean up unwanted formatting
            story_text = story_text.replace("```", "").replace("\n", " ").strip()

            return story_text
        else:
            return "Error: No valid response from the model."

    except Exception as e:
        return f"Error generating story: {str(e)}"

if __name__ == "__main__":
    test_text = "A boy finds a magic book in an old library..."
    print(generate_story_from_text(test_text))
