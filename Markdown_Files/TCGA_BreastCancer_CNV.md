#TCGA_BreastCancer_CNV
## Status: False
#### Date: 08/08/18
Only files in the "TCGA_BreastCancer_CNV" or "Helper" directory should be changed. The following files were also changed in this branch:
- GSE62944_Tumor_TPM/cleanup.sh
- GSE62944_Tumor_TPM/parse.py
- GSE62944_Tumor_TPM/parse.sh
- GSE62944_Tumor_TPM/scrapeWebTCGA.R
- GSE62944_Tumor_TPM/translate.py
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

Executing /app/testing/TCGA_BreastCancer_CNV/install.sh: Success

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

&#9989;	description.md exists.

&#9989;	config.yaml exists.

#### Results: PASS
---
### Running user scripts . . .

Executing /app/testing/TCGA_BreastCancer_CNV/install.sh: Success

Executing /app/testing/TCGA_BreastCancer_CNV/download.sh: Success

Executing /app/testing/TCGA_BreastCancer_CNV/parse.sh: Success

&#9989;	data.tsv.gz was created and zipped correctly.

&#9989;	metadata.tsv.gz was created and zipped correctly.

&#9989;	Clinical.tsv.gz was created and zipped correctly.

#### Results: PASS
---
### Testing Test Files:

&#10060;	Data file metadata.tsv.gz is missing required test file "test_metadata.tsv"

#### Results: FAIL


### Testing Directory after cleanup . . .

&#10060;	"Clinical.tsv.gz" should have been deleted during cleanup.

#### Results: **<font color="red">FAIL</font>**
---
