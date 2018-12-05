#BiomarkerBenchmark_GSE2109_Prostate
## Status: True
#### Date: 07/31/18
Only files in the "BiomarkerBenchmark_GSE2109_Prostate" or "Helper" directory should be changed. The following files were also changed in this branch:
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

Executing /app/testing/BiomarkerBenchmark_GSE2109_Prostate/install.sh: Success

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

&#9989;	description.md exists.

&#9989;	config.yaml exists.

#### Results: PASS
---
### Running user scripts . . .

Executing /app/testing/BiomarkerBenchmark_GSE2109_Prostate/install.sh: Success

Executing /app/testing/BiomarkerBenchmark_GSE2109_Prostate/download.sh: Success

Executing /app/testing/BiomarkerBenchmark_GSE2109_Prostate/parse.sh: Success

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
		<td>GSM38079</td>
		<td>1.88023305705882</td>
		<td>-0.27722608</td>
		<td>1.88733032333333</td>
		<td>0.3769980525</td>

	</tr>
	<tr>
		<td>GSM46837</td>
		<td>1.49190971470588</td>
		<td>-0.2337158125</td>
		<td>2.36947264444444</td>
		<td>1.4301921496875</td>

	</tr>
	<tr>
		<td>GSM46866</td>
		<td>2.06201953529412</td>
		<td>-0.19376123625</td>
		<td>2.22562798</td>
		<td>0.5496713615625</td>

	</tr>
	<tr>
		<td>GSM53061</td>
		<td>1.46081964764706</td>
		<td>-0.1735639225</td>
		<td>1.92268529666667</td>
		<td>0.2441607125</td>

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
		<th>Alcohol_Consumption</th>
		<th>Cancer_discovered_by_digital_exam</th>
		<th>Clinical_Gleason_Score</th>
		<th>Clinical_Grade</th>

	</tr>
	<tr>
		<td>GSM38079</td>
		<td>Yes</td>
		<td>Yes</td>
		<td>NA</td>
		<td>NA</td>

	</tr>
	<tr>
		<td>GSM46837</td>
		<td>Yes</td>
		<td>Yes</td>
		<td>NA</td>
		<td>NA</td>

	</tr>
	<tr>
		<td>GSM46866</td>
		<td>Yes</td>
		<td>NA</td>
		<td>NA</td>
		<td>NA</td>

	</tr>
	<tr>
		<td>GSM53061</td>
		<td>Yes</td>
		<td>Yes</td>
		<td>NA</td>
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
