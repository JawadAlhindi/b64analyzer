import base64
import json
import sys
from datetime import datetime

filename = sys.argv[1] if len(sys.argv) > 1 else "token.txt"

try:
    with open(filename, "r") as file:
        b64_string = file.read().strip()

    if b64_string.startswith("base64-"):
        b64_string = b64_string[len("base64-"):]

    b64_string = b64_string.replace("\n", "")
    missing_padding = len(b64_string) % 4
    if missing_padding:
        b64_string += "=" * (4 - missing_padding)

    decoded_bytes = base64.urlsafe_b64decode(b64_string)
    decoded_str = decoded_bytes.decode("utf-8")
    data = json.loads(decoded_str)

    # Print to terminal
    print(json.dumps(data, indent=2))

    # Save output to a new file with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"decoded_{timestamp}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"\n[+] Decoded JSON saved to: {output_file}")

except Exception as e:
    print(f"Error decoding file '{filename}': {e}")
