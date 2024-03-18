#script to extract the links from the phishing_domains.txt and save them into a separate file
def filter_http_links(input_filename, phishing_output_filename):
    """
    Filters out lines starting with "http" or "https" from an input file and
    saves them into a separate file.

    Args:
        input_filename (str): The name of the input text file.
        phishing_output_filename (str): The name of the output file to save potential phishing links.
    """

    with open(input_filename, 'r') as infile, open(phishing_output_filename, 'w') as outfile:
        for line in infile:
            if line.startswith(('http://', 'https://')):
                outfile.write(line)

# Example usage
filter_http_links('phishing_domains.txt', 'phishing_links.txt')
