---
role: proof
locale: en
of_concept: lightcone-is-lightlike-submanifold
source_book: gtm048
source_chapter: "1"
source_section: "1.1"
---

Regard $(V, g)$ as a Lorentzian manifold. The function $f: V \to \mathbb{R}$ defined by $f(v) = g(v, v)$ is smooth. The lightcone $\mathcal{L}_0 = f^{-1}(0) \setminus \{0\}$ is the zero-set of $f$ with the origin removed. Since $df_v(w) = 2g(v, w)$, for any $v \in \mathcal{L}_0$ we have $df_v \neq 0$ (otherwise $v$ would be orthogonal to all of $V$, contradicting non-degeneracy of $g$). Thus $0$ is a regular value of $f|_{V \setminus \{0\}}$, and $\mathcal{L}_0$ is a smooth hypersurface (submanifold of codimension 1) in $V$.

To determine the causal character of $\mathcal{L}_0$: for any $v \in \mathcal{L}_0$, the tangent space $T_v \mathcal{L}_0 = \ker df_v = v^\perp$. Since $v$ is lightlike ($g(v, v) = 0$), by Lemma 1.1.3(b), the subspace $\operatorname{span}\{v\}$ is lightlike. Then $v^\perp$ contains $v$ itself and cannot contain any timelike vector (otherwise its orthogonal complement would be spacelike by Lemma 1.1.3(a), but it contains the lightlike $v$). Thus $v^\perp$ is lightlike, making $\mathcal{L}_0$ a lightlike submanifold.

For the timelike vectors $\mathcal{T}_0 = \{v \in V \mid g(v, v) < 0\}$: this is an open subset (preimage of $(-\infty, 0)$ under the continuous map $f$), hence an open submanifold. Choosing a timelike vector $e \in V$, define $\mathcal{T}_0^+ = \{v \in \mathcal{T}_0 \mid g(e, v) < 0\}$ and $\mathcal{T}_0^- = \{v \in \mathcal{T}_0 \mid g(e, v) > 0\}$. The function $v \mapsto g(e, v)$ is continuous and non-zero on $\mathcal{T}_0$ (by the reverse Schwarz inequality, Exercise 1.1.10), so $\mathcal{T}_0^+$ and $\mathcal{T}_0^-$ are disjoint open sets partitioning $\mathcal{T}_0$, giving two connected components. Using an orthonormal basis, each component is diffeomorphic to $\mathbb{R}^N$.

For $N \geq 3$, the same reasoning applied to $\mathcal{L}_0$ (with the splitting given by the sign of $g(e, v)$) yields two components $\mathcal{L}_0^+$ and $\mathcal{L}_0^-$, each diffeomorphic to $\mathbb{R} \times S^{N-2}$.
