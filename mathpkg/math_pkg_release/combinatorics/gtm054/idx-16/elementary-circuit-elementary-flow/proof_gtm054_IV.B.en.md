---
role: proof
locale: en
of_concept: elementary-circuit-elementary-flow
source_book: gtm054
source_chapter: "IV"
source_section: "B"
---

In order to show that $h_D$ is an elementary flow, it suffices to prove that $h_D$ is a minimal flow, since by definition, $h_D[W] \subseteq \{0, 1, -1\}$.

We select a minimal flow $h$ such that $\sigma(h) \subseteq \sigma(h_D)$. By the first part of this same proof (Lemma B7), there exists an elementary circuit $D''$ such that $\sigma(h_{D''}) \subseteq \sigma(h)$, and so $\sigma(h_{D''}) \subseteq \sigma(h_D)$. By IIIA9, both $\sigma(h_{D''})$ and $\sigma(h_D)$ are elementary cycles of $\Gamma$. Hence
$$\sigma(h_D) = \sigma(h) = \sigma(h_{D''}) \in \mathcal{M}(F),$$
which implies that $h_D$ is itself minimal, and therefore elementary, in $F(V)$.
