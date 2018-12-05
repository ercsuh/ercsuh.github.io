# ICGC_BRCA-US_exp_seq
## Status: True
#### Date: 08/17/18
Only files in the "ICGC_BRCA-US_exp_seq" or "Helper" directory should be changed. The following files were also changed in this branch:
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

Executing /Shared/testing/ICGC_BRCA-US_exp_seq/install.sh: Success

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

&#9989;	description.md exists.

&#9989;	config.yaml exists.

#### Results: PASS
---
### Running user scripts . . .

Executing /Shared/testing/ICGC_BRCA-US_exp_seq/install.sh: Success

Executing /Shared/testing/ICGC_BRCA-US_exp_seq/download.sh: Success

Executing /Shared/testing/ICGC_BRCA-US_exp_seq/parse.sh: Success

&#9989;	data.tsv.gz was created and zipped correctly.

&#9989;	Clinical.tsv.gz was created and zipped correctly.

#### Results: PASS
---
### Testing Test Files:

#### Running "test_Clinical.tsv"

&#9989;	"test_Clinical.tsv" has three columns with the correct headers

&#9989;	"test_Clinical.tsv" contains enough unique samples to test

&#9989;	"test_Clinical.tsv" has enough features to test (min: 1)

&#9989;	"test_Clinical.tsv" contains enough test cases (9; min: 8)

#### Running "test_data.tsv"

&#9989;	"test_data.tsv" has three columns with the correct headers

&#9989;	"test_data.tsv" contains enough unique samples to test

&#9989;	"test_data.tsv" has enough features to test (min: 1)

&#9989;	"test_data.tsv" contains enough test cases (9; min: 8)

#### Results: PASS
---
### Comparing Files:

#### Comparing "data.tsv.gz" and "test_data.tsv"


### First 5 columns and 5 rows of data.tsv.gz:

<table style="width:100%; border: 1px solid black;">
	<tr>
		<th>Sample</th>
		<th>A1BG</th>
		<th>A1CF</th>
		<th>A2BP1</th>
		<th>A2LD1</th>

	</tr>
	<tr>
		<td>DO1249</td>
		<td>644</td>
		<td>0</td>
		<td>0</td>
		<td>144</td>

	</tr>
	<tr>
		<td>DO1250</td>
		<td>514</td>
		<td>0</td>
		<td>0</td>
		<td>87</td>

	</tr>
	<tr>
		<td>DO1251</td>
		<td>541</td>
		<td>0</td>
		<td>4</td>
		<td>451</td>

	</tr>
	<tr>
		<td>DO1252</td>
		<td>467</td>
		<td>0</td>
		<td>0</td>
		<td>184</td>

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

&#9989;	Row 9: Success

#### Comparing "Clinical.tsv.gz" and "test_Clinical.tsv"


### First 5 columns and 5 rows of Clinical.tsv.gz:

<table style="width:100%; border: 1px solid black;">
	<tr>
		<th>Sample</th>
		<th>TCGA_ID</th>
		<th>age_at_diagnosis</th>
		<th>age_at_last_followup</th>
		<th>disease_status_last_followup</th>

	</tr>
	<tr>
		<td>DO1808</td>
		<td>TCGA-E2-A15C</td>
		<td>61</td>
		<td>62</td>
		<td>complete remission</td>

	</tr>
	<tr>
		<td>DO1802</td>
		<td>TCGA-AR-A250</td>
		<td>58</td>
		<td>62</td>
		<td>complete remission</td>

	</tr>
	<tr>
		<td>DO1842</td>
		<td>TCGA-A2-A0YM</td>
		<td>67</td>
		<td>68</td>
		<td>complete remission</td>

	</tr>
	<tr>
		<td>DO1848</td>
		<td>TCGA-AR-A1AS</td>
		<td>54</td>
		<td>57</td>
		<td>NA</td>

	</tr>
</table>
&#9989;	First column of "Clinical.tsv.gz" is titled "Sample"

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

&#9989;	Row 9: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

### Comparing Samples

&#9989;	Samples are the same in all data files

#### Results: PASS
---
### Testing Directory after cleanup . . .

#### Results: PASS
---
