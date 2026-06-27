---
role: proof
locale: en
of_concept: components-are-closed-and-separated
source_book: gtm027
source_chapter: "1"
source_section: "Bases and Subbases"
---

# Proof of Properties of Connected Components

**Theorem 22.** Each connected subset of a topological space is contained in a component, and each component is closed. If $A$ and $B$ are distinct components of a space, then $A$ and $B$ are separated.

**Proof.** Let $A$ be a non-void connected subset of a topological space and let $C$ be the union of all connected sets containing $A$. By Theorem 21 (union of non-separated connected sets is connected), any two connected sets containing $A$ are not separated (they intersect at $A$), so $C$ is connected. If $D$ is a connected set containing $C$, then since $D$ contains $A$, $D$ is one of the sets whose union is $C$, hence $D \subseteq C$. Thus $C = D$, and $C$ is a maximal connected set, i.e., a component.

(If $A$ is void and the space is non-void, a set consisting of a single point is contained in a component, and hence so is $A$.)

Each component $C$ is connected, and by Theorem 20 (closure of a connected set is connected), the closure $C^{-}$ is connected. Since $C$ is maximal among connected sets and $C \subseteq C^{-}$, we must have $C = C^{-}$. Therefore $C$ is closed.

If $A$ and $B$ are distinct components and are not separated, then their union $A \cup B$ is connected by Theorem 21, contradicting the maximality of $A$ and $B$. Hence $A$ and $B$ must be separated. $\square$
