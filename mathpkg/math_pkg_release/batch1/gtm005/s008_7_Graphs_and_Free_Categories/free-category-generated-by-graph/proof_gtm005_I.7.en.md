---
role: proof
locale: en
of_concept: free-category-generated-by-graph
source_book: gtm005
source_chapter: "I"
source_section: "7"
---

Take the objects of $C$ to be those of $G$ and the arrows of $C$ to be the finite strings (or "paths")

$$a_1 \xrightarrow{f_1} a_2 \xrightarrow{f_2} a_3 \longrightarrow \dots \xrightarrow{f_{n-1}} a_n$$

composed of $n$ objects $a_1, \ldots, a_n$ of $G$ connected by $n-1$ arrows $f_i : a_i \to a_{i+1}$ of $G$. Regard each such string as an arrow $\langle a_1, f_1, \ldots, f_{n-1}, a_n \rangle : a_1 \to a_n$ in $C$, and define the composite of two strings by juxtaposition (i.e., by concatenation), identifying the common end. This composition is manifestly associative, and strings $\langle a_1 \rangle$ of length $n=1$ are its identities.

Every string of length $n>1$ is a composite of strings of length 2:

$$\langle a_1, f_1, a_2, \ldots, a_{n-1}, f_{n-1}, a_n \rangle = \langle a_{n-1}, f_{n-1}, a_n \rangle \circ \cdots \circ \langle a_1, f_1, a_2 \rangle.$$

The desired morphism $P : G \to UC$ of graphs sends each arrow $f : a \to b$ of $G$ to the string $\langle a, f, b \rangle$.