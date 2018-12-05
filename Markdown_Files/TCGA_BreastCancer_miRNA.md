#TCGA_BreastCancer_miRNA
## Status: False
#### Date: 08/17/18
Only files in the "TCGA_BreastCancer_miRNA" or "Helper" directory should be changed. The following files were also changed in this branch:
- GSE62944_Tumor_TPM/cleanup.sh
- GSE62944_Tumor_TPM/parse.py
- GSE62944_Tumor_TPM/parse.sh
- GSE62944_Tumor_TPM/scrapeWebTCGA.R
- GSE62944_Tumor_TPM/translate.py
- TCGA_BreastCancer_CNV/download.sh
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

Executing /Shared/testing/TCGA_BreastCancer_miRNA/install.sh: Success

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

&#9989;	description.md exists.

&#9989;	config.yaml exists.

#### Results: PASS
---
### Running user scripts . . .

Executing /Shared/testing/TCGA_BreastCancer_miRNA/install.sh: Success

Executing /Shared/testing/TCGA_BreastCancer_miRNA/download.sh: Success

Executing /Shared/testing/TCGA_BreastCancer_miRNA/parse.sh: Success

&#9989;	miRNA.tsv.gz was created and zipped correctly.

&#9989;	Clinical.tsv.gz was created and zipped correctly.

#### Results: PASS
---
### Testing Test Files:

&#10060;	Test file test_data.tsv is missing required data file "data.tsv.gz"

#### Results: FAIL


### Testing Directory after cleanup . . .

#### Results: PASS
---
