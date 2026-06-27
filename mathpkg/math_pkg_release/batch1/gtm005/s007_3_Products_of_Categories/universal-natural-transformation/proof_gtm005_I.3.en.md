---
role: proof
locale: en
of_concept: universal-natural-transformation
source_book: gtm005
source_chapter: "I"
source_section: "3. Products of Categories"
---

\textbf{Naturality of $\mu$.} For any arrow $f: c \to c'$ in $C$, consider the diagram:
$$\begin{CD}
T_0 c = \langle c, 0 \rangle @>{\mu c = \langle 1_c, \downarrow \rangle}>> \langle c, 1 \rangle = T_1 c \\
@V{T_0 f = \langle f, 1_0 \rangle}VV @VV{T_1 f = \langle f, 1_1 \rangle}V \\
T_0 c' = \langle c', 0 \rangle @>>{\mu c' = \langle 1_{c'}, \downarrow \rangle}> \langle c', 1 \rangle = T_1 c'
\end{CD}$$

Both composites give $\langle f, \downarrow \rangle$, since:
$$\langle 1_{c'}, \downarrow \rangle \circ \langle f, 1_0 \rangle = \langle 1_{c'} \circ f, \downarrow \circ 1_0 \rangle = \langle f, \downarrow \rangle,$$
$$\langle f, 1_1 \rangle \circ \langle 1_c, \downarrow \rangle = \langle f \circ 1_c, 1_1 \circ \downarrow \rangle = \langle f, \downarrow \rangle.$$

Thus the square commutes and $\mu$ is natural.

\textbf{Universal property.} Given a natural transformation $\tau: S \to T$ with $S, T: C \to D$, define $F: C \times 2 \to D$ as follows. On objects:
$$F\langle c, 0 \rangle = Sc, \quad F\langle c, 1 \rangle = Tc.$$

On arrows of the form $\langle f, 1_0 \rangle: \langle c, 0 \rangle \to \langle c', 0 \rangle$, define $F\langle f, 1_0 \rangle = Sf$. On arrows $\langle f, 1_1 \rangle: \langle c, 1 \rangle \to \langle c', 1 \rangle$, define $F\langle f, 1_1 \rangle = Tf$. On the "vertical" arrow $\langle 1_c, \downarrow \rangle: \langle c, 0 \rangle \to \langle c, 1 \rangle$, define $F\langle 1_c, \downarrow \rangle = \tau c$.

Every arrow in $C \times 2$ is uniquely a composite of these three types. One verifies that $F$ is a functor, $F \circ T_0 = S$, $F \circ T_1 = T$, and $F \circ \mu = \tau$. The naturality of $\tau$ guarantees that $F$ preserves all compositions. Moreover, these conditions force $F$ to be defined as above, so $F$ is unique.
