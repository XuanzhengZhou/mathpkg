---
role: proof
locale: en
of_concept: kernel-residue-at-diagonal
source_book: gtm035
source_chapter: "Chapter 13"
source_section: "13.7"
---
# Proof of Lemma 13.7 (Residue of Cauchy-Fantappie Kernel at the Diagonal)

**Lemma 13.7.** Fix $z \in D$, and choose $\epsilon > 0$ such that the closed ball $\{|\zeta - z| \leq \epsilon\}$ is contained in $D$. Then

$$1 = a_0 \int_{\{|\zeta - z| = \epsilon\}} K_w(\zeta, z),$$

where $a_0 = \frac{(-1)^{n(n-1)/2}(n-1)!}{(2\pi i)^n}$.

**Proof.** Put $D_\epsilon = D \setminus \{|\zeta - z| \leq \epsilon\}$. The boundary of $D_\epsilon$ consists of two components: the outer boundary $\partial D$ and the inner boundary $\{|\zeta - z| = \epsilon\}$, the latter with the orientation induced as the boundary of the removed ball.

By Stokes' Theorem,

$$\int_{\partial D_\epsilon} K_w = \int_{D_\epsilon} dK_w.$$

By Lemma 13.6, $dK_w = 0$ on $D \setminus \{z\}$, so in particular $dK_w = 0$ on $D_\epsilon$. Hence

$$\int_{\partial D_\epsilon} K_w = 0.$$

But $\partial D_\epsilon = \partial D \cup \{|\zeta - z| = \epsilon\}$ (with the sphere oppositely oriented relative to $\partial D$). Thus

$$\int_{\partial D} K_w - \int_{\{|\zeta - z| = \epsilon\}} K_w = 0,$$

or equivalently

$$\int_{\partial D} K_w = \int_{\{|\zeta - z| = \epsilon\}} K_w.$$

Now apply Leray's formula (Theorem 13.4) with the constant function $f \equiv 1$. Since $1 \in A(D) \cap \mathcal{C}^1(\bar{D})$, Theorem 13.4 gives

$$1 = a_0 \int_{\partial D} K_w(\zeta, z),$$

where $a_0 = \frac{(-1)^{n(n-1)/2}(n-1)!}{(2\pi i)^n}$.

Combining the two equalities,

$$1 = a_0 \int_{\{|\zeta - z| = \epsilon\}} K_w(\zeta, z),$$

which is precisely the assertion of the lemma. $\square$

**Remark.** This lemma shows that the Cauchy-Fantappie kernel $K_w$ has a "residue" of $1/a_0$ at the diagonal $\zeta = z$, independent of the particular choice of the weight functions $w_j$ satisfying the normalization condition (13). This is the higher-dimensional analogue of the residue theorem for the Cauchy kernel $d\zeta/(\zeta - z)$.
