---
role: proof
locale: en
of_concept: equivalence-preserves-abscissa-of-absolute-convergence
source_book: gtm041
source_chapter: "8"
source_section: "8.7"
---

**Proof.** Equivalence implies $|b(n)| = |a(n)|$, so the series have the same abscissa of absolute convergence.

Now let $B$ and $\Gamma$ be two bases for $\Lambda$, and assume that two series are equivalent with respect to $B$. We will show that they are also equivalent with respect to $\Gamma$. The equivalence with respect to $B$ means there exists a real sequence $Y = \{y_n\}$ such that

$$b(n) = a(n)e^{ix_n}, \quad \text{where} \quad X = \{x_n\} = R_B Y.$$

We need to find a real sequence $V = \{v_n\}$ such that $X = R_\Gamma V$, where $R_\Gamma$ is the Bohr matrix expressing $\Lambda$ in terms of $\Gamma$. Since $\Gamma = AB$ for some Bohr matrix $A$, we have $R_\Gamma A = R_B$. Setting $V = AY$ gives

$$R_\Gamma V = R_\Gamma A Y = R_B Y = X,$$

which shows that the two series are also equivalent with respect to $\Gamma$. This completes the proof.
