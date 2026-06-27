---
role: proof
locale: en
of_concept: continuity-theorem-characteristic-functions
source_book: gtm017
source_chapter: "IV"
source_section: "b"
---
The proof shows that $\varphi_n(t) \to \varphi(t)$ pointwise with $\varphi$ continuous at 0 implies:
1. The sequence $\{F_n\}$ is tight (uniformly bounded tail probabilities).
2. Every subsequence has a further subsequence converging weakly to some distribution function $F$.
3. The limit of any convergent subsequence has characteristic function $\varphi$.
4. By uniqueness of characteristic functions, all subsequential limits coincide, so $F_n \to F$ completely.

The key estimate: $1 - \Re \varphi(t) = \int (1 - \cos tx) dF(x) \geq \int_{|x| \geq 2/|t|} 2 dF(x)$. Since $\varphi$ is continuous at 0, tails are uniformly small.
