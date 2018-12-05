# LINCS_PhaseI_Level3
## Status: True
#### Date: 10/02/18
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


### First 5 columns and 5 rows of /Shared/testing/LINCS_PhaseI_Level3/LINCS_PhaseI_Level3/Gene_Expression.tsv:

<table style="width:100%; border: 1px solid black;">
	<tr align='left'>
		<th align='left'>Sample</th>
		<th align='left'>PSME1</th>
		<th align='left'>ATF1</th>
		<th align='left'>RHEB</th>
		<th align='left'>FOXO3</th>

	</tr>
	<tr align='left'>
		<td align='left'>CPC005_A375_6H_X1_B3_DUO52HI53LO:K06</td>
		<td align='left'>11.0495</td>
		<td align='left'>8.168</td>
		<td align='left'>12.7962</td>
		<td align='left'>5.4546</td>

	</tr>
	<tr align='left'>
		<td align='left'>CPC005_A375_6H_X2_B3_DUO52HI53LO:K06</td>
		<td align='left'>10.6128</td>
		<td align='left'>7.78685</td>
		<td align='left'>12.0471</td>
		<td align='left'>6.3285</td>

	</tr>
	<tr align='left'>
		<td align='left'>CPC005_A375_6H_X3_B3_DUO52HI53LO:K06</td>
		<td align='left'>10.6833</td>
		<td align='left'>7.74605</td>
		<td align='left'>12.3448</td>
		<td align='left'>6.06805</td>

	</tr>
	<tr align='left'>
		<td align='left'>CPC005_A375_6H_X1_B3_DUO52HI53LO:C19</td>
		<td align='left'>10.6188</td>
		<td align='left'>8.2274</td>
		<td align='left'>12.7085</td>
		<td align='left'>5.3931</td>

	</tr>
</table>
&#9989;	First column of "Gene_Expression.tsv" is titled "Sample"

&#9989;	Success: The value (14.0261) for the "ACTB" variable in Gene_Expression.tsv matches the test value (14.0261) for CPC001_HA1E_24H_X1_B3_DUO52HI53LO:H01.

&#9989;	Success: The value (11.464849) for the "PSME1" variable in Gene_Expression.tsv matches the test value (11.464849) for CPC001_HA1E_24H_X1_B3_DUO52HI53LO:H01.

&#9989;	Success: The value (11.8344) for the "ACTB" variable in Gene_Expression.tsv matches the test value (11.8344) for ASG001_PC3_24H_X5_B7_DUO52HI53LO:P21.

&#9989;	Success: The value (3.91395) for the "PSME1" variable in Gene_Expression.tsv matches the test value (3.91395) for ASG001_PC3_24H_X5_B7_DUO52HI53LO:P21.

&#9989;	Success: The value (12.380751) for the "ACTB" variable in Gene_Expression.tsv matches the test value (12.380751) for CPC001_VCAP_6H_X5_B5_DUO52HI53LO:M23.

&#9989;	Success: The value (10.971399) for the "PSME1" variable in Gene_Expression.tsv matches the test value (10.971399) for CPC001_VCAP_6H_X5_B5_DUO52HI53LO:M23.

&#9989;	Success: The value (11.7008) for the "ACTB" variable in Gene_Expression.tsv matches the test value (11.7008) for KDB001_MCF7_96H_X2_B1_DUO52HI53LO:D22.

&#9989;	Success: The value (10.91925) for the "PSME1" variable in Gene_Expression.tsv matches the test value (10.91925) for KDB001_MCF7_96H_X2_B1_DUO52HI53LO:D22.

&#9989;	Success: The value (11.49585) for the "ACTB" variable in Gene_Expression.tsv matches the test value (11.49585) for PCLB002_HT29_24H_X1_B13:E08.

&#9989;	Success: The value (10.74125) for the "PSME1" variable in Gene_Expression.tsv matches the test value (10.74125) for PCLB002_HT29_24H_X1_B13:E08.

&#9989;	Success: The value (9.533) for the "ACTB" variable in Gene_Expression.tsv matches the test value (9.533) for PCLB002_HT29_24H_X3_B13:H13.

&#9989;	Success: The value (10.37165) for the "PSME1" variable in Gene_Expression.tsv matches the test value (10.37165) for PCLB002_HT29_24H_X3_B13:H13.

#### Comparing "Metadata.tsv" and "test_Metadata.tsv"


### First 5 columns and 5 rows of /Shared/testing/LINCS_PhaseI_Level3/LINCS_PhaseI_Level3/Metadata.tsv:

