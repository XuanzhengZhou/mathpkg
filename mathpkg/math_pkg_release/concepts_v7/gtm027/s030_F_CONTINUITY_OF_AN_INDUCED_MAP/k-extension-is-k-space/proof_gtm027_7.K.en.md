---
role: proof
locale: en
of_concept: k-extension-is-k-space
source_book: gtm027
source_chapter: "7"
source_section: "K"
---

# Proof of The k-Extension Is a k-Space

Let $(X, \mathcal{I})$ be a Hausdorff space. We prove that $(X, \mathcal{I}_k)$ is a $k$-space, i.e., a set is closed in $\mathcal{I}_k$ iff its intersection with every $\mathcal{I}_k$-compact set is $\mathcal{I}_k$-closed.

First, by part (a), a set is $\mathcal{I}$-compact iff it is $\mathcal{I}_k$-compact. So we may speak simply of "compact" sets.

Let $A \subseteq X$ be $\mathcal{I}_k$-closed. Then $X \setminus A \in \mathcal{I}_k$. By definition of $\mathcal{I}_k$, for every compact $C$, $(X \setminus A) \cap C$ is $\mathcal{I}$-open in $C$. Hence $A \cap C = C \setminus ((X \setminus A) \cap C)$ is $\mathcal{I}$-closed in $C$, and therefore $\mathcal{I}_k$-closed in $C$ (by part (a) the relativizations agree on compact sets).

Conversely, suppose $A \cap C$ is $\mathcal{I}_k$-compact for every compact $C$. In particular, for any compact $C$, $A \cap C$ is $\mathcal{I}$-compact (hence $\mathcal{I}$-closed, since $\mathcal{I}$ is Hausdorff). Then $(X \setminus A) \cap C = C \setminus (A \cap C)$ is $\mathcal{I}$-open in $C$. Since this holds for all compact $C$, $X \setminus A \in \mathcal{I}_k$, so $A$ is $\mathcal{I}_k$-closed.

Thus $(X, \mathcal{I}_k)$ is a $k$-space.
