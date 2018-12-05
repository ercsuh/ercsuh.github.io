# LINCS_PhaseII_Level4
## Status: True
#### Date: 08/27/18
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

&#9989;	Metadata.tsv.gz was created and zipped correctly.

#### Results: PASS
---
### Running user scripts . . .



&#9989;	install.sh executed properly.



&#9989;	download.sh executed properly.



&#9989;	parse.sh executed properly.

#### Results: PASS
---
### Testing Files:

#### Running "/Shared/testing/LINCS_PhaseII_Level4/LINCS_PhaseII_Level4/test_Metadata.tsv"

&#9989;	"test_Metadata.tsv" has three columns with the correct headers

&#9989;	"test_Metadata.tsv" contains enough unique samples to test

&#9989;	"test_Metadata.tsv" contains enough test cases (15; min: 8)

#### Running "/Shared/testing/LINCS_PhaseII_Level4/LINCS_PhaseII_Level4/test_Gene_Expression.tsv"

&#9989;	"test_Gene_Expression.tsv" has three columns with the correct headers

&#9989;	"test_Gene_Expression.tsv" contains enough unique samples to test

&#9989;	"test_Gene_Expression.tsv" contains enough test cases (12; min: 8)

#### Results: PASS
---
### Comparing Files:

#### Comparing "Gene_Expression.tsv.gz" and "test_Gene_Expression.tsv"


### First 5 columns and 5 rows of /Shared/testing/LINCS_PhaseII_Level4/LINCS_PhaseII_Level4/Gene_Expression.tsv.gz:

<table style="width:100%; border: 1px solid black;">
	<tr align='left'>
		<th align='left'>Sample</th>
		<th align='left'>DDR1</th>
		<th align='left'>PAX8</th>
		<th align='left'>GUCA1A</th>
		<th align='left'>EPHB3</th>

	</tr>
	<tr align='left'>
		<td align='left'>REP.A001_A375_24H_X1_B22:A03</td>
		<td align='left'>14.8204</td>
		<td align='left'>0.0</td>
		<td align='left'>-1.332</td>
		<td align='left'>1.4469</td>

	</tr>
	<tr align='left'>
		<td align='left'>REP.A001_A375_24H_X1_B22:A04</td>
		<td align='left'>-0.52</td>
		<td align='left'>4.3134</td>
		<td align='left'>-1.821</td>
		<td align='left'>-1.3211</td>

	</tr>
	<tr align='left'>
		<td align='left'>REP.A001_A375_24H_X1_B22:A05</td>
		<td align='left'>-1.0369</td>
		<td align='left'>-1.1246</td>
		<td align='left'>0.8054</td>
		<td align='left'>-0.7457</td>

	</tr>
	<tr align='left'>
		<td align='left'>REP.A001_A375_24H_X1_B22:A06</td>
		<td align='left'>-0.3005</td>
		<td align='left'>-0.467</td>
		<td align='left'>-0.4439</td>
		<td align='left'>-0.7768</td>

	</tr>
</table>
&#9989;	First column of "Gene_Expression.tsv.gz" is titled "Sample"

&#9989;	Success: The value (-0.4007) for the "ACTB" variable in Gene_Expression.tsv.gz matches the test value (-0.4007) for REP.A028_YAPC_24H_X1_B25:G09.

&#9989;	Success: The value (-0.5475) for the "DDR1" variable in Gene_Expression.tsv.gz matches the test value (-0.5475) for REP.A028_YAPC_24H_X1_B25:G09.

&#9989;	Success: The value (0.3173) for the "ACTB" variable in Gene_Expression.tsv.gz matches the test value (0.3173) for REP.A028_YAPC_24H_X3_B25:B12.

&#9989;	Success: The value (-0.0078) for the "DDR1" variable in Gene_Expression.tsv.gz matches the test value (-0.0078) for REP.A028_YAPC_24H_X3_B25:B12.

&#9989;	Success: The value (0.8233) for the "ACTB" variable in Gene_Expression.tsv.gz matches the test value (0.8233) for LJP005_A375_24H_X1_B19:A03.

&#9989;	Success: The value (-0.3186) for the "DDR1" variable in Gene_Expression.tsv.gz matches the test value (-0.3186) for LJP005_A375_24H_X1_B19:A03.

&#9989;	Success: The value (-1.1757) for the "ACTB" variable in Gene_Expression.tsv.gz matches the test value (-1.1757) for LJP006_A375_24H_X1_B19:L06.

&#9989;	Success: The value (-0.3564) for the "DDR1" variable in Gene_Expression.tsv.gz matches the test value (-0.3564) for LJP006_A375_24H_X1_B19:L06.

&#9989;	Success: The value (0.2358) for the "ACTB" variable in Gene_Expression.tsv.gz matches the test value (0.2358) for LJP006_A549_24H_X2_B19:J22.

&#9989;	Success: The value (-0.0797) for the "DDR1" variable in Gene_Expression.tsv.gz matches the test value (-0.0797) for LJP006_A549_24H_X2_B19:J22.

&#9989;	Success: The value (0.9876) for the "ACTB" variable in Gene_Expression.tsv.gz matches the test value (0.9876) for LJP009_PC3_24H_X2_B20:O08.

