# BiomarkerBenchmark_GSE37745
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

Executing /Shared/testing/BiomarkerBenchmark_GSE37745/install.sh: Success

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

&#9989;	description.md exists.

&#9989;	config.yaml exists.

#### Results: PASS
---
### Running user scripts . . .

Executing /Shared/testing/BiomarkerBenchmark_GSE37745/install.sh: Success

Executing /Shared/testing/BiomarkerBenchmark_GSE37745/download.sh: Success

Executing /Shared/testing/BiomarkerBenchmark_GSE37745/parse.sh: Success

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
		<td>GSM1019138</td>
		<td>2.38672876470588</td>
		<td>-0.2312441775</td>
		<td>2.39797594555556</td>
		<td>0.8360657109375</td>

	</tr>
	<tr>
		<td>GSM1019140</td>
		<td>2.12064393</td>
		<td>-0.24214592875</td>
		<td>2.11962213888889</td>
		<td>0.7670303515625</td>

	</tr>
	<tr>
		<td>GSM1019143</td>
		<td>1.38787672176471</td>
		<td>-0.2046060075</td>
		<td>1.98675505111111</td>
		<td>0.8303490778125</td>

	</tr>
	<tr>
		<td>GSM1019144</td>
		<td>1.72496427294118</td>
		<td>-0.21692284875</td>
		<td>2.02115597777778</td>
		<td>0.5870620659375</td>

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
		<th>adjuvant_treatment</th>
		<th>age</th>
		<th>days_to_determined_death_status</th>
		<th>days_to_recurrence__to_last_visit</th>

	</tr>
	<tr>
		<td>GSM1019138</td>
		<td>no</td>
		<td>66</td>
		<td>3418</td>
		<td>2637</td>

	</tr>
	<tr>
		<td>GSM1019139</td>
		<td>no</td>
		<td>66</td>
		<td>3186</td>
		<td>3223</td>

	</tr>
	<tr>
		<td>GSM1019140</td>
		<td>no</td>
		<td>77</td>
		<td>162</td>
		<td>154</td>

	</tr>
	<tr>
		<td>GSM1019141</td>
		<td>NA</td>
		<td>72</td>
		<td>6</td>
		<td>NA</td>

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
