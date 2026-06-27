---
role: proof
locale: en
of_concept: structure-of-modular-form-spaces
source_book: gtm007
source_chapter: "VII"
source_section: "1"
---

**Proof of (i).** Let $f$ be a nonzero element of $M_k$. Applying the valence formula (Theorem 3), all terms on the left-hand side
$$v_\infty(f) + \frac{1}{2}v_i(f) + \frac{1}{3}v_\rho(f) + \sum_{p \in H/G}^* v_p(f) = \frac{k}{6}$$
are $\geq 0$. Hence $k \geq 0$. If $k = 1$, the right-hand side is $1/6$, which is impossible since the left-hand side is a sum of nonnegative multiples of $1/3, 1/2, 1$ and cannot equal $1/6$. Thus $M_1 = 0$.

**Proof of (ii).** For $k = 0$, any modular form of weight $0$ is a holomorphic function on $H/G \cup \{\infty\}$, which is a compact Riemann surface, hence constant. So $M_0 = \mathbf{C}$ with basis $1$. For $k = 2, 3$, the valence formula forces $M_k$ to be one-dimensional, and $G_k$ is a nonzero element. For $k = 4, 5$, $G_k \in M_k$ and the valence formula again gives $\dim M_k = 1$. In all these cases $k < 6$, so $M_k^0 = 0$ since a cusp form would require $v_\infty(f) \geq 1$, making the sum $> k/6$, impossible for $k < 6$.

**Proof of (iii).** $\Delta$ is a cusp form of weight $12$, i.e. $\Delta \in M_6^0$. The map $f \mapsto \Delta f$ is an injection from $M_{k-6}$ into $M_k^0$. Conversely, if $g \in M_k^0$, then $g/\Delta$ is holomorphic on $H$ (since $\Delta \neq 0$ on $H$) and meromorphic at infinity (since $g$ vanishes at infinity and $\Delta$ has a simple zero there), so $g/\Delta \in M_{k-6}$. Hence multiplication by $\Delta$ is an isomorphism.
