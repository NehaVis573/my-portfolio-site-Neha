import boto3
import json

session = boto3.Session(profile_name='cic-sandbox')
bedrock = session.client('bedrock-runtime', region_name='us-east-1')

messages = [
    {
        "role": "user",
        "content": [{"text": "What is the capital of France? Reply in one sentence."}]
    }
]

response = bedrock.converse(
    modelId="us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    messages=messages,
    inferenceConfig={
        "maxTokens": 500,
        "temperature": 0.7
    }
)

answer = response['output']['message']['content'][0]['text']
print(f"Claude says: {answer}")