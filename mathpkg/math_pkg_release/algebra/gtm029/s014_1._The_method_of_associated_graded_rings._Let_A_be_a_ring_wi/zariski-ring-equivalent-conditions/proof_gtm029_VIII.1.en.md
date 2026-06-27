---
role: proof
locale: en
of_concept: zariski-ring-equivalent-conditions
source_book: gtm029
source_chapter: "VIII"
source_section: "1. The method of associated graded rings"
---

(a) $\Rightarrow$ (b): By the Artin-Rees Lemma, every submodule $F$ of a finite $A$-module $E$ is closed. In particular, $(0)$ is closed, so $\bigcap \mathfrak{m}^n E = (0)$, i.e., $E$ is Hausdorff.

(b) $\Rightarrow$ (c): $A/\mathfrak{a}$ is a finite $A$-module, so $\bigcap \mathfrak{m}^n(A/\mathfrak{a}) = (0)$, i.e., $\bigcap (\mathfrak{m}^n + \mathfrak{a}) = \mathfrak{a}$.

(c) $\Rightarrow$ (d): If $\mathfrak{p}$ is a maximal ideal with $\mathfrak{p} + \mathfrak{m} = A$, then $\mathfrak{m}^n + \mathfrak{p} = A$ for all $n$, so $\bigcap (\mathfrak{m}^n + \mathfrak{p}) = A \neq \mathfrak{p}$, contradicting (c).

(d) $\Rightarrow$ (e): For $m \in \mathfrak{m}$, $1+m \notin \mathfrak{p}$ for any maximal ideal $\mathfrak{p}$, so $(1+m) = A$ and $1+m$ is a unit.

(e) $\Rightarrow$ (f): If $E = \mathfrak{m}E$ with $\{x_1,\ldots,x_q\}$ a finite basis, write $x_i = \sum m_{ij}x_j$. Let $d = \det(\delta_{ij} - m_{ij}) \in 1+\mathfrak{m}$. Then $dx_i = 0$, and since $d$ is a unit, $x_i = 0$, so $E = (0)$.

(f) $\Rightarrow$ (a): Let $\mathfrak{p}$ be a maximal ideal. Suppose $\mathfrak{m} \not\subset \mathfrak{p}$. Then $\mathfrak{p} + \mathfrak{m} = A$. The module $A/\mathfrak{p}$ is simple (hence finite) and satisfies $\mathfrak{m}(A/\mathfrak{p}) = (\mathfrak{m}+\mathfrak{p})/\mathfrak{p} = A/\mathfrak{p}$, forcing $A/\mathfrak{p} = (0)$, contradiction.