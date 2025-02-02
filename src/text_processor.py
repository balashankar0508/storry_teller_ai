from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_length=500):
    summary = summarizer(text, max_length=max_length, min_length=50, do_sample=False)
    return summary[0]["summary_text"]

if __name__ == "__main__":
    sample_text = "Once upon a time, in a faraway land..."
    print(summarize_text(sample_text))
