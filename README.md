# [cite_start]Password Security Auditing with John the Ripper [cite: 1]

## Project Overview
[cite_start]The objective was to demonstrate how John the Ripper identifies weak passwords using wordlists and hash algorithms[cite: 2].

## Environment & Tools
* [cite_start]**Operating System**: Kali Linux[cite: 38].
* [cite_start]**Virtualization**: Oracle VirtualBox[cite: 38].
* [cite_start]**Primary Tool**: John the Ripper v1.9.0-jumbo-1[cite: 2, 40, 47].
* [cite_start]**Hash Algorithms**: Support for various types including MD5 and SHA-1[cite: 7].

## Attack Methodologies
[cite_start]The lab explored three primary password cracking methods[cite: 12]:
* [cite_start]**Dictionary Attacks**: Rely on a precompiled wordlist of likely passwords, comparing each to the target hash[cite: 13, 14].
* [cite_start]**Brute-Force Attacks**: Systematically try every possible character combination (letters, numbers, symbols) until the correct password is found[cite: 16].
* [cite_start]**Hybrid Attacks**: Combine dictionary speed with brute-force thoroughness by adding common variations to wordlist entries[cite: 18, 19].

## Lab Execution & Findings
* [cite_start]**Vulnerability Assessment**: Simple passwords like "password123" are highly probable to be found quickly using wordlists[cite: 4, 5].
* [cite_start]**Cracking Results**: Successfully cracked weak passwords (e.g., "123456" and "larry") using different hashing methods[cite: 15, 60, 66].
* [cite_start]**Algorithm Impact**: Older algorithms like MD5 are faster to crack because they often lack complexity and modern "salt" mechanisms[cite: 8].

## Ethical & Legal Considerations
* [cite_start]**Consent**: Explicit permission must be secured before attempting to crack any password[cite: 24].
* [cite_start]**Legal Compliance**: Unauthorized password cracking is illegal under laws like the CFAA and GDPR[cite: 26, 27].
* [cite_start]**Responsibility**: Ethical hackers must always respect privacy and operate within strictly defined boundaries[cite: 25, 28].

##  Security Recommendations
* [cite_start]**Password Policy**: Organizations must enforce policies requiring minimum length and complexity for all passwords[cite: 33].
* [cite_start]**Layered Defense**: Multi-Factor Authentication (MFA) should be mandated as an essential second layer of protection[cite: 34].
