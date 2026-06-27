---
role: proof
locale: en
of_concept: whitney-ctopology-product-homeomorphism
source_book: gtm014
source_chapter: "II"
source_section: "3"
---

**Proof.** Define $\Phi: C^\infty(X, Y) \times C^\infty(X, Z) \to C^\infty(X, Y \times Z)$ by $\Phi(f, g) = f \times g$, where $(f \times g)(x) = (f(x), g(x))$. Define $\Psi: C^\infty(X, Y \times Z) \to C^\infty(X, Y) \times C^\infty(X, Z)$ by $\Psi(h) = (\pi_Y \circ h, \pi_Z \circ h)$ where $\pi_Y, \pi_Z$ are the canonical projections. Clearly $\Phi$ and $\Psi$ are mutual inverses, so the identification is a set-theoretic bijection.

To prove $\Phi$ is a homeomorphism in the Whitney $C^\infty$ topology, it suffices to prove that $\Phi$ and $\Psi$ are continuous in each Whitney $C^k$ topology for all $k \ge 0$. The $k$-jet extension satisfies
$$j^k(f \times g)(x) \in J^k(X, Y \times Z) \cong J^k(X, Y) \times_X J^k(X, Z),$$
where the fiber product $J^k(X, Y) \times_X J^k(X, Z)$ consists of pairs $(\sigma, \tau)$ with $\alpha(\sigma) = \alpha(\tau) = x$.

For continuity of $\Phi$: Given a subbasic open set $M(S) \subset C^\infty(X, Y \times Z)$ with $S \subset J^k(X, Y \times Z)$ open, suppose $f \times g \in M(S)$. Then $S$ is an open neighborhood of $j^k(f \times g)(X)$ in $J^k(X, Y \times Z)$. Identifying $J^k(X, Y \times Z)$ with the fiber product $J^k(X, Y) \times_X J^k(X, Z)$, we can apply Lemma 3.7 with $A = J^k(X, Y)$, $B = J^k(X, Z)$, $P = X$, $\pi_A = \alpha$, $\pi_B = \alpha$, $K = j^k f(X)$, $L = j^k g(X)$. Since $\alpha$ restricted to the compact images of $k$-jets under $f$ and $g$ is proper, Lemma 3.7 provides neighborhoods $V$ of $j^k f(X)$ and $W$ of $j^k g(X)$ such that $V \times_X W \subset S$. Then $M(V) \times M(W) \subset \Phi^{-1}(M(S))$, proving continuity.

Continuity of $\Psi$ follows directly from the continuity of post-composition with the smooth projections $\pi_Y$ and $\pi_Z$, which induce continuous maps between $C^\infty$ spaces in the Whitney topology. Specifically, $(\pi_Y)_*: C^\infty(X, Y \times Z) \to C^\infty(X, Y)$ and $(\pi_Z)_*: C^\infty(X, Y \times Z) \to C^\infty(X, Z)$ are continuous, so their product $\Psi$ is continuous.
