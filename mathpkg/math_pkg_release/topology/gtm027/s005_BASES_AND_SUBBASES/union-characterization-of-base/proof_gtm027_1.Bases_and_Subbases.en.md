---
role: proof
locale: en
of_concept: union-characterization-of-base
source_book: gtm027
source_chapter: "1"
source_section: "Bases and Subbases"
---

# Proof of Union Characterization of a Base

**Proposition.** A subfamily $\mathcal{B}$ of a topology $\mathfrak{J}$ is a base for $\mathfrak{J}$ if and only if each member of $\mathfrak{J}$ is the union of members of $\mathcal{B}$.

**Proof.** ($\Rightarrow$) Suppose that $\mathcal{B}$ is a base for the topology $\mathfrak{J}$ and let $U \in \mathfrak{J}$. For each point $x \in U$, since $\mathcal{B}$ is a base, there exists a member $V_x \in \mathcal{B}$ such that $x \in V_x \subseteq U$. Then $U = \bigcup_{x \in U} V_x$, which expresses $U$ as a union of members of $\mathcal{B}$.

($\Leftarrow$) Conversely, suppose that each member of $\mathfrak{J}$ is a union of members of $\mathcal{B}$. Let $x$ be a point of the space and $U$ a neighborhood of $x$ with $U \in \mathfrak{J}$. By hypothesis, $U = \bigcup_{\alpha} V_{\alpha}$ for some subfamily $\{V_{\alpha}\} \subseteq \mathcal{B}$. Since $x \in U$, there exists some $\alpha$ with $x \in V_{\alpha} \subseteq U$. Thus $\mathcal{B}$ satisfies the defining property of a base for $\mathfrak{J}$. $\square$
