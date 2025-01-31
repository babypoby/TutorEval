import json

def process_json(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    new_data = []

    for item in data:
        base_entry = {
            "conversation_id": item["c_id"],
            "lesson_topic": item["lesson_topic"],
            "conversation_history": item["c_h"]
        }

        # First entry with c_r
        entry1 = base_entry.copy()
        entry1["conversation_id"] += "_1"
        entry1["conversation_response"] = item["c_r"]
        new_data.append(entry1)

        # Second entry with c_r_
        entry2 = base_entry.copy()
        entry2["conversation_id"] += "_2"
        entry2["conversation_response"] = item["c_r_"]
        new_data.append(entry2)

    with open(output_file, 'w') as f:
        json.dump(new_data, f, indent=2)

# Usage
input_file = 'train.json'  # Replace with your input file name
output_file = 'train_edited.json'  # Replace with your desired output file name

process_json(input_file, output_file)