<table style="width:100%; border: 1px solid black;">
	<tr align='left'>
		<th align='left'>Sample</th>
		<th align='left'>base_cell_id</th>
		<th align='left'>canonical_smiles</th>
		<th align='left'>cell_id</th>
		<th align='left'>cell_type</th>

	</tr>
	<tr align='left'>
		<td align='left'>ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13</td>
		<td align='left'>MCF7</td>
		<td align='left'>CS(=O)C</td>
		<td align='left'>MCF7</td>
		<td align='left'>cell line</td>

	</tr>
	<tr align='left'>
		<td align='left'>ASG001_MCF7_24H_X1_B7_DUO52HI53LO:G13</td>
		<td align='left'>MCF7</td>
		<td align='left'>CS(=O)C</td>
		<td align='left'>MCF7</td>
		<td align='left'>cell line</td>

	</tr>
	<tr align='left'>
		<td align='left'>ASG001_MCF7_24H_X1_B7_DUO52HI53LO:I13</td>
		<td align='left'>MCF7</td>
		<td align='left'>CS(=O)C</td>
		<td align='left'>MCF7</td>
		<td align='left'>cell line</td>

	</tr>
	<tr align='left'>
		<td align='left'>ASG001_MCF7_24H_X1_B7_DUO52HI53LO:K13</td>
		<td align='left'>MCF7</td>
		<td align='left'>CS(=O)C</td>
		<td align='left'>MCF7</td>
		<td align='left'>cell line</td>

	</tr>
</table>
&#9989;	First column of "Metadata.tsv" is titled "Sample"

&#9989;	Success: The value (CS(=O)C) for the "canonical_smiles" variable in Metadata.tsv matches the test value (CS(=O)C) for ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13.

&#9989;	Success: The value (MCF7) for the "cell_id" variable in Metadata.tsv matches the test value (MCF7) for ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13.

&#9989;	Success: The value (cell line) for the "cell_type" variable in Metadata.tsv matches the test value (cell line) for ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13.

&#9989;	Success: The value (Caucasian) for the "donor_ethnicity" variable in Metadata.tsv matches the test value (Caucasian) for ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13.

&#9989;	Success: The value (0.313591927289963) for the "icc" variable in Metadata.tsv matches the test value (0.313591927289963) for ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13.

&#9989;	Success: The value (1) for the "is_touchstone" variable in Metadata.tsv matches the test value (1) for ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13.

&#9989;	Success: The value (DMSO) for the "pert_id" variable in Metadata.tsv matches the test value (DMSO) for ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13.

&#9989;	Success: The value (DMSO) for the "pert_iname" variable in Metadata.tsv matches the test value (DMSO) for ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13.

&#9989;	Success: The value (ASG001_MCF7_24H_X1) for the "rna_plate" variable in Metadata.tsv matches the test value (ASG001_MCF7_24H_X1) for ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13.

&#9989;	Success: The value (0.122766) for the "tas_q75" variable in Metadata.tsv matches the test value (0.122766) for ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13.

&#9989;	Success: The value (VCAP) for the "cell_id" variable in Metadata.tsv matches the test value (VCAP) for CPC001_VCAP_6H_X5_B5_DUO52HI53LO:M23.

&#9989;	Success: The value (cell line) for the "cell_type" variable in Metadata.tsv matches the test value (cell line) for CPC001_VCAP_6H_X5_B5_DUO52HI53LO:M23.

&#9989;	Success: The value (M) for the "donor_sex" variable in Metadata.tsv matches the test value (M) for CPC001_VCAP_6H_X5_B5_DUO52HI53LO:M23.

&#9989;	Success: The value (0.394875109195709) for the "icc" variable in Metadata.tsv matches the test value (0.394875109195709) for CPC001_VCAP_6H_X5_B5_DUO52HI53LO:M23.

&#9989;	Success: The value (1) for the "is_touchstone" variable in Metadata.tsv matches the test value (1) for CPC001_VCAP_6H_X5_B5_DUO52HI53LO:M23.

&#9989;	Success: The value (BRD-A66927094) for the "pert_id" variable in Metadata.tsv matches the test value (BRD-A66927094) for CPC001_VCAP_6H_X5_B5_DUO52HI53LO:M23.

&#9989;	Success: The value (nemonapride) for the "pert_iname" variable in Metadata.tsv matches the test value (nemonapride) for CPC001_VCAP_6H_X5_B5_DUO52HI53LO:M23.

&#9989;	Success: The value (4452) for the "pubchem_cid" variable in Metadata.tsv matches the test value (4452) for CPC001_VCAP_6H_X5_B5_DUO52HI53LO:M23.

