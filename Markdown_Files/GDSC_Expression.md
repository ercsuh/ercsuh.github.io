#GDSC_Expression
## Status: False
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

&#9989;	Annotations.tsv.gz was created and zipped correctly.

#### Results: PASS
---
### Running user scripts . . .



&#9989;	install.sh executed properly.



&#9989;	download.sh executed properly.



&#9989;	parse.sh executed properly.

#### Results: PASS
---
### Testing Files:

#### Running "/Shared/testing/GDSC_Expression/GDSC_Expression/test_Annotations.tsv"

&#9989;	"test_Annotations.tsv" has three columns with the correct headers

&#9989;	"test_Annotations.tsv" contains enough unique samples to test

&#9989;	"test_Annotations.tsv" contains enough test cases (83; min: 8)

#### Running "/Shared/testing/GDSC_Expression/GDSC_Expression/test_Gene_Expression.tsv"

&#9989;	"test_Gene_Expression.tsv" has three columns with the correct headers

&#9989;	"test_Gene_Expression.tsv" contains enough unique samples to test

&#9989;	"test_Gene_Expression.tsv" contains enough test cases (8; min: 8)

#### Results: PASS
---
### Comparing Files:

#### Comparing "Gene_Expression.tsv.gz" and "test_Gene_Expression.tsv"


### First 5 columns and 5 rows of /Shared/testing/GDSC_Expression/GDSC_Expression/Gene_Expression.tsv.gz:

<table style="width:100%; border: 1px solid black;">
	<tr align='left'>
		<th align='left'>Sample</th>
		<th align='left'>ENSG00000000003</th>
		<th align='left'>ENSG00000000005</th>
		<th align='left'>ENSG00000000419</th>
		<th align='left'>ENSG00000000457</th>

	</tr>
	<tr align='left'>
		<td align='left'>CAL-120</td>
		<td align='left'>7.63202317146339</td>
		<td align='left'>2.96458512058924</td>
		<td align='left'>10.3795526353077</td>
		<td align='left'>3.61479404843988</td>

	</tr>
	<tr align='left'>
		<td align='left'>DMS-114</td>
		<td align='left'>7.54867116637172</td>
		<td align='left'>2.77771614989839</td>
		<td align='left'>11.8073412488458</td>
		<td align='left'>4.066886747621</td>

	</tr>
	<tr align='left'>
		<td align='left'>CAL-51</td>
		<td align='left'>8.71233752103624</td>
		<td align='left'>2.6435077554121</td>
		<td align='left'>9.88073281995499</td>
		<td align='left'>3.95622995046262</td>

	</tr>
	<tr align='left'>
		<td align='left'>H2869</td>
		<td align='left'>7.79714221650204</td>
		<td align='left'>2.8179230218265</td>
		<td align='left'>9.88347076381233</td>
		<td align='left'>4.06370139098185</td>

	</tr>
</table>
&#9989;	First column of "Gene_Expression.tsv.gz" is titled "Sample"

&#9989;	Success: The value (7.63202317146339) for the "ENSG00000000003" variable in Gene_Expression.tsv.gz matches the test value (7.63202317146339) for CAL-120.

&#9989;	Success: The value (7.28473262883457) for the "ENSG00000266753" variable in Gene_Expression.tsv.gz matches the test value (7.28473262883457) for CAL-120.

&#9989;	Success: The value (8.82719752679088) for the "ENSG00000000003" variable in Gene_Expression.tsv.gz matches the test value (8.82719752679088) for NCI-H522.

&#9989;	Success: The value (8.98731486372535) for the "ENSG00000266753" variable in Gene_Expression.tsv.gz matches the test value (8.98731486372535) for NCI-H522.

&#9989;	Success: The value (7.36084795571653) for the "ENSG00000000003" variable in Gene_Expression.tsv.gz matches the test value (7.36084795571653) for ESS-1.

&#9989;	Success: The value (7.30348973531859) for the "ENSG00000266753" variable in Gene_Expression.tsv.gz matches the test value (7.30348973531859) for ESS-1.

&#10060;	The value (7.31906561147659) for the "ENSG00000000003" variable in Gene_Expression.tsv.gz does not match the test value (7.31906561148) for SK-MEL-28.

&#10060;	The value (7.350374611598085) for the "ENSG00000266753" variable in Gene_Expression.tsv.gz does not match the test value (7.3503746116) for SK-MEL-28.

