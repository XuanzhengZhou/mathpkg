---
role: proof
locale: en
of_concept: e1-transversals-independence-system
source_book: gtm054
source_chapter: "X"
source_section: "50"
---

Let $\Gamma = ([V, E], \mathcal{F})$ be the bipartite graph of the system $\Lambda$. Let $\Theta = (V \cup E, \mathcal{M})$ denote the matching matroid of $\Gamma$. We shall show that $\mathcal{T} = \mathcal{I}(\Theta_V)$.

A subset $T \subseteq V$ is in $\mathcal{T}$ if and only if for some $E' \subseteq E$ and some matching $\mathcal{F}' \subseteq \mathcal{F}$, we have $T \cup E' = \bigcup_{F \in \mathcal{F}'} F$; that is to say, $T \cup E'$ is a matched set of $\Gamma$. By Exercise A10, this is equivalent to saying that $T \cup E'$ is contained in some member of $\mathcal{B}$, or equivalently, $T \cup E' \in \mathcal{I}(\Theta)$. Hence $T \in \mathcal{I}(\Theta) \cap \mathcal{P}(V) = \mathcal{I}(\Theta_V)$, by Exercise D12a. Conversely, if $T \in \mathcal{I}(\Theta_V)$, then $T \in \mathcal{I}(\Theta)$. Hence $T$ is contained in some member of $\mathcal{B}$, and using the definition of $\mathcal{B}$, we return through the above chain of equivalent statements.

Since $\mathcal{I}(\Theta_V)$ is an independence system, $(V, \mathcal{T})$ is an independence system.
