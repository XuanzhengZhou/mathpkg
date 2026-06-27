---
role: proof
locale: en
of_concept: hilbert-chain-of-syzygies
source_book: gtm004
source_chapter: "VII"
source_section: "7"
---

# Proof of Hilbert's Chain-of-Syzygies Theorem

**Theorem 7.1 (Hilbert).** The global dimension of $P = K[x_1, \ldots, x_m]$ is $m$. Moreover, every projective graded $P$-module is free.

In particular, for any finitely generated $P$-module $M$, there exists a finite free resolution of length at most $m$.

**Proof.** The proof proceeds in several steps.

**Step 1: $\operatorname{gl.dim} P \leq m$.** The Koszul resolution (Proposition 7.2) provides a free resolution of $K$ of length $m$:

$$0 \to D_m \to D_{m-1} \to \cdots \to D_0 \to K \to 0.$$

For the Koszul complex, $D_m \otimes_P K \cong K$ (since $E_m \mathfrak{a} \cong K$), and the map

$$d_m \otimes 1 : D_m \otimes_P K \to D_{m-1} \otimes_P K$$

is the zero map because

$$d_m \langle x_1, \ldots, x_m \rangle = \sum_{i} \pm x_i \langle x_1, \ldots, \hat{x}_i, \ldots, x_m \rangle$$

and $x_i K = 0$ (all variables act as zero on $K$).

Hence $\operatorname{Tor}_m^P(K, K) \cong K \neq 0$. By standard homological dimension theory, $\operatorname{gl.dim} P \geq m$. Combined with the existence of a length-$m$ resolution of $K$, we obtain $\operatorname{gl.dim} P = m$.

**Step 2: Every projective graded $P$-module is free.** Let $B$ be a projective graded $P$-module. Since $\operatorname{Tor}_1^P(B, K) = 0$ (projectivity implies all higher Tor vanish), Theorem 7.4 applies, yielding that $B$ is free.

**Step 3: The chain-of-syzygies.** Let $M$ be a finitely generated graded $P$-module. Construct a free resolution by iteratively taking syzygies:

$$0 \to Z_n \to F_{n-1} \to \cdots \to F_0 \to M \to 0,$$

where each $F_i$ is free and $Z_n$ is the $n$-th syzygy. By Step 2, $Z_m$ is projective, hence free (by the graded Quillen–Suslin theorem, or more elementarily in this context, since $P$ is a polynomial ring over a field). Thus the resolution can be terminated at length $m$ with a free module, giving a finite free resolution.

**Step 4: Hilbert's original formulation.** Classically, Hilbert proved that for any homogeneous ideal $J \subset P$, the syzygy module $Z_m$ (the $m$-th syzygy in a minimal free resolution) is free. In modern homological language, this is equivalent to the statement that $\operatorname{gl.dim} P = m$ and that every projective graded $P$-module is free. $\square$

**Remark.** For the classical statement, note that the graded Nakayama lemma (Proposition 7.3) replaces the usual Nakayama lemma, and the Tor-vanishing criterion (Theorem 7.4) ensures freeness. The proof illustrates the power of homological methods in commutative algebra.
