---
role: proof
locale: en
of_concept: closure-of-identity-is-closed-normal-subgroup
source_book: gtm015
source_chapter: "1"
source_section: "4"
---

# Proof of Closure of the identity is a closed normal subgroup

**Corollary (4.2).** In a topological group $G$, with neutral element $e$, $\overline{\{e\}}$ is a closed normal subgroup of $G$.

*Proof.* The singleton $\{e\}$ is trivially a normal subgroup of $G$ (it is the trivial subgroup). By a standard result in the theory of topological groups (see Exercise (4.6) or more generally (2.2)), the closure of a subgroup in a topological group is again a subgroup, and the closure of a normal subgroup is again a normal subgroup. Therefore $\overline{\{e\}}$ is a normal subgroup of $G$.

Moreover, by definition of closure, $\overline{\{e\}}$ is closed in $G$. Hence $\overline{\{e\}}$ is a closed normal subgroup of $G$.

(One may also argue directly: $\overline{\{e\}}$ is closed by definition. Normality follows because for any $a \in G$, the conjugation map $x \mapsto a x a^{-1}$ is a homeomorphism of $G$ fixing $e$, hence maps $\{e\}$ to itself and therefore maps $\overline{\{e\}}$ to itself, i.e., $a \overline{\{e\}} a^{-1} = \overline{\{e\}}$.)
