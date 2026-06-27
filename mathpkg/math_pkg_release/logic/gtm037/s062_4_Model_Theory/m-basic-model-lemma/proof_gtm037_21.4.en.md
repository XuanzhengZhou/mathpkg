---
role: proof
locale: en
of_concept: m-basic-model-lemma
source_book: gtm037
source_chapter: "21"
source_section: "4"
---

Let $\mathfrak{A} = \langle A, R \rangle$. For $i \in \{1, \ldots, m\}$ let $C_i = \{X : X \in A/R, |X| = i\}$. Let $f$ be a choice function for nonempty sets of subsets of $A$. For each $i \in \{1, \ldots, m\}$ let

$$g_i = C_i \quad \text{if } |C_i| \leq m,$$
$$g_i = f(\{X : X \subseteq C_i, |X| = m\}) \quad \text{if } |C_i| > m.$$

Then let $B = \bigcup_{X \in A/R} g_X$ where $g_X$ is the set of elements selected from the equivalence class $X$ (at most $m$ per class), $S = {}^2B \cap R$, $\mathfrak{B} = \langle B, S \rangle$. Thus $\mathfrak{B}$ is a model of $\Gamma_{\text{equiv}}$, $\mathfrak{B} \subseteq \mathfrak{A}$, and each $\mathfrak{B}$-equivalence class contains at most $m$ elements. Assume that $X \subseteq B$ and $|X| < m$, and also that $a \in A \setminus B$. Since $a \in A \setminus B$, it follows from our construction that $|[a]_R| > m$. Choose $b \in g_{[a]} \setminus X$, and let $h$ be the transposition $(a, b)$. Clearly $h$ is an automorphism of $\mathfrak{A}$ and $h a \in B$. Hence by Lemma 21.12, $\mathfrak{B} \preceq_m \mathfrak{A}$.
