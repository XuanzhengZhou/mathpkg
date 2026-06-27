---
role: proof
locale: en
of_concept: equivalent-conditions-realcompact
source_book: gtm043
source_chapter: "8"
source_section: "16"
---

It is obvious that (1) $$\Rightarrow$$ (2) and (3) $$\Rightarrow$$ (4). Also, by Theorem 8.16, (4) implies that $$Y$$ is realcompact. (And by Theorem 8.9, (4) implies that every proper subspace of $$Y$$ is realcompact, so that (4) $$\Rightarrow$$ (3).)

**(2) $$\Rightarrow$$ (3).** Given a subspace $$F$$ of $$Y$$, enlarge the topology of $$Y$$ by making both $$F$$ and $$Y - F$$ open. The new space $$X$$ thus defined is completely regular and the relative topology on $$F$$ is the same in $$X$$ as in $$Y$$. Since the identity map from $$X$$ onto $$Y$$ is continuous, (2) implies that $$X$$ is realcompact. Therefore $$F$$, which is a closed subset of $$X$$ (though not necessarily of $$Y$$), is realcompact.

**(4) $$\Rightarrow$$ (1).** Let $$X$$ and $$\tau$$ satisfy the hypotheses of (1). By (4), as already noted, $$Y$$ is realcompact. Therefore $$\tau$$ has a continuous extension $$\tau^{\circ}: vX \to Y$$. Now consider any point $$y \in Y$$. By Theorem 8.13, the set

$$S = \tau^{\circ\leftarrow}[Y - \{y\}]$$

is realcompact, and so, by Theorem 8.16, $$S \cup \tau^{\leftarrow}(y)$$ is realcompact. Since this space lies between $$X$$ and $$vX$$, it must be $$vX$$ itself. In other words, $$\tau^{\circ\leftarrow}(y) \subset X$$ for every $$y \in Y$$. Hence $$X = vX$$, so $$X$$ is realcompact.
