import os
from openai import OpenAI
import json
client = OpenAI(
    # api_key = os.environ.get("ARK_API_KEY"),
	api_key = "fd669268-fc1d-48a2-aadc-f9a206c8079a",
    base_url = "https://ark.cn-beijing.volces.com/api/v3",
)

# Image input:
response = client.chat.completions.create(
    model="ep-20241208134922-k9gl6",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "这是哪里？"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://ark-project.tos-cn-beijing.ivolces.com/images/view.jpeg"
                    }
                },
            ],
        }
    ],
)

print(json.dumps(client))
print(response.choices[0])