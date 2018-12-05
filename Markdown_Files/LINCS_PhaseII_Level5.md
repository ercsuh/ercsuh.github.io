# LINCS_PhaseII_Level5
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

#### Running "/Shared/testing/LINCS_PhaseII_Level5/LINCS_PhaseII_Level5/test_Metadata.tsv"

&#9989;	"test_Metadata.tsv" has three columns with the correct headers

&#9989;	"test_Metadata.tsv" contains enough unique samples to test

&#9989;	"test_Metadata.tsv" contains enough test cases (42; min: 8)

#### Running "/Shared/testing/LINCS_PhaseII_Level5/LINCS_PhaseII_Level5/test_Gene_Expression.tsv"

&#9989;	"test_Gene_Expression.tsv" has three columns with the correct headers

&#9989;	"test_Gene_Expression.tsv" contains enough unique samples to test

&#9989;	"test_Gene_Expression.tsv" contains enough test cases (14; min: 8)

#### Results: PASS
---
### Comparing Files:

#### Comparing "Gene_Expression.tsv.gz" and "test_Gene_Expression.tsv"


### First 5 columns and 5 rows of /Shared/testing/LINCS_PhaseII_Level5/LINCS_PhaseII_Level5/Gene_Expression.tsv.gz:

<table style="width:100%; border: 1px solid black;">
	<tr align='left'>
		<th align='left'>Sample</th>
		<th align='left'>DDR1</th>
		<th align='left'>PAX8</th>
		<th align='left'>GUCA1A</th>
		<th align='left'>EPHB3</th>

	</tr>
	<tr align='left'>
		<td align='left'>REP.A001_A375_24H:A03</td>
		<td align='left'>4.2641425</td>
		<td align='left'>0.057249196</td>
		<td align='left'>-1.0124799</td>
		<td align='left'>0.3088984</td>

	</tr>
	<tr align='left'>
		<td align='left'>REP.A001_A375_24H:A04</td>
		<td align='left'>-0.3822108</td>
		<td align='left'>0.30431318</td>
		<td align='left'>-0.6749917</td>
		<td align='left'>-0.33593124</td>

	</tr>
	<tr align='left'>
		<td align='left'>REP.A001_A375_24H:A05</td>
		<td align='left'>-0.57171094</td>
		<td align='left'>-0.75499886</td>
		<td align='left'>0.41451538</td>
		<td align='left'>-0.5023232</td>

	</tr>
	<tr align='left'>
		<td align='left'>REP.A001_A375_24H:A06</td>
		<td align='left'>0.5843761</td>
		<td align='left'>-0.58997315</td>
		<td align='left'>-0.22760315</td>
		<td align='left'>-1.7752469</td>

	</tr>
</table>
&#9989;	First column of "Gene_Expression.tsv.gz" is titled "Sample"

&#9989;	Success: The value (1.02984) for the "ACTB" variable in Gene_Expression.tsv.gz matches the test value (1.02984) for LJP007_HUES3_24H:E15.

&#9989;	Success: The value (0.29355788) for the "DDR1" variable in Gene_Expression.tsv.gz matches the test value (0.29355788) for LJP007_HUES3_24H:E15.

&#9989;	Success: The value (0.45621133) for the "ACTB" variable in Gene_Expression.tsv.gz matches the test value (0.45621133) for LJP005_A375_24H:A03.

&#9989;	Success: The value (-0.15452647) for the "DDR1" variable in Gene_Expression.tsv.gz matches the test value (-0.15452647) for LJP005_A375_24H:A03.

&#9989;	Success: The value (0.23095118) for the "ACTB" variable in Gene_Expression.tsv.gz matches the test value (0.23095118) for LJP005_A375_24H:I14.

&#9989;	Success: The value (-1.9250643) for the "DDR1" variable in Gene_Expression.tsv.gz matches the test value (-1.9250643) for LJP005_A375_24H:I14.

&#9989;	Success: The value (-0.52239954) for the "ACTB" variable in Gene_Expression.tsv.gz matches the test value (-0.52239954) for LJP005_HA1E_24H:M01.

&#9989;	Success: The value (0.44523814) for the "DDR1" variable in Gene_Expression.tsv.gz matches the test value (0.44523814) for LJP005_HA1E_24H:M01.

&#9989;	Success: The value (0.007703185) for the "ACTB" variable in Gene_Expression.tsv.gz matches the test value (0.007703185) for LJP007_SKL.C_24H:B16.

&#9989;	Success: The value (-0.12825866) for the "DDR1" variable in Gene_Expression.tsv.gz matches the test value (-0.12825866) for LJP007_SKL.C_24H:B16.

&#9989;	Success: The value (0.7115803) for the "ACTB" variable in Gene_Expression.tsv.gz matches the test value (0.7115803) for LJP007_SKL.C_24H:K05.

&#9989;	Success: The value (-0.63504004) for the "DDR1" variable in Gene_Expression.tsv.gz matches the test value (-0.63504004) for LJP007_SKL.C_24H:K05.

