from tqdm import tqdm
from functions import (
    get_chat_response,
    save_to_file,
    read_txt_to_string
)

if __name__== "__main__":
    context = "You are a seasoned programmer and educator."

    prompt_main_topics = """
        Please curate a comprehensive list of topics in {main_topic}, 
        organized to cover a learning progression from beginner to advanced levels. 
        Aim for diversity in subject matter, ensuring that the list forms a coherent learning pathway 
        for individuals aiming to master the topic. Present the topics in a text-based, CSV-like format, 
        with each record consisting of the level and a brief description of the topic. 
        The format should be: "Level, Topic with Short Description". 
        Don not include any additional text of your own, just topics formatted as follow: 
        "Level, Topic with Short Description".
        """
    
    prompt_create_note = """
        Given your expertise, please prepare a Markdown-formatted page or note aimed at a {level} audience. 
        This document will be part of a wiki focused on {main_topic}, 
        and should provide a detailed exploration of the subtopic: {subtopic}. 
        Utilize a diverse range of Markdown styling features—such as bullet points, tables, 
        and callouts—to effectively convey the information and maximize educational value. 
        Do not include table of contents it is not necessary. Be as detailed and precise as possible.
        """
    
    main_topic = "miniconda environments (mac)"

    main_topics_response = get_chat_response(context, prompt_main_topics.format(main_topic=main_topic))
    save_to_file(main_topics_response, "miniconda/topics", "txt")

    main_topics_split = main_topics_response.split("\n")
    main_topics_split = [s for s in main_topics_split if len(s) > 0]
    print(main_topics_split)

    for row in tqdm(main_topics_split, desc="Processing topics..."):
        level, topic = row.split(", ", 1)

        prompt = prompt_create_note.format(level = level, 
                                           main_topic = main_topic,
                                           subtopic = topic)
        
        note = get_chat_response(context, prompt)

        note_name = "miniconda/" + topic.replace("_", "-")
        save_to_file(note, note_name, extension="md")