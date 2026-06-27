---
role: proof
locale: en
of_concept: easton-main-lemma
source_book: gtm008
source_chapter: "23"
source_section: "3"
---

Without loss of generality, we may take $I = \aleph_\alpha$. First, we assume that $\aleph_\alpha$ is regular. The proof constructs $\bar{r}$ and $\Lambda$ by an inductive process of length $\aleph_\alpha$, using the $\aleph_\alpha$-bounded and strongly coatomic properties.

For $\mu < \aleph_\alpha$, define $S_\mu = \bigcup_{\nu < \aleph_\alpha \cdot \mu} IC(p_\nu)$. By the $\aleph_\alpha$-bounded property, $\overline{IC(p_\nu)} < \aleph_\alpha$ and $\overline{S_\mu} = \aleph_\alpha$. The set $\{p \mid CA(p) \subseteq S_\mu\}$ is enumerated and at each stage we pick $p_\nu, q_\nu', q_\nu$ satisfying compatibility conditions.

For the regular case, after the induction, we obtain $\bar{q}$ and $\Lambda = \bigcup_{\mu < \aleph_\alpha} \Lambda_\mu$ satisfying the required properties. For an arbitrary $r = p \cdot q$, we apply the construction to $q$ and define $\bar{r} = p \cdot \bar{q}$.

When $\aleph_\alpha$ is singular, $\aleph_\alpha = \sup_{\mu < \alpha'} \aleph_{\alpha_\mu}$ where $\alpha' = cf(\aleph_\alpha) < \aleph_\alpha$. Since each $\aleph_{\alpha_\mu+1}$ is regular, we apply the regular case inductively on $\mu$, obtaining $r_\mu$ and $\Lambda_\mu$ with $\bar{\Lambda}_\mu \leq \aleph_{\alpha_\mu+1}$. By compatibility, there exists $r$ below all $r_\nu$, and the construction yields the desired $\bar{r}$ and $\Lambda$.
