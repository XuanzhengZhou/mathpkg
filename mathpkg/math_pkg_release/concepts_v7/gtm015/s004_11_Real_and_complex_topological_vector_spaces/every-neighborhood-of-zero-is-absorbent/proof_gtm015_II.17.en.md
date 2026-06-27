---
role: proof
locale: en
of_concept: every-neighborhood-of-zero-is-absorbent
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "17. Balanced sets, absorbent sets"
---

# Proof that Every Neighborhood of the Origin is Absorbent

**Lemma (17.11).** In a TVS, every neighborhood of $\theta$ is absorbent.

*Proof.* Let $V$ be a neighborhood of $\theta$ and let $x \in E$. Since the mapping $\lambda \mapsto \lambda x$ is continuous at $\lambda = 0$ (by (11.1) or (11.3)(ii)), and since $0x = \theta$, there exists an $\varepsilon > 0$ such that $\lambda x \in V$ whenever $|\lambda| \leq \varepsilon$. This is precisely the definition of absorbent: for each $x \in E$, there exists $\varepsilon > 0$ such that $\lambda x \in V$ for all $|\lambda| \leq \varepsilon$. $\square$
