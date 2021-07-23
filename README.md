# DoctorHelp
[![Build Status](https://travis-ci.com/0x0is1/drhelp.svg?branch=master)](https://travis-ci.com/0x0is1/dehelp)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FStrinTH%2FBSFramework.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2FStrinTH%2FBSFramework?ref=badge_shield)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/0x0is1off@gmail.com)
[![Documentation Status](https://readthedocs.org/projects/drhelp/badge/?version=latest)](https://drhelp.readthedocs.io/en/latest/?badge=latest)

### Microbiology and Viralogy research companion framework

### ***Sample Preview***

Samples available [here](./assets/)

# Installation

```sh
$ git clone https://github.com/0x0is1/DrHelp
$ cd DrHelp
$ pip install -r requirements.txt
$ chmod +x drhelp.sh
$ bash drhelp.sh --shell
```

# Test Run


```sh
$ searchl nuccore covid

output: 
    Trying attempt0...
    1519315500

$ set id=1519315500

output:
    {1: 'id', 2: 'type', 3: 'report', 4: 'doc'}
    {1: '1519315500', 2: 'nuccore', 3: 'genbank', 4: 'html'}

$ get intro

output:
    REFERENCE   8  (bases 1 to 4962)
    AUTHORS   Jeunemaitre X, Lifton RP, Hunt SC, Williams RR and Lalouel JM.
    TITLE     Absence of linkage between the angiotensin converting enzyme locus
                and human essential hypertension
    JOURNAL   Nat. Genet. 1 (1), 72-75 (1992)
    PUBMED   <a href="https://www.ncbi.nlm.nih.gov/pubmed/1338766">1338766</a>
    REFERENCE   9  (bases 1 to 4962)
    AUTHORS   Ehlers MR and Riordan JF.
    TITLE     Angiotensin-converting enzyme: zinc- and inhibitor-binding
                stoichiometries of the somatic and testis isozymes
```


# Documentation
Complete help module and all documentations are available at https://drhelp.readthedocs.io/

### **Support authors**:

[![Donate](./assets/default-pink.png)](https://www.buymeacoffee.com/6dciIwk)

[![Donate](./assets/-460.png)](https://paypal.me/0x0is1?locale.x=en_GB)


## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our [code of conduct](CODE_OF_CONDUCT.md) and the process of submitting pull requests to us.

## License 
[![GitHub license](https://img.shields.io/github/license/StrinTH/DrHelp)](https://github.com/StrinTH/DrHelp/blob/master/LICENSE)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details


[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FStrinTH%2FBSFramework.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2FStrinTH%2FBSFramework?ref=badge_large)

<a href="NOTICE.md">Notice</a>
