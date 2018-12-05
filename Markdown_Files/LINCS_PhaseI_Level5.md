# LINCS_PhaseI_Level5
## Status: True
#### Date: 10/03/18
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

### Testing tsv files:

#### Results: PASS
---
### Running user scripts . . .



&#9989;	install.sh executed properly.



&#9989;	download.sh executed properly.



&#9989;	parse.sh executed properly.

#### Results: PASS
---
### Testing files:

### Comparing Files:

#### Comparing "Gene_Expression.tsv" and "test_Gene_Expression.tsv"


### First 5 columns and 5 rows of /Shared/testing/LINCS_PhaseI_Level5/LINCS_PhaseI_Level5/Gene_Expression.tsv:

<table style="width:100%; border: 1px solid black;">
	<tr align='left'>
		<th align='left'>Sample</th>
		<th align='left'>PSME1</th>
		<th align='left'>ATF1</th>
		<th align='left'>RHEB</th>
		<th align='left'>FOXO3</th>

	</tr>
	<tr align='left'>
		<td align='left'>CPC005_A375_6H:BRD-A85280935-003-01-7:10</td>
		<td align='left'>0.77376896</td>
		<td align='left'>-0.81846803</td>
		<td align='left'>0.18957229</td>
		<td align='left'>-0.14603077</td>

	</tr>
	<tr align='left'>
		<td align='left'>CPC005_A375_6H:BRD-A07824748-001-02-6:10</td>
		<td align='left'>-0.64558613</td>
		<td align='left'>-0.8107487</td>
		<td align='left'>0.45906025</td>
		<td align='left'>-0.22467646</td>

	</tr>
	<tr align='left'>
		<td align='left'>CPC004_A375_6H:BRD-K20482099-001-01-1:10</td>
		<td align='left'>-5.4496655</td>
		<td align='left'>2.393775</td>
		<td align='left'>1.2797899</td>
		<td align='left'>2.167868</td>

	</tr>
	<tr align='left'>
		<td align='left'>CPC005_A375_6H:BRD-K62929068-001-03-3:10</td>
		<td align='left'>0.19340771</td>
		<td align='left'>-0.58224326</td>
		<td align='left'>-0.17897698</td>
		<td align='left'>-1.1820246</td>

	</tr>
</table>
&#9989;	First column of "Gene_Expression.tsv" is titled "Sample"

&#9989;	Success: The value (0.4717968) for the "ACTB" variable in Gene_Expression.tsv matches the test value (0.4717968) for CPC009_PC3_6H:BRD-A05565054-001-01-7:10.

&#9989;	Success: The value (-2.7532787) for the "PSME1" variable in Gene_Expression.tsv matches the test value (-2.7532787) for CPC009_PC3_6H:BRD-A05565054-001-01-7:10.

&#9989;	Success: The value (-0.4875) for the "ACTB" variable in Gene_Expression.tsv matches the test value (-0.4875) for AML001_CD34_24H:BRD-A03772856:10.

&#9989;	Success: The value (0.36540002) for the "PSME1" variable in Gene_Expression.tsv matches the test value (0.36540002) for AML001_CD34_24H:BRD-A03772856:10.

&#9989;	Success: The value (-0.1684264) for the "ACTB" variable in Gene_Expression.tsv matches the test value (-0.1684264) for TAK004_U2OS_96H:TRCN0000381509:1.

&#9989;	Success: The value (0.4213416) for the "PSME1" variable in Gene_Expression.tsv matches the test value (0.4213416) for TAK004_U2OS_96H:TRCN0000381509:1.

&#9989;	Success: The value (0.4219) for the "ACTB" variable in Gene_Expression.tsv matches the test value (0.4219) for AML001_CD34_24H:A05.

&#9989;	Success: The value (0.5774) for the "PSME1" variable in Gene_Expression.tsv matches the test value (0.5774) for AML001_CD34_24H:A05.

&#9989;	Success: The value (1.1224) for the "ACTB" variable in Gene_Expression.tsv matches the test value (1.1224) for AML001_CD34_6H:A05.

&#9989;	Success: The value (-0.1224) for the "PSME1" variable in Gene_Expression.tsv matches the test value (-0.1224) for AML001_CD34_6H:A05.

&#9989;	Success: The value (-0.6934756) for the "ACTB" variable in Gene_Expression.tsv matches the test value (-0.6934756) for CPC009_PC3_6H:A17.