#### Comparing "Annotations.tsv.gz" and "test_Annotations.tsv"


### First 5 columns and 5 rows of /Shared/testing/GDSC_Expression/GDSC_Expression/Annotations.tsv.gz:

<table style="width:100%; border: 1px solid black;">
	<tr align='left'>
		<th align='left'>Sample</th>
		<th align='left'>Cancer Type (matching TCGA label)</th>
		<th align='left'>Drug_ AUY_AUC</th>
		<th align='left'>Drug_ AUY_LN_IC50</th>
		<th align='left'>Drug_ AUY_MAX_CONC_MICROMOLAR</th>

	</tr>
	<tr align='left'>
		<td align='left'>CAL-120</td>
		<td align='left'>Breast invasive carcinoma</td>
		<td align='left'>0.59883051</td>
		<td align='left'>-3.43144162</td>
		<td align='left'>0.256</td>

	</tr>
	<tr align='left'>
		<td align='left'>DMS-114</td>
		<td align='left'>Small Cell Lung Cancer</td>
		<td align='left'>0.89632896</td>
		<td align='left'>-0.84806601</td>
		<td align='left'>0.256</td>

	</tr>
	<tr align='left'>
		<td align='left'>CAL-51</td>
		<td align='left'>Breast invasive carcinoma</td>
		<td align='left'>0.36415609</td>
		<td align='left'>-4.94243304</td>
		<td align='left'>0.256</td>

	</tr>
	<tr align='left'>
		<td align='left'>H2869</td>
		<td align='left'>Mesothelioma</td>
		<td align='left'>0.64519554</td>
		<td align='left'>-3.10942469</td>
		<td align='left'>0.256</td>

	</tr>
</table>
&#9989;	First column of "Annotations.tsv.gz" is titled "Sample"

&#9989;	Success: The value (Breast invasive carcinoma) for the "Cancer Type (matching TCGA label)" variable in Annotations.tsv.gz matches the test value (Breast invasive carcinoma) for CAL-120.

&#9989;	Success: The value (1.024) for the "Drug_Doxil_MAX_CONC_MICROMOLAR" variable in Annotations.tsv.gz matches the test value (1.024) for CAL-120.

&#9989;	Success: The value (0.03204478) for the "Drug_Doxil_RMSE" variable in Annotations.tsv.gz matches the test value (0.03204478) for CAL-120.

&#9989;	Success: The value (1.024) for the "Drug_Doxorubicin_MAX_CONC_MICROMOLAR" variable in Annotations.tsv.gz matches the test value (1.024) for CAL-120.

&#9989;	Success: The value (0.03204478) for the "Drug_Doxorubicin_RMSE" variable in Annotations.tsv.gz matches the test value (0.03204478) for CAL-120.

&#9989;	Success: The value (1.024) for the "Drug_Doxorubicine_MAX_CONC_MICROMOLAR" variable in Annotations.tsv.gz matches the test value (1.024) for CAL-120.

&#9989;	Success: The value (0.03204478) for the "Drug_Doxorubicine_RMSE" variable in Annotations.tsv.gz matches the test value (0.03204478) for CAL-120.

&#9989;	Success: The value (1.0) for the "Drug_MLN-4924_MAX_CONC_MICROMOLAR" variable in Annotations.tsv.gz matches the test value (1.0) for CAL-120.

&#9989;	Success: The value (0.05728674) for the "Drug_MLN-4924_RMSE" variable in Annotations.tsv.gz matches the test value (0.05728674) for CAL-120.

&#9989;	Success: The value (1.0) for the "Drug_MLN4924_MAX_CONC_MICROMOLAR" variable in Annotations.tsv.gz matches the test value (1.0) for CAL-120.

&#9989;	Success: The value (0.05728674) for the "Drug_MLN4924_RMSE" variable in Annotations.tsv.gz matches the test value (0.05728674) for CAL-120.

&#9989;	Success: The value (1.0) for the "Drug_Pevonedistat_MAX_CONC_MICROMOLAR" variable in Annotations.tsv.gz matches the test value (1.0) for CAL-120.

&#9989;	Success: The value (0.05728674) for the "Drug_Pevonedistat_RMSE" variable in Annotations.tsv.gz matches the test value (0.05728674) for CAL-120.

&#9989;	Success: The value (breast) for the "GDSC Tissue descriptor 1" variable in Annotations.tsv.gz matches the test value (breast) for CAL-120.

