---
role: proof
locale: en
of_concept: klee-biuniform-characterization
source_book: gtm015
source_chapter: "10"
source_section: "Bi-uniform topological groups"
---

# Proof of Klee's theorem: metrizable bi-uniform iff bi-invariant metric exists

Let $G$ be a metrizable topological group.

**($\Leftarrow$)** If $G$ admits a bi-invariant compatible metric $d$, then $G$ is bi-uniform by Lemma (10.4).

**($\Rightarrow$)** Conversely, suppose $G$ is bi-uniform, i.e., $\mathcal{U}_s = \mathcal{U}_r$. In the proof of the Birkhoff-Kakutani metrization theorem (6.3), one constructs a sequence of symmetric neighborhoods $V_n$ of $e$ satisfying $V_{n+1}^3 \subset V_n$.

By (10.2), the bi-uniformity condition $\mathcal{U}_s = \mathcal{U}_r$ implies that for every neighborhood $V$ of $e$, the set $\bigcap_{a \in G} a V a^{-1}$ is also a neighborhood of $e$. Consequently, in the construction of the $V_n$, one may choose them to be invariant under all inner automorphisms of $G$, i.e., $a V_n a^{-1} = V_n$ for all $a \in G$.

The function $f(x, y) = \min\{(\frac{1}{2})^k : x^{-1}y \in V_k\}$ (with $f(x, x) = 0$) then satisfies the hypotheses of Lemma (6.2), yielding a left-invariant compatible metric $d$. Since $x^{-1}y \in V_n$ iff $(a x a^{-1})^{-1}(a y a^{-1}) = a(x^{-1}y)a^{-1} \in V_n$ (because $V_n$ is invariant under inner automorphisms), we have

$$f(a x a^{-1}, a y a^{-1}) = f(x, y)$$

for all $a, x, y \in G$. The construction of $d$ from $f$ via Lemma (6.2) then yields

$$d(a x a^{-1}, a y a^{-1}) = d(x, y)$$

for all $a, x, y$. From this we deduce right-invariance:

$$d(x a, y a) = d(a(x a)a^{-1}, a(y a)a^{-1}) = d(a x, a y) = d(x, y).$$

Thus $d$ is both left- and right-invariant, i.e., bi-invariant.
