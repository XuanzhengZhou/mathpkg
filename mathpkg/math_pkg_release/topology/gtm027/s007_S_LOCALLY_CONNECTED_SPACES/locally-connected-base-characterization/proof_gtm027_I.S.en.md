---
role: proof
locale: en
of_concept: locally-connected-base-characterization
source_book: gtm027
source_chapter: "1"
source_section: "S. Locally Connected Spaces"
---

# Proof of Base Characterization of Locally Connected Spaces

Let $X$ be a topological space. We prove the equivalence.

**($\Rightarrow$)** Suppose $X$ is locally connected. Let $U$ be an open set and $x \in U$. We must find an open connected set $V$ such that $x \in V \subseteq U$. Since $U$ is a neighborhood of $x$ and $X$ is locally connected, the component $C$ of $U$ to which $x$ belongs is a neighborhood of $x$. By part (a), $C$ is open in $X$. Moreover, $C$ is connected (being a component). Setting $V = C$, we have $x \in V \subseteq U$ with $V$ open and connected. Hence the family of all open connected subsets of $X$ forms a base for the topology.

**($\Leftarrow$)** Suppose the family $\mathcal{B}$ of all open connected subsets of $X$ is a base for the topology. Let $x \in X$ and let $U$ be a neighborhood of $x$. Then there exists $V \in \mathcal{B}$ such that $x \in V \subseteq U$. Since $V$ is connected and $V \subseteq U$, the component $C$ of $U$ containing $x$ contains $V$. Hence $V \subseteq C$, and since $V$ is open and contains $x$, the component $C$ is a neighborhood of $x$. Therefore $X$ is locally connected.

$\square$
