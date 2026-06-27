---
role: proof
locale: en
of_concept: quotient-group-is-topological-group
source_book: gtm015
source_chapter: "1"
source_section: "4"
---

# Proof of Quotient of a topological group by a normal subgroup is a topological group

**Theorem (4.5).** If $N$ is a normal subgroup of a topological group $G$, then $G/N$ equipped with the quotient topology is a topological group. Moreover, $G/N$ is separated if and only if $N$ is closed in $G$.

*Proof.* Let $\mathcal{V}$ be the system of neighborhoods of the neutral element $e$ in $G$, and consider the image system

$$\pi(\mathcal{V}) = \{\pi(V) : V \in \mathcal{V}\}$$

in $G/N$, where $\pi: G \to G/N$ is the canonical mapping. We verify that $\pi(\mathcal{V})$ satisfies the neighborhood axioms for a topological group given in (3.2).

**Condition (3):** For any neighborhood $V \in \mathcal{V}$ of $e$, there exists $W \in \mathcal{V}$ such that $WW \subset V$ (by (3.2) applied to $G$). Then

$$\pi(W)\pi(W) = \pi(WW) \subset \pi(V),$$

so $\pi(V)$ satisfies condition (3) of (3.2) with respect to $\pi(\mathcal{V})$.

**Condition (4):** If $V \in \mathcal{V}$, then $V^{-1} \in \mathcal{V}$ (by (3.2)), and

$$(\pi(V))^{-1} = \pi(V^{-1}) \in \pi(\mathcal{V}),$$

so $\pi(V)$ satisfies condition (4).

**Condition (5):** If $V \in \mathcal{V}$ and $a \in G$, then $aVa^{-1} \in \mathcal{V}$ (by (3.2)). Since $N$ is normal,

$$\pi(a)\pi(V)\pi(a)^{-1} = \pi(aVa^{-1}) \in \pi(\mathcal{V}),$$

verifying condition (5) of (3.2).

It now follows from (3.2) that there exists a topology $\tau$ on $G/N$ compatible with the group structure, for which $\pi(\mathcal{V})$ is the system of neighborhoods of $\pi(e)$. By (2.9), the $\tau$-neighborhoods of $\pi(a)$ are the sets $\pi(a)\pi(V)$ for $V \in \mathcal{V}$.

By Lemma (4.4)(ii), the neighborhoods of $\pi(a)$ in the quotient topology are precisely the sets $\pi(aV) = \pi(a)\pi(V)$ for $V \in \mathcal{V}$. Hence the $\tau$-neighborhoods coincide with the quotient topology neighborhoods. Therefore the quotient topology itself is compatible with the group structure on $G/N$, so $G/N$ is a topological group.

**(iv) Separatedness.** If $G/N$ is separated, then by (3.4) the singleton $\{\pi(e)\}$ is closed in $G/N$. By continuity of $\pi$, its inverse image $N = \pi^{-1}(\{\pi(e)\})$ is closed in $G$.

Conversely, suppose $N$ is closed in $G$. Then its complement $\complement N$ is open. By Lemma (4.4)(i), $\pi$ is an open mapping, so $\pi(\complement N)$ is open in $G/N$. But

$$\pi(\complement N) = G/N \setminus \{\pi(e)\},$$

since $\pi(x) = \pi(e)$ if and only if $x \in N$. Thus $G/N \setminus \{\pi(e)\}$ is open, meaning $\{\pi(e)\}$ is closed in $G/N$. By (3.4), this implies $G/N$ is separated.

This completes the proof.