&#9989;	Success: The value (CPC001_VCAP_6H_X5) for the "rna_plate" variable in Metadata.tsv matches the test value (CPC001_VCAP_6H_X5) for CPC001_VCAP_6H_X5_B5_DUO52HI53LO:M23.

&#9989;	Success: The value (0.219453) for the "tas_q75" variable in Metadata.tsv matches the test value (0.219453) for CPC001_VCAP_6H_X5_B5_DUO52HI53LO:M23.

&#9989;	Success: The value (MCF7) for the "cell_id" variable in Metadata.tsv matches the test value (MCF7) for KDB001_MCF7_144H_X3_B1_DUO53HI52LO:D04.

&#9989;	Success: The value (cell line) for the "cell_type" variable in Metadata.tsv matches the test value (cell line) for KDB001_MCF7_144H_X3_B1_DUO53HI52LO:D04.

&#9989;	Success: The value (Caucasian) for the "donor_ethnicity" variable in Metadata.tsv matches the test value (Caucasian) for KDB001_MCF7_144H_X3_B1_DUO53HI52LO:D04.

&#9989;	Success: The value (0.682715356349945) for the "icc" variable in Metadata.tsv matches the test value (0.682715356349945) for KDB001_MCF7_144H_X3_B1_DUO53HI52LO:D04.

&#9989;	Success: The value (1) for the "is_touchstone" variable in Metadata.tsv matches the test value (1) for KDB001_MCF7_144H_X3_B1_DUO53HI52LO:D04.

&#9989;	Success: The value (TRCN0000286150) for the "pert_id" variable in Metadata.tsv matches the test value (TRCN0000286150) for KDB001_MCF7_144H_X3_B1_DUO53HI52LO:D04.

&#9989;	Success: The value (MRPS2) for the "pert_iname" variable in Metadata.tsv matches the test value (MRPS2) for KDB001_MCF7_144H_X3_B1_DUO53HI52LO:D04.

&#9989;	Success: The value (KDB001_MCF7_144H_X3) for the "rna_plate" variable in Metadata.tsv matches the test value (KDB001_MCF7_144H_X3) for KDB001_MCF7_144H_X3_B1_DUO53HI52LO:D04.

&#9989;	Success: The value (0.3074425) for the "tas_q75" variable in Metadata.tsv matches the test value (0.3074425) for KDB001_MCF7_144H_X3_B1_DUO53HI52LO:D04.

&#9989;	Success: The value (COCC1OC(=O)c2coc3c2C1(C)C1=C(C2CCC(=O)C2(C)CC1OC(C)=O)C3=O) for the "canonical_smiles" variable in Metadata.tsv matches the test value (COCC1OC(=O)c2coc3c2C1(C)C1=C(C2CCC(=O)C2(C)CC1OC(C)=O)C3=O) for PCLB002_MCF7_24H_X3_B13:P24.

&#9989;	Success: The value (MCF7) for the "cell_id" variable in Metadata.tsv matches the test value (MCF7) for PCLB002_MCF7_24H_X3_B13:P24.

&#9989;	Success: The value (cell line) for the "cell_type" variable in Metadata.tsv matches the test value (cell line) for PCLB002_MCF7_24H_X3_B13:P24.

&#9989;	Success: The value (Caucasian) for the "donor_ethnicity" variable in Metadata.tsv matches the test value (Caucasian) for PCLB002_MCF7_24H_X3_B13:P24.

&#9989;	Success: The value (0.478662326931953) for the "icc" variable in Metadata.tsv matches the test value (0.478662326931953) for PCLB002_MCF7_24H_X3_B13:P24.

&#9989;	Success: The value (0) for the "is_touchstone" variable in Metadata.tsv matches the test value (0) for PCLB002_MCF7_24H_X3_B13:P24.

&#9989;	Success: The value (BRD-A75409952) for the "pert_id" variable in Metadata.tsv matches the test value (BRD-A75409952) for PCLB002_MCF7_24H_X3_B13:P24.

&#9989;	Success: The value (wortmannin) for the "pert_iname" variable in Metadata.tsv matches the test value (wortmannin) for PCLB002_MCF7_24H_X3_B13:P24.

&#9989;	Success: The value (PCLB002_MCF7_24H_X3) for the "rna_plate" variable in Metadata.tsv matches the test value (PCLB002_MCF7_24H_X3) for PCLB002_MCF7_24H_X3_B13:P24.

&#9989;	Success: The value (0.41063425) for the "tas_q75" variable in Metadata.tsv matches the test value (0.41063425) for PCLB002_MCF7_24H_X3_B13:P24.

#### Results: PASS
---
