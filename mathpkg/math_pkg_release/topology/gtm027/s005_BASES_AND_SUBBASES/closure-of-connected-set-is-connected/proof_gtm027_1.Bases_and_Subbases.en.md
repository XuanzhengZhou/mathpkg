---
role: proof
locale: en
of_concept: closure-of-connected-set-is-connected
source_book: gtm027
source_chapter: "1"
source_section: "Bases and Subbases"
---

# Proof of Closure of a Connected Set is Connected

**Theorem 20.** The closure of a connected set is connected.

**Proof.** Suppose that $Y$ is a connected subset of a topological space and that $Y^{-} = A \cup B$, where $A$ and $B$ are both open and closed in $Y^{-}$ (with the relative topology). Then each of $A \cap Y$ and $B \cap Y$ is open and closed in $Y$, and since $Y$ is connected, one of these two sets must be void. Suppose that $B \cap Y$ is void. Then $Y \subseteq A$, and consequently $Y^{-} \subseteq A$ because $A$ is closed in $Y^{-}$. Hence $B$ is void, and it follows that $Y^{-}$ is connected. $\square$

**Remark.** There is an apparently stronger form of this theorem: if $Y$ is a connected subset of $X$ and $Z$ is a set such that $Y \subseteq Z \subseteq Y^{-}$, then $Z$ is connected. This follows immediately by applying the theorem to $Y$ as a subset of the subspace $Z$ (with the relative topology), since the closure of $Y$ in $Z$ is $Y^{-} \cap Z = Z$.
