---
role: proof
locale: en
of_concept: maximum-condition-induction
source_book: gtm030
source_chapter: "Chapter VI"
source_section: "4. The chain conditions"
---

**Proof.** Assume the maximum condition holds. Let $\mathcal{C}$ be the collection of submodules $\mathfrak{N}$ such that $P(\mathfrak{N})$ is false. If $\mathcal{C}$ is non-vacuous, then by the maximum condition $\mathcal{C}$ contains a maximal element $\mathfrak{N}_0$. For any submodule $\mathfrak{N}'$ strictly containing $\mathfrak{N}_0$, we have $\mathfrak{N}' \notin \mathcal{C}$, so $P(\mathfrak{N}')$ holds. By the hypothesis on $P$, it follows that $P(\mathfrak{N}_0)$ holds, contradicting $\mathfrak{N}_0 \in \mathcal{C}$. Hence $\mathcal{C}$ must be empty, and $P(\mathfrak{N})$ is true for all submodules $\mathfrak{N}$.
