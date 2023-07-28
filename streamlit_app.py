import openai
import streamlit as st
import os

# streamlit run streamlit_app.py
# chatgpt plot to story
# https://www.taskade.com/templates/ai/chatgpt-novel-writing
# https://www.storyflint.com/blog/how-to-use-chat-gpt-for-storytelling
# https://www.allabtai.com/how-to-write-a-story-in-chatgpt-prompt-engineering/
# https://www.makeuseof.com/use-chatgpt-to-write-novel/
# https://www.makeuseof.com/chatgpt-how-to-master-storytelling/
# https://medium.com/@neonforge/how-to-write-a-book-with-help-of-chatgpt-practical-step-by-step-guide-d190994b67b4
# https://basmo.app/how-to-write-a-book-with-chatgpt/
# https://www.writingbeginner.com/how-to-write-a-novel-with-chatgpt/
# https://www.nichepursuits.com/how-to-use-chatgpt-to-write-a-book/
# https://www.griproom.com/fun/how-to-use-chatgpt-to-write-a-short-story
# 

try:
    st.title('AI Story Writing Assistant :sunglasses:')

    service_type = st.sidebar.radio(
    "Select a type of service that you want",
    ('Plot and Story Development', 'Characters', 'Setting'))

    prompt_prefix = ""
    prompt_prefix_list = []

    if service_type == "Plot and Story Development":
        prompt_prefix_list.append('Write a one-sentence premise for a novel about:')
        prompt_prefix_list.append('Develop a detailed summary of the plot for a novel about:')
        prompt_prefix_list.append('Create a list of potential titles for a novel about:')
        prompt_prefix_list.append('Create a list of potential subplots for a novel about:')
        prompt_prefix_list.append('Develop a list of symbols for a novel about:')
        prompt_prefix_list.append('Create a list of potential imagery that will be used in a novel about:')
    elif service_type == "Characters":
        prompt_prefix_list.append('Generate a list of character names for a novel about:')
        prompt_prefix_list.append('Write a descriptive paragraph about the protagonist for a novel about:')
        prompt_prefix_list.append('Write a descriptive paragraph about the antagonist for a novel about:')
        prompt_prefix_list.append('Develop a list of potential conflicts that the main characters will face in a novel about:')
        prompt_prefix_list.append('Develop a list of potential character relationships for the main characters for a novel about:')
        prompt_prefix_list.append('Generate a list of potential character strengths for the main characters for a novel about:')
    elif service_type == "Setting":
        prompt_prefix_list.append('Generate a list of potential locations for a novel about:')
        prompt_prefix_list.append('Create a list of potential weather conditions for a novel about:')
        prompt_prefix_list.append('Write a descriptive paragraph about culture and society for a novel about:')
        prompt_prefix_list.append('Develop a list of potential technological advancements for a novel about:')
        prompt_prefix_list.append('Write a descriptive paragraph about the economy for a novel about:')
        prompt_prefix_list.append('Describe overall atmosphere and mood for a novel about:')
        prompt_prefix_list.append('Develop a list of potential symbols for a novel about:')

    prompt_prefix = st.sidebar.radio(
    "Select a prompt type", tuple(prompt_prefix_list))

    st.text(service_type)
    st.text(prompt_prefix)

    story_plot = st.text_area('Write your plot here')
    story_plot = story_plot.strip()


    if st.button('Submit your plot'):
        if len(story_plot) <= 0:
            st.error('Please type some text input and try again.')
        else:
            prompt = f'{prompt_prefix} "{story_plot}"'
            # st.write(f'prompt: {prompt}')
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=1,
            )

            #st.write(response)
            st.header('Response from OpenAI / ChatGPT:')
            st.success(response['choices'][0]['message']['content'])
            #st.write('You selected movie plot is: ', prompt)

except Exception as error:
    st.error('An error has occurred. Please try again.', icon="🚨")
    error_message = f"An exception occurred: {error}" 
    st.error(error_message)