&#9989;	Success: The value (-0.323) for the "DDR1" variable in Gene_Expression.tsv.gz matches the test value (-0.323) for LJP009_PC3_24H_X2_B20:O08.

#### Comparing "Metadata.tsv.gz" and "test_Metadata.tsv"


### First 5 columns and 5 rows of /Shared/testing/LINCS_PhaseII_Level4/LINCS_PhaseII_Level4/Metadata.tsv.gz:

<table style="width:100%; border: 1px solid black;">
	<tr align='left'>
		<th align='left'>Sample</th>
		<th align='left'>base_cell_id</th>
		<th align='left'>canonical_smiles</th>
		<th align='left'>cell_id</th>
		<th align='left'>cell_type</th>

	</tr>
	<tr align='left'>
		<td align='left'>LJP005_A375_24H_X1_B19:A03</td>
		<td align='left'>A375</td>
		<td align='left'>CS(=O)C</td>
		<td align='left'>A375</td>
		<td align='left'>cell line</td>

	</tr>
	<tr align='left'>
		<td align='left'>LPROT001_A375_6H_X1_B20:B03</td>
		<td align='left'>A375</td>
		<td align='left'>CS(=O)C</td>
		<td align='left'>A375</td>
		<td align='left'>cell line</td>

	</tr>
	<tr align='left'>
		<td align='left'>LPROT001_A375_6H_X1_B20:B05</td>
		<td align='left'>A375</td>
		<td align='left'>CS(=O)C</td>
		<td align='left'>A375</td>
		<td align='left'>cell line</td>

	</tr>
	<tr align='left'>
		<td align='left'>LPROT002_A375_6H_X1_B22:B03</td>
		<td align='left'>A375</td>
		<td align='left'>CS(=O)C</td>
		<td align='left'>A375</td>
		<td align='left'>cell line</td>

	</tr>
</table>
&#9989;	First column of "Metadata.tsv.gz" is titled "Sample"

&#9989;	Success: The value (CS(=O)C) for the "canonical_smiles" variable in Metadata.tsv.gz matches the test value (CS(=O)C) for LJP005_A375_24H_X1_B19:A03.

&#9989;	Success: The value (A375) for the "cell_id" variable in Metadata.tsv.gz matches the test value (A375) for LJP005_A375_24H_X1_B19:A03.

&#9989;	Success: The value (cell line) for the "cell_type" variable in Metadata.tsv.gz matches the test value (cell line) for LJP005_A375_24H_X1_B19:A03.

&#9989;	Success: The value (LJP005_A375_24H_X1_B19) for the "det_plate" variable in Metadata.tsv.gz matches the test value (LJP005_A375_24H_X1_B19) for LJP005_A375_24H_X1_B19:A03.

&#9989;	Success: The value (F) for the "donor_sex" variable in Metadata.tsv.gz matches the test value (F) for LJP005_A375_24H_X1_B19:A03.

&#9989;	Success: The value (IAZDPXIOMUYVGZ-UHFFFAOYSA-N) for the "inchi_key" variable in Metadata.tsv.gz matches the test value (IAZDPXIOMUYVGZ-UHFFFAOYSA-N) for LJP005_A375_24H_X1_B19:A03.

&#9989;	Success: The value (DMSO) for the "pert_id" variable in Metadata.tsv.gz matches the test value (DMSO) for LJP005_A375_24H_X1_B19:A03.

&#9989;	Success: The value (DMSO) for the "pert_iname" variable in Metadata.tsv.gz matches the test value (DMSO) for LJP005_A375_24H_X1_B19:A03.

&#9989;	Success: The value (YAPC) for the "cell_id" variable in Metadata.tsv.gz matches the test value (YAPC) for REP.A028_YAPC_24H_X3_B25:P24.

&#9989;	Success: The value (cell line) for the "cell_type" variable in Metadata.tsv.gz matches the test value (cell line) for REP.A028_YAPC_24H_X3_B25:P24.

&#9989;	Success: The value (REP.A028_YAPC_24H_X3_B25) for the "det_plate" variable in Metadata.tsv.gz matches the test value (REP.A028_YAPC_24H_X3_B25) for REP.A028_YAPC_24H_X3_B25:P24.

&#9989;	Success: The value (M) for the "donor_sex" variable in Metadata.tsv.gz matches the test value (M) for REP.A028_YAPC_24H_X3_B25:P24.

&#9989;	Success: The value (FMCRMSOQAVOHRD-SBGISONWSA-M) for the "inchi_key" variable in Metadata.tsv.gz matches the test value (FMCRMSOQAVOHRD-SBGISONWSA-M) for REP.A028_YAPC_24H_X3_B25:P24.

&#9989;	Success: The value (BRD-A97502381) for the "pert_id" variable in Metadata.tsv.gz matches the test value (BRD-A97502381) for REP.A028_YAPC_24H_X3_B25:P24.

&#9989;	Success: The value (cyanocobalamin) for the "pert_iname" variable in Metadata.tsv.gz matches the test value (cyanocobalamin) for REP.A028_YAPC_24H_X3_B25:P24.

#### Results: PASS
---
