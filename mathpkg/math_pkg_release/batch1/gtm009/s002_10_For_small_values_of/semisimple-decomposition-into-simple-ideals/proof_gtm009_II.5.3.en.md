---
role: proof
locale: en
of_concept: semisimple-decomposition-into-simple-ideals
source_book: gtm009
source_chapter: "II"
source_section: "5.3"
---
First step: Let $I$ be an arbitrary ideal of $L$. Define $I^\perp = \{x \in L \mid \kappa(x, y) = 0 \text{ for all } y \in I\}$. By the associativity of $\kappa$, $I^\perp$ is also an ideal of $L$. Apply Cartan's Criterion to the Lie algebra $I \cap I^\perp$: for any $x, y \in I \cap I^\perp$, the Killing form restricted to this intersection vanishes, so Cartan's Criterion implies $I \cap I^\perp$ is solvable. But $L$ is semisimple (Rad $L = 0$), so $I \cap I^\perp = 0$. Since $\dim I + \dim I^\perp = \dim L$ (by nondegeneracy of $\kappa$ on $L$ and the fact that the pairing $I \times I^\perp \to F$ is zero), we have $L = I \oplus I^\perp$.

Now proceed by induction on $\dim L$. If $L$ has no nonzero proper ideal, $L$ is simple and we are done. Otherwise, let $L_1$ be a minimal nonzero proper ideal. By the above, $L = L_1 \oplus L_1^\perp$. Any ideal of $L_1$ is an ideal of the semisimple $L$, so $L_1$ is semisimple; by minimality it is simple. Similarly, $L_1^\perp$ is semisimple; by induction it splits into a direct sum of simple ideals $L_2 \oplus \cdots \oplus L_t$, which are also ideals of $L$.

Uniqueness: If $I$ is any simple ideal of $L$, then $[IL] \neq 0$ (since $Z(L) = 0$), so $[IL] = I$. On the other hand, $[IL] = [IL_1] \oplus \cdots \oplus [IL_t]$. Since $I$ is simple, it must equal exactly one of the $[IL_i] = L_i$ and be orthogonal to the others. Hence every simple ideal of $L$ coincides with one of the $L_i$.
