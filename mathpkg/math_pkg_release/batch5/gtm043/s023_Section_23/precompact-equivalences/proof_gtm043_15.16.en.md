---
role: proof
locale: en
of_concept: precompact-equivalences
source_book: gtm043
source_chapter: "15"
source_section: "23"
---

(1) implies (2). A $d$-discrete set in $X$ is $d$-discrete in $\gamma X$, and hence is closed and discrete in the compact space $\gamma X$, so it must be finite.

(2) implies (3). Suppose that for some $d \in \mathcal{D}$ and $\epsilon > 0$, $X$ is not the union of any finite number of zero-sets of $d$-diameter $\leq \epsilon$. Inductively, choose $x_n$ in the complement of
$$\bigcup_{k=1}^{n-1} \{x : d(x, x_k) \leq \epsilon/2\}.$$
The set $\{x_n\}_{n \in \mathbf{N}}$ is obviously infinite and $d$-discrete, contradicting (2).

(3) implies (4). Every $z$-ultrafilter is prime; using (3), one shows that every $z$-ultrafilter contains arbitrarily small sets, hence is a Cauchy $z$-filter.

(4) implies (1). Under the hypothesis, $\gamma X$ is a continuous image of $\beta X$ (by 15.9(c)), hence compact.

It follows from the theorem that every admissible structure contained in a precompact structure is precompact.
