import re

def convert(symbol, text):
	symbols = {
		"p": "medium",
		"##": "x-large",
		"#": "xx-large",
	}

	if symbol in symbols:
		return f"<span style=\"font-family: Comfortaa; font-size: {symbols[symbol]};\">{text}</span><br>"


def pre_process_text(text: str) -> str:
	'''
	Converts bold and links and returns text
	'''
	regex_bold = r"\*(.*?)\*"
	regex_link = r"\[(.*?)\]\((.*?)\)"

	text = re.sub(regex_bold, r"<b>\1</b>", text)
	text = re.sub(regex_link, "<a href = \"\\2\" target = \"_blank\">\\1</a>", text)
		
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
			text = pre_process_text(text)

			converted_line = convert(symbol, text)

		processed_text_lines.append(converted_line)
		
	processed_text = "\n".join(processed_text_lines)
	return processed_text
	
	
def read_file():
	with open("article.txt", "r", encoding="utf8") as f:
		text = f.read()
	return text


def save_file(text):
	with open("output/out.txt", "w", encoding="utf8") as f:
		f.write(text)


def main():
	text = read_file()
	processed_text = process(text)
	save_file(processed_text)


if __name__ == "__main__":
	main()