# https://platform.openai.com/examples/default-grammar

from openai import OpenAI
client = OpenAI()

bad_sentence = input("Write a sentence you want the grammar corrected for:")

completions = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with statements, and your task is to convert them to standard English."
    },
    {
      "role": "user",
      "content": bad_sentence
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)

print(response.choices[0].message)