#                  -----WARNING----
# this python logic is correct but requiers me to pay so the GPT model would work
# and am not paying , i didnt got enough protein today ;(
#  to see full expermint working code go see {name file} , that's a free one




from anthropic import Anthropic

client = Anthropic()

file = client.files.create(
    file = open("Parsing_PDF_using_LLM/sample.pdf","rb"),
    purpose="user_data"
)


completion = client.chat.completions.create(
    model="gpt-5.1",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "file",
                    "file": {
                        "file_id": file.id,
                    }
                },
                {
                    "type": "text",
                    "text": """Extract the text content from the file. Exclude
                    texts from tables or images.""",
                },
            ]
        }
    ]
)

print(completion.choices[0].message.content)

