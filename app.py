def process_link(link):
    # Remove "http://" and "https://" from the beginning of the link
    if link.startswith("http://"):
        link = link[len("http://"):]
    elif link.startswith("https://"):
        link = link[len("https://"):]
    
    # Remove "/" at the end of the link
    link = link.rstrip("/")
    
    # Add "0.0.0.0 " at the beginning of the link
    return "0.0.0.0 " + link

def main():
    input_file = "input.txt"  # Replace with the path to your input file
    output_file = "output.txt"  # Replace with the path to your output file

    with open(input_file, "r") as file:
        links = file.readlines()

    with open(output_file, "w") as file:
        for link in links:
            processed_link = process_link(link.strip())
            file.write(processed_link + "\n")

if __name__ == "__main__":
    main()
