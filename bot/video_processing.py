import os
import numpy as np
import librosa
import whisper
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, concatenate_videoclips
from gtts import gTTS

def extract_audio_peak(video_path):
    temp_audio = "temp.wav"
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(temp_audio)
    y, sr = librosa.load(temp_audio)
    volume = librosa.feature.rms(y=y)[0]
    spike_idx = np.argmax(volume)
    spike_time = spike_idx * 512 / sr
    os.remove(temp_audio)
    return max(0, spike_time - 10), min(video.duration, spike_time + 20)

def add_watermark(clip, watermark_path="assets/watermark.png"):
    logo = (ImageClip(watermark_path)
            .set_duration(clip.duration)
            .resize(height=100)
            .margin(right=10, bottom=10)
            .set_pos(("right", "bottom")))
    return CompositeVideoClip([clip, logo])

def generate_subtitles(video_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    srt_text = ""
    for segment in result['segments']:
        start = segment['start']
        end = segment['end']
        text = segment['text']
        srt_text += f"{start:.2f} --> {end:.2f}\n{text}\n"
    return srt_text

def add_voiceover(text, output_audio="voice.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(output_audio)
    return output_audio

def process_video(input_path):
    start, end = extract_audio_peak(input_path)
    base_clip = VideoFileClip(input_path).subclip(start, end)
    base_clip = base_clip.resize(height=1920, width=1080)

    watermarked = add_watermark(base_clip)

    outro = VideoFileClip("assets/outro.mp4").resize(watermarked.size)
    final = concatenate_videoclips([watermarked, outro])

    subtitles = generate_subtitles(input_path)
    voiceover_path = add_voiceover(subtitles[:200])  # Limit to avoid long audio
    voice_audio = VideoFileClip(voiceover_path).audio
    final = final.set_audio(voice_audio)

    output_file = "short_final.mp4"
    final.write_videofile(output_file, codec="libx264", audio_codec="aac")
    return output_file