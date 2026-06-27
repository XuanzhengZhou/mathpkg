---
role: proof
locale: en
of_concept: trivial-summand-existence-for-vector-bundles
source_book: gtm020
source_chapter: "9"
source_section: "1"
---

Let $\xi_0$ denote the subbundle of nonzero vectors of $\xi$. The fibre of $\xi_0$ is $F^k \setminus \{0\}$, which is $(ck-2)$-connected. By Theorem 2(7.1) (the obstruction-theoretic existence theorem for cross sections), under the hypothesis $n \leq ck-1 = (ck-2) + 1$, the bundle $\xi_0$ admits a cross section $s: X \to \xi_0$.

This cross section can be viewed as an everywhere-nonzero cross section of $\xi$. Define a monomorphism $u: \theta^1 \to \xi$ by
$$u(b, a) = a \cdot s(b)$$
for $(b, a) \in X \times F = E(\theta^1)$, where scalar multiplication uses the $F$-vector bundle structure.

Let $\eta$ be the cokernel of $u$. By 3(8.2), $\eta$ is a vector bundle (the quotient of a vector bundle by a subbundle exists for paracompact base spaces). Since $X$ is a CW-complex, it is paracompact, so by 3(9.6) there is an isomorphism
$$\xi \cong \eta \oplus \theta^1,$$
completing the proof.
