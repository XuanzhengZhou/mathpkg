---
role: proof
locale: en
of_concept: isotopy-of-orientation-preserving-embeddings
source_book: gtm033
source_chapter: "IV"
source_section: "6"
---

# Proof of Isotopy of Orientation-Preserving Embeddings of Disks (Theorem 6.6)

**Theorem (6.6).** Let $E^n = D^n$ or $\mathbb{R}^n$ and let $f_i: (E^n, 0) \rightarrow (V, x_0)$ be embeddings, $i = 0, 1$, where $n = \dim V$ and $\partial V = \varnothing$. If

$$\operatorname{Det}\big(D(f_1^{-1} \circ f_0)(0)\big) > 0$$

then $f_0$ and $f_1$ are isotopic relative to $0$.

*Proof.* Note that $f_1^{-1} \circ f_0$ is well-defined on a neighborhood of $0$ in $E^n$ (since $f_1$ is an embedding), so its derivative at $0$ is defined.

By isotopy of tubular neighborhoods (Theorem 5.3) we can assume, after an isotopy of $f_1$, that $f_1^{-1} \circ f_0$ is a linear automorphism on a neighborhood of $0$. More precisely, each $f_i$ determines a disk neighborhood (closed tubular neighborhood of radius 1) of $x_0$ in $V$. Any two such neighborhoods are isotopic by Theorem 5.3, so after applying a suitable isotopy to $f_1$, we may assume that

$$f_1^{-1} \circ f_0 = L \in GL(n, \mathbb{R})$$

on a neighborhood of $0$ in $E^n$, with $L = D(f_1^{-1} \circ f_0)(0)$.

The hypothesis gives $\det L > 0$. Since $\det L > 0$, the matrix $L$ lies in the identity component of $GL(n, \mathbb{R})$. Hence there exists a smooth path $L_t$, $0 \leq t \leq 1$, in $GL(n, \mathbb{R})$ such that

$$L_0 = f_1^{-1} \circ f_0, \quad L_1 = 1_{\mathbb{R}^n}.$$

The required isotopy from $f_0$ to $f_1$ is given by

$$F_t = f_1 \circ L_t^{-1} \circ f_1^{-1} \circ f_0, \quad 0 \leq t \leq 1.$$

At $t = 0$: $F_0 = f_1 \circ L_0^{-1} \circ f_1^{-1} \circ f_0 = f_1 \circ (f_0^{-1} \circ f_1) \circ f_1^{-1} \circ f_0 = f_1.$

At $t = 1$: $F_1 = f_1 \circ 1_{\mathbb{R}^n} \circ f_1^{-1} \circ f_0 = f_0.$

Thus $F_t$ is an isotopy from $f_1$ to $f_0$ (equivalently, from $f_0$ to $f_1$ after reversing the parameter). Moreover, since each $L_t^{-1}$ fixes $0$, we have $F_t(0) = f_1(0) = x_0$ for all $t$, so the isotopy is relative to $0$. ∎
