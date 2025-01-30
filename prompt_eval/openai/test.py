from openai import OpenAI


client = OpenAI()

try:
    # Create a file for batch input
    with open("batchinput_2.jsonl", "rb") as file:
        batch_input_file = client.files.create(
            file=file,
            purpose="batch"
        )

    print("Batch input file created:", batch_input_file)

    # Create a batch request
    response = client.batches.create(
        input_file_id=batch_input_file.id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
        metadata={
            "description": "temperature 0"
        }
    )

    print("Batch response:", response)

except Exception as e:
    print("An error occurred:", e)