&#9989;	Success: The value (-0.0035670642) for the "PSME1" variable in Gene_Expression.tsv matches the test value (-0.0035670642) for CPC009_PC3_6H:A17.

#### Comparing "Metadata.tsv" and "test_Metadata.tsv"


### First 5 columns and 5 rows of /Shared/testing/LINCS_PhaseI_Level5/LINCS_PhaseI_Level5/Metadata.tsv:

<table style="width:100%; border: 1px solid black;">
	<tr align='left'>
		<th align='left'>Sample</th>
		<th align='left'>base_cell_id</th>
		<th align='left'>canonical_smiles</th>
		<th align='left'>cell_id</th>
		<th align='left'>cell_type</th>

	</tr>
	<tr align='left'>
		<td align='left'>AML001_CD34_24H:A05</td>
		<td align='left'>CD34</td>
		<td align='left'>CS(=O)C</td>
		<td align='left'>CD34</td>
		<td align='left'>primary</td>

	</tr>
	<tr align='left'>
		<td align='left'>AML001_CD34_24H:A06</td>
		<td align='left'>CD34</td>
		<td align='left'>CS(=O)C</td>
		<td align='left'>CD34</td>
		<td align='left'>primary</td>

	</tr>
	<tr align='left'>
		<td align='left'>AML001_CD34_24H:B05</td>
		<td align='left'>CD34</td>
		<td align='left'>CS(=O)C</td>
		<td align='left'>CD34</td>
		<td align='left'>primary</td>

	</tr>
	<tr align='left'>
		<td align='left'>AML001_CD34_24H:B06</td>
		<td align='left'>CD34</td>
		<td align='left'>CS(=O)C</td>
		<td align='left'>CD34</td>
		<td align='left'>primary</td>

	</tr>
</table>
&#9989;	First column of "Metadata.tsv" is titled "Sample"

&#9989;	Success: The value (CS(=O)C) for the "canonical_smiles" variable in Metadata.tsv matches the test value (CS(=O)C) for AML001_CD34_24H:A05.

&#9989;	Success: The value (CD34) for the "cell_id" variable in Metadata.tsv matches the test value (CD34) for AML001_CD34_24H:A05.

&#9989;	Success: The value (primary) for the "cell_type" variable in Metadata.tsv matches the test value (primary) for AML001_CD34_24H:A05.

&#9989;	Success: The value (1) for the "distil_nsample" variable in Metadata.tsv matches the test value (1) for AML001_CD34_24H:A05.

&#9989;	Success: The value (4.78894) for the "distil_ss" variable in Metadata.tsv matches the test value (4.78894) for AML001_CD34_24H:A05.

&#9989;	Success: The value (0.313591927289963) for the "icc" variable in Metadata.tsv matches the test value (0.313591927289963) for AML001_CD34_24H:A05.

&#9989;	Success: The value (1) for the "is_touchstone" variable in Metadata.tsv matches the test value (1) for AML001_CD34_24H:A05.

&#9989;	Success: The value (suspension) for the "original_growth_pattern" variable in Metadata.tsv matches the test value (suspension) for AML001_CD34_24H:A05.

&#9989;	Success: The value (DMSO) for the "pert_id" variable in Metadata.tsv matches the test value (DMSO) for AML001_CD34_24H:A05.

&#9989;	Success: The value (24 h) for the "pert_itime" variable in Metadata.tsv matches the test value (24 h) for AML001_CD34_24H:A05.

&#9989;	Success: The value (0.122766) for the "tas_q75" variable in Metadata.tsv matches the test value (0.122766) for AML001_CD34_24H:A05.

&#9989;	Success: The value (CS(=O)C) for the "canonical_smiles" variable in Metadata.tsv matches the test value (CS(=O)C) for AML001_CD34_24H:A06.

&#9989;	Success: The value (CD34) for the "cell_id" variable in Metadata.tsv matches the test value (CD34) for AML001_CD34_24H:A06.

&#9989;	Success: The value (primary) for the "cell_type" variable in Metadata.tsv matches the test value (primary) for AML001_CD34_24H:A06.

&#9989;	Success: The value (1) for the "distil_nsample" variable in Metadata.tsv matches the test value (1) for AML001_CD34_24H:A06.

&#9989;	Success: The value (3.87045) for the "distil_ss" variable in Metadata.tsv matches the test value (3.87045) for AML001_CD34_24H:A06.

