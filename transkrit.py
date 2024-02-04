from openai import OpenAI

client = OpenAI(api_key="") #add yours :)


def transcribe_audio(audio_file_path):
    print("transcribing audio...")
    with open(audio_file_path, 'rb') as audio_file:
        transcription = client.audio.transcriptions.create(file=audio_file, model="whisper-1")
    print(transcription)
    return transcription.text


def meeting_minutes(transcription):
    print("generating minutes...")
    abstract_summary = abstract_summary_extraction(transcription)
    key_points = key_points_extraction(transcription)
    action_items = action_item_extraction(transcription)
    sentiment = sentiment_analysis(transcription)
    return {
        'abstract_summary': abstract_summary,
        'key_points': key_points,
        'action_items': action_items,
        'sentiment': sentiment
    }

def abstract_summary_extraction(transcription):
    print("extrcting summary...")
    response = client.chat.completions.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a highly skilled AI trained in language comprehension and summarization. I would like you to read the following text and summarize it into a concise abstract paragraph. Aim to retain the most important points, providing a coherent and readable summary that could help a person understand the main points of the discussion without needing to read the entire text. Please avoid unnecessary details or tangential points."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    print(response)
    return response.choices[0].message.content


def key_points_extraction(transcription):
    print("extracting keypoints...")
    response = client.chat.completions.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a proficient AI with a specialty in distilling information into key points. Based on the following text, identify and list the main points that were discussed or brought up. These should be the most important ideas, findings, or topics that are crucial to the essence of the discussion. Your goal is to provide a list that someone could read to quickly understand what was talked about."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response.choices[0].message.content


def action_item_extraction(transcription):
    print("extracting action-items...")
    response = client.chat.completions.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are an AI expert in analyzing conversations and extracting action items. Please review the text and identify any tasks, assignments, or actions that were agreed upon or mentioned as needing to be done. These could be tasks assigned to specific individuals, or general actions that the group has decided to take. Please list these action items clearly and concisely."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response.choices[0].message.content

def sentiment_analysis(transcription):
    print("analysing sentiment...")
    response = client.chat.completions.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "As an AI with expertise in language and emotion analysis, your task is to analyze the sentiment of the following text. Please consider the overall tone of the discussion, the emotion conveyed by the language used, and the context in which words and phrases are used. Indicate whether the sentiment is generally positive, negative, or neutral, and provide brief explanations for your analysis where possible."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response.choices[0].message.content

# def save_as_docx(minutes, filename):
#     doc = Document()
#     for key, value in minutes.items():
#         # Replace underscores with spaces and capitalize each word for the heading
#         heading = ' '.join(word.capitalize() for word in key.split('_'))
#         doc.add_heading(heading, level=1)
#         doc.add_paragraph(value)
#         # Add a line break between sections
#         doc.add_paragraph()
#     doc.save(filename)

def save_as_txt(minutes, filename):
    with open(filename, 'w') as file:
        for key, value in minutes.items():
            heading = ' '.join(word.capitalize() for word in key.split('_'))
            file.write(f"{heading}\n{value}\n\n")

audio_file_path = "transcript-2.mp3"
transcription = transcribe_audio(audio_file_path)
minutes = meeting_minutes(transcription)
print(minutes)

save_as_txt(minutes, 'meeting_minutes.txt')