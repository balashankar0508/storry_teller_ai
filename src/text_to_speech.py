import pyttsx3

def speak_text(text):
    """
    Converts text to speech using the system's default voice (pyttsx3).
    :param text: The story to be spoken.
    """
    engine = pyttsx3.init()

    # Adjust voice properties
    engine.setProperty("rate", 150)  # Adjust speech speed
    engine.setProperty("volume", 1.0)  # Set max volume

    try:
        print("\n🎤 Speaking story...")
        engine.say(text)
        engine.runAndWait()
    except KeyboardInterrupt:
        print("❌ Speech interrupted.")
    finally:
        engine.stop()

if __name__ == "__main__":
    sample_story = "Once upon a time in a magical land, a young boy named Leo discovered an ancient book..."
    speak_text(sample_story)
