---
role: proof
locale: en
of_concept: subring-e-is-a-field
source_book: gtm028
source_chapter: "II"
source_section: "4. The characteristic of a field"
---

Let $k$ be a field of characteristic $p \neq 0$, with identity $e$. Consider the homomorphism $\varphi: \mathbb{Z} \to k$ defined by $n \mapsto ne$, whose image is the subring $E$.

Since $p$ is the characteristic, $\ker \varphi = p\mathbb{Z}$. Thus $ne = 0$ if and only if $p \mid n$. For any integer $n$, write $n = qp + r$ with $0 \le r < p$. Then
$$
ne = qpe + re = re,
$$
since $qpe = (qp)e = 0$ (because $p \mid qp$). Hence every element of $E$ can be written as $re$ for some $r$ with $0 \le r < p$, so
$$
E = \{0, e, 2e, \dots, (p-1)e\}.
$$

These $p$ elements are distinct: if $re = se$ with $0 \le r, s < p$, then $(r-s)e = 0$, so $p \mid (r-s)$. Since $|r-s| < p$, this forces $r = s$. Thus $E$ has exactly $p$ elements.

To show $E$ is a field, let $ne \in E$ be nonzero. Then $n$ is not divisible by $p$, so $\gcd(n, p) = 1$. Hence there exist integers $m, q$ such that $mn - qp = 1$. Then
$$
(me)(ne) = (mn)e = (qp + 1)e = qpe + e = 0 + e = e,
$$
since $qpe = 0$. Thus $me$ is the multiplicative inverse of $ne$ in $E$. Therefore $E$ is a field, and being the least subring containing $e$, it is the prime subfield of $k$. It is isomorphic to $\mathbb{F}_p$ via $re \leftrightarrow r \bmod p$.
