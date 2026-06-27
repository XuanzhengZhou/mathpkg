---
role: proof
locale: en
of_concept: canonical-mapping-to-quotient-is-open-continuous
source_book: gtm015
source_chapter: "1"
source_section: "4"
---

# Proof of Canonical mapping to quotient space is open and continuous

**Lemma (4.4).** If $H$ is a subgroup of a topological group $G$, $G/H$ is the space of left cosets equipped with the quotient topology, and $\pi: G \rightarrow G/H$ is the canonical mapping, then

(i) $\pi$ is an open, continuous mapping, and

(ii) for each $a \in G$, the neighborhoods of $\pi(a)$ are precisely the sets $\pi(aV)$, where $V$ is a neighborhood of the neutral element $e$ of $G$.

*Proof.* By definition, the quotient topology on $G/H$ is the final topology for the mapping $\pi$; thus the open sets of $G/H$ are precisely the sets $A \subset G/H$ such that $\pi^{-1}(A)$ is open in $G$. In particular, $\pi$ is continuous.

(i) If $U$ is an open subset of $G$, then $\pi^{-1}(\pi(U)) = UH$ is open in $G$ by (2.10); therefore $\pi(U)$ is open in $G/H$. Thus $\pi$ is an open mapping. Together with continuity from the definition of quotient topology, this proves (i).

(ii) Fix $a \in G$. If $V$ is a neighborhood of $e$, then $aV$ is a neighborhood of $a$ by (2.9). Since $\pi$ is open by (i), $\pi(aV)$ is an open set in $G/H$ containing $\pi(a)$, hence a neighborhood of $\pi(a)$.

Conversely, let $W$ be any neighborhood of $\pi(a)$ in $G/H$. Then $\pi^{-1}(W)$ is an open neighborhood of $a$ in $G$ (by continuity of $\pi$). By (3.2), there exists a neighborhood $V$ of $e$ such that $aV \subset \pi^{-1}(W)$. Applying $\pi$, we obtain $\pi(aV) \subset W$. Thus every neighborhood of $\pi(a)$ in the quotient topology contains some $\pi(aV)$. Together with the first direction, this shows that the neighborhoods of $\pi(a)$ are precisely the sets $\pi(aV)$ where $V$ is a neighborhood of $e$.
