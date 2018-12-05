# BiomarkerBenchmark_GSE5460
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

Executing /Shared/testing/BiomarkerBenchmark_GSE5460/install.sh: Success

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

&#9989;	description.md exists.

&#9989;	config.yaml exists.

#### Results: PASS
---
### Running user scripts . . .

Executing /Shared/testing/BiomarkerBenchmark_GSE5460/install.sh: Success

Executing /Shared/testing/BiomarkerBenchmark_GSE5460/download.sh: Success

Executing /Shared/testing/BiomarkerBenchmark_GSE5460/parse.sh: Success

&#9989;	data.tsv.gz was created and zipped correctly.

&#9989;	Clinical.tsv.gz was created and zipped correctly.

#### Results: PASS
---
### Testing Test Files:

#### Running "test_Clinical.tsv"

&#9989;	"test_Clinical.tsv" has three columns with the correct headers

&#9989;	"test_Clinical.tsv" contains enough unique samples to test

&#9989;	"test_Clinical.tsv" has enough features to test (min: 1)

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
		<td>GSM124994</td>
		<td>2.08956412647059</td>
		<td>-0.148133205</td>
		<td>2.25227292</td>
		<td>0.864307255</td>

	</tr>
	<tr>
		<td>GSM124995</td>
		<td>1.26125375588235</td>
		<td>-0.03312075375</td>
		<td>2.04449278444444</td>
		<td>0.5485343171875</td>

	</tr>
	<tr>
		<td>GSM124996</td>
		<td>1.32433761941176</td>
		<td>-0.22014343</td>
		<td>2.37620385</td>
		<td>1.030412526875</td>

	</tr>
	<tr>
		<td>GSM124997</td>
		<td>1.48421910529412</td>
		<td>-0.21437974375</td>
		<td>1.83627522666667</td>
		<td>0.5865589234375</td>

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
		<th>B-R_grade</th>
		<th>ER</th>
		<th>HER2</th>
		<th>LVI</th>

	</tr>
	<tr>
		<td>GSM124994</td>
		<td>III</td>
		<td>neg</td>
		<td>pos</td>
		<td>pos</td>

	</tr>
	<tr>
		<td>GSM124995</td>
		<td>III</td>
		<td>neg</td>
		<td>neg</td>
		<td>neg</td>

	</tr>
	<tr>
		<td>GSM124996</td>
		<td>III</td>
		<td>neg</td>
		<td>pos</td>
		<td>pos</td>

	</tr>
	<tr>
		<td>GSM124997</td>
		<td>III</td>
		<td>neg</td>
		<td>neg</td>
		<td>neg</td>

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
