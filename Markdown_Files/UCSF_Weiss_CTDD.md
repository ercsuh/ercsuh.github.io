# UCSF_Weiss_CTDD
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


### First 5 columns and 5 rows of /Shared/testing/UCSF_Weiss_CTDD/UCSF_Weiss_CTDD/Gene_Expression.tsv:

<table style="width:100%; border: 1px solid black;">
	<tr align='left'>
		<th align='left'>Sample</th>
		<th align='left'>0610007C21Rik</th>
		<th align='left'>0610007L01Rik</th>
		<th align='left'>0610007P08Rik</th>
		<th align='left'>0610007P14Rik</th>

	</tr>
	<tr align='left'>
		<td align='left'>RU109_1355</td>
		<td align='left'>9.1900</td>
		<td align='left'>8.3670</td>
		<td align='left'>6.2000</td>
		<td align='left'>8.9890</td>

	</tr>
	<tr align='left'>
		<td align='left'>RU109_1358</td>
		<td align='left'>8.8340</td>
		<td align='left'>8.5230</td>
		<td align='left'>5.9945</td>
		<td align='left'>9.3620</td>

	</tr>
	<tr align='left'>
		<td align='left'>RU109_1359</td>
		<td align='left'>9.1900</td>
		<td align='left'>8.2750</td>
		<td align='left'>5.9500</td>
		<td align='left'>8.9350</td>

	</tr>
	<tr align='left'>
		<td align='left'>RU109_1361</td>
		<td align='left'>9.1380</td>
		<td align='left'>8.3780</td>
		<td align='left'>5.8920</td>
		<td align='left'>8.8210</td>

	</tr>
</table>
&#9989;	First column of "Gene_Expression.tsv" is titled "Sample"

&#9989;	Success: The value (6.7410) for the "Cxx1a" variable in Gene_Expression.tsv matches the test value (6.7410) for RU109_1355.

&#9989;	Success: The value (4.8500) for the "Prrg1" variable in Gene_Expression.tsv matches the test value (4.8500) for RU109_1355.

&#9989;	Success: The value (6.9190) for the "Robo2" variable in Gene_Expression.tsv matches the test value (6.9190) for RU109_1355.

&#9989;	Success: The value (6.3453) for the "Cspp1" variable in Gene_Expression.tsv matches the test value (6.3453) for RU109_1358.

&#9989;	Success: The value (6.7620) for the "Robo2" variable in Gene_Expression.tsv matches the test value (6.7620) for RU109_1358.

&#9989;	Success: The value (7.0360) for the "Cxx1a" variable in Gene_Expression.tsv matches the test value (7.0360) for RU109_1460.

&#9989;	Success: The value (4.8120) for the "Prrg1" variable in Gene_Expression.tsv matches the test value (4.8120) for RU109_1460.

&#9989;	Success: The value (6.6990) for the "Robo2" variable in Gene_Expression.tsv matches the test value (6.6990) for RU109_1460.

&#9989;	Success: The value (6.3305) for the "Cxx1a" variable in Gene_Expression.tsv matches the test value (6.3305) for RU109_1518.

&#9989;	Success: The value (4.8270) for the "Prrg1" variable in Gene_Expression.tsv matches the test value (4.8270) for RU109_1518.

&#9989;	Success: The value (6.5440) for the "Robo2" variable in Gene_Expression.tsv matches the test value (6.5440) for RU109_1518.

#### Comparing "Metadata.tsv" and "test_Metadata.tsv"


### First 5 columns and 5 rows of /Shared/testing/UCSF_Weiss_CTDD/UCSF_Weiss_CTDD/Metadata.tsv:

<table style="width:100%; border: 1px solid black;">
	<tr align='left'>
		<th align='left'>Sample</th>
		<th align='left'>Color</th>
		<th align='left'>Germline Hras1 status</th>
		<th align='left'>Sex</th>

	</tr>
	<tr align='left'>
		<td align='left'>RU109_1355</td>
		<td align='left'>agouti (tan)</td>
		<td align='left'>Hras1-/-</td>
		<td align='left'>M</td>

	</tr>
	<tr align='left'>
		<td align='left'>RU109_1358</td>
		<td align='left'>agouti (tan)</td>
		<td align='left'>Wild Type</td>
		<td align='left'>M</td>

	</tr>
	<tr align='left'>
		<td align='left'>RU109_1359</td>
		<td align='left'>agouti (tan)</td>
		<td align='left'>Hras1-/-</td>
		<td align='left'>M</td>

	</tr>
	<tr align='left'>
		<td align='left'>RU109_1361</td>
		<td align='left'>white (albino)</td>
		<td align='left'>Hras1-/-</td>
		<td align='left'>F</td>

	</tr>
</table>
&#9989;	First column of "Metadata.tsv" is titled "Sample"

&#9989;	Success: The value (agouti (tan)) for the "Color" variable in Metadata.tsv matches the test value (agouti (tan)) for RU109_1355.

&#9989;	Success: The value (Hras1-/-) for the "Germline Hras1 status" variable in Metadata.tsv matches the test value (Hras1-/-) for RU109_1355.

&#9989;	Success: The value (M) for the "Sex" variable in Metadata.tsv matches the test value (M) for RU109_1355.

&#9989;	Success: The value (agouti (tan)) for the "Color" variable in Metadata.tsv matches the test value (agouti (tan)) for RU109_1358.

&#9989;	Success: The value (Wild Type) for the "Germline Hras1 status" variable in Metadata.tsv matches the test value (Wild Type) for RU109_1358.

&#9989;	Success: The value (M) for the "Sex" variable in Metadata.tsv matches the test value (M) for RU109_1358.

&#9989;	Success: The value (white (albino)) for the "Color" variable in Metadata.tsv matches the test value (white (albino)) for RU109_1445.

&#9989;	Success: The value (Hras1-/-) for the "Germline Hras1 status" variable in Metadata.tsv matches the test value (Hras1-/-) for RU109_1445.

&#9989;	Success: The value (F) for the "Sex" variable in Metadata.tsv matches the test value (F) for RU109_1445.

#### Results: PASS
---
