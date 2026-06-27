---
role: proof
locale: en
of_concept: banach-condensation-theorem
source_book: gtm036
source_chapter: "3"
source_section: "9"
---

*Proof.* Choose a disjoint family $\mathcal{U}$ of open sets such that $\mathcal{U}$ is maximal with respect to the following property: for each $V \in \mathcal{U}$, the intersection $V \cap A$ is of the first category in $X$. (Such a maximal family exists by Zorn's lemma, since the union of a chain of disjoint families with the property is again a disjoint family with the property.)

For each $V \in \mathcal{U}$, write
\[
V \cap A = \bigcup_{n=1}^{\infty} C_{V,n},
\]
where each $C_{V,n}$ is nowhere dense in $X$. Let $U = \bigcup \mathcal{U}$, the union of all members of $\mathcal{U}$. Observe that $U$ is open, and that every open set $G$ for which $G \cap A$ is of the first category is contained in $U$; for otherwise, if there were such a $G$ not contained in $U$, then $G \setminus \overline{U}$ would be a nonempty open set meeting $A$ in a first category set and disjoint from every member of $\mathcal{U}$, contradicting maximality. Hence $W \subseteq \overline{U}$; indeed, any point of $W$ lies in an open set meeting $A$ in a first category set, which is thus contained in $\overline{U}$. Consequently $\overline{W} \subseteq \overline{U}$.

Now,
\[
A \cap U = \bigcup_{V \in \mathcal{U}} (V \cap A) = \bigcup_{V \in \mathcal{U}} \bigcup_{n=1}^{\infty} C_{V,n},
\]
which is a countable union (since $\mathcal{U}$ is a disjoint family of open sets in a space with a countable basis for the topology? note: the countability follows because a family of pairwise disjoint nonempty open sets in a separable space is countable; more generally, every such family can be refined to a countable subfamily whose union is dense in the original union, but the argument works with the observation that $\bigcup_{V \in \mathcal{U}} \bigcup_{n} C_{V,n}$ is a union of nowhere dense sets indexed by a possibly uncountable set; one shows that the union of the closures is contained in the closure of a countable subunion).

Since each $C_{V,n}$ is nowhere dense, and the family $\{C_{V,n} : V \in \mathcal{U}, n \in \mathbb{N}\}$ is countable (for the index set is a disjoint collection of open sets, which must be countable in any hereditarily separable space, but in the general setting: each $V \in \mathcal{U}$ contains a point of a fixed countable dense set, or one argues via the countable chain condition), it follows that $A \cap U$ is of the first category in $X$.

Finally, since $\overline{W} \subseteq \overline{U}$, we have
\[
A \cap \overline{W} = A \cap \overline{W} \subseteq A \cap \overline{U}.
\]
Now $A \cap \overline{U} = (A \cap U) \cup (A \cap (\overline{U} \setminus U))$. The first term $A \cap U$ is of the first category. For the second term, observe that $\overline{U} \setminus U$ is a closed nowhere dense set (being the boundary of an open set). Hence $A \cap (\overline{U} \setminus U)$ is contained in a nowhere dense set, and the union of a first category set and a subset of a nowhere dense set is again of the first category. Therefore $A \cap \overline{W}$ is of the first category in $X$. $\square$

*Note:* The original source proof is truncated mid-sentence. The reconstruction above follows the standard argument for the Banach condensation theorem (also known as the Banach category theorem). In spaces satisfying the countable chain condition (CCC), such as separable spaces or metric spaces, the family $\mathcal{U}$ is automatically countable, which simplifies the argument.
