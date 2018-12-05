#BiomarkerBenchmark_GSE4271
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

Executing /Shared/testing/BiomarkerBenchmark_GSE4271/install.sh: Success

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

&#9989;	description.md exists.

&#9989;	config.yaml exists.

#### Results: PASS
---
### Running user scripts . . .

Executing /Shared/testing/BiomarkerBenchmark_GSE4271/install.sh: Success

Executing /Shared/testing/BiomarkerBenchmark_GSE4271/download.sh: Success

Executing /Shared/testing/BiomarkerBenchmark_GSE4271/parse.sh: Success

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
		<td>GSM96950</td>
		<td>1.69214850411765</td>
		<td>-0.14303780375</td>
		<td>1.56810911555556</td>
		<td>0.0430233856521739</td>

	</tr>
	<tr>
		<td>GSM96952</td>
		<td>1.17177955470588</td>
		<td>-0.2111959625</td>
		<td>1.25885920888889</td>
		<td>-0.0729167382608696</td>

	</tr>
	<tr>
		<td>GSM96954</td>
		<td>1.09448393705882</td>
		<td>-0.25773861375</td>
		<td>1.16117150111111</td>
		<td>0.248244886521739</td>

	</tr>
	<tr>
		<td>GSM96956</td>
		<td>0.938071818823529</td>
		<td>-0.25361511</td>
		<td>1.38457541777778</td>
		<td>0.00498863347826087</td>

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
		<th>censor</th>
		<th>matching_sample</th>

	</tr>
	<tr>
		<td>GSM96950</td>
		<td>M</td>
		<td>60</td>
		<td>no</td>
		<td>PRB3777 (HG-U133A)</td>

	</tr>
	<tr>
		<td>GSM96951</td>
		<td>F</td>
		<td>48</td>
		<td>no</td>
		<td>NA</td>

	</tr>
	<tr>
		<td>GSM96952</td>
		<td>M</td>
		<td>43</td>
		<td>no</td>
		<td>PRB3785 (HG-U133A)</td>

	</tr>
	<tr>
		<td>GSM96953</td>
		<td>M</td>
		<td>38</td>
		<td>no</td>
		<td>NA</td>

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
