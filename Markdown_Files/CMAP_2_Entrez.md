# CMAP_2_Entrez
## Status: True
#### Date: 08/19/18
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

Executing /Shared/testing/CMAP_2_Entrez/install.sh: Success

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

&#9989;	description.md exists.

&#9989;	config.yaml exists.

#### Results: PASS
---
### Running user scripts . . .

Executing /Shared/testing/CMAP_2_Entrez/install.sh: Success

Executing /Shared/testing/CMAP_2_Entrez/download.sh: Success

Executing /Shared/testing/CMAP_2_Entrez/parse.sh: Success

&#9989;	Gene_Expression.tsv.gz was created and zipped correctly.

&#9989;	Metadata.tsv.gz was created and zipped correctly.

#### Results: PASS
---
### Testing Test Files:

#### Running "test_Metadata.tsv"

&#9989;	"test_Metadata.tsv" has three columns with the correct headers

&#9989;	"test_Metadata.tsv" contains enough unique samples to test

&#9989;	"test_Metadata.tsv" has enough features to test (min: 1)

&#9989;	"test_Metadata.tsv" contains enough test cases (28; min: 8)

#### Running "test_Gene_Expression.tsv"

&#9989;	"test_Gene_Expression.tsv" has three columns with the correct headers

&#9989;	"test_Gene_Expression.tsv" contains enough unique samples to test

&#9989;	"test_Gene_Expression.tsv" has enough features to test (min: 1)

&#9989;	"test_Gene_Expression.tsv" contains enough test cases (8; min: 8)

#### Results: PASS
---
### Comparing Files:

#### Comparing "Gene_Expression.tsv.gz" and "test_Gene_Expression.tsv"


### First 5 columns and 5 rows of Gene_Expression.tsv.gz:

<table style="width:100%; border: 1px solid black;">
	<tr>
		<th>Sample</th>
		<th>NAT2</th>
		<th>ADA</th>
		<th>CDH2</th>
		<th>AKT3</th>

	</tr>
	<tr>
		<td>5202764005789148112904.A01</td>
		<td>-0.0721155659798336</td>
		<td>0.549026317009599</td>
		<td>0.20674284888983</td>
		<td>0.24321594022442</td>

	</tr>
	<tr>
		<td>5202764005789148112904.A02</td>
		<td>-0.108647346134676</td>
		<td>0.528871093351372</td>
		<td>0.267105619444701</td>
		<td>0.134633600039991</td>

	</tr>
	<tr>
		<td>5202764005789148112904.A03</td>
		<td>-0.0639074169054108</td>
		<td>0.382801847992761</td>
		<td>0.279920356828535</td>
		<td>0.20550249824079</td>

	</tr>
	<tr>
		<td>5202764005789148112904.A04</td>
		<td>-0.0796867840644685</td>
		<td>0.4322912761935</td>
		<td>0.19673071135504</td>
		<td>0.185533826820587</td>

	</tr>
</table>
&#9989;	First column of "Gene_Expression.tsv.gz" is titled "Sample"

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

#### Comparing "Metadata.tsv.gz" and "test_Metadata.tsv"


### First 5 columns and 5 rows of Metadata.tsv.gz:

<table style="width:100%; border: 1px solid black;">
	<tr>
		<th>Sample</th>
		<th>MainCategory</th>
		<th>InstanceID</th>
		<th>DrugName</th>
		<th>Concentration</th>

	</tr>
	<tr>
		<td>EC2003090503AA</td>
		<td>Perturbed</td>
		<td>1</td>
		<td>metformin</td>
		<td>0.00001</td>

	</tr>
	<tr>
		<td>5202764005791175120104.E08</td>
		<td>Perturbed</td>
		<td>1000</td>
		<td>vorinostat</td>
		<td>0.00001</td>

	</tr>
	<tr>
		<td>5202764005791175120104.E10</td>
		<td>Perturbed</td>
		<td>1001</td>
		<td>sirolimus</td>
		<td>0.0000001</td>

	</tr>
	<tr>
		<td>5202764005791175120104.E11</td>
		<td>Perturbed</td>
		<td>1002</td>
		<td>valproic_acid</td>
		<td>0.00005</td>

	</tr>
</table>
&#9989;	First column of "Metadata.tsv.gz" is titled "Sample"

&#9989;	Row 1: Success

&#9989;	Row 2: Success

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

&#9989;	Row 22: Success

&#9989;	Row 23: Success

&#9989;	Row 24: Success

&#9989;	Row 25: Success

&#9989;	Row 26: Success

&#9989;	Row 27: Success

&#9989;	Row 28: Success

&#9989;	Row 15: Success

&#9989;	Row 16: Success

&#9989;	Row 17: Success

&#9989;	Row 18: Success

&#9989;	Row 19: Success

&#9989;	Row 20: Success

&#9989;	Row 21: Success

### Comparing Samples

&#9989;	Samples are the same in all data files

#### Results: PASS
---
### Testing Directory after cleanup . . .

#### Results: PASS
---
