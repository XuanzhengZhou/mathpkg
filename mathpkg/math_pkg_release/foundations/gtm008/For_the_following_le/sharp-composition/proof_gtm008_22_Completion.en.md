---
role: proof
locale: en
of_concept: sharp-composition
source_book: gtm008
source_chapter: "22"
source_section: "The Completion of a Boolean Algebra"
---

The map $\#: B_2 \to B_0$ is open, continuous, and onto $B_0$ since it is the composition of two open continuous onto maps (each $\#_j$ has these properties by Theorem 22.11).

For the preimage, we compute:
$$\#^{-1} = (\#_1 \circ \#_2)^{-1} = \#_2^{-1} \circ \#_1^{-1}.$$

For a basic open set $[b_0]$ in $B_0$, we have by Theorem 22.11(1):
$$(\#_1^{-1})``[b_0] = [i_1(b_0)],$$
and similarly
$$(\#_2^{-1})``[i_1(b_0)] = [i_2(i_1(b_0))] = [(i_2 \circ i_1)(b_0)] = [i(b_0)].$$

Therefore
$$(\#^{-1})``[b_0] = [i(b_0)],$$
which means $\#$ induces $i$, as required.
