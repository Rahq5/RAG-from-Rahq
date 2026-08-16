from anthropic import Anthropic

client = Anthropic()

# 1. Upload the file — lives under `beta` because the Files API is still beta
with open("Parsing_PDF_using_LLM/sample.pdf", "rb") as f:
    file_upload = client.beta.files.upload(
        file=("sample.pdf", f, "application/pdf")
    )

# 2. Reference the uploaded file by its id in a message
#    Note: must use client.beta.messages.create() + the betas flag
#    whenever a file_id from the Files API is involved.
message = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    betas=["files-api-2025-04-14"],
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "file",
                        "file_id": file_upload.id,
                    },
                },
                {
                    "type": "text",
                    "text": """Extract the text content from the file. Exclude
                    texts from tables or images.""",
                },
            ],
        }
    ],
)

print(message.content[0].text)