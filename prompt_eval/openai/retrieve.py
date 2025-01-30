from openai import OpenAI
client = OpenAI()

try:
    response = client.batches.list()
    print("Response:", response)
    file_response = client.files.content("file-3uJA6E4CoXbXGS6JQXaKCd")
    
    with open('output_yn.txt', 'w') as file:
    # Write the text content to the file
        file.write(file_response.text)
    
except Exception as e:
    print("An error occurred:", e)