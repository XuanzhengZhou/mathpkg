---
role: proof
locale: en
of_concept: homotopy-geodesic-length-lemma
source_book: gtm051
source_chapter: "6"
source_section: "6.6"
---

Let $\rho = \pi/\sqrt{K_1}$. Since $K \leq K_1$, (6.5.6) implies that all geodesics emanating from $p$ are free of conjugate points in $B_\rho(p)$. By (6.5.2), this means that $\exp_p$ on $B_\rho(0)$ is regular (i.e., of maximal rank).

If $L(c_0) \geq \rho$ there is nothing to prove, so assume $L(c_0) < \rho$.

Let $\tilde{c}_0 = \tilde{c}_0(t) = t\tilde{c}'(0)$, $0 \leq t \leq t_0$, be the line segment in $T_pM$ which begins at $0 \in T_pM$, satisfies $c_0(t) = \exp_p \tilde{c}_0(t)$, and ends at $\tilde{q} = \tilde{c}_0(t_0)$.

Consider a homotopy $H: [0,1] \times [0,1] \to M$ between $c_0$ and $c_1$ with $H(s,0) = p$, $H(s,1) = q$. For each fixed $s$, let $c_s(t) = H(s,t)$. Since $\exp_p$ is regular on $B_\rho(0)$, we may lift the homotopy to $T_pM$ via the inverse of $\exp_p$, obtaining curves $\tilde{c}_s$ in $T_pM$ starting at $0$. The curve $\tilde{c}_1$ must reach the boundary of $B_\rho(0)$. The length of $\tilde{c}_s$ is at least $2\rho - 2\varepsilon - L(c_0)$. Consequently, by (6.6.2),

$$L(c_s) + L(c_0) \geq 2\rho - 2\varepsilon.$$

Since this inequality holds for all $\varepsilon > 0$, we obtain $L(c_1) + L(c_0) \geq 2\rho = 2\pi/\sqrt{K_1}$, and the lemma follows.

**Remark.** This lemma and its proof carry over word-for-word to Riemannian manifolds.
