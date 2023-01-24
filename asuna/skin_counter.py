import os, json

def get_skin_counter():
	skin_counter = {}
	n = 0
	for file in os.listdir("./"):
		if os.path.isdir(file):
			skin_counter[n] = {'file': f'{file}/{file}.model.json', 'name': file}
			n += 1
			print(n, file)
	return skin_counter

if __name__ == "__main__":
	with open('skins.json', 'w') as f:
		json.dump(get_skin_counter(), f, indent=0, sort_keys=True)