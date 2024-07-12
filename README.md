
https://github.com/user-attachments/assets/9fe72ffe-e971-4d0a-92ce-31bf24a662d9

# Text Summarizer

This is a command-line tool that summarizes text using the Ollama API with the Qwen2 0.5B model. 
It can summarize text from a file or direct input.

## Prerequisites

- Python 3.6 or higher
- Ollama installed and running on your system
- Qwen2 0.5B model pulled into Ollama

## Installation

1. Save this script as 'summarizer.py'.

2. Install the required Python libraries:

   pip install click requests

3. Ensure Ollama is running with the Qwen2 0.5B model:

   ollama serve
   ollama pull qwen2:0.5b

## Usage

### Summarize a text file:

python summarizer.py -t path/to/your/file.txt

This will create a new file named ".Summary of [your_file_name].txt" in the same directory, containing the summary.

### Summarize text input directly:

python summarizer.py "Your text goes here. This is the text you want to summarize."

This will print the summary to the console.

## Examples

1. Summarize a file named 'book.txt':
   python summarizer.py -t book.txt
   Output: Creates a file named ".Summary of book.txt"

2. Summarize direct text input:
   python summarizer.py "The quick brown fox jumped over the lazy dog."
   Output: Prints "Summary of text pasted:" followed by the summary.

## Note

- Ensure that Ollama is running and the Qwen2 0.5B model is available before using this tool.
- The quality of the summary depends on the capabilities of the Qwen2 0.5B model.

## Troubleshooting

- If you encounter issues with Ollama, ensure it's properly installed and running.
- Check that the Qwen2 0.5B model is pulled into Ollama.
- Verify that the Ollama API is accessible at http://localhost:11434/api/generate.
