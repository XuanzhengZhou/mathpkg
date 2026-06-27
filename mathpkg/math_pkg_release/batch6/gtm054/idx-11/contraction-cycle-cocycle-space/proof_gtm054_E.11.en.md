---
role: proof
locale: en
of_concept: contraction-cycle-cocycle-space
source_book: gtm054
source_chapter: "E"
source_section: "11"
---

In the light of Exercise E13(a) and the fact that every contraction of $\Gamma$ may be obtained by iterating the procedure of E13(d)(iii), we may assume that $\Gamma_1$ has been obtained from $\Gamma$ by just one application of this procedure. Thus

$$V_1 = \{ \{w\} : w \in V \setminus \{x, y\} \} \cup \{ \{x, y\} \}$$

and

$$E_1 = \{e \in E : f(e) \neq \{x, y\}\}.$$

Now $\mathcal{Z}^\perp(\Gamma_1)$ is spanned by the collection of its vertex cocycles, and these are

$$f_1^*(\{w\}) = f^*(w) \quad \text{for } w \in V \setminus \{x, y\},$$
$$f_1^*(\{x, y\}) = f^*(x) + f^*(y).$$

We show that this very same collection spans $\mathcal{Z}^\perp(\Gamma) \cap \mathcal{P}(E_1)$. For if $C \in \mathcal{Z}^\perp(\Gamma) \cap \mathcal{P}(E_1)$, then $C$ is a linear combination of vertex cocycles of $\Gamma$, and restricting to $E_1$ yields the same linear combination in terms of the vertex cocycles of $\Gamma_1$. Conversely, any linear combination of vertex cocycles of $\Gamma_1$ yields a cocycle that lies in $\mathcal{Z}^\perp(\Gamma)$ when extended by zero on $E \setminus E_1$.

The equality $\mathcal{Z}(\Gamma_1) = \pi_{E_1}[\mathcal{Z}(\Gamma)]$ follows by duality from the first equality, using the fact that the cycle and cocycle spaces are orthogonal complements.
