import re

def extract_emails(input_file, output_file):
    try:
        # Read the input file
        with open(input_file, "r") as file:
            content = file.read()

        # Regular expression to find email addresses
        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", content)

        # Remove duplicates while keeping order
        unique_emails = list(dict.fromkeys(emails))

        # Write emails to the output file
        with open(output_file, "w") as file:
            for email in unique_emails:
                file.write(email + "\n")

        print("=" * 40)
        print("Email Extraction Completed Successfully!")
        print("=" * 40)
        print(f"Total Emails Found: {len(unique_emails)}")
        print(f"Saved to: {output_file}")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "emails.txt"
    extract_emails(input_file, output_file)
