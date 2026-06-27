---
role: proof
locale: en
of_concept: coproducts-in-abelian-groups
source_book: gtm026
source_chapter: "1"
source_section: "1. The Base Category"
---

Define $\bigoplus_{i \in I} A_i$ as the subgroup of $\prod_{i \in I} A_i$ consisting of all $I$-tuples $(a_i)_{i \in I}$ with $a_i \in A_i$ and $a_i = 0$ for all but finitely many $i$. Define $\text{in}_i: A_i \to \bigoplus_j A_j$ by $\text{in}_i(a) = (\delta^i_j a)_{j \in I}$ where $\delta^i_j$ is the Kronecker delta.

Given homomorphisms $f_i: A_i \to B$, define $f: \bigoplus A_i \to B$ by
$$f((a_i)_{i \in I}) = \sum_{i \in I} f_i(a_i).$$
Since only finitely many $a_i$ are nonzero, this sum is well-defined (pointwise finite). For any $a \in A_i$,
$$(\text{in}_i \circ f)(a) = f((\delta^i_j a)_{j \in I}) = f_i(a),$$
since the only nonzero term in the sum occurs at $j = i$ where $\delta^i_i = 1$, giving $f_i(a \cdot 1) = f_i(a)$. Thus $\text{in}_i \circ f = f_i$.

For uniqueness, if $g: \bigoplus A_i \to B$ is a homomorphism with $\text{in}_i \circ g = f_i$ for all $i$, then for any $(a_i) \in \bigoplus A_i$, writing $(a_i) = \sum_{i \in I} \text{in}_i(a_i)$ (finite sum), we have
$$g((a_i)) = g\!\left(\sum_i \text{in}_i(a_i)\right) = \sum_i g(\text{in}_i(a_i)) = \sum_i (\text{in}_i \circ g)(a_i) = \sum_i f_i(a_i) = f((a_i)).$$
Thus $g = f$.