&#9989;	Success: The value (Adherent) for the "Growth Properties" variable in Annotations.tsv.gz matches the test value (Adherent) for CAL-120.

&#9989;	Success: The value (carcinoma) for the "Histology" variable in Annotations.tsv.gz matches the test value (carcinoma) for CAL-120.

&#9989;	Success: The value (Microsatillite class stable (0 of 5 markers show instability)/Microsatillite instability low (1 of 5 markers show instability)) for the "Microsatellite  instability Status (MSI)" variable in Annotations.tsv.gz matches the test value (Microsatillite class stable (0 of 5 markers show instability)/Microsatillite instability low (1 of 5 markers show instability)) for CAL-120.

&#10060;	The value (cnaBRCA16) for the "RACS_Amplification" variable in Annotations.tsv.gz does not match the test value (cnaBRCA10 (MDM2,NUP107)) for CAL-120.

&#9989;	Success: The value (cnaBRCA22 (SYNCRIP,ZNF292)) for the "RACS_Deletion" variable in Annotations.tsv.gz matches the test value (cnaBRCA22 (SYNCRIP,ZNF292)) for CAL-120.

&#9989;	Success: The value (DMEM/F12: DMEM/F12, 10% FBS, 1% PenStrep) for the "Screen Medium" variable in Annotations.tsv.gz matches the test value (DMEM/F12: DMEM/F12, 10% FBS, 1% PenStrep) for CAL-120.

&#9989;	Success: The value (breast) for the "Site" variable in Annotations.tsv.gz matches the test value (breast) for CAL-120.

&#9989;	Success: The value (ZNF628) for the "Variant_missense" variable in Annotations.tsv.gz matches the test value (ZNF628) for CAL-120.

&#9989;	Success: The value (Skin Cutaneous Melanoma) for the "Cancer Type (matching TCGA label)" variable in Annotations.tsv.gz matches the test value (Skin Cutaneous Melanoma) for SK-MEL-28.

&#9989;	Success: The value (1.024) for the "Drug_Doxil_MAX_CONC_MICROMOLAR" variable in Annotations.tsv.gz matches the test value (1.024) for SK-MEL-28.

&#9989;	Success: The value (0.12082764) for the "Drug_Doxil_RMSE" variable in Annotations.tsv.gz matches the test value (0.12082764) for SK-MEL-28.

&#9989;	Success: The value (1.024) for the "Drug_Doxorubicin_MAX_CONC_MICROMOLAR" variable in Annotations.tsv.gz matches the test value (1.024) for SK-MEL-28.

&#9989;	Success: The value (0.12082764) for the "Drug_Doxorubicin_RMSE" variable in Annotations.tsv.gz matches the test value (0.12082764) for SK-MEL-28.

&#9989;	Success: The value (1.024) for the "Drug_Doxorubicine_MAX_CONC_MICROMOLAR" variable in Annotations.tsv.gz matches the test value (1.024) for SK-MEL-28.

&#9989;	Success: The value (0.12082764) for the "Drug_Doxorubicine_RMSE" variable in Annotations.tsv.gz matches the test value (0.12082764) for SK-MEL-28.

&#9989;	Success: The value (10.24) for the "Drug_NPK76-II-72-1_MAX_CONC_MICROMOLAR" variable in Annotations.tsv.gz matches the test value (10.24) for SK-MEL-28.

&#9989;	Success: The value (0.04253059) for the "Drug_NPK76-II-72-1_RMSE" variable in Annotations.tsv.gz matches the test value (0.04253059) for SK-MEL-28.

&#9989;	Success: The value (skin) for the "GDSC Tissue descriptor 1" variable in Annotations.tsv.gz matches the test value (skin) for SK-MEL-28.

&#9989;	Success: The value (Adherent) for the "Growth Properties" variable in Annotations.tsv.gz matches the test value (Adherent) for SK-MEL-28.

&#9989;	Success: The value (malignant_melanoma) for the "Histology" variable in Annotations.tsv.gz matches the test value (malignant_melanoma) for SK-MEL-28.

&#9989;	Success: The value (Microsatillite class stable (0 of 5 markers show instability)/Microsatillite instability low (1 of 5 markers show instability)) for the "Microsatellite  instability Status (MSI)" variable in Annotations.tsv.gz matches the test value (Microsatillite class stable (0 of 5 markers show instability)/Microsatillite instability low (1 of 5 markers show instability)) for SK-MEL-28.

