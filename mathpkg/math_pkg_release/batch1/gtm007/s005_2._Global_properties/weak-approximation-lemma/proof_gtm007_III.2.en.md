---
role: proof
locale: en
of_concept: weak-approximation-lemma
source_book: gtm007
source_chapter: "III"
source_section: "2"
---

By Lemma 1 (Chinese Remainder Theorem) applied to $m_i = p_i^N$, there exists $x_0 \in \mathbb{Z}$ such that $v_{p_i}(x_0 - x_i) \geq N$ for all $i$. Choose now an integer $q \geq 2$ which is prime to all the $p_i$ (for example a prime number). The rational numbers of the form $a/q^m$, $a \in \mathbb{Z}$, $m \geq 0$, are dense in $\mathbb{R}$ (this follows simply from the fact $q^m \to \infty$ when $m \to \infty$). Choose such a number $u = a/q^m$ with

$$|x_0 - x_\infty + u p_1^N \cdots p_n^N| \leq \varepsilon.$$

The rational number $x = x_0 + u p_1^N \cdots p_n^N$ has the desired property.
