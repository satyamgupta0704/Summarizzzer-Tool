import click
import requests
import os

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def summarize_text(text):
    prompt = f"Summarize the following text:\n\n{text}\n\nSummary:"
    
    payload = {
        "model": "qwen2:0.5b",
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(OLLAMA_API_URL, json=payload)
    
    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        return f"Error: Unable to generate summary. Status code: {response.status_code}"

@click.command()
@click.option('-t', '--text-file', type=click.Path(exists=True), help='Path to the text file to summarize')
@click.argument('text', nargs=-1, type=click.UNPROCESSED)
def main(text_file, text):
    if text_file:
        with open(text_file, 'r') as file:
            content = file.read()
        summary = summarize_text(content)
        
        output_file = f"summary of {os.path.basename(text_file)}"
   
        with open(output_file, 'w') as file:
            file.write(summary)
        
        click.echo(f"Summary has been written to {output_file}")
    elif text:
        text = ' '.join(text)
        summary = summarize_text(text)
        click.echo(f"Summary of text pasted:\n{summary}")
    else:
        click.echo("Please provide either a text file or direct text input.")

if __name__ == '__main__':
    main()