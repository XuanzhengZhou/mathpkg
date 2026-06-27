---
role: proof
locale: en
of_concept: acf-decidability
source_book: gtm053
source_chapter: "4"
source_section: "4.12"
---

The explicit axiomatizations of $\text{ACF}_p$ and $\text{RCF}$ are clearly recursive; hence decidability follows from the general proposition.

For the incomplete theory $\text{ACF}$ (axiomatized by the recursive set of axioms 4.1, I and II), we use a refinement of the same argument. We know that if a sentence $P$ is not deducible from $\text{ACF}$, then $\neg P$ is consistent with some $\text{ACF}_p$, for $p$ prime or $0$. 

There is an obvious enumeration of the family $\{\text{ACF}_p : p \in \text{Primes} \cup \{0\}\}$: for each $p$ and number $n$ we can effectively produce an axiom $S_{pn} \in \text{ACF}_p$, listing eventually all of the axioms. This can be extended to an algorithm that for each $n \in \mathbf{N}$ produces formulas $P_{p,k}$, $p = 0$ or prime, $k \in \mathbf{N}$, $p, k \leq n$, such that $\{P_{p,k} : k \in \mathbf{N}\} = \text{ACF}_p$.

Now, given a sentence $P$, run an algorithm that for increasing $n \in \mathbf{N}$ produces the first $n$ consequences of $\text{ACF}$ together with the first $n$ axioms of each $\text{ACF}_p$ for $p \leq n$. Check whether $P$ appears among the consequences of $\text{ACF}$, or whether $\neg P$ is consistent with each $\text{ACF}_p$ considered so far. By the structure of the family, one of these conditions must eventually be verified, deciding whether $P \in \text{ACF}$.
