import openai # openai v1.0.0+

client = openai.OpenAI(api_key="sk-ihowCuDNWOYpdv9-foT7BA",base_url="https://litellm.dccp.pbu.dedalus.com") # set proxy to base_url

# request sent to model set on litellm proxy, litellm --model

response = client.chat.completions.create(model="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0", messages = [

    {
        "role": "user",

        "content": "this is a test request, write a short poem"
    }

])
 
print(response.choices[0].message.content)