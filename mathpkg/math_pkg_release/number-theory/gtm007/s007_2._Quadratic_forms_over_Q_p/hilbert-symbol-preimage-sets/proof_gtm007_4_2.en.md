---
role: proof
locale: en
of_concept: hilbert-symbol-preimage-sets
source_book: gtm007
source_chapter: "4"
source_section: "2"
---

**Proof of (a).** The structure of $k^*/k^{*2}$ for $k = \mathbb{Q}_p$ follows from the explicit description of $p$-adic numbers. For $p \neq 2$, every element of $\mathbb{Q}_p^*$ can be written uniquely as $p^\nu u$ where $\nu \in \mathbb{Z}$ and $u \in \mathbb{Z}_p^*$. An element is a square if and only if $\nu$ is even and $u$ is a square in $\mathbb{Z}_p^*$. The group $\mathbb{Z}_p^*/\mathbb{Z}_p^{*2}$ has order $2$, with representatives $\{1, u_0\}$ where $u_0$ is a quadratic non-residue. Hence $k^*/k^{*2}$ has $2 \times 2 = 4 = 2^2$ elements, so $r = 2$.

For $p = 2$, every element of $\mathbb{Q}_2^*$ can be written as $2^\nu u$ with $u \in \mathbb{Z}_2^*$, and $u$ is a square if and only if $u \equiv 1 \pmod{8}$. The group $\mathbb{Z}_2^*/\mathbb{Z}_2^{*2}$ has order $4$, with representatives $\{\pm 1, \pm 5\}$ (or equivalently $\{1, 3, 5, 7\}$ modulo 8). Hence $k^*/k^{*2}$ has $2 \times 4 = 8 = 2^3$ elements, so $r = 3$.

**Proof of (b).** The Hilbert symbol $(x, a)$ defines a nondegenerate bilinear pairing on the $\mathbf{F}_2$-vector space $k^*/k^{*2}$. When $a = 1$, we have $(x, 1) = 1$ for all $x$, so $H_1^1 = k^*/k^{*2}$ (which has $2^r$ elements) and $H_1^{-1} = \varnothing$. When $a \neq 1$, the map $x \mapsto (x, a)$ is a nontrivial linear functional on the $\mathbf{F}_2$-vector space $k^*/k^{*2}$. The kernel of a nonzero linear functional on a vector space of dimension $r$ over $\mathbf{F}_2$ is a subspace of dimension $r-1$, hence has $2^{r-1}$ elements. Thus both $H_a^1$ (the kernel) and $H_a^{-1}$ (its complement) have exactly $2^{r-1}$ elements.

**Proof of (c).** Suppose $H_a^\varepsilon = H_{a'}^{\varepsilon'}$ and this set is nonempty. By part (b), if $a \neq a'$ then $H_a^\varepsilon$ and $H_{a'}^{\varepsilon'}$ are distinct cosets of the kernels of distinct linear functionals. Since $a \neq a'$, the linear functionals $x \mapsto (x, a)$ and $x \mapsto (x, a')$ are distinct nonzero functionals. For two distinct nonzero linear functionals on an $\mathbf{F}_2$-vector space, the equality of preimage sets $H_a^\varepsilon = H_{a'}^{\varepsilon'}$ forces $\varepsilon = \varepsilon'$ and the functionals to be identical, contradicting $a \neq a'$. Therefore $a = a'$, and consequently $\varepsilon = \varepsilon'$ as well.