&#9989;	Success: The value (0.313591927289963) for the "icc" variable in Metadata.tsv matches the test value (0.313591927289963) for AML001_CD34_24H:A06.

&#9989;	Success: The value (1) for the "is_touchstone" variable in Metadata.tsv matches the test value (1) for AML001_CD34_24H:A06.

&#9989;	Success: The value (suspension) for the "original_growth_pattern" variable in Metadata.tsv matches the test value (suspension) for AML001_CD34_24H:A06.

&#9989;	Success: The value (DMSO) for the "pert_id" variable in Metadata.tsv matches the test value (DMSO) for AML001_CD34_24H:A06.

&#9989;	Success: The value (24 h) for the "pert_itime" variable in Metadata.tsv matches the test value (24 h) for AML001_CD34_24H:A06.

&#9989;	Success: The value (0.122766) for the "tas_q75" variable in Metadata.tsv matches the test value (0.122766) for AML001_CD34_24H:A06.

&#9989;	Success: The value (U2OS) for the "cell_id" variable in Metadata.tsv matches the test value (U2OS) for TAK004_U2OS_96H:TRCN0000370751:1.

&#9989;	Success: The value (cell line) for the "cell_type" variable in Metadata.tsv matches the test value (cell line) for TAK004_U2OS_96H:TRCN0000370751:1.

&#9989;	Success: The value (0.29) for the "distil_cc_q75" variable in Metadata.tsv matches the test value (0.29) for TAK004_U2OS_96H:TRCN0000370751:1.

&#9989;	Success: The value (3) for the "distil_nsample" variable in Metadata.tsv matches the test value (3) for TAK004_U2OS_96H:TRCN0000370751:1.

&#9989;	Success: The value (Caucasian) for the "donor_ethnicity" variable in Metadata.tsv matches the test value (Caucasian) for TAK004_U2OS_96H:TRCN0000370751:1.

&#9989;	Success: The value (0) for the "is_touchstone" variable in Metadata.tsv matches the test value (0) for TAK004_U2OS_96H:TRCN0000370751:1.

&#9989;	Success: The value (TRCN0000370751) for the "pert_id" variable in Metadata.tsv matches the test value (TRCN0000370751) for TAK004_U2OS_96H:TRCN0000370751:1.

&#9989;	Success: The value (96 h) for the "pert_itime" variable in Metadata.tsv matches the test value (96 h) for TAK004_U2OS_96H:TRCN0000370751:1.

&#9989;	Success: The value (0.288657) for the "tas_q75" variable in Metadata.tsv matches the test value (0.288657) for TAK004_U2OS_96H:TRCN0000370751:1.

&#9989;	Success: The value (U2OS) for the "cell_id" variable in Metadata.tsv matches the test value (U2OS) for TAK004_U2OS_96H:TRCN0000381509:1.

&#9989;	Success: The value (cell line) for the "cell_type" variable in Metadata.tsv matches the test value (cell line) for TAK004_U2OS_96H:TRCN0000381509:1.

&#9989;	Success: The value (0.23) for the "distil_cc_q75" variable in Metadata.tsv matches the test value (0.23) for TAK004_U2OS_96H:TRCN0000381509:1.

&#9989;	Success: The value (3) for the "distil_nsample" variable in Metadata.tsv matches the test value (3) for TAK004_U2OS_96H:TRCN0000381509:1.

&#9989;	Success: The value (Caucasian) for the "donor_ethnicity" variable in Metadata.tsv matches the test value (Caucasian) for TAK004_U2OS_96H:TRCN0000381509:1.

&#9989;	Success: The value (0) for the "is_touchstone" variable in Metadata.tsv matches the test value (0) for TAK004_U2OS_96H:TRCN0000381509:1.

&#9989;	Success: The value (TRCN0000381509) for the "pert_id" variable in Metadata.tsv matches the test value (TRCN0000381509) for TAK004_U2OS_96H:TRCN0000381509:1.

&#9989;	Success: The value (96 h) for the "pert_itime" variable in Metadata.tsv matches the test value (96 h) for TAK004_U2OS_96H:TRCN0000381509:1.

&#9989;	Success: The value (0.169385) for the "tas_q75" variable in Metadata.tsv matches the test value (0.169385) for TAK004_U2OS_96H:TRCN0000381509:1.

#### Results: PASS
---
