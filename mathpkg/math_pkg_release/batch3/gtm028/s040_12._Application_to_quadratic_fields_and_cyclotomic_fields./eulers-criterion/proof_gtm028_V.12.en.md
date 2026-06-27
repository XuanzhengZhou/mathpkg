---
role: proof
locale: en
of_concept: eulers-criterion
source_book: gtm028
source_chapter: "V"
source_section: "12"
---

As the multiplicative group of $\mathbb{Z}/(p)$ is a cyclic group of order $p-1$ (Chapter II, §9), let $g$ be a generator. Every element not divisible by $p$ can be written as $g^k$ for some integer $k$. Then $s \equiv g^k \pmod{p}$ for some $k$.

The element $s$ is a quadratic residue modulo $p$ if and only if $k$ is even (since $g^{k} = (g^{k/2})^2$ when $k$ is even). Now compute:
$$s^{\frac{1}{2}(p-1)} \equiv (g^k)^{\frac{1}{2}(p-1)} = g^{k(p-1)/2} \pmod{p}.$$

If $k$ is even, say $k = 2\ell$, then $g^{2\ell(p-1)/2} = g^{\ell(p-1)} = (g^{p-1})^{\ell} \equiv 1 \pmod{p}$, so $s^{(p-1)/2} \equiv 1 \pmod{p}$.

If $k$ is odd, say $k = 2\ell + 1$, then $g^{(2\ell+1)(p-1)/2} = g^{\ell(p-1)} \cdot g^{(p-1)/2} \equiv g^{(p-1)/2} \pmod{p}$. Since $g$ is a generator of a cyclic group of even order $p-1$, the element $g^{(p-1)/2}$ is the unique element of order $2$ in the group, which is $-1 \pmod{p}$. Thus $s^{(p-1)/2} \equiv -1 \pmod{p}$.

Therefore $\left(\frac{s}{p}\right) = 1$ if and only if $s^{(p-1)/2} \equiv 1 \pmod{p}$, and $\left(\frac{s}{p}\right) = -1$ if and only if $s^{(p-1)/2} \equiv -1 \pmod{p}$.
