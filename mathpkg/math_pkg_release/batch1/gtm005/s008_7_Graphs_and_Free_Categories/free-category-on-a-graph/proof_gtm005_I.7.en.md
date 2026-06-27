---
role: proof
locale: en
of_concept: free-category-on-a-graph
source_book: gtm005
source_chapter: "I"
source_section: "7"
---
Take the objects of $C_G$ to be those of $G$ and the arrows of $C_G$ to be the finite strings (paths)
\[
a_1 \xrightarrow{f_1} a_2 \xrightarrow{f_2} a_3 \longrightarrow \cdots \xrightarrow{f_{n-1}} a_n
\]
composed of $n$ objects $a_1, \ldots, a_n$ connected by $n-1$ arrows $f_i: a_i \rightarrow a_{i+1}$ of $G$. Regard each such string as an arrow $\langle a_1, f_1, \ldots, f_{n-1}, a_n\rangle: a_1 \rightarrow a_n$. Define composition by concatenation, identifying the common end. This is associative, and strings of length 1 are identities.

Every string of length $n > 1$ decomposes uniquely as a composite of strings of length 2:
\[
\langle a_1, f_1, a_2, \ldots, a_{n-1}, f_{n-1}, a_n\rangle = \langle a_{n-1}, f_{n-1}, a_n\rangle \circ \cdots \circ \langle a_1, f_1, a_2\rangle.
\]

The morphism $P: G \rightarrow UC_G$ sends each arrow $f$ to the string $\langle a_1, f, a_2\rangle$ of length 2. For any graph morphism $D: G \rightarrow UB$, define $D'$ on strings by
\[
D'\langle a_1, f_1, \ldots, f_{n-1}, a_n\rangle = D f_{n-1} \circ \cdots \circ D f_1,
\]
taking identity strings to identity arrows. This gives the required unique factorization.