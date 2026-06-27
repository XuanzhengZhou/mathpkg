---
role: proof
locale: en
of_concept: inseparable-implies-essentially-undecidable
source_book: gtm037
source_chapter: "15"
source_section: "3"
---

Let $\Gamma$ be an inseparable theory in $\mathcal{L}$. Thus the sets $g^{+*} \Gamma$ and $A = g^{+*} \{\varphi : \varphi \text{ is a sentence and } \neg \varphi \in \Gamma\}$ are disjoint, by 6.21, so $\Gamma$ is consistent.

Suppose that $\Delta$ is a consistent theory in $\mathcal{L}$ with $\Gamma \subseteq \Delta$. Let $B = g^{+*} \{\varphi : \varphi \text{ is a sentence and } \neg \varphi \in \Delta\}$. Thus $g^{+*} \Gamma \subseteq g^{+*} \Delta$, $A \subseteq B$, and $g^{+*} \Delta \cap B = 0$.

Clearly $B$ is recursive if $g^{+*} \Delta$ is recursive, so the recursive inseparability of $g^{+*} \Gamma$ and $A$ implies that $g^{+*} \Delta$ is not recursive, i.e., $\Delta$ is undecidable. Hence $\Gamma$ is essentially undecidable.

Trivially, every essentially undecidable theory is undecidable (by considering $\Delta = \Gamma$ itself).