&#9989;	Success: The value (cnaSKCM21 (FOXP1,MITF)) for the "RACS_Amplification" variable in Annotations.tsv.gz matches the test value (cnaSKCM21 (FOXP1,MITF)) for SK-MEL-28.

&#9989;	Success: The value (cnaSKCM4 (BNC2,CDKN2A,JAK2,PSIP1)) for the "RACS_Deletion" variable in Annotations.tsv.gz matches the test value (cnaSKCM4 (BNC2,CDKN2A,JAK2,PSIP1)) for SK-MEL-28.

&#9989;	Success: The value (DMEM/F12: DMEM/F12, 10% FBS, 1% PenStrep) for the "Screen Medium" variable in Annotations.tsv.gz matches the test value (DMEM/F12: DMEM/F12, 10% FBS, 1% PenStrep) for SK-MEL-28.

&#9989;	Success: The value (skin) for the "Site" variable in Annotations.tsv.gz matches the test value (skin) for SK-MEL-28.

&#9989;	Success: The value (ZSCAN21) for the "Variant_missense" variable in Annotations.tsv.gz matches the test value (ZSCAN21) for SK-MEL-28.

&#9989;	Success: The value (Lung adenocarcinoma) for the "Cancer Type (matching TCGA label)" variable in Annotations.tsv.gz matches the test value (Lung adenocarcinoma) for NCI-H522.

&#9989;	Success: The value (0.008) for the "Drug_Bryostatin 1_MAX_CONC_MICROMOLAR" variable in Annotations.tsv.gz matches the test value (0.008) for NCI-H522.

&#9989;	Success: The value (0.10946682) for the "Drug_Bryostatin 1_RMSE" variable in Annotations.tsv.gz matches the test value (0.10946682) for NCI-H522.

&#9989;	Success: The value (0.008) for the "Drug_Bryostatin_MAX_CONC_MICROMOLAR" variable in Annotations.tsv.gz matches the test value (0.008) for NCI-H522.

&#9989;	Success: The value (0.10946682) for the "Drug_Bryostatin_RMSE" variable in Annotations.tsv.gz matches the test value (0.10946682) for NCI-H522.

&#9989;	Success: The value (1.024) for the "Drug_Doxil_MAX_CONC_MICROMOLAR" variable in Annotations.tsv.gz matches the test value (1.024) for NCI-H522.

&#9989;	Success: The value (0.13644181) for the "Drug_Doxil_RMSE" variable in Annotations.tsv.gz matches the test value (0.13644181) for NCI-H522.

&#9989;	Success: The value (1.024) for the "Drug_Doxorubicin_MAX_CONC_MICROMOLAR" variable in Annotations.tsv.gz matches the test value (1.024) for NCI-H522.

&#9989;	Success: The value (0.13644181) for the "Drug_Doxorubicin_RMSE" variable in Annotations.tsv.gz matches the test value (0.13644181) for NCI-H522.

&#9989;	Success: The value (1.024) for the "Drug_Doxorubicine_MAX_CONC_MICROMOLAR" variable in Annotations.tsv.gz matches the test value (1.024) for NCI-H522.

&#9989;	Success: The value (0.13644181) for the "Drug_Doxorubicine_RMSE" variable in Annotations.tsv.gz matches the test value (0.13644181) for NCI-H522.

&#9989;	Success: The value (lung_NSCLC) for the "GDSC Tissue descriptor 1" variable in Annotations.tsv.gz matches the test value (lung_NSCLC) for NCI-H522.

&#9989;	Success: The value (Adherent) for the "Growth Properties" variable in Annotations.tsv.gz matches the test value (Adherent) for NCI-H522.

&#9989;	Success: The value (carcinoma) for the "Histology" variable in Annotations.tsv.gz matches the test value (carcinoma) for NCI-H522.

&#9989;	Success: The value (Microsatillite class stable (0 of 5 markers show instability)/Microsatillite instability low (1 of 5 markers show instability)) for the "Microsatellite  instability Status (MSI)" variable in Annotations.tsv.gz matches the test value (Microsatillite class stable (0 of 5 markers show instability)/Microsatillite instability low (1 of 5 markers show instability)) for NCI-H522.

&#9989;	Success: The value (cnaLUAD34 (FAT1,IRF2)) for the "RACS_Deletion" variable in Annotations.tsv.gz matches the test value (cnaLUAD34 (FAT1,IRF2)) for NCI-H522.

