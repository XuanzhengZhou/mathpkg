---
role: proof
locale: en
of_concept: interpolation-lemma-for-prime-ideal
source_book: gtm043
source_chapter: "13"
source_section: "13.7"
---
Assume $A$ has no maximum and $B$ no minimum (otherwise trivial). Let $(a_n)$ be cofinal increasing in $A$ and $(b_n)$ coinitial decreasing in $B$.

By Lemma 13.5, lift to preimages $f_n$ of $a_n$ and $g_n$ of $b_n$ with $f_k \leq f_n \leq g_n \leq g_k$ for $k < n$.

Choose $s \in C(X)$, $s \geq 1$, with $M(s)$ infinitely large. Define $\varphi_k \in C(\mathbb{R})$:
$$\varphi_k(r) = \begin{cases} r - k + 1 & k-1 \leq r \leq k, \\ k+1-r & k \leq r \leq k+1, \\ 0 & \text{otherwise.} \end{cases}$$

Define $h(x) = \sum_{k=1}^\infty \varphi_k(s(x)) f_k(x)$. For each $x$, at most two terms are nonzero.

If $s(x) \geq n$, then $\varphi_k(s(x)) = 0$ for $k < n$, so
$$h(x) = \sum_{k \geq n} \varphi_k(s(x)) f_k(x) \geq f_n(x)$$
on $Z_n = \{x : s(x) \geq n\} \in Z[M]$ (5.7(a)). By 5.4(a), $M(h) \geq M(f_n)$. Set $v = M(h)$; then $v \geq a_n$ for all $n$, so $v \geq A$.

Since $h$ averages the $f_k$ and $f_k \leq g_n$ for all $k, n$, we have $h \leq g_n$, so $v \leq b_n$ for all $n$, hence $v \leq B$.