from pdf_reader import extract_text_from_pdf
from llm_handler import generate_story_from_text
from text_to_speech import speak_text

def main():
    pdf_path = "data/stories/sample_story.pdf"  # Make sure the PDF file exists!
    
    # Step 1: Extract text from PDF
    text = extract_text_from_pdf(pdf_path)
    
    if not text:
        print("❌ No text extracted from the PDF!")
        return
    
    print("\n✅ Extracted Text:\n", text[:500])  # Print a small preview
    
    # Step 2: Generate a story using LLaMA 2
    story = generate_story_from_text(text)
    
    print("\n✅ Generated Story:\n", story)  # Print for verification
    
    input("\nPress Enter to start speaking...")  # Allow user to verify before speaking
    
    # Step 3: Speak the story
    print("\n🎙️ Speaking story...")
    speak_text(story)
    print("✅ Finished speaking.")

if __name__ == "__main__":
    main()
