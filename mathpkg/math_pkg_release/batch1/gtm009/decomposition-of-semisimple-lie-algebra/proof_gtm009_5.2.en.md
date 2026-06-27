---
role: proof
locale: en
of_concept: decomposition-of-semisimple-lie-algebra
source_book: gtm009
source_chapter: "5"
source_section: "5.2-5.3"
---

\textbf{Proof.} Let $I$ be an arbitrary ideal of $L$. Define $I^\perp = \{x \in L \mid \kappa(x, y) = 0 \text{ for all } y \in I\}$, which is also an ideal by associativity of $\kappa$. Cartan's Criterion applied to $I$ shows that $I \cap I^\perp$ is solvable, hence 0 (since $L$ is semisimple). Since $\dim I + \dim I^\perp = \dim L$ (nondegeneracy of $\kappa$), we must have $L = I \oplus I^\perp$.

Now proceed by induction on $\dim L$. If $L$ has no nonzero proper ideal, $L$ is simple and we are done. Otherwise, let $L_1$ be a minimal nonzero ideal. By the above, $L = L_1 \oplus L_1^\perp$. Any ideal of $L_1$ is also an ideal of $L$, so $L_1$ is semisimple (hence simple by minimality). Similarly, $L_1^\perp$ is semisimple; by induction it decomposes as a direct sum of simple ideals, which are also ideals of $L$.

Uniqueness: If $I$ is any simple ideal of $L$, then $[I L]$ is a nonzero ideal of $I$, forcing $[I L] = I$. Since $[I L] = \bigoplus [I L_i]$ and each $[I L_i]$ is an ideal of $L_i$, simplicity forces $I = L_i$ for some $i$.
