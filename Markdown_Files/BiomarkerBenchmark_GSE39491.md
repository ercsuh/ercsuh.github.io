#BiomarkerBenchmark_GSE39491
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

Executing /Shared/testing/BiomarkerBenchmark_GSE39491/install.sh: Success

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

&#9989;	description.md exists.

&#9989;	config.yaml exists.

#### Results: PASS
---
### Running user scripts . . .

Executing /Shared/testing/BiomarkerBenchmark_GSE39491/install.sh: Success

Executing /Shared/testing/BiomarkerBenchmark_GSE39491/download.sh: Success

Executing /Shared/testing/BiomarkerBenchmark_GSE39491/parse.sh: Success

&#9989;	data.tsv.gz was created and zipped correctly.

&#9989;	Clinical.tsv.gz was created and zipped correctly.

#### Results: PASS
---
### Testing Test Files:

#### Running "test_Clinical.tsv"

&#9989;	"test_Clinical.tsv" has three columns with the correct headers

&#9989;	"test_Clinical.tsv" contains enough unique samples to test

&#10060;	Sample "GSM969967" does not have enough features to test (min: 2)

&#10060;	Sample "GSM969968" does not have enough features to test (min: 2)

&#10060;	Sample "GSM969969" does not have enough features to test (min: 2)

&#10060;	Sample "GSM969970" does not have enough features to test (min: 2)

&#10060;	Sample "GSM970165" does not have enough features to test (min: 2)

&#10060;	Sample "GSM970171" does not have enough features to test (min: 2)

&#10060;	Sample "GSM970172" does not have enough features to test (min: 2)

&#10060;	Sample "GSM970173" does not have enough features to test (min: 2)

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
		<td>GSM969967</td>
		<td>0.759423532941176</td>
		<td>-0.13312531875</td>
		<td>2.15413860222222</td>
		<td>0.317525506086957</td>

	</tr>
	<tr>
		<td>GSM969968</td>
		<td>1.17060186294118</td>
		<td>-0.20801410125</td>
		<td>1.57464724222222</td>
		<td>0.321630730434783</td>

	</tr>
	<tr>
		<td>GSM969969</td>
		<td>2.52226859470588</td>
		<td>-0.13015529125</td>
		<td>1.59645342333333</td>
		<td>0.0990446852173913</td>

	</tr>
	<tr>
		<td>GSM969970</td>
		<td>1.15890751352941</td>
		<td>-0.2273869175</td>
		<td>1.22849183444444</td>
		<td>0.0270785452173913</td>

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
		<th>cell_type</th>

	</tr>
	<tr>
		<td>GSM969967</td>
		<td>NC</td>

	</tr>
	<tr>
		<td>GSM969968</td>
		<td>BE</td>

	</tr>
	<tr>
		<td>GSM969969</td>
		<td>NE</td>

	</tr>
	<tr>
		<td>GSM969970</td>
		<td>NC</td>

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
