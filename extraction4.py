#script which is being used to remove the links from the phishing_domains.txt 
def remove_http_links(input_filename):
    """
    Removes lines starting with "http" or "https" from an input file (in-place modification).

    Args:
        input_filename (str): The name of the input text file.
    """

    with open(input_filename, 'r') as infile:
        lines = infile.readlines()  # Read all lines

    with open(input_filename, 'w') as outfile:  # Open for overwriting
        for line in lines:
            if not line.startswith(('http://', 'https://')):
                outfile.write(line)

# Example usage
remove_http_links('phishing_domains.txt')
