---
role: proof
locale: en
of_concept: finitely-spanned-maximal-submodule
source_book: gtm013
source_chapter: "1"
source_section: "2"
---

Let $M$ be spanned by a finite set. Among all finite spanning sets for $M$, select one $\{x_1, \ldots, x_n\}$ of minimal length $n$. (Since $M \neq 0$, $n \geq 1$.) Set

$$L = K + R x_2 + \cdots + R x_n$$

where $K$ is any submodule (e.g., $K = 0$ for the basic case). Then $L$ is a proper submodule of $M$; otherwise the shorter sequence $x_2, \ldots, x_n$ would span $M$, contradicting minimality of $n$.

Let $\mathcal{P}$ be the set of all proper submodules of $M$ that contain $L$. Clearly $\mathcal{P}$ is non-empty since $L \in \mathcal{P}$. A submodule $N$ containing $L$ belongs to $\mathcal{P}$ if and only if $x_1 \notin N$.

We apply the Maximal Principle to $\mathcal{P}$. Let $\mathcal{C}$ be a non-empty chain in $\mathcal{P}$ and set $V = \bigcup \mathcal{C}$. We claim $V$ is a submodule of $M$. For if $a, b \in R$ and $x, y \in V$, then for some $N_x, N_y \in \mathcal{C}$, $x \in N_x$ and $y \in N_y$. Since $\mathcal{C}$ is a chain, we may assume $N_x \leq N_y$. So $x, y \in N_y$ and by (2.3), $a x + b y \in N_y \subseteq V$. Thus $V$ is a submodule as claimed. Since $x_1$ is in no element of $\mathcal{C}$, $x_1 \notin V$.

We have shown that every non-empty chain in $\mathcal{P}$ has an upper bound in $\mathcal{P}$, namely its union. By the Maximal Principle, $\mathcal{P}$ has a maximal element $N$. Since $N$ is maximal in $\mathcal{P}$, any strictly larger submodule of $M$ is not in $\mathcal{P}$ and therefore contains $x_1$. But then any such module must contain $N + R x_1$, which equals $M$ by the spanning property. Hence $N$ is a maximal proper submodule of $M$.
