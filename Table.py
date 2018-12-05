from SqliteDao import SqliteDao as sql
import sqlite3
import pandas as pd
from pandas import DataFrame
import os

directory = "Markdown_Files"
try:
	os.mkdir(directory)
	print("Directory \'" + directory + "\' created.")
except FileExistsError:
	print("Directory \'" + directory + "\' already exists.")

db = sql('history.sql')
df = sql.get_all_recents(db)

new_path = "{0}/Table.md".format(directory)
out_file = open(new_path, "w")

output = ""
output += "Data Set | User | Status | Date | Time Elapsed | Samples | Meta Data Variables | Feature Variables\n"
output += "-------- | ---- | ------ | ---- | ------------ | ------- | ------------------- | -----------------\n"

for pull_request in df:
	branch = pull_request[1]
	user = pull_request[11]
	status = pull_request[13]
	date = pull_request[2]
	time_elapsed = pull_request[10]
	num_samples = pull_request[8]
	meta_data_variables = pull_request[5]
	feature_variables = pull_request[4]

	output += branch + " | " + user + " | "
	output += "[{0}](./Markdown_Files/{1}.md)".format(status, branch) + " | "
	output += str(date) + " | " + str(time_elapsed) + " | " + str(num_samples) + " | "
	output += str(meta_data_variables) + " | " + str(feature_variables) + "\n"


out_file.write(output)
out_file.close()




# df = pd.read_sql_table("RecentPullRequests", db)


