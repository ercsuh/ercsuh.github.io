# BiomarkerBenchmark_GSE30784
## Status: True
#### Date: 08/17/18
### Testing Directory . . .

#### Results: PASS
---
### Testing Configuration File . . .

&#9989;	config.yaml contains all necessary configurations.

&#9989;	Title is less than 300 characters

&#9989;	description.md contains a description.

#### Results: PASS
---

### Testing file paths:

### Running install

Executing /Shared/testing/BiomarkerBenchmark_GSE30784/install.sh: Success

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

&#9989;	description.md exists.

&#9989;	config.yaml exists.

#### Results: PASS
---
### Running user scripts . . .

Executing /Shared/testing/BiomarkerBenchmark_GSE30784/install.sh: Success

Executing /Shared/testing/BiomarkerBenchmark_GSE30784/download.sh: Success

Executing /Shared/testing/BiomarkerBenchmark_GSE30784/parse.sh: Success

&#9989;	data.tsv.gz was created and zipped correctly.

&#9989;	Clinical.tsv.gz was created and zipped correctly.

#### Results: PASS
---
### Testing Test Files:

#### Running "test_Clinical.tsv"

&#9989;	"test_Clinical.tsv" has three columns with the correct headers

&#9989;	"test_Clinical.tsv" contains enough unique samples to test

&#9989;	"test_Clinical.tsv" has enough features to test (min: 1)

&#9989;	"test_Clinical.tsv" contains enough test cases (8; min: 8)

#### Running "test_data.tsv"

&#9989;	"test_data.tsv" has three columns with the correct headers

&#9989;	"test_data.tsv" contains enough unique samples to test

&#9989;	"test_data.tsv" has enough features to test (min: 1)

&#9989;	"test_data.tsv" contains enough test cases (8; min: 8)

#### Results: PASS
---
### Comparing Files:

#### Comparing "data.tsv.gz" and "test_data.tsv"


### First 5 columns and 5 rows of data.tsv.gz:

<table style="width:100%; border: 1px solid black;">
	<tr>
		<th>Sample</th>
		<th>ENSG00000000003</th>
		<th>ENSG00000000005</th>
		<th>ENSG00000000419</th>
		<th>ENSG00000000457</th>

	</tr>
	<tr>
		<td>GSM764749</td>
		<td>2.07598720058824</td>
		<td>-0.20218943375</td>
		<td>2.91173383222222</td>
		<td>0.5654668003125</td>

	</tr>
	<tr>
		<td>GSM764750</td>
		<td>1.52020662176471</td>
		<td>-0.2662692825</td>
		<td>2.55659381222222</td>
		<td>0.3702671903125</td>

	</tr>
	<tr>
		<td>GSM764751</td>
		<td>1.21595023764706</td>
		<td>-0.27813332125</td>
		<td>2.54325946222222</td>
		<td>0.452511955</td>

	</tr>
	<tr>
		<td>GSM764752</td>
		<td>1.34750764352941</td>
		<td>-0.2356730175</td>
		<td>2.54195578111111</td>
		<td>0.4074068203125</td>

	</tr>
</table>
&#9989;	First column of "data.tsv.gz" is titled "Sample"

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

#### Comparing "Clinical.tsv.gz" and "test_Clinical.tsv"


### First 5 columns and 5 rows of Clinical.tsv.gz:

<table style="width:100%; border: 1px solid black;">
	<tr>
		<th>Sample</th>
		<th>Sex</th>
		<th>age</th>
		<th>status</th>

	</tr>
	<tr>
		<td>GSM764749</td>
		<td>F</td>
		<td>40-49</td>
		<td>cancer</td>

	</tr>
	<tr>
		<td>GSM764750</td>
		<td>M</td>
		<td>40-49</td>
		<td>cancer</td>

	</tr>
	<tr>
		<td>GSM764751</td>
		<td>M</td>
		<td>50-59</td>
		<td>cancer</td>

	</tr>
	<tr>
		<td>GSM764752</td>
		<td>M</td>
		<td>60-88</td>
		<td>cancer</td>

	</tr>
</table>
&#9989;	First column of "Clinical.tsv.gz" is titled "Sample"

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

### Comparing Samples

&#9989;	Samples are the same in all data files

#### Results: PASS
---
### Testing Directory after cleanup . . .

#### Results: PASS
---
