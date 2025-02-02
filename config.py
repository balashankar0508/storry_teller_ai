import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data", "stories")
MODEL_DIR = os.path.join(BASE_DIR, "models", "llm")
AUDIO_OUTPUT = os.path.join(BASE_DIR, "output.wav")

# Model Settings
LLM_MODEL_PATH = os.path.join(MODEL_DIR, "mistral-7b-instruct-v0.1.Q4_K_M.gguf")
TEXT_SUMMARIZATION_MODEL = "facebook/bart-large-cnn"
TTS_MODEL = "tts_models/en/ljspeech/tacotron2-DCA"

# LLM Settings
MAX_TOKENS = 500
CONTEXT_WINDOW = 2048
