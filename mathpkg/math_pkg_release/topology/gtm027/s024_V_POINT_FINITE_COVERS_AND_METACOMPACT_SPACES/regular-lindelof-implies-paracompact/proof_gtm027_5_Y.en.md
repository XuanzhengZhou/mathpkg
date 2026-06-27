---
role: proof
locale: en
of_concept: regular-lindelof-implies-paracompact
source_book: gtm027
source_chapter: "5"
source_section: "Y. Paracompact Spaces"
---

# Proof that Each Regular Lindelöf Space is Paracompact

Let $X$ be a regular Lindelöf space. We prove $X$ is paracompact.

Let $\mathcal{U}$ be an arbitrary open cover of $X$. For each $x \in X$, choose $U_x \in \mathcal{U}$ containing $x$. By regularity, there exist open sets $V_x, W_x$ such that $x \in V_x \subset \overline{V_x} \subset W_x \subset \overline{W_x} \subset U_x$.

The family $\{V_x : x \in X\}$ is an open cover of $X$. Since $X$ is Lindelöf, there exists a countable subcover $\{V_{x_n} : n \in \mathbb{N}\}$. Set $V_n = V_{x_n}$ and $W_n = W_{x_n}$ for brevity.

Now define $C_1 = \overline{V_1}$, and for $n > 1$,
$$C_n = \overline{V_n} \setminus \bigcup_{i=1}^{n-1} W_i.$$

Each $C_n$ is closed (as the difference of a closed set and an open set). The family $\{C_n\}$ is a locally finite closed cover of $X$ (since each point has a neighborhood intersecting only finitely many $W_n$, hence only finitely many $C_n$). Moreover, $C_n \subset \overline{V_n} \subset W_n \subset U_{x_n}$.

For each $n$, choose an open set $G_n$ with $C_n \subset G_n \subset \overline{G_n} \subset U_{x_n}$ (using normality, which follows from regularity and Lindelöf). The family $\{G_n\}$ is a locally finite open refinement of $\mathcal{U}$. Therefore $X$ is paracompact.

(Note: This proof uses the standard construction that a regular Lindelöf space is normal, and then constructs a locally finite refinement via a shrinking of a countable cover.)
