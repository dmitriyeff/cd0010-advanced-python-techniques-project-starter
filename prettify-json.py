import json

with open('./data/cad.json', 'r') as data:
	cad_data = json.load(data)

with open('./data/cad.json', 'w') as f:
	prettified_json = json.dumps(cad_data, indent=4)
	for line in prettified_json:
		# Prettify JSON
		f.write(line)
