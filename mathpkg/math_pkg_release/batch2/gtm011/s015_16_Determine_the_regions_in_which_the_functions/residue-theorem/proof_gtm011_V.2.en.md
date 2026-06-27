---
role: proof
locale: en
of_concept: residue-theorem
source_book: gtm011
source_chapter: "V"
source_section: "§2. Residues"
content_hash: ""
written_against: ""
---

For each singularity $a_k$, let $\gamma_k$ be the circle $|z - a_k| = r_k$ traversed in the clockwise direction, where $r_k > 0$ is chosen sufficiently small so that $\overline{B}(a_k; r_k) \subset G$ and these closed disks are pairwise disjoint. Then $\gamma \approx \sum_{k=1}^{m} (-\gamma_k)$ in $G \setminus \{a_1, \ldots, a_m\}$. Since $f$ is analytic in $G \setminus \{a_1, \ldots, a_m\}$, Cauchy's Theorem (Theorem IV.5.7) gives
$$0 = \int_{\gamma} f + \sum_{k=1}^{m} \int_{\gamma_k} f.$$
Hence
$$\int_{\gamma} f = -\sum_{k=1}^{m} \int_{\gamma_k} f = \sum_{k=1}^{m} \int_{-\gamma_k} f.$$

Now fix one singularity $a_k$ and let
$$f(z) = \sum_{n=-\infty}^{\infty} b_n (z - a_k)^n$$
be the Laurent expansion of $f$ about $z = a_k$. This series converges uniformly on $\partial B(a_k; r_k)$, so we may interchange the sum and the integral:
$$\int_{-\gamma_k} f = \sum_{n=-\infty}^{\infty} b_n \int_{-\gamma_k} (z - a_k)^n.$$

For $n \neq -1$, the function $(z - a_k)^n$ has a primitive in $G \setminus \{a_k\}$, namely $\frac{1}{n+1}(z - a_k)^{n+1}$. Therefore $\int_{-\gamma_k} (z - a_k)^n = 0$ for $n \neq -1$.

For $n = -1$, we have
$$\int_{-\gamma_k} (z - a_k)^{-1} = 2\pi i \, n(-\gamma_k; a_k) = 2\pi i \, n(\gamma; a_k),$$
since $-\gamma_k$ is traversed counterclockwise and $n(-\gamma_k; a_k) = n(\gamma; a_k)$ because $\gamma \approx \sum (-\gamma_k)$ implies the winding numbers match.

Thus
$$\int_{-\gamma_k} f = b_{-1} \cdot 2\pi i \, n(\gamma; a_k) = 2\pi i \, n(\gamma; a_k) \operatorname{Res}(f; a_k).$$

Summing over all $k = 1, \ldots, m$ yields
$$\int_{\gamma} f = 2\pi i \sum_{k=1}^{m} n(\gamma; a_k) \operatorname{Res}(f; a_k).$$

**Remark.** The condition that $f$ has only finitely many isolated singularities is not essential. If $f$ has infinitely many isolated singularities, they can only accumulate on $\partial G$. If $r = d(\{\gamma\}, \partial G)$, then $\gamma \approx 0$ implies $n(\gamma; a) = 0$ whenever $d(a; \partial G) < \frac{1}{2} r$, so only finitely many singularities have non-zero winding number and contribute to the sum.
