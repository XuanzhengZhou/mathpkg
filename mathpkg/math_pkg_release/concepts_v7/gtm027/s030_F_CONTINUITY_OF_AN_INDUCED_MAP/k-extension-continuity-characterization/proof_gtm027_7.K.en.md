---
role: proof
locale: en
of_concept: k-extension-continuity-characterization
source_book: gtm027
source_chapter: "7"
source_section: "K"
---

# Proof of Continuity in the k-Extension Topology

Let $(X, \mathcal{I})$ be a Hausdorff space and $f : X \to Y$ a function into a topological space $Y$. We prove that $f$ is $\mathcal{I}_k$-continuous iff it is $\mathcal{I}$-continuous on every $\mathcal{I}$-compact subset of $X$.

($\Rightarrow$) Suppose $f$ is $\mathcal{I}_k$-continuous. Let $C$ be an $\mathcal{I}$-compact subset. By part (a), the relativizations of $\mathcal{I}$ and $\mathcal{I}_k$ to $C$ coincide. Since $f$ is $\mathcal{I}_k$-continuous, $f|_C$ is $\mathcal{I}_k|_C$-continuous, hence $\mathcal{I}|_C$-continuous. Thus $f$ is $\mathcal{I}$-continuous on $C$.

($\Leftarrow$) Suppose $f|_C$ is $\mathcal{I}|_C$-continuous for every $\mathcal{I}$-compact $C$. Let $V \subseteq Y$ be open. We must show $f^{-1}(V) \in \mathcal{I}_k$, i.e., $f^{-1}(V) \cap C$ is $\mathcal{I}$-open in $C$ for every $\mathcal{I}$-compact $C$.

Given an $\mathcal{I}$-compact $C$, $f|_C$ is $\mathcal{I}|_C$-continuous, so $(f|_C)^{-1}(V) = f^{-1}(V) \cap C$ is $\mathcal{I}$-open in $C$. This holds for all compact $C$, hence $f^{-1}(V) \in \mathcal{I}_k$. Thus $f$ is $\mathcal{I}_k$-continuous.
