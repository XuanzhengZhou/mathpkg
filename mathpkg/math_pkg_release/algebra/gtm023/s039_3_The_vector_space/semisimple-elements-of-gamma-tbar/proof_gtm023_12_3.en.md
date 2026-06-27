---
role: proof
locale: en
of_concept: semisimple-elements-of-gamma-tbar
source_book: gtm023
source_chapter: "12"
source_section: "3"
---

**Proof of 4):** We show first that every element in $A$ is semisimple. Let $\bar{x} \in A$. Then, by Theorem IV, sec. 12.16, there are elements $\bar{x}_S \in \Gamma(\bar{x})$, $\bar{x}_N \in \Gamma(\bar{x})$ such that $\bar{x}_S$ is semisimple, $\bar{x}_N$ is nilpotent and
$$
\bar{x} = \bar{x}_S + \bar{x}_N.
$$
In particular, $\bar{x}_N$ is nilpotent in $A$. Since $A$ is a direct sum of fields (by part 1), it contains no nonzero nilpotent elements. Thus $\bar{x}_N = 0$ and so $\bar{x}$ is semisimple.

Conversely, let $\bar{x} \in \Gamma(\bar{t})$ be semisimple. In view of the direct sum decomposition (statement 3) we can write
$$
\bar{x} = \bar{x}_A + \bar{x}_R \quad \bar{x}_A \in A, \quad \bar{x}_R \in \operatorname{rad} \Gamma(\bar{t}). \tag{12.38}
$$
Then $\bar{x}_A$ is semisimple (by the first part) and $\bar{x}_R$ is nilpotent (since it lies in the radical). Thus (12.38) must be the unique decomposition of $\bar{x}$ into its semisimple and nilpotent parts. Since $\bar{x}$ is semisimple it follows that $\bar{x}_R = 0$ whence $\bar{x} \in A$.
