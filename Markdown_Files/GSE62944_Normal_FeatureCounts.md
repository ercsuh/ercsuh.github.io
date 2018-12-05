# GSE62944_Normal_FeatureCounts
## Status: True
#### Date: 08/17/18
Only files in the "GSE62944_Normal_FeatureCounts" or "Helper" directory should be changed. The following files were also changed in this branch:
- BiomarkerBenchmark_GSE10320/install.sh
- BiomarkerBenchmark_GSE10320/test_Clinical.tsv
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

Executing /Shared/testing/GSE62944_Normal_FeatureCounts/install.sh: Success

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

&#9989;	description.md exists.

&#9989;	config.yaml exists.

#### Results: PASS
---
### Running user scripts . . .

Executing /Shared/testing/GSE62944_Normal_FeatureCounts/install.sh: Success

Executing /Shared/testing/GSE62944_Normal_FeatureCounts/download.sh: Success

Executing /Shared/testing/GSE62944_Normal_FeatureCounts/parse.sh: Success

&#9989;	data.tsv.gz was created and zipped correctly.

&#9989;	Clinical.tsv.gz was created and zipped correctly.

#### Results: PASS
---
### Testing Test Files:

#### Running "test_Clinical.tsv"

&#9989;	"test_Clinical.tsv" has three columns with the correct headers

&#9989;	"test_Clinical.tsv" contains enough unique samples to test

&#10060;	Sample "TCGA-K4-A3WV-11A-21R-A22U-07" does not have enough features to test (min: 2)

&#10060;	Sample "TCGA-49-6742-11A-01R-1858-07" does not have enough features to test (min: 2)

&#10060;	Sample "TCGA-DD-A3A2-11A-11R-A213-07" does not have enough features to test (min: 2)

&#10060;	Sample "TCGA-BH-A0DV-11A-22R-A12P-07" does not have enough features to test (min: 2)

&#10060;	Sample "TCGA-GE-A2C6-11A-11R-A16R-07" does not have enough features to test (min: 2)

&#10060;	Sample "TCGA-56-7730-11A-01R-2125-07" does not have enough features to test (min: 2)

&#10060;	Sample "TCGA-BH-A0H5-11A-62R-A115-07" does not have enough features to test (min: 2)

&#10060;	Sample "TCGA-22-5489-11A-01R-1635-07" does not have enough features to test (min: 2)

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
		<th>1/2-SBSRNA4</th>
		<th>A1BG</th>
		<th>A1BG-AS1</th>
		<th>A1CF</th>

	</tr>
	<tr>
		<td>TCGA-06-0675-11A-32R-A36H-07</td>
		<td>48</td>
		<td>206</td>
		<td>87</td>
		<td>8</td>

	</tr>
	<tr>
		<td>TCGA-06-0678-11A-32R-A36H-07</td>
		<td>25</td>
		<td>112</td>
		<td>44</td>
		<td>2</td>

	</tr>
	<tr>
		<td>TCGA-06-0680-11A-32R-A36H-07</td>
		<td>36</td>
		<td>223</td>
		<td>122</td>
		<td>5</td>

	</tr>
	<tr>
		<td>TCGA-06-0681-11A-41R-A36H-07</td>
		<td>28</td>
		<td>361</td>
		<td>120</td>
		<td>1</td>

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
		<th>Cancer_Type</th>

	</tr>
	<tr>
		<td>TCGA-06-0675-11A-32R-A36H-07</td>
		<td>Glioblastoma multiforme</td>

	</tr>
	<tr>
		<td>TCGA-06-0678-11A-32R-A36H-07</td>
		<td>Glioblastoma multiforme</td>

	</tr>
	<tr>
		<td>TCGA-06-0680-11A-32R-A36H-07</td>
		<td>Glioblastoma multiforme</td>

	</tr>
	<tr>
		<td>TCGA-06-0681-11A-41R-A36H-07</td>
		<td>Glioblastoma multiforme</td>

	</tr>
</table>
&#9989;	First column of "Clinical.tsv.gz" is titled "Sample"

&#9989;	Row 8: Success

&#9989;	Row 2: Success

&#9989;	Row 6: Success

&#9989;	Row 4: Success

&#9989;	Row 7: Success

&#9989;	Row 3: Success

&#9989;	Row 5: Success

&#9989;	Row 1: Success

### Comparing Samples

&#9989;	Samples are the same in all data files

#### Results: PASS
---
### Testing Directory after cleanup . . .

#### Results: PASS
---
