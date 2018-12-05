#BiomarkerBenchmark_GSE10320
## Status: True
#### Date: 08/17/18
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

Executing /Shared/testing/BiomarkerBenchmark_GSE10320/install.sh: Success

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

&#9989;	description.md exists.

&#9989;	config.yaml exists.

#### Results: PASS
---
### Running user scripts . . .

Executing /Shared/testing/BiomarkerBenchmark_GSE10320/install.sh: Success

Executing /Shared/testing/BiomarkerBenchmark_GSE10320/download.sh: Success

Executing /Shared/testing/BiomarkerBenchmark_GSE10320/parse.sh: Success

&#9989;	data.tsv.gz was created and zipped correctly.

&#9989;	Clinical.tsv.gz was created and zipped correctly.

#### Results: PASS
---
### Testing Test Files:

#### Running "test_Clinical.tsv"

&#9989;	"test_Clinical.tsv" has three columns with the correct headers

&#9989;	"test_Clinical.tsv" contains enough unique samples to test

&#10060;	Sample "GSM260728" does not have enough features to test (min: 2)

&#10060;	Sample "GSM260729" does not have enough features to test (min: 2)

&#10060;	Sample "GSM260730" does not have enough features to test (min: 2)

&#10060;	Sample "GSM260731" does not have enough features to test (min: 2)

&#10060;	Sample "GSM260868" does not have enough features to test (min: 2)

&#10060;	Sample "GSM260869" does not have enough features to test (min: 2)

&#10060;	Sample "GSM260870" does not have enough features to test (min: 2)

&#10060;	Sample "GSM260871" does not have enough features to test (min: 2)

&#9989;	"test_Clinical.tsv" contains enough test cases (8; min: 8)

#### Running "test_data.tsv"

&#9989;	"test_data.tsv" has three columns with the correct headers

&#9989;	"test_data.tsv" contains enough unique samples to test

&#9989;	"test_data.tsv" has enough features to test (min: 1)

&#9989;	"test_data.tsv" contains enough test cases (8; min: 8)

#### Results: PASS
---
### Comparing Files:

#### Comparing "data.tsv.gz" and "test_data.tsv"


### First 5 columns and 5 rows of data.tsv.gz:

<table style="width:100%; border: 1px solid black;">
	<tr>
		<th>Sample</th>
		<th>ENSG00000000003</th>
		<th>ENSG00000000005</th>
		<th>ENSG00000000419</th>
		<th>ENSG00000000457</th>

	</tr>
	<tr>
		<td>GSM260728</td>
		<td>1.96299861705882</td>
		<td>-0.24701918625</td>
		<td>1.85661267</td>
		<td>0.117242436956522</td>

	</tr>
	<tr>
		<td>GSM260729</td>
		<td>1.60463381823529</td>
		<td>-0.30471235625</td>
		<td>1.52185132888889</td>
		<td>0.0680259504347826</td>

	</tr>
	<tr>
		<td>GSM260730</td>
		<td>1.50979470470588</td>
		<td>-0.2583563075</td>
		<td>1.20168762888889</td>
		<td>0.32772114173913</td>

	</tr>
	<tr>
		<td>GSM260731</td>
		<td>1.77584751352941</td>
		<td>-0.240847395</td>
		<td>1.19865990111111</td>
		<td>0.0518993904347826</td>

	</tr>
</table>
&#9989;	First column of "data.tsv.gz" is titled "Sample"

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

#### Comparing "Clinical.tsv.gz" and "test_Clinical.tsv"


### First 5 columns and 5 rows of Clinical.tsv.gz:

<table style="width:100%; border: 1px solid black;">
	<tr>
		<th>Sample</th>
		<th>Relapse</th>

	</tr>
	<tr>
		<td>GSM260728</td>
		<td>Non-relapse</td>

	</tr>
	<tr>
		<td>GSM260729</td>
		<td>Relapse</td>

	</tr>
	<tr>
		<td>GSM260730</td>
		<td>Non-relapse</td>

	</tr>
	<tr>
		<td>GSM260731</td>
		<td>Non-relapse</td>

	</tr>
</table>
&#9989;	First column of "Clinical.tsv.gz" is titled "Sample"

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

### Comparing Samples

&#9989;	Samples are the same in all data files

#### Results: PASS
---
### Testing Directory after cleanup . . .

#### Results: PASS
---
