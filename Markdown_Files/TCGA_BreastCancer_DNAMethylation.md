# TCGA_BreastCancer_DNAMethylation
## Status: False
#### Date: 07/31/18
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

Executing /app/testing/TCGA_BreastCancer_DNAMethylation/install.sh: 

&#10060;	install.sh returned an error:
```bash
mkdir: cannot create directory ‘//Rlib’: Permission denied
Warning in install.packages("readr", lib = "~/Rlib", repos = "https://cloud.r-project.org/") :
  'lib = "~/Rlib"' is not writable
Error in install.packages("readr", lib = "~/Rlib", repos = "https://cloud.r-project.org/") : 
  unable to install packages
Execution halted
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

Executing /app/testing/TCGA_BreastCancer_DNAMethylation/install.sh: 

&#10060;	install.sh returned an error:
```bash
mkdir: cannot create directory ‘//Rlib’: Permission denied
Warning in install.packages("readr", lib = "~/Rlib", repos = "https://cloud.r-project.org/") :
  'lib = "~/Rlib"' is not writable
Error in install.packages("readr", lib = "~/Rlib", repos = "https://cloud.r-project.org/") : 
  unable to install packages
Execution halted
```

#### Results: **<font color="red">FAIL</font>**
---