&#9989;	Success: The value (-0.3084) for the "ACTB" variable in Gene_Expression.tsv.gz matches the test value (-0.3084) for LJP007_SKL_24H:C19.

&#9989;	Success: The value (3.0807) for the "DDR1" variable in Gene_Expression.tsv.gz matches the test value (3.0807) for LJP007_SKL_24H:C19.

#### Comparing "Metadata.tsv.gz" and "test_Metadata.tsv"


### First 5 columns and 5 rows of /Shared/testing/LINCS_PhaseII_Level5/LINCS_PhaseII_Level5/Metadata.tsv.gz:

<table style="width:100%; border: 1px solid black;">
	<tr align='left'>
		<th align='left'>Sample</th>
		<th align='left'>base_cell_id</th>
		<th align='left'>canonical_smiles</th>
		<th align='left'>cell_id</th>
		<th align='left'>cell_type</th>

	</tr>
	<tr align='left'>
		<td align='left'>LJP005_A375_24H:A03</td>
		<td align='left'>A375</td>
		<td align='left'>CS(=O)C</td>
		<td align='left'>A375</td>
		<td align='left'>cell line</td>

	</tr>
	<tr align='left'>
		<td align='left'>LJP005_A375_24H:A04</td>
		<td align='left'>A375</td>
		<td align='left'>CS(=O)C</td>
		<td align='left'>A375</td>
		<td align='left'>cell line</td>

	</tr>
	<tr align='left'>
		<td align='left'>LJP005_A375_24H:A05</td>
		<td align='left'>A375</td>
		<td align='left'>CS(=O)C</td>
		<td align='left'>A375</td>
		<td align='left'>cell line</td>

	</tr>
	<tr align='left'>
		<td align='left'>LJP005_A375_24H:A06</td>
		<td align='left'>A375</td>
		<td align='left'>CS(=O)C</td>
		<td align='left'>A375</td>
		<td align='left'>cell line</td>

	</tr>
</table>
&#9989;	First column of "Metadata.tsv.gz" is titled "Sample"

&#9989;	Success: The value (CS(=O)C) for the "canonical_smiles" variable in Metadata.tsv.gz matches the test value (CS(=O)C) for LJP005_A375_24H:A03.

&#9989;	Success: The value (A375) for the "cell_id" variable in Metadata.tsv.gz matches the test value (A375) for LJP005_A375_24H:A03.

&#9989;	Success: The value (cell line) for the "cell_type" variable in Metadata.tsv.gz matches the test value (cell line) for LJP005_A375_24H:A03.

&#9989;	Success: The value (0.37) for the "distil_cc_q75" variable in Metadata.tsv.gz matches the test value (0.37) for LJP005_A375_24H:A03.

&#9989;	Success: The value (3) for the "distil_nsample" variable in Metadata.tsv.gz matches the test value (3) for LJP005_A375_24H:A03.

&#9989;	Success: The value (F) for the "donor_sex" variable in Metadata.tsv.gz matches the test value (F) for LJP005_A375_24H:A03.

&#9989;	Success: The value (IAZDPXIOMUYVGZ-UHFFFAOYSA-N) for the "inchi_key" variable in Metadata.tsv.gz matches the test value (IAZDPXIOMUYVGZ-UHFFFAOYSA-N) for LJP005_A375_24H:A03.

&#9989;	Success: The value (DMSO) for the "pert_id" variable in Metadata.tsv.gz matches the test value (DMSO) for LJP005_A375_24H:A03.

&#9989;	Success: The value (DMSO) for the "pert_iname" variable in Metadata.tsv.gz matches the test value (DMSO) for LJP005_A375_24H:A03.

&#9989;	Success: The value (24 h) for the "pert_itime" variable in Metadata.tsv.gz matches the test value (24 h) for LJP005_A375_24H:A03.

&#9989;	Success: The value (0.150663) for the "tas" variable in Metadata.tsv.gz matches the test value (0.150663) for LJP005_A375_24H:A03.

&#9989;	Success: The value (Nc1cccc(c1)-c1cc2c(Oc3cccc(O)c3)ncnc2[nH]1) for the "canonical_smiles" variable in Metadata.tsv.gz matches the test value (Nc1cccc(c1)-c1cc2c(Oc3cccc(O)c3)ncnc2[nH]1) for LJP005_HA1E_24H:M02.

&#9989;	Success: The value (HA1E) for the "cell_id" variable in Metadata.tsv.gz matches the test value (HA1E) for LJP005_HA1E_24H:M02.

&#9989;	Success: The value (cell line) for the "cell_type" variable in Metadata.tsv.gz matches the test value (cell line) for LJP005_HA1E_24H:M02.

&#9989;	Success: The value (0.4) for the "distil_cc_q75" variable in Metadata.tsv.gz matches the test value (0.4) for LJP005_HA1E_24H:M02.

&#9989;	Success: The value (3) for the "distil_nsample" variable in Metadata.tsv.gz matches the test value (3) for LJP005_HA1E_24H:M02.

