---
role: proof
locale: en
of_concept: free-category
source_book: gtm005
source_chapter: "II"
source_section: "7"
---

\textbf{Proof.} Take the objects of $C$ to be those of $G$ and the arrows of $C$ to be the finite strings (or "paths")

$$a_1 \xrightarrow{f_1} a_2 \xrightarrow{f_2} a_3 \longrightarrow \cdots \xrightarrow{f_{n-1}} a_n$$

composed of $n$ objects $a_1, \ldots, a_n$ of $G$ connected by $n-1$ arrows $f_i: a_i \to a_{i+1}$ of $G$. Regard each such string as an arrow

$$\langle a_1, f_1, \ldots, f_{n-1}, a_n\rangle: a_1 \to a_n$$

in $C$, and define the composite of two strings by juxtaposition (i.e., concatenation), identifying the common end. This composition is manifestly associative, and strings $\langle a_1\rangle$ of length $n=1$ are its identities. Every string of length $n>1$ is a composite of strings of length $2$:

$$\langle a_1, f_1, a_2, \ldots, a_{n-1}, f_{n-1}, a_n\rangle = \langle a_{n-1}, f_{n-1}, a_n\rangle \circ \cdots \circ \langle a_1, f_1, a_2\rangle.$$

The desired morphism $P: G \to UC$ of graphs sends each arrow $f: a \to b$ of $G$ to the string $\langle a, f, b\rangle$ of length $2$. If $B$ is given with $D: G \to UB$, define $D'$ on objects by $D' a = D_O a$, and on each arrow $\langle a_1, f_1, \ldots, f_{n-1}, a_n\rangle$ of $C$ by

$$D'\langle a_1, f_1, \ldots, f_{n-1}, a_n\rangle = (D_A f_{n-1}) \circ \cdots \circ (D_A f_1),$$

where the right side is composition in $B$. Since $D$ is a morphism of graphs, the composable pairs are preserved, so the right side is defined. The definition of $D'$ on strings of length $2$ is forced by the condition $(UD') \circ P = D$, since $P$ sends $f$ to $\langle a, f, b\rangle$; the definition on longer strings is then forced by functoriality. This yields the unique functor with the required property.

If $B$ has $O$ as its set of objects and $D$ is a morphism of $O$-graphs, then $D_O$ is the identity on $O$, so $D'$ is the identity on objects as asserted.

In the special case where $G$ has just one object, a graph $G$ with one object is just a set $X$ (the set of arrows), and $C_G$ is the free monoid on $X$. Its universal property: For any monoid $L$ and any function $h: X \to UL$, there is a unique morphism $h': C_G \to L$ of monoids with $h = Uh' \circ p$. The elements of $C_G$ are the identity and strings $\langle x_1, \ldots, x_{n-1}\rangle$ for $x_i \in X$.
