---
role: proof
locale: en
of_concept: bounded-formula-subalgebra-invariance
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

The proof proceeds by induction on the number of logical symbols in $\varphi$.

**Base case.** If $\varphi$ is atomic (i.e., $u \in v$ or $u = v$), the result is exactly Theorem 13.15.

**Inductive steps for propositional connectives.** If $\varphi = \neg \psi$, then $[\![\varphi]\!]^{(B)} = -[\![\psi]\!]^{(B)} = -[\![\psi]\!]^{(B')} = [\![\varphi]\!]^{(B')}$ by the induction hypothesis. The cases for $\wedge$, $\vee$, and $\rightarrow$ are similar.

**Inductive step for bounded quantifiers.** The only nontrivial case is when
$$\varphi(u, u_1, \ldots, u_n) = (\exists x \in u) \psi(x, u, u_1, \ldots, u_n).$$

By Theorem 13.13:
$$[\![\varphi(u, u_1, \ldots, u_n)]\!]^{(B)} = \sum_{x \in \mathcal{D}(u)} u(x) \cdot [\![\psi(x, u, u_1, \ldots, u_n)]\!]^{(B)}.$$

Since $\mathcal{D}(u) \subseteq V^{(B)}$ by assumption, each $x \in \mathcal{D}(u)$ belongs to $V^{(B)}$. By the induction hypothesis, $[\![\psi(x, u, u_1, \ldots, u_n)]\!]^{(B)} = [\![\psi(x, u, u_1, \ldots, u_n)]\!]^{(B')}$ for each $x$. Moreover, the supremum $\sum_{x \in \mathcal{D}(u)}$ over values in $B$ is the same whether computed in $B$ or in $B'$, since $B$ is a complete subalgebra of $B'$.

Thus:
$$[\![\varphi]\!]^{(B)} = \sum_{x \in \mathcal{D}(u)} u(x) \cdot [\![\psi]\!]^{(B')} = [\![\varphi]\!]^{(B')}.$$

The case for the bounded universal quantifier $(\forall x \in u) \psi$ is treated dually using Boolean products.
