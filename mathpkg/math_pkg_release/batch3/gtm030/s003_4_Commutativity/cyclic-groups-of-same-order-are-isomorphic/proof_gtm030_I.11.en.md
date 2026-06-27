---
role: proof
locale: en
of_concept: cyclic-groups-of-same-order-are-isomorphic
source_book: gtm030
source_chapter: "I"
source_section: "11"
---

Let $\mathfrak{Z} = [a]$ be an infinite cyclic group. Define $\varphi : \mathbb{Z} \to \mathfrak{Z}$ by $\varphi(n) = a^n$. Since $a^{m+n} = a^m a^n$, this is a homomorphism. If $\varphi$ were not injective, then $a^m = a^n$ for $m \neq n$, say $n > m$, giving $a^{n-m} = 1$, contradicting infinitude of $\mathfrak{Z}$. Surjectivity follows from the definition of cyclic group. Hence $\varphi$ is an isomorphism.

Let $\mathfrak{Z} = [a]$ and $\mathfrak{W} = [b]$ be cyclic groups of order $r$. Define $\varphi : \mathfrak{Z} \to \mathfrak{W}$ by $\varphi(a^k) = b^k$. If $a^m = a^n$, then $a^{m-n} = 1$, so $r \mid (m-n)$. Hence $b^{m-n} = 1$ and $b^m = b^n$, so $\varphi$ is well-defined. It is clearly a homomorphism and surjective. Since both groups have order $r$, $\varphi$ is also injective, hence an isomorphism.
