---
role: proof
locale: en
of_concept: decidability-of-theory-of-equality
source_book: gtm022
source_chapter: "V"
source_section: "4"
---

\textbf{Proof.} Let $p \in \mathcal{L}(\mathcal{E})$. The reduction process described in Example~4.2 gives an element $q$, equivalent to $p$ in $\mathcal{E}$, which is a propositional combination of elements of

\[
\Pi = \{\text{al}(n) \mid n \in \mathbb{N}\} \cup \{x_i = x_j \mid i, j \in \mathbb{N}\},
\]

such that $\text{var}(q) \subseteq \text{var}(p)$. Since $\text{var}(p) = \emptyset$, $q$ is a propositional combination of elements of the form $p_n = \text{al}(n+1)$ for $n \geqslant 1$. Hence $q$ is a propositional combination of $p_1, p_2, \ldots, p_k$ for some $k$. Let $f: \mathbb{Z}_2^k \to \mathbb{Z}_2$ be the corresponding truth function. Then $\mathcal{E} \vdash q$ if and only if $f(x_1, \ldots, x_k) = 1$ for all $(x_1, \ldots, x_k) \in \mathbb{Z}_2^k$ such that, for some $n$ ($0 \leqslant n \leqslant k$), $x_1 = x_2 = \cdots = x_n = 1$ and $x_{n+1} = x_{n+2} = \cdots = x_k = 0$. This is so because these are the only possible combinations of truth values for $p_1, \ldots, p_k$ in models of $\mathcal{E}$ (the truth of $\text{al}(n+1)$ implies the truth of $\text{al}(n)$, so the sequence of truth values must be an initial segment of $1$'s followed by $0$'s). Decidability follows, since only finitely many truth assignments need to be checked.