&#9989;	Success: The value (RPMI: RPMI, 10% FBS, % PenStrep, % Glucose, 1mM Sodium Pyruvate) for the "Screen Medium" variable in Annotations.tsv.gz matches the test value (RPMI: RPMI, 10% FBS, % PenStrep, % Glucose, 1mM Sodium Pyruvate) for NCI-H522.

&#9989;	Success: The value (lung) for the "Site" variable in Annotations.tsv.gz matches the test value (lung) for NCI-H522.

&#9989;	Success: The value (ZP1) for the "Variant_missense" variable in Annotations.tsv.gz matches the test value (ZP1) for NCI-H522.

&#9989;	Success: The value (1.024) for the "Drug_Doxil_MAX_CONC_MICROMOLAR" variable in Annotations.tsv.gz matches the test value (1.024) for ESS-1.

&#9989;	Success: The value (0.07144754) for the "Drug_Doxil_RMSE" variable in Annotations.tsv.gz matches the test value (0.07144754) for ESS-1.

&#9989;	Success: The value (1.024) for the "Drug_Doxorubicin_MAX_CONC_MICROMOLAR" variable in Annotations.tsv.gz matches the test value (1.024) for ESS-1.

&#9989;	Success: The value (0.07144754) for the "Drug_Doxorubicin_RMSE" variable in Annotations.tsv.gz matches the test value (0.07144754) for ESS-1.

&#9989;	Success: The value (1.024) for the "Drug_Doxorubicine_MAX_CONC_MICROMOLAR" variable in Annotations.tsv.gz matches the test value (1.024) for ESS-1.

&#9989;	Success: The value (0.07144754) for the "Drug_Doxorubicine_RMSE" variable in Annotations.tsv.gz matches the test value (0.07144754) for ESS-1.

&#9989;	Success: The value (10.0) for the "Drug_SB 216763_MAX_CONC_MICROMOLAR" variable in Annotations.tsv.gz matches the test value (10.0) for ESS-1.

&#9989;	Success: The value (0.02381139) for the "Drug_SB 216763_RMSE" variable in Annotations.tsv.gz matches the test value (0.02381139) for ESS-1.

&#9989;	Success: The value (10.0) for the "Drug_SB-216763_MAX_CONC_MICROMOLAR" variable in Annotations.tsv.gz matches the test value (10.0) for ESS-1.

&#9989;	Success: The value (0.02381139) for the "Drug_SB-216763_RMSE" variable in Annotations.tsv.gz matches the test value (0.02381139) for ESS-1.

&#9989;	Success: The value (10.0) for the "Drug_SB216763_MAX_CONC_MICROMOLAR" variable in Annotations.tsv.gz matches the test value (10.0) for ESS-1.

&#9989;	Success: The value (0.02381139) for the "Drug_SB216763_RMSE" variable in Annotations.tsv.gz matches the test value (0.02381139) for ESS-1.

&#9989;	Success: The value (urogenital_system) for the "GDSC Tissue descriptor 1" variable in Annotations.tsv.gz matches the test value (urogenital_system) for ESS-1.

&#9989;	Success: The value (Adherent) for the "Growth Properties" variable in Annotations.tsv.gz matches the test value (Adherent) for ESS-1.

&#9989;	Success: The value (carcinoma) for the "Histology" variable in Annotations.tsv.gz matches the test value (carcinoma) for ESS-1.

&#9989;	Success: The value (Microsatillite class stable (0 of 5 markers show instability)/Microsatillite instability low (1 of 5 markers show instability)) for the "Microsatellite  instability Status (MSI)" variable in Annotations.tsv.gz matches the test value (Microsatillite class stable (0 of 5 markers show instability)/Microsatillite instability low (1 of 5 markers show instability)) for ESS-1.

&#9989;	Success: The value (RPMI: RPMI, 10% FBS, % PenStrep, % Glucose, 1mM Sodium Pyruvate) for the "Screen Medium" variable in Annotations.tsv.gz matches the test value (RPMI: RPMI, 10% FBS, % PenStrep, % Glucose, 1mM Sodium Pyruvate) for ESS-1.

&#9989;	Success: The value (endometrium) for the "Site" variable in Annotations.tsv.gz matches the test value (endometrium) for ESS-1.

&#9989;	Success: The value (ZZEF1) for the "Variant_missense" variable in Annotations.tsv.gz matches the test value (ZZEF1) for ESS-1.

#### Results: FAIL
---
