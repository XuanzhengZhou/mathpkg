---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The Display Lemma is the technical core of self-reference in SAr. Given any formula $P(x)$, one can construct a modified formula $P_E(x) = P(x \cdot 10^x)$ such that an expression $Q$ satisfies $P_E$ exactly when the display of $Q$ (the concatenation $Q * Q*$) satisfies $P$. The proof relies on the numerical identity $n(Q * Q*) = n(Q) \cdot 10^{n(Q)}$, which follows from the specific Gödel numbering where $\bar{1}$ is assigned digit 9 and numbers are read in decimal. This lemma is the SAr analogue of the self-reference mechanism in the language SELF (where $E$ acts as the display operator), and it directly enables the proof of Tarski's undefinability theorem.
