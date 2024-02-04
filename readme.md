# Audio Transcription and Meeting Insights Generator

Welcome to our latest foray into the magical world of AI, where we turn tedious meeting audios into insightful, actionable, and occasionally hilarious text summaries. Because why should robots have all the fun?

## What Does This Do?

Ever sat through a meeting and thought, "This could have been an email"? Well, now it can be an email, a report, or even a bedtime story (if you find corporate strategies and action items oddly comforting). Our script takes your audio files, transcribes them, and then distills them down into the essence of what was actually important. It's like having your own personal scribe, only this one doesn't get tired or judge your meeting topics.

### Features

- **Transcribe Audio:** Converts your audio files into text with the patience and accuracy not found in most humans.
- **Generate Minutes:** Like magic, but with AI, it turns those transcriptions into abstract summaries, key points, action items, and even analyzes the sentiment (happy, sad, or the ever-popular existential dread).
- **Save the World:** Okay, maybe not yet, but at least save some time and sanity.

## How to Use

1. **Install Dependencies:** Make sure you have `openai` installed. If not, run `pip install openai` and wait for the magic of the internet to do its thing.
2. **API Key:** Insert your OpenAI API key in the placeholder. If you don't have one, time to visit [OpenAI](https://openai.com/api/) and convince them you're worthy.
3. **Run the Script:** Place your audio file path into the `audio_file_path` variable and let it rip. Watch as your console fills with the sweet, sweet text of productivity.
4. **Save Your Minutes:** Decide if you're old school and want a text file with your meeting's greatest hits, or if you're feeling adventurous, uncomment the docx function and go wild.

### Example Usage

```python
audio_file_path = "your_audio_file.mp3"
transcription = transcribe_audio(audio_file_path)
minutes = meeting_minutes(transcription)
print(minutes)
save_as_txt(minutes, 'meeting_minutes.txt')
```

## Cautionary Advice

- **This script assumes your meetings make sense:** It's not a miracle worker. Garbage in, garbage out.
- **API Costs:** Remember, with great power comes great API costs. Keep an eye on your usage unless you want a surprise bill.
- **Sentience:** If your script starts asking existential questions, please turn off your computer and go outside.

## Contributing

Found a way to make the AI even snarkier? Got a feature request, like adding a "translate to pirate" option? We're all ears. Fork the project, make your changes, and submit a pull request. Let's make meetings fun again!
