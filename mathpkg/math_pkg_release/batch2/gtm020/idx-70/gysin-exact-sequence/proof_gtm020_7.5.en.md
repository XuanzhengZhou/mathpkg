---
role: proof
locale: en
of_concept: gysin-exact-sequence
source_book: gtm020
source_chapter: "7"
source_section: "7.5"
---

We have the following commutative diagram with top row exact.

$$\begin{array}{cccccccccccccc}
\longrightarrow H^{i+n}(E, E_0) & \xrightarrow{j^*} H^{i+n}(E) & \longrightarrow H^{i+n}(E_0) & \longrightarrow H^{i+n+1}(E, E_0) & \longrightarrow \\
\phantom{\longrightarrow} \Bigg\downarrow & & \phantom{\Bigg\downarrow} \Bigg\downarrow & & \phantom{\Bigg\downarrow} \Bigg\downarrow & & \phantom{\Bigg\downarrow} \Bigg\downarrow
\end{array}$$

Let $\psi$ denote the composition of the coboundary $H^i(E_0) \rightarrow H^{i+1}(E, E_0)$ and $\phi^{-1}: H^{i+1}(E, E_0) \rightarrow H^{i+1-n}(B)$, where $\phi(a) = p^*(a)U_\xi$. The top row is the long exact sequence of the pair $(E, E_0)$, and the vertical maps are the Thom isomorphisms from Theorem 7.3. Using that $p^*: H^*(B) \to H^*(E)$ is an isomorphism (since $E$ deformation retracts to $B$ along fibres), the diagram transforms the exact sequence of the pair into the stated Gysin sequence. The multiplication by $e(\xi)$ in the sequence follows from the definition $e(\xi) = \phi^{-1}(U_\xi \cup U_\xi)$ and the commutativity of the diagram.
