---
role: proof
locale: en
of_concept: ehrenfeucht-fraisse-criterion
source_book: gtm053
source_chapter: "X"
source_section: "3"
---

# Proof of Ehrenfeucht-Fraisse Criterion for Saturated Models

**Definition 3.14 (Back-and-forth system).** A *back-and-forth system* between $L$-structures $\mathbf{A}$ and $\mathbf{B}$ is a nonempty set $I$ of isomorphisms of substructures of $\mathbf{A}$ and substructures of $\mathbf{B}$ such that:

- (forth) For every $f \in I$ and $a \in A$, there exists $g \in I$ such that $f \subseteq g$ and $a \in \operatorname{Dom} g$;
- (back) For every $f \in I$ and $b \in B$, there exists $g \in I$ such that $f \subseteq g$ and $b \in \operatorname{Range} g$.

**Theorem 3.15 (Ehrenfeucht-Fraisse Criterion).** Given $\aleph_0$-saturated $L$-structures $\mathbf{A}$ and $\mathbf{B}$, $\mathbf{A} \equiv \mathbf{B}$ if and only if there exists a back-and-forth system between the two structures.

*Proof.* ($\Leftarrow$) Suppose there exists a back-and-forth system $I$ between $\mathbf{A}$ and $\mathbf{B}$. We prove $\mathbf{A} \equiv \mathbf{B}$ by induction on formula complexity. One shows that for any $f \in I$ with domain $\{a_1, \ldots, a_n\}$ and any formula $P(x_1, \ldots, x_n)$,

$$\mathbf{A} \models P(a_1, \ldots, a_n) \iff \mathbf{B} \models P(f(a_1), \ldots, f(a_n)).$$

The base case for atomic formulas follows from $f$ being an isomorphism of substructures. The inductive steps for Boolean connectives are straightforward. For $\exists y\, P(\bar{x}, y)$: if $\mathbf{A} \models \exists y\, P(\bar{a}, y)$, then there exists $a \in A$ with $\mathbf{A} \models P(\bar{a}, a)$. By the forth property, extend $f$ to $g \in I$ with $a \in \operatorname{Dom} g$. By induction hypothesis, $\mathbf{B} \models P(g(\bar{a}), g(a))$, so $\mathbf{B} \models \exists y\, P(g(\bar{a}), y)$. The converse uses the back property symmetrically.

($\Rightarrow$) Assume $\mathbf{A} \equiv \mathbf{B}$ and both are $\aleph_0$-saturated. Define $I$ to be the set of all finite partial elementary maps between $\mathbf{A}$ and $\mathbf{B}$; that is, $f \in I$ if $f$ is a map from a finite subset $\{a_1, \ldots, a_n\} \subseteq A$ to $\{b_1, \ldots, b_n\} \subseteq B$ such that $\operatorname{tp}^{\mathbf{A}}(a_1, \ldots, a_n) = \operatorname{tp}^{\mathbf{B}}(b_1, \ldots, b_n)$. This set is nonempty (the empty map is in $I$ since $\mathbf{A} \equiv \mathbf{B}$ implies both satisfy the same sentences).

We verify the forth property. Let $f \in I$ with domain $\bar{a} = (a_1, \ldots, a_n)$ and image $\bar{b} = (b_1, \ldots, b_n)$, and let $a \in A$. Consider the type $p(x, \bar{a}) = \operatorname{tp}^{\mathbf{A}}(a, \bar{a})$. Since $f$ is elementary, by $\mathbf{A} \equiv \mathbf{B}$, the type $p(x, \bar{b})$ is consistent with $T = \operatorname{Th}(\mathbf{B})$. By $\aleph_0$-saturation of $\mathbf{B}$, this type is realized by some $b \in B$. Extending $f$ by $a \mapsto b$ gives an elementary map, so it belongs to $I$. The back property is verified symmetrically. $\square$
