---
role: proof
locale: en
of_concept: kuratowski-closure-operator-theorem
source_book: gtm027
source_chapter: "1"
source_section: "Topological Spaces"
---

# Proof of Kuratowski's Closure Operator Characterization of Topology

**Theorem.** Let $X$ be a set and let $c : \mathcal{P}(X) \to \mathcal{P}(X)$ be a closure operator on $X$, i.e., an operator satisfying the Kuratowski closure axioms:

(a) $\emptyset^c = \emptyset$;
(b) $A \subseteq A^c$ for each $A \subseteq X$;
(c) $A^{cc} = A^c$ for each $A \subseteq X$;
(d) $(A \cup B)^c = A^c \cup B^c$ for all $A, B \subseteq X$.

Let $\mathfrak{F} = \{A \subseteq X : A^c = A\}$ be the family of $c$-closed sets, and let $\mathfrak{J} = \{X \setminus F : F \in \mathfrak{F}\}$ be the family of complements of $c$-closed sets. Then $\mathfrak{J}$ is a topology for $X$, and for each subset $A \subseteq X$, $A^c$ is precisely the $\mathfrak{J}$-closure of $A$.

*Proof.* We first show that $\mathfrak{F}$ satisfies the conditions to be the family of closed sets for a topology.

By axiom (a), $\emptyset^c = \emptyset$, so $\emptyset \in \mathfrak{F}$. By axiom (b), $X \subseteq X^c$, and trivially $X^c \subseteq X$, so $X^c = X$, hence $X \in \mathfrak{F}$.

Let $A, B \in \mathfrak{F}$, so $A^c = A$ and $B^c = B$. By axiom (d), $(A \cup B)^c = A^c \cup B^c = A \cup B$, hence $A \cup B \in \mathfrak{F}$. By induction, the union of any finite subfamily of $\mathfrak{F}$ belongs to $\mathfrak{F}$.

Now let $\{F_\alpha\}$ be an arbitrary non-void subfamily of $\mathfrak{F}$, and let $F = \bigcap_\alpha F_\alpha$. Since $F \subseteq F_\alpha$ for each $\alpha$, and $c$ is monotone (which follows from axiom (d): if $A \subseteq B$, then $B = A \cup B$, so $B^c = A^c \cup B^c$, hence $A^c \subseteq B^c$), we have $F^c \subseteq F_\alpha^c = F_\alpha$ for each $\alpha$. Thus $F^c \subseteq \bigcap_\alpha F_\alpha = F$. By axiom (b), $F \subseteq F^c$, so $F^c = F$ and $F \in \mathfrak{F}$. Thus $\mathfrak{F}$ is closed under arbitrary non-void intersections.

Therefore $\mathfrak{F}$ is precisely the family of closed sets for the topology $\mathfrak{J}$. Consequently $\mathfrak{J}$ is a topology on $X$.

It remains to show that $A^c$ is the $\mathfrak{J}$-closure of $A$ for each $A \subseteq X$. By axiom (c), $A^{cc} = A^c$, so $A^c \in \mathfrak{F}$, i.e., $A^c$ is $\mathfrak{J}$-closed. By axiom (b), $A \subseteq A^c$, so $A^c$ is a closed set containing $A$.

If $F \in \mathfrak{F}$ and $A \subseteq F$, then by monotonicity (which follows from axiom (d)), $A^c \subseteq F^c = F$. Thus $A^c$ is contained in every $c$-closed set containing $A$. Hence $A^c$ is precisely the smallest closed set containing $A$, i.e., the $\mathfrak{J}$-closure of $A$. $\square$
