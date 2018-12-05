# TCGA_BreastCancer_GDC
## Status: False
#### Date: 07/31/18
Only files in the "TCGA_BreastCancer_GDC" or "Helper" directory should be changed. The following files were also changed in this branch:
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

Executing /app/testing/TCGA_BreastCancer_GDC/install.sh: 

&#10060;	install.sh returned an error:
```bash
cp: cannot stat '../Helper/converTallFormatToWide.py': No such file or directory
```

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

&#9989;	description.md exists.

&#9989;	config.yaml exists.

#### Results: **<font color="red">FAIL</font>**
---
### Running user scripts . . .

Executing /app/testing/TCGA_BreastCancer_GDC/install.sh: 

&#10060;	install.sh returned an error:
```bash
cp: cannot stat '../Helper/converTallFormatToWide.py': No such file or directory
```

#### Results: **<font color="red">FAIL</font>**
---
