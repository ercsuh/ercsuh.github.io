#GSE62944_Tumor_TPM
## Status: True
#### Date: 08/25/18
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

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

&#9989;	description.md exists.

&#9989;	config.yaml exists.

#### Results: PASS
---

### Testing gzip files:

&#9989;	Gene_Expression.tsv.gz was created and zipped correctly.

&#9989;	Clinical.tsv.gz was created and zipped correctly.

#### Results: PASS
---
### Running user scripts . . .



&#9989;	install.sh executed properly.



&#9989;	download.sh executed properly.



&#9989;	parse.sh executed properly.

#### Results: PASS
---
### Testing Files:

#### Running "/Shared/testing/GSE62944_Tumor_TPM/GSE62944_Tumor_TPM/test_Gene_Expression.tsv"

&#9989;	"test_Gene_Expression.tsv" has three columns with the correct headers

&#9989;	"test_Gene_Expression.tsv" contains enough unique samples to test

&#9989;	"test_Gene_Expression.tsv" contains enough test cases (8; min: 8)

#### Running "/Shared/testing/GSE62944_Tumor_TPM/GSE62944_Tumor_TPM/test_Clinical.tsv"

&#9989;	"test_Clinical.tsv" has three columns with the correct headers

&#9989;	"test_Clinical.tsv" contains enough unique samples to test

&#9989;	"test_Clinical.tsv" contains enough test cases (10; min: 8)

#### Results: PASS
---
### Comparing Files:

#### Comparing "Gene_Expression.tsv.gz" and "test_Gene_Expression.tsv"


### First 5 columns and 5 rows of /Shared/testing/GSE62944_Tumor_TPM/GSE62944_Tumor_TPM/Gene_Expression.tsv.gz:

<table style="width:100%; border: 1px solid black;">
	<tr align='left'>
		<th align='left'>Sample</th>
		<th align='left'>1/2-SBSRNA4</th>
		<th align='left'>A1BG</th>
		<th align='left'>A1BG-AS1</th>
		<th align='left'>A1CF</th>

	</tr>
	<tr align='left'>
		<td align='left'>TCGA-02-0047-01A-01R-1849-01</td>
		<td align='left'>2.34180779897709</td>
		<td align='left'>11.7173931223676</td>
		<td align='left'>1.33274150888264</td>
		<td align='left'>0.00783961263378836</td>

	</tr>
	<tr align='left'>
		<td align='left'>TCGA-02-0055-01A-01R-1849-01</td>
		<td align='left'>1.64575215578575</td>
		<td align='left'>24.7763572132346</td>
		<td align='left'>1.08603706301478</td>
		<td align='left'>0.015495311808889</td>

	</tr>
	<tr align='left'>
		<td align='left'>TCGA-02-2483-01A-01R-1849-01</td>
		<td align='left'>2.43263380829254</td>
		<td align='left'>20.2648719245462</td>
		<td align='left'>1.09297209133143</td>
		<td align='left'>0.00479039331850954</td>

	</tr>
	<tr align='left'>
		<td align='left'>TCGA-02-2485-01A-01R-1849-01</td>
		<td align='left'>2.04036406475485</td>
		<td align='left'>5.1177123833555</td>
		<td align='left'>0.707189363771972</td>
		<td align='left'>0.00585469442145148</td>

	</tr>
</table>
&#9989;	First column of "Gene_Expression.tsv.gz" is titled "Sample"

&#9989;	Success: The value (2.34180779897709) for the "1/2-SBSRNA4" variable in Gene_Expression.tsv.gz matches the test value (2.34180779897709) for TCGA-02-0047-01A-01R-1849-01.

&#9989;	Success: The value (0.053474351315225) for the "tAKR" variable in Gene_Expression.tsv.gz matches the test value (0.053474351315225) for TCGA-02-0047-01A-01R-1849-01.

&#9989;	Success: The value (1.64575215578575) for the "1/2-SBSRNA4" variable in Gene_Expression.tsv.gz matches the test value (1.64575215578575) for TCGA-02-0055-01A-01R-1849-01.

&#9989;	Success: The value (0.0352314068782874) for the "tAKR" variable in Gene_Expression.tsv.gz matches the test value (0.0352314068782874) for TCGA-02-0055-01A-01R-1849-01.

&#9989;	Success: The value (0.509342962675824) for the "1/2-SBSRNA4" variable in Gene_Expression.tsv.gz matches the test value (0.509342962675824) for TCGA-ZS-A9CG-01A-11R-A37K-07.

&#9989;	Success: The value (8.91331954798559) for the "tAKR" variable in Gene_Expression.tsv.gz matches the test value (8.91331954798559) for TCGA-ZS-A9CG-01A-11R-A37K-07.