&#9989;	Success: The value (VPVLEBIVXZSOMQ-UHFFFAOYSA-N) for the "inchi_key" variable in Metadata.tsv.gz matches the test value (VPVLEBIVXZSOMQ-UHFFFAOYSA-N) for LJP005_HA1E_24H:M02.

&#9989;	Success: The value (adherent) for the "original_growth_pattern" variable in Metadata.tsv.gz matches the test value (adherent) for LJP005_HA1E_24H:M02.

&#9989;	Success: The value (BRD-K94176593) for the "pert_id" variable in Metadata.tsv.gz matches the test value (BRD-K94176593) for LJP005_HA1E_24H:M02.

&#9989;	Success: The value (3.33 um) for the "pert_idose" variable in Metadata.tsv.gz matches the test value (3.33 um) for LJP005_HA1E_24H:M02.

&#9989;	Success: The value (TWS-119) for the "pert_iname" variable in Metadata.tsv.gz matches the test value (TWS-119) for LJP005_HA1E_24H:M02.

&#9989;	Success: The value (24 h) for the "pert_itime" variable in Metadata.tsv.gz matches the test value (24 h) for LJP005_HA1E_24H:M02.

&#9989;	Success: The value (Cc1ccc(NC(=O)c2cccc(c2)C(C)(C)C#N)cc1Nc1ccc2ncn(C)c(=O)c2c1) for the "canonical_smiles" variable in Metadata.tsv.gz matches the test value (Cc1ccc(NC(=O)c2cccc(c2)C(C)(C)C#N)cc1Nc1ccc2ncn(C)c(=O)c2c1) for LJP007_HUES3_24H:E15.

&#9989;	Success: The value (HUES3) for the "cell_id" variable in Metadata.tsv.gz matches the test value (HUES3) for LJP007_HUES3_24H:E15.

&#9989;	Success: The value (ESC) for the "cell_type" variable in Metadata.tsv.gz matches the test value (ESC) for LJP007_HUES3_24H:E15.

&#9989;	Success: The value (0.47) for the "distil_cc_q75" variable in Metadata.tsv.gz matches the test value (0.47) for LJP007_HUES3_24H:E15.

&#9989;	Success: The value (3) for the "distil_nsample" variable in Metadata.tsv.gz matches the test value (3) for LJP007_HUES3_24H:E15.

&#9989;	Success: The value (ZGBGPEDJXCYQPH-UHFFFAOYSA-N) for the "inchi_key" variable in Metadata.tsv.gz matches the test value (ZGBGPEDJXCYQPH-UHFFFAOYSA-N) for LJP007_HUES3_24H:E15.

&#9989;	Success: The value (adherent) for the "original_growth_pattern" variable in Metadata.tsv.gz matches the test value (adherent) for LJP007_HUES3_24H:E15.

&#9989;	Success: The value (BRD-K05804044) for the "pert_id" variable in Metadata.tsv.gz matches the test value (BRD-K05804044) for LJP007_HUES3_24H:E15.

&#9989;	Success: The value (1.11 um) for the "pert_idose" variable in Metadata.tsv.gz matches the test value (1.11 um) for LJP007_HUES3_24H:E15.

&#9989;	Success: The value (AZ-628) for the "pert_iname" variable in Metadata.tsv.gz matches the test value (AZ-628) for LJP007_HUES3_24H:E15.

&#9989;	Success: The value (24 h) for the "pert_itime" variable in Metadata.tsv.gz matches the test value (24 h) for LJP007_HUES3_24H:E15.

&#9989;	Success: The value (YAPC.311) for the "cell_id" variable in Metadata.tsv.gz matches the test value (YAPC.311) for XPR002_YAPC.311_96H:N12.

&#9989;	Success: The value (cell line) for the "cell_type" variable in Metadata.tsv.gz matches the test value (cell line) for XPR002_YAPC.311_96H:N12.

&#9989;	Success: The value (0.29) for the "distil_cc_q75" variable in Metadata.tsv.gz matches the test value (0.29) for XPR002_YAPC.311_96H:N12.

&#9989;	Success: The value (2) for the "distil_nsample" variable in Metadata.tsv.gz matches the test value (2) for XPR002_YAPC.311_96H:N12.

&#9989;	Success: The value (M) for the "donor_sex" variable in Metadata.tsv.gz matches the test value (M) for XPR002_YAPC.311_96H:N12.

&#9989;	Success: The value (BRDN0000735469) for the "pert_id" variable in Metadata.tsv.gz matches the test value (BRDN0000735469) for XPR002_YAPC.311_96H:N12.

&#9989;	Success: The value (ACLY) for the "pert_iname" variable in Metadata.tsv.gz matches the test value (ACLY) for XPR002_YAPC.311_96H:N12.

&#9989;	Success: The value (96 h) for the "pert_itime" variable in Metadata.tsv.gz matches the test value (96 h) for XPR002_YAPC.311_96H:N12.

&#9989;	Success: The value (0.137759) for the "tas" variable in Metadata.tsv.gz matches the test value (0.137759) for XPR002_YAPC.311_96H:N12.

#### Results: PASS
---
