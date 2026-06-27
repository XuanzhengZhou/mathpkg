---
role: proof
locale: en
of_concept: reinhardt-domain-holomorphic-5-4-
source_book: gtm038
source_chapter: "I"
source_section: "5. Expansion in Reinhardt Domains"
---

**Theorem 5.4.** Let $G \subset \mathbb{C}^n$ be a proper Reinhardt domain, $f$ holomorphic in $G$. Then there is a power series $\mathfrak{P}(z) = \sum_{v=0}^{\infty} a_v z^v$ which converges in $G$ with $f(z) = \mathfrak{P}(z)$ for $z \in G$.

**Proof.** If $z_0 \in G$, then there exists $z_1 \in G$ with $|z_j^{(0)}| < |z_j^{(1)}|$ for $j = 1, \ldots, n$ (since $G$ is proper). Thus $z_0 \in P_{z_1}$. Let $\text{ch}(f|T_{z_1})(z) = \sum_{v=0}^{\infty} a_v z^v$ for $z \in P_{z_1}$ be the Cauchy integral expansion. The coefficients $a_v$ are those of the Taylor series about 0; they do not depend on $z_1$. Since $z_0$ was arbitrary, the Taylor series of $f$ about 0 converges in all of $G$. It defines a holomorphic function $g$, which coincides with $f$ near the origin. By the identity theorem, $f = g$ on $G$.
