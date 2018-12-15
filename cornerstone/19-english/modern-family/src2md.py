"""
src -> markdown 
"""

import argparse

def src2md(file):
	script_path = file
	directory = "/".join(script_path.split("/")[:-1])
	name = script_path.split("/")[-1].strip(".srt")
	# print(name)

	with open(script_path, encoding='utf-8') as f:
		read_data = f.read()

	block = read_data.split("\n\n") 

	# print(block[11]) # 
	"""
	Output: 
	23
	00:00:01,530 --> 00:00:03,740
	真想知道曼尼现在在做什么
	I wonder what Manny's doing right now.
	"""

	markdown = "# " + name + "\n"

	markdown += """
| Number  | Timeline  | Chinese  | English  | 
| :-------- | :---------: | :---------: | :---------: | 
"""


	lines = block[11:]
	for line in lines:
		group = line.split("\n")
		if len(group) != 4: continue 
		index, timeline, chinese, english = line.split("\n")
		markdown += "|" + index + "|" + timeline + "|" + chinese + "|" + english + "|" + "\n"

	markdown += "\n"

	authors = block[2:7]
	for i in authors:
		author = i.split("}")[-1]
		markdown += "* " + author + "\n"

	output_file_path = directory + "/" + name + ".md"

	with open(output_file_path, mode="w", encoding="utf-8") as f2:
		f2.write(markdown)
	return lines


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", nargs = 1, help="src to markdown")
    args = parser.parse_args()
    if args.file:
    	src2md(args.file[0])

