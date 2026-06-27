---
role: proof
locale: en
of_concept: commutator-expansion-formula
source_book: gtm009
source_chapter: "21"
source_section: "21.4"
---

Use induction on $k$. The case $k = 1$ is the identity $[y, z] = [y, z]$.

For the induction step, assume the formula holds for $k$ and compute:

$$[y^{k+1}, z] = y[y^k, z] + [y, z]y^k.$$

Substituting the induction hypothesis for $[y^k, z]$:

$$[y^{k+1}, z] = y\left(\binom{k}{1}[y, z]y^{k-1} + \binom{k}{2}[y, [y, z]]y^{k-2} + \cdots + [y, [y, \ldots, [y, z] \ldots]]\right) + [y, z]y^k.$$

Using the identity $\binom{k}{i-1} + \binom{k}{i} = \binom{k+1}{i}$ to combine the coefficients of terms with the same iterated commutator appearing in the two sums, we obtain the formula for $k+1$. The induction step is straightforward and completes the proof.
