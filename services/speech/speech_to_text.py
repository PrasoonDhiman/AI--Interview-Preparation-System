from services.groq_service import client


def transcribe_audio(audio_path):

    with open(audio_path, "rb") as audio_file:

        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-large-v3"
        )

    return transcription.text


def process_audio(audio_path):

    transcript = transcribe_audio(audio_path)

    return {
        "text": transcript
    }