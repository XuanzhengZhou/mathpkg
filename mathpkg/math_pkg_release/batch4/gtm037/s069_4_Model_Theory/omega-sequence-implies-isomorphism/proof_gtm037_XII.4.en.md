---
role: proof
locale: en
of_concept: omega-sequence-implies-isomorphism
source_book: gtm037
source_chapter: "XII"
source_section: "4"
---

Let $A = \{a_i : i \in \omega\}$ and $B = \{b_i : i \in \omega\}$. Let $\langle I_m : m \in \omega \rangle$ be an $\omega$-sequence for $\mathfrak{A}$, $\mathfrak{B}$. We define sequences $x \in {}^\omega A$, $y \in {}^\omega B$ by recursion.

Suppose that $x_i$ and $y_i$ have been defined for all $i < 2m$ in such a way that

$$\langle x_0, \ldots, x_{2m-1} \rangle \, I_{2m} \, \langle y_0, \ldots, y_{2m-1} \rangle$$

(note that this holds if $m = 0$). Choose $i$ minimum such that $a_i \notin \{x_0, \ldots, x_{2m-1}\}$, and let $x_{2m} = a_i$. Then choose $j$ minimum such that $\langle x_0, \ldots, x_{2m} \rangle \, I_{2m+1} \, \langle y_0, \ldots, y_{2m-1}, b_j \rangle$ (possible by the back-and-forth property of $I_{2m+1}$), and set $y_{2m} = b_j$.

Now choose $j$ minimum such that $b_j \notin \{y_0, \ldots, y_{2m}\}$ and let $y_{2m+1} = b_j$. Then choose $i$ minimum such that $\langle x_0, \ldots, x_{2m+1} \rangle \, I_{2m+2} \, \langle y_0, \ldots, y_{2m+1} \rangle$ (possible by the back-and-forth property), and set $x_{2m+1} = a_i$.

By construction, the map $f : A \to B$ defined by $f(x_k) = y_k$ for all $k \in \omega$ is a bijection. Moreover, for any atomic formula $\varphi$ with free variables among $\{v_0, \ldots, v_{m-1}\}$ and any $k_0, \ldots, k_{m-1} \in \omega$, since $\langle x_0, \ldots, x_{\max k_i} \rangle$ and $\langle y_0, \ldots, y_{\max k_i} \rangle$ are related by $I_{\max k_i + 1}$, the definition of an $\omega$-sequence (specifically condition 26.6(ii)(4)) yields

$$\mathfrak{A} \models \varphi[x_{k_0}, \ldots, x_{k_{m-1}}] \quad \text{iff} \quad \mathfrak{B} \models \varphi[y_{k_0}, \ldots, y_{k_{m-1}}].$$

Thus $f$ is an isomorphism, so $\mathfrak{A} \cong \mathfrak{B}$.
