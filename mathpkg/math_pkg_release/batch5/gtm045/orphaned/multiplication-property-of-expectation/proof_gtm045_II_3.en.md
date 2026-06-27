---
role: proof
locale: en
of_concept: multiplication-property-of-expectation
source_book: gtm045
source_chapter: "Introductory Part, II"
source_section: "3. Independence"
---
It suffices to give the proof for two independent simple random variables,

$$X = \sum_{j=1}^{m} x_j I_{A_j}, \quad Y = \sum_{k=1}^{n} y_k I_{B_k},$$

with all $x_j$ (respectively $y_k$) distinct, since the general case follows by induction. Because of independence,

$$EXY = E \sum_{j=1}^{m} \sum_{k=1}^{n} x_j y_k I_{A_j B_k} = \sum_{j=1}^{m} \sum_{k=1}^{n} x_j y_k P(A_j B_k)$$

$$= \sum_{j=1}^{m} \sum_{k=1}^{n} x_j y_k P A_j P B_k = \left(\sum_{j=1}^{m} x_j P A_j\right) \left(\sum_{k=1}^{n} y_k P B_k\right) = EX \cdot EY.$$

The third equality uses independence: $P(A_j B_k) = P A_j \cdot P B_k$.
