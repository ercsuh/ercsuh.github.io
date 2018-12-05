from SqliteDao import SqliteDao as sql
import json
import os

directory = "Markdown_Files"
try:
	os.mkdir(directory)
	print("Directory \'" + directory + "\' created.")
except FileExistsError:
	print("Directory \'" + directory + "\' already exists.")

db = sql('history.sql')
sql.create_recent_entries_db(db)
reports = sql.get_reports(db)

for branch in reports.keys():
	new_path = "{0}/{1}.md".format(directory, branch)
	out_file = open(new_path, "w")

	output = ""
	output += "# {}\n".format(branch)
	report = json.loads(reports[branch][1])

	statuses = []
	for key in report:
		if key == "valid_files" or key == "pass_cleanup" or ("test" in key and "report" not in key):
			# print("In tests. The current key is " + key + ".")
			statuses.append(report[key])

	if False in statuses:
		status = False
	else:
		status = True

	output += "## Status: {}\n".format(status)
	output += "#### Date: {}\n".format(reports[branch][0])  # FIXME: Ask Dr. Piccolo

	for key in report:
		if "report" in key:
			# print("In reports. The current key is " + key + ".")
			output += "{}".format(report[key])

	out_file.write(output)
	out_file.close()
