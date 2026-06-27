---
role: proof
locale: en
of_concept: homomorphism-determined-by-spanning-set
source_book: gtm013
source_chapter: "1"
source_section: "3. Homomorphisms of Modules"
---

**Proof.** The first statement follows from (2.7) in view of the fact that
$$\text{Im}\, f = f(RX) = Rf(X).$$

One implication in the final statement is trivial. For the converse, suppose $f(x) = g(x)$ for all $x \in X$. It is easy to check that
$$K = \{ y \in M \mid f(y) = g(y) \}$$
is a submodule of $M$. But since $X \subseteq K$, we have $M = RX \subseteq K$ by (2.3). Thus $f(y) = g(y)$ for all $y \in M$. $\square$
