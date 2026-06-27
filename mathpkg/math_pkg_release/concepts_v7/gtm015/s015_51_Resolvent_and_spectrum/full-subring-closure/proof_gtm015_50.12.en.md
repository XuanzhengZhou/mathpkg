---
role: proof
locale: en
of_concept: full-subring-closure
source_book: gtm015
source_chapter: "50"
source_section: "50.12"
---

# Proof of Closure of a Full Subring

**Proof.** Let $B$ be a full subring of $A$ and let $x \in \bar{B}$. We must show that if $x$ is invertible in $A$, then $x^{-1} \in \bar{B}$. 

Choose a sequence $(x_n)$ in $B$ such that $x_n \to x$. Since $x$ is invertible, $x_n$ is eventually invertible (50.5) and $x_n^{-1} \to x^{-1}$ (50.7). By hypothesis, $B$ is a full subring, so $x_n^{-1} \in B$ for all $n$. Therefore $x^{-1} = \lim x_n^{-1} \in \bar{B}$. Thus $\bar{B}$ is a full subring.
