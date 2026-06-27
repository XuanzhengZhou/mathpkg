---
role: proof
locale: en
of_concept: k-extension-relativization-identity
source_book: gtm027
source_chapter: "7"
source_section: "K"
---

# Proof of k-Extension Relativization Identity

Let $(X, \mathcal{I})$ be a Hausdorff space and let $\mathcal{I}_k$ be the $k$-extension of $\mathcal{I}$. We prove that if $C$ is an $\mathcal{I}$-compact subset of $X$, then the relativization of $\mathcal{I}$ to $C$ is identical with that of $\mathcal{I}_k$.

Let $U \subseteq C$ be $\mathcal{I}$-open in $C$. Then $U = V \cap C$ for some $V \in \mathcal{I}$. Since $C$ is $\mathcal{I}$-compact, for any $\mathcal{I}$-compact set $K$, $U \cap K = (V \cap C) \cap K = V \cap (C \cap K)$. But $C \cap K$ is $\mathcal{I}$-compact (closed subset of compact $C$ intersected with compact $K$), and $V \cap (C \cap K)$ is $\mathcal{I}$-open in $C \cap K$. This means $U \in \mathcal{I}_k|_C$.

Conversely, let $U \subseteq C$ be $\mathcal{I}_k$-open in $C$, so $U = W \cap C$ with $W \in \mathcal{I}_k$. Then for any $\mathcal{I}$-compact $K$, $W \cap K$ is $\mathcal{I}$-open in $K$. In particular, taking $K = C$, we have $W \cap C$ is $\mathcal{I}$-open in $C$. Thus $U$ is $\mathcal{I}$-open in $C$.

Consequently, a set is $\mathcal{I}$-compact iff it is $\mathcal{I}_k$-compact, since compactness depends only on the relativized topology.
