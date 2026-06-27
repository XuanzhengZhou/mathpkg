---
role: proof
locale: en
of_concept: theorem-13-4
source_book: gtm055
source_chapter: "13-14"
source_section: "Section 15_Section_15"
---

Proof. The sufficiency of the condition is easily established. To see this, let $T$ be continuous, and let $(x_0, y_0)$ be a vector in $\mathcal{E} \oplus_1 \mathcal{F}$ that does not belong to $\mathcal{G}$, so that $y_0 \neq Tx_0$. Then there exist disjoint open sets $W_1$ and $W_2$ in $\mathcal{F}$ such that $y_0 \in W_1$ and $Tx_0 \in W_2$. Moreover, since $T$ is continuous, there exists a neighborhood $V$ of $x_0$ in $\mathcal{E}$ such that $T(V) \subset W_1$, and it is readily seen that $V \times W_2$ is a neighborhood of $(x_0, y_0)$ in $\mathcal{E} \oplus_1 \mathcal{F}$ that is disjoint from $\mathcal{G}$. Hence $\mathcal{G}$ is closed.

To prove the necessity of the condition we note, to begin with, that if $\mathcal{G}$ is closed in $\mathcal{E} \oplus_1 \mathcal{F}$, then $\mathcal{G}$ is itself an $F$-space (since a closed subset of a complete metric space is complete, and $\mathcal{E} \oplus_1 \mathcal{F}$ is complete by Example 11L). Consider the mapping $S$ of $\mathcal{G}$ into $\mathcal{E}$ defined by $S(x, Tx) = x$, $x \in \mathcal{E}$. Since $S$ is the restriction to $\mathcal{G}$ of the projection $\pi_1$ of $\mathcal{E} \oplus_1 \mathcal{F}$ onto $\mathcal{E}$, it is clear that $S$ is a continuous linear transformation. But also, just as clearly, $S$ is a one-to-one mapping of $\mathcal

$z_n \to 0$ and such that the sequence $\{Tz_n\}$ is Cauchy in $\mathcal{F}$, it is true that $Tz_n \to 0$. Then $T$ is continuous.

Proof. Consider the graph $\mathcal{G}$ of $T$ as a linear submanifold of $\mathcal{E} \oplus_1 \hat{\mathcal{F}}$, where $\hat{\mathcal{F}}$ denotes the completion of $\mathcal{F}$ (Th. 11.16). If $\{(x_n, Tx_n)\}$ is a sequence in $\mathcal{G}$ that converges in $\mathcal{E} \oplus_1 \hat{\mathcal{F}}$ to a limit $(x_0, y_0)$, and if we set $z_n = x_n - x_0$, then $z_n \to 0$ and $Tz_n - Tz_m = Tx_n - Tx_m$, so $\{Tz_n\}$ is Cauchy. Hence, by hypothesis, $Tz_n \to 0$. But $\{Tz_n = Tx_n - Tx_0\}$ tends to $y_0 - Tx_0$. Thus $y_0 = Tx_0$, so $\mathcal{G}$ is closed in $\mathcal{E} \oplus_1 \hat{\mathcal{F}}$, and therefore $T$ is continuous as a mapping of $\mathcal{E}$ into $\hat{\mathcal{F}}$. Since $T$ takes its values in $\mathcal{F}$, it is continuous as a mapping of $\mathcal{E}$ into $\mathcal{F}$ as well.

Example D ([1; Ch. III, Lemme 1]). Suppose $\mathcal{E}_1$ and $\mathcal{E}_2$ are $F$-spaces, and $T_1$ and $T_2$ are continuous linear transformations of $\mathcal{E}_1$ and $\mathcal{E}_2$, respectively, into a quasinormed space $\mathcal{F}$. Suppose also that for each $x$ in $\mathcal{E}_1$ there is exactly one $y$ in $\mathcal{E}_2$ such that $T_1x = T_2y$. If we define $Sx = y$, then

in Problem 11F.) The linear transformation $L$ of $\mathcal{D}$ onto $\mathcal{C}([a, b])$ defined in Example B is clearly not bounded, but it is closed. (Recall from advanced calculus that if $\{f_n\}$ is a uniformly convergent sequence of continuously differentiable functions such that the sequence $\{f'_n\}$ also converges uniformly, then $\lim_n f'_n = (\lim_n f_n)'$.