&#9989;	Success: The value (1.48192576535246) for the "1/2-SBSRNA4" variable in Gene_Expression.tsv.gz matches the test value (1.48192576535246) for TCGA-ZX-AA5X-01A-11R-A42T-07.

&#9989;	Success: The value (0.0676784995200338) for the "tAKR" variable in Gene_Expression.tsv.gz matches the test value (0.0676784995200338) for TCGA-ZX-AA5X-01A-11R-A42T-07.

#### Comparing "Clinical.tsv.gz" and "test_Clinical.tsv"


### First 5 columns and 5 rows of /Shared/testing/GSE62944_Tumor_TPM/GSE62944_Tumor_TPM/Clinical.tsv.gz:

<table style="width:100%; border: 1px solid black;">
	<tr align='left'>
		<th align='left'>Sample</th>
		<th align='left'>Cancer Type</th>
		<th align='left'>ablation_embolization_tx_adjuvant</th>
		<th align='left'>abnormal_lymphocyte_percent</th>
		<th align='left'>age_at_diagnosis</th>

	</tr>
	<tr align='left'>
		<td align='left'>TCGA-G9-A9S0-01A-11R-A41O-07</td>
		<td align='left'>Prostate adenocarcinoma</td>
		<td align='left'>NA</td>
		<td align='left'>NA</td>
		<td align='left'>NA</td>

	</tr>
	<tr align='left'>
		<td align='left'>TCGA-E1-5318-01A-01R-1470-07</td>
		<td align='left'>Brain Lower Grade Glioma</td>
		<td align='left'>NA</td>
		<td align='left'>NA</td>
		<td align='left'>NA</td>

	</tr>
	<tr align='left'>
		<td align='left'>TCGA-25-1625-01A-01R-1566-13</td>
		<td align='left'>Ovarian serous cystadenocarcinoma</td>
		<td align='left'>NA</td>
		<td align='left'>NA</td>
		<td align='left'>NA</td>

	</tr>
	<tr align='left'>
		<td align='left'>TCGA-A2-A0T1-01A-21R-A084-07</td>
		<td align='left'>Breast invasive carcinoma</td>
		<td align='left'>NA</td>
		<td align='left'>NA</td>
		<td align='left'>55</td>

	</tr>
</table>
&#9989;	First column of "Clinical.tsv.gz" is titled "Sample"

&#9989;	Success: The value (Prostate adenocarcinoma) for the "Cancer Type" variable in Clinical.tsv.gz matches the test value (Prostate adenocarcinoma) for TCGA-G9-A9S0-01A-11R-A41O-07.

&#9989;	Success: The value (429) for the "days_to_biochemical_recurrence_first" variable in Clinical.tsv.gz matches the test value (429) for TCGA-G9-A9S0-01A-11R-A41O-07.

&#9989;	Success: The value (2014-6-17) for the "form_completion_date" variable in Clinical.tsv.gz matches the test value (2014-6-17) for TCGA-G9-A9S0-01A-11R-A41O-07.

&#9989;	Success: The value (Cervical squamous cell carcinoma and endocervical adenocarcinoma) for the "Cancer Type" variable in Clinical.tsv.gz matches the test value (Cervical squamous cell carcinoma and endocervical adenocarcinoma) for TCGA-ZX-AA5X-01A-11R-A42T-07.

&#9989;	Success: The value (NA) for the "tumor_response" variable in Clinical.tsv.gz matches the test value (NA) for TCGA-ZX-AA5X-01A-11R-A42T-07.

&#9989;	Success: The value (Glioblastoma multiforme) for the "Cancer Type" variable in Clinical.tsv.gz matches the test value (Glioblastoma multiforme) for TCGA-02-0047-01A-01R-1849-01.

&#9989;	Success: The value (NO) for the "history_lgg_dx_of_brain_tissue" variable in Clinical.tsv.gz matches the test value (NO) for TCGA-02-0047-01A-01R-1849-01.

&#9989;	Success: The value (Uterine Corpus Endometrial Carcinoma) for the "Cancer Type" variable in Clinical.tsv.gz matches the test value (Uterine Corpus Endometrial Carcinoma) for TCGA-A5-A0VQ-01A-11R-A104-07.

&#9989;	Success: The value (2010-11-15) for the "form_completion_date" variable in Clinical.tsv.gz matches the test value (2010-11-15) for TCGA-A5-A0VQ-01A-11R-A104-07.

&#9989;	Success: The value (0) for the "lymph_nodes_aortic_pos_total" variable in Clinical.tsv.gz matches the test value (0) for TCGA-A5-A0VQ-01A-11R-A104-07.

#### Results: PASS
---
