---
role: proof
locale: en
of_concept: addition-property-of-expectation
source_book: gtm045
source_chapter: "Introductory Part, II"
source_section: "2. Simple random variables"
---
It suffices to prove the assertion for a sum of two simple random variables

$$X = \sum_{j=1}^{m} x_j I_{A_j}, \quad Y = \sum_{k=1}^{n} y_k I_{B_k},$$

since the general case follows by induction. Because of the properties of probabilities and indicators,

$$EX + EY = \sum_{j=1}^{m} x_j PA_j + \sum_{k=1}^{n} y_k PB_k = \sum_{j=1}^{m} \sum_{k=1}^{n} (x_j + y_k) PA_j B_k$$

while

$$E(X + Y) = E \sum_{j=1}^{m} \sum_{k=1}^{n} (x_j + y_k) I_{A_j B_k} = \sum_{j=1}^{m} \sum_{k=1}^{n} (x_j + y_k) PA_j B_k.$$

The two expressions are identical, proving the result.
