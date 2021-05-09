import re

def convert(symbol, text):
	symbols = {
		"p": "medium",
		"##": "x-large",
		"#": "xx-large",
	}

	if symbol in symbols:
		return f"<span style=\"font-family: Comfortaa; font-size: {symbols[symbol]};\">{text}</span><br>"


def get_bold_text(text: str) -> str:
	regex = r"\*(.*?)\*"

	for word in text.split(" "):
		to_bold = re.search(regex, word)
		if to_bold == None:
			continue

		text = text.replace(to_bold.group(), f"<b>{to_bold.group(1)}</b>")
		
	return text


def process(text):
	processed_text_lines = [] 
	lines = text.split("\n")

	for line in lines:
		converted_line = "<br>"

		if line != "":
			#? Split only the first word, which will act as a symbol. Example - p for <p>
			symbol, text = line.split(" ", 1)

			#? Get the bolded text beforehand.
			text = get_bold_text(text)

			converted_line = convert(symbol, text)

		processed_text_lines.append(converted_line)
		
	processed_text = "\n".join(processed_text_lines)
	return processed_text
	
	
def read_file():
	with open("article.txt", "r") as f:
		text = f.read()
	return text


def save_file(text):
	with open("output/out.txt", "w") as f:
		f.write(text)


def main():
	text = read_file()
	processed_text = process(text)
	save_file(processed_text)


if __name__ == "__main__":
	main()