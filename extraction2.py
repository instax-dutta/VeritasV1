#script to divide the phishing_domains.txt into multiple files containing 500 domains each
import os

def extract_domains_efficiently(input_filename, output_folder, domains_per_file=500):
    """
    Extracts domains from a text file, saves them into multiple files, and stops when no domains are left.

    Args:
        input_filename (str): The name of the input text file.
        output_folder (str): The name of the folder to store divided files.
        domains_per_file (int): The number of domains to include in each output file.
    """

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Create the output folder if needed

    output_file_index = 1
    domains_extracted = 0

    with open(input_filename, 'r') as infile:
        while True:
            domains = []
            for _ in range(domains_per_file):
                line = infile.readline()
                if not line:  # End of file reached
                    break
                domains.append(line.strip())

            if not domains:  # No more domains in the file
                break

            output_filename = os.path.join(output_folder, f'links_{output_file_index}.txt')
            with open(output_filename, 'w') as outfile:
                outfile.writelines(domain + '\n' for domain in domains)

            domains_extracted += len(domains)
            output_file_index += 1

    print(f"Extracted a total of {domains_extracted} links.")

# Example usage
extract_domains_efficiently('phishing_links.txt', 'divided2') 
