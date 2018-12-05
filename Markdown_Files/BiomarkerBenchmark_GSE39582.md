# BiomarkerBenchmark_GSE39582
## Status: True
#### Date: 07/31/18
Only files in the "BiomarkerBenchmark_GSE39582" or "Helper" directory should be changed. The following files were also changed in this branch:
- GSE62944_Tumor_TPM/cleanup.sh
- GSE62944_Tumor_TPM/parse.py
- GSE62944_Tumor_TPM/parse.sh
- GSE62944_Tumor_TPM/scrapeWebTCGA.R
- GSE62944_Tumor_TPM/translate.py
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

Executing /app/testing/BiomarkerBenchmark_GSE39582/install.sh: Success

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

&#9989;	description.md exists.

&#9989;	config.yaml exists.

#### Results: PASS
---
### Running user scripts . . .

Executing /app/testing/BiomarkerBenchmark_GSE39582/install.sh: Success

Executing /app/testing/BiomarkerBenchmark_GSE39582/download.sh: Success

Executing /app/testing/BiomarkerBenchmark_GSE39582/parse.sh: Success

&#9989;	data.tsv.gz was created and zipped correctly.

&#9989;	Clinical.tsv.gz was created and zipped correctly.

#### Results: PASS
---
### Testing Test Files:

#### Running "test_data.tsv"

&#9989;	"test_data.tsv" has three columns with the correct headers

&#9989;	"test_data.tsv" contains enough unique samples to test

&#9989;	"test_data.tsv" has enough features to test (min: 1)

&#9989;	"test_data.tsv" contains enough test cases (8; min: 8)

#### Running "test_Clinical.tsv"

&#9989;	"test_Clinical.tsv" has three columns with the correct headers

&#9989;	"test_Clinical.tsv" contains enough unique samples to test

&#9989;	"test_Clinical.tsv" has enough features to test (min: 1)

&#9989;	"test_Clinical.tsv" contains enough test cases (8; min: 8)

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
		<td>GSM971957</td>
		<td>2.11019764117647</td>
		<td>0.29710354625</td>
		<td>2.54086968444444</td>
		<td>0.8408434203125</td>

	</tr>
	<tr>
		<td>GSM971958</td>
		<td>2.69180617705882</td>
		<td>0.03353052625</td>
		<td>2.76094172666667</td>
		<td>0.444017269375</td>

	</tr>
	<tr>
		<td>GSM971959</td>
		<td>2.30993825352941</td>
		<td>-0.148700045</td>
		<td>2.49540275111111</td>
		<td>0.3675600628125</td>

	</tr>
	<tr>
		<td>GSM971960</td>
		<td>3.40408548235294</td>
		<td>0.2708252125</td>
		<td>2.63223672333333</td>
		<td>0.6184695296875</td>

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
		<th>age.at.diagnosis_year</th>
		<th>braf.mutation</th>
		<th>chemotherapy.adjuvant</th>

	</tr>
	<tr>
		<td>GSM971957</td>
		<td>Male</td>
		<td>34.5</td>
		<td>WT</td>
		<td>N</td>

	</tr>
	<tr>
		<td>GSM971958</td>
		<td>Female</td>
		<td>36.4</td>
		<td>WT</td>
		<td>N</td>

	</tr>
	<tr>
		<td>GSM971959</td>
		<td>Male</td>
		<td>36.9</td>
		<td>WT</td>
		<td>N</td>

	</tr>
	<tr>
		<td>GSM971960</td>
		<td>Female</td>
		<td>38.2</td>
		<td>WT</td>
		<td>N</td>

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
