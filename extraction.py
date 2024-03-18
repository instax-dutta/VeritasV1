import re

def extract_domains(input_filename, output_filename):
    """
    Extracts domains from a text file and saves them to another file.

    Args:
        input_filename (str): The name of the input text file.
        output_filename (str): The name of the output file to save domains.
    """

    # Regular expression to match common domain patterns
    domain_pattern = r'(?:https?:\/\/)?(?:www\.)?(?:[\w-]+\.)+[a-zA-Z]{2,}(?:\/\S*)?'

    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            domains = re.findall(domain_pattern, line)
            for domain in domains:
                outfile.write(domain + '\n')

# Example usage
extract_domains('raw.txt', 'extracted_domains.txt')
