---
role: proof
locale: en
of_concept: k-extension-maximality
source_book: gtm027
source_chapter: "7"
source_section: "K"
---

# Proof of Maximality of the k-Extension

Let $(X, \mathcal{I})$ be a Hausdorff space. We prove that $\mathcal{I}_k$ is the largest topology on $X$ which agrees with $\mathcal{I}$ on compact sets.

Let $\mathcal{J}$ be any topology on $X$ such that for every $\mathcal{I}$-compact set $C$, the relativization $\mathcal{J}|_C = \mathcal{I}|_C$. We must show $\mathcal{J} \subseteq \mathcal{I}_k$.

Take $U \in \mathcal{J}$. For any $\mathcal{I}$-compact set $C$, $U \cap C$ is $\mathcal{J}$-open in $C$ (since $U \in \mathcal{J}$), and by hypothesis $\mathcal{J}|_C = \mathcal{I}|_C$, so $U \cap C$ is $\mathcal{I}$-open in $C$. Since this holds for every $\mathcal{I}$-compact $C$, we have $U \in \mathcal{I}_k$ by definition of the $k$-extension.

Thus $\mathcal{J} \subseteq \mathcal{I}_k$, proving maximality.
