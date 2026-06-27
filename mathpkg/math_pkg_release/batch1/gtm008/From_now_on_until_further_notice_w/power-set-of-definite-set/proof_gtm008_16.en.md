---
role: proof
locale: en
of_concept: power-set-of-definite-set
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Note that $B^{\mathcal{D}(u)} \subseteq V^{(\mathbf{B})}$ and $B^{\mathcal{D}(u)}$ is a set. Let $x \in V^{(\mathbf{B})}$ and define
$$A_u = \{v \in V^{(\mathbf{B})} \mid \mathcal{D}(v) = \mathcal{D}(u)\}.$$

Then
\begin{align*}
\llbracket x \in B^{\mathcal{D}(u)} \times \{1\} \rrbracket &= \sum_{v \in A_u} \llbracket x = v \rrbracket \\
&= \sum_{v \in A_u} \llbracket x = v \rrbracket \quad\text{(since $u$ is definite)} \\
&= \llbracket x \subseteq u \rrbracket \quad\text{by Theorem 16.25.}
\end{align*}

Since this holds for all $x$, we have
$$\llbracket \mathcal{P}(u) = B^{\mathcal{D}(u)} \times \{1\} \rrbracket = 1.$$
