---
role: proof
locale: en
of_concept: lemma-positive-epsilon-set
source_book: gtm018
source_chapter: "31"
source_section: "31. The Radon-Nikodym Theorem"
---

Let $X = A_n \cup B_n$ be a Hahn decomposition with respect to the signed measure $\nu - \frac{1}{n}\mu$, $n = 1, 2, \dots$, and write

$$A_0 = \bigcup_{n=1}^{\infty} A_n, \quad B_0 = \bigcap_{n=1}^{\infty} B_n.$$

Since $B_0 \subset B_n$, we have

$$0 \leq \nu(B_0) \leq \frac{1}{n}\mu(B_0)$$

for every $n = 1, 2, \dots$. It follows that $\nu(B_0) = 0$. Since $\nu$ is not identically zero, we must have $\nu(A_0) > 0$, and consequently, by absolute continuity ($\nu \ll \mu$), $\mu(A_0) > 0$. Hence there exists a positive integer $n$ such that $\mu(A_n) > 0$; we take $\varepsilon = \frac{1}{n}$ and $A = A_n$. By definition of the Hahn decomposition, $A_n$ is a positive set for $\nu - \frac{1}{n}\mu = \nu - \varepsilon\mu$, completing the proof.
