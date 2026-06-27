---
role: proof
locale: en
of_concept: proposition-1-16
source_book: gtm040
source_chapter: "1"
source_section: "16"
---

Proof: Write $B_n = A_n - (\bigcup_{k=1}^{n-1} A_k)$. The sets $B_n$ are disjoint in pairs, and consequently the sets $A \cap B_n$ are also disjoint. Furthermore, $\bigcup_n B_n = \bigcup_n A_n$ so that

$$A = A \cap (\bigcup_n A_n)$$

$$= A \cap (\bigcup_n B_n)$$

$$= \bigcup_n (A \cap B_n).$$

By hypothesis $\mu$ is a measure. It is therefore completely additive and

$$\mu(A) = \sum_n \mu(A \cap B_n)$$

$$\leq \sum_n \mu(B_n) \quad \text{since } A \cap B_n \subset B_n$$

$$\leq \sum_n \mu(A_n) \quad \text{since } B_n \subset A_n.$$

To conclude this section we shall establish a result known as the Extension Theorem. The proof follows the proof of Rudin [1953].

Theorem 1-19: Let $\mathcal{F}$ be a field of sets in a space $X$ and let $\nu$ be a measure defined on $\mathcal{F}$. Suppose $X$ can be written as the denumerable union of sets in $\mathcal{F}$ of finite measure. If $\mathcal{G}$ is the smallest Borel field containing $\mathcal{F}$, then $\nu$ can be extended in one and only one way to a measure defined on all of $\mathcal{G}$ which agrees with $\nu$ on sets of $\mathcal{F}$.

Before proving the theorem, we need some preliminary lemmas and definitions. The property in the statement of the theorem that $X$ is the denumerable union of sets of finite measure is summarized by saying that $\nu$ is sigma-finite

Proof: We see that $\mu$ is non-negative because $\mu$ is the limit of non-negative quantities. If $A \subset B$, then $\mu(A) \leq \mu(B)$ because every covering of $B$ is a covering of $A$. Let $C$ be in $\mathcal{F}$. Then $\{C\}$ is a covering of $C$ and $\mu(C) \leq \nu(C)$. And for any covering $\{C_n\}$,

$$\nu(C) \leq \sum_n \nu(C_n)$$

by Proposition 1-18. Therefore,

$$\nu(C) \leq \inf \sum_n \nu(C_n) = \mu(C).$$

Lemma 1-21: If $\{A_n\}$ is an arbitrary sequence of subsets of $X$ and if $A = \bigcup_n A_n$, then $\mu(A) \leq \sum_n \mu(A_n)$.

Proof: Let $\epsilon > 0$ be given. Let $\{B_k^{(n)}\}$ with $k = 1, 2, 3, \ldots$ be a denumerable covering of $A_n$ such that $B_k^{(n)}$ is in $\mathcal{F}$ and $\sum_k \nu(B_k^{(n)}) \leq \mu(A_n) + \epsilon/2^n$. This choice is possible by the definition of $\mu$. Then since all the $B$'s form a covering of $A$, we have

$$\mu(A) \leq \sum_n \sum_k \nu(B_k^{(n)})$$

$$\leq \sum_n \mu(A_n) + \epsilon$$

and the assertion follows.

We define a set theoretic operation $\oplus$ for subsets of $X$ by

$$A \oplus B = (A \cap \tilde{B}) \cup (B \cap \tilde{A}).$$

The set $A \oplus B$ is called the symmetric difference of $A$ and $B$. A point is in $A \oplus B$ if it is in $A$ or $B$ but not both. We leave the details of the proof of the next lemma to the reader.

Lemma 1-22: The subsets of a

and by Lemmas 1-20 and 1-21

$$\mu(A) \leq d(A, B) + \mu(B).$$

Replacing $A$ by $A \oplus B$ and $B$ by $C \oplus B$, we obtain the triangle inequality

$$d(A, B) \leq d(A, C) + d(C, B).$$
