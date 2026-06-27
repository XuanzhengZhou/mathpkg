---
role: proof
locale: en
of_concept: fundamental-theorem-of-symmetric-polynomials
source_book: gtm030
source_chapter: "III"
source_section: "11"
---

**Proof.** The equation $\mathfrak{S} = \mathfrak{A}[p_1, p_2, \cdots, p_r]$ means that every symmetric polynomial can be expressed as a polynomial in the elementary symmetric functions $p_i$. It suffices to prove this for homogeneous polynomials. By a homogeneous polynomial we mean one in which all of the terms $a x_1^{k_1} x_2^{k_2} \cdots x_r^{k_r}$ have the same total degree $k = k_1 + k_2 + \cdots + k_r$. Any polynomial can be expressed in one and only one way as a sum of homogeneous polynomials of different degrees. Since the automorphisms $\sigma^*$ preserve degree, it is clear that, if $f(x_1, x_2, \cdots, x_r)$ is symmetric, then so are its homogeneous parts.

Suppose now that $f(x_1, x_2, \cdots, x_r)$ is a homogeneous symmetric polynomial of degree $m$. We introduce the lexicographic ordering for the monomials. The highest term of $p_1^{d_1} p_2^{d_2} \cdots p_r^{d_r}$ in this ordering is $x_1^{k_1} x_2^{k_2} \cdots x_r^{k_r}$ where

$$k_1 = d_1 + d_2 + \cdots + d_r, \quad k_2 = d_2 + \cdots + d_r, \quad \cdots, \quad k_r = d_r.$$

If the highest term of $f$ is $a x_1^{k_1} x_2^{k_2} \cdots x_r^{k_r}$, then by symmetry the exponents satisfy $k_1 \geq k_2 \geq \cdots \geq k_r$. Set

$$d_1 = k_1 - k_2, \quad d_2 = k_2 - k_3, \quad \cdots, \quad d_{r-1} = k_{r-1} - k_r, \quad d_r = k_r.$$

Then the highest term of $a p_1^{d_1} p_2^{d_2} \cdots p_r^{d_r}$ is $a x_1^{k_1} x_2^{k_2} \cdots x_r^{k_r}$, which matches the highest term of $f$. Hence the highest term of the homogeneous symmetric polynomial

$$f_1 = f - a p_1^{d_1} p_2^{d_2} \cdots p_r^{d_r}$$

is strictly less than that of $f$ in the lexicographic ordering. We can repeat this process with $f_1$. Since there are only finitely many highest terms lower than a given one, a finite number of applications yields a representation of $f$ as a polynomial in the $p_i$. This proves $\mathfrak{S} = \mathfrak{A}[p_1, p_2, \cdots, p_r]$.

We now show that the elementary symmetric polynomials are algebraically independent. Suppose there is a relation $\sum a_{d_1 \cdots d_r} p_1^{d_1} p_2^{d_2} \cdots p_r^{d_r} = 0$ in $\mathfrak{A}[p_1, \cdots, p_r]$. If any coefficient $a_{d_1 \cdots d_r} \neq 0$, consider the set of exponent tuples $(d_1, d_2, \cdots, d_r)$ for which $a_{d_1 \cdots d_r} \neq 0$. For each such tuple, define

$$k_1 = d_1 + d_2 + \cdots + d_r, \quad k_2 = d_2 + \cdots + d_r, \quad \cdots, \quad k_r = d_r.$$

The highest term in the lexicographic ordering of $a_{d_1 \cdots d_r} p_1^{d_1} p_2^{d_2} \cdots p_r^{d_r}$ is $a_{d_1 \cdots d_r} x_1^{k_1} x_2^{k_2} \cdots x_r^{k_r}$. If $(d_1', d_2', \cdots, d_r')$ is another tuple with $a_{d_1' \cdots d_r'} \neq 0$, then the corresponding highest term is $a_{d_1' \cdots d_r'} x_1^{k_1'} x_2^{k_2'} \cdots x_r^{k_r'}$ with $k_i'$ defined analogously. The mapping $(d_1, \cdots, d_r) \mapsto (k_1, \cdots, k_r)$ is injective (since $d_i = k_i - k_{i+1}$ for $i < r$ and $d_r = k_r$), so distinct tuples yield distinct exponent vectors. Thus the sum cannot vanish, since the term with the lexicographically largest $(k_1, \cdots, k_r)$ would have a nonzero coefficient in the expanded polynomial. Hence all $a_{d_1 \cdots d_r} = 0$, proving the algebraic independence of the $p_i$.
