#CCLE_mRNA_gene_kallisto_Tatlow
## Status: True
#### Date: 07/31/18
Only files in the "CCLE_mRNA_gene_kallisto_Tatlow" or "Helper" directory should be changed. The following files were also changed in this branch:
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

Executing /app/testing/CCLE_mRNA_gene_kallisto_Tatlow/install.sh: Success

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

&#9989;	description.md exists.

&#9989;	config.yaml exists.

#### Results: PASS
---
### Running user scripts . . .

Executing /app/testing/CCLE_mRNA_gene_kallisto_Tatlow/install.sh: Success

Executing /app/testing/CCLE_mRNA_gene_kallisto_Tatlow/download.sh: Success

Executing /app/testing/CCLE_mRNA_gene_kallisto_Tatlow/parse.sh: Success

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

&#9989;	"test_Clinical.tsv" contains enough test cases (20; min: 8)

#### Results: PASS
---
### Comparing Files:

#### Comparing "data.tsv.gz" and "test_data.tsv"


### First 5 columns and 5 rows of data.tsv.gz:

<table style="width:100%; border: 1px solid black;">
	<tr>
		<th>Sample</th>
		<th>ARF5</th>
		<th>M6PR</th>
		<th>ESRRA</th>
		<th>FKBP4</th>

	</tr>
	<tr>
		<td>CORL24_LUNG</td>
		<td>185.74321500000002</td>
		<td>102.68621531890001</td>
		<td>18.638011</td>
		<td>114.56292900000001</td>

	</tr>
	<tr>
		<td>HSC3_UPPER_AERODIGESTIVE_TRACT</td>
		<td>111.76097300000002</td>
		<td>137.56579900000003</td>
		<td>33.803128</td>
		<td>90.439629</td>

	</tr>
	<tr>
		<td>KMS11_HAEMATOPOIETIC_AND_LYMPHOID_TISSUE</td>
		<td>137.16564</td>
		<td>120.71723099999998</td>
		<td>23.442102999999996</td>
		<td>168.42325000000002</td>

	</tr>
	<tr>
		<td>C2BBE1_LARGE_INTESTINE</td>
		<td>230.49874299999996</td>
		<td>211.75282130402402</td>
		<td>35.42388900000001</td>
		<td>142.86827899999997</td>

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
		<th>Cell line aliases</th>
		<th>Drug__17-AAG__ActArea</th>
		<th>Drug__17-AAG__Amax</th>
		<th>Drug__17-AAG__EC50 (uM)</th>

	</tr>
	<tr>
		<td>CORL24_LUNG</td>
		<td>NA</td>
		<td>NA</td>
		<td>NA</td>
		<td>NA</td>

	</tr>
	<tr>
		<td>HSC3_UPPER_AERODIGESTIVE_TRACT</td>
		<td>NA</td>
		<td>NA</td>
		<td>NA</td>
		<td>NA</td>

	</tr>
	<tr>
		<td>KMS11_HAEMATOPOIETIC_AND_LYMPHOID_TISSUE</td>
		<td>NA</td>
		<td>5.4708</td>
		<td>-91.73921204</td>
		<td>0.031390667</td>

	</tr>
	<tr>
		<td>C2BBE1_LARGE_INTESTINE</td>
		<td>NA</td>
		<td>2.2767</td>
		<td>-73.16810608</td>
		<td>0.549149871</td>

	</tr>
</table>
&#9989;	First column of "Clinical.tsv.gz" is titled "Sample"

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 15: Success

&#9989;	Row 16: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

&#9989;	Row 9: Success

&#9989;	Row 10: Success

&#9989;	Row 11: Success

&#9989;	Row 12: Success

&#9989;	Row 13: Success

&#9989;	Row 14: Success

&#9989;	Row 17: Success

&#9989;	Row 18: Success

&#9989;	Row 19: Success

&#9989;	Row 20: Success

### Comparing Samples

&#9989;	Samples are the same in all data files

#### Results: PASS
---
### Testing Directory after cleanup . . .

#### Results: PASS
---
