---
role: proof
locale: en
of_concept: irreducible-endomorphism-continuous-functions
source_book: gtm003
source_chapter: "Appendix D"
source_section: "3. The Peripheral Point Spectrum"
---

**Proof of (3.3).** By the corollary of (2.6), there exists a positive Radon measure $\mu_0$ on $X$ such that $r\mu_0 = u'(\mu_0)$. Since $\{f: \mu_0(|f|) = 0\}$ is a solid subspace of $\mathcal{C}_{\mathbb{R}}(X)$ invariant under $u$, $\mu_0$ is strictly positive, which is equivalent to the assertion that the support $S_0$ of $\mu_0$ equals $X$.

**(i):** By (2.5), $r = \|u\|_{\mu_0} \leq \|u\|$; from $\langle \mathbf{1}, r\mu_0 \rangle = \langle u(\mathbf{1}), \mu_0 \rangle \leq \|u\| \langle \mathbf{1}, \mu_0 \rangle$ it follows that $r \leq \|u\|$. If $\|u\| = r$, then $\langle r\mathbf{1} - u(\mathbf{1}), \mu_0 \rangle = 0$ and since $u(\mathbf{1}) \leq r\mathbf{1}$ by (2.5) and $\mu_0$ is strictly positive, we obtain $u(\mathbf{1}) = r\mathbf{1}$. Conversely, $u(\mathbf{1}) = r\mathbf{1}$ implies $\|u\| = r$ because $\|\mathbf{1}\| = 1$ and $u$ is positive. Finally, $r > 0$ follows from (3.2)(i).

**(ii):** Let $r\alpha$, $|\alpha| = 1$, be an eigenvalue of $u$ and let $f$ be a corresponding eigenfunction. Writing $f = |f|g$ with $|g| = 1$, we have $r|f| = r|f| \cdot |g| = |r\alpha f| = |u(f)| \leq u(|f|)$, hence $\langle r|f| - u(|f|), \mu_0 \rangle \leq 0$; but $\langle u(|f|), \mu_0 \rangle = r\langle |f|, \mu_0 \rangle$, so $\langle r|f| - u(|f|), \mu_0 \rangle = 0$. Since $\mu_0$ is strictly positive, we obtain $u(|f|) = r|f|$, hence $|f|$ is an eigenfunction for $r$ and $|f|(t) > 0$ for all $t \in X$.

Define $v$ on $\mathcal{C}_{\mathbb{C}}(X)$ by $v(h) = r^{-1}|f|^{-1} u(|f|h)$. Then $v$ is a positive endomorphism on $\mathcal{C}_{\mathbb{R}}(X)$ (extended to the complexification) with $v(\mathbf{1}) = \mathbf{1}$, and $v(g) = \alpha g$. From Lemma 2 it follows that $\alpha^n g^n = v(g^n)$ for all $n \in \mathbb{Z}$, which implies that $r\alpha^n$ is an eigenvalue of $u$ with eigenfunction $|f|g^n$. Thus the peripheral point spectrum is cyclic.

**(iii):** Let $r\alpha$, where $\alpha = \exp i\theta$, be an eigenvalue of $u$. It has been shown under (ii) that any eigenfunction $f$ pertaining to $r\alpha$ satisfies $|f|(t) > 0$ for all $t \in X$, i.e., $f$ is $\neq 0$ throughout. Moreover, $f_0 = |f|$ is an eigenfunction for $r$. If $h$ is any other eigenfunction for $r$, we can assume $h$ is real valued; set $c = \sup \{h(t)/f_0(t): t \in X\}$. The function $c f_0 - h$ belongs to the eigenspace $N(r)$ and vanishes for at least one $t \in X$, since the supremum is attained in $X$. Hence $c f_0 - h = 0$, proving that the multiplicity of $r$ is $1$.

Denote by $w$ the endomorphism of $\mathcal{C}_{\mathbb{C}}(X)$ defined by $h \mapsto g h$, where $g = f/|f|$ (so $|g| = 1$). Define $v = \alpha^{-1} w^{-1} u w$; as a continuous endomorphism of $\mathcal{C}_{\mathbb{C}}(X)$, $v$ is given by
$$v(h)(s) = \int h(t) \, d\nu_s(t) \quad (s \in X),$$
where each $\nu_s$ is a uniquely determined complex Radon measure on $X$. Similarly, let $u(h)(s) = \int h(t) \, d\mu_s(t)$ $(s \in X)$. In view of $|g| = 1$, we obtain
$$\left|\int h(t) \, d\nu_s(t)\right| = |g(s)^{-1} u(g h)(s)| \leq u(|h|)(s) = \int |h(t)| \, d\mu_s(t)$$
for all $s \in X$. Thus if $\nu_s = \rho_s + i\tau_s$ is the Lebesgue decomposition of $\nu_s$ with respect to $\mu_s$, then $|\nu_s| \leq \mu_s$. Since $v(\mathbf{1}) = \mathbf{1}$, we have $\int d\nu_s(t) = 1$ for all $s$, and the preceding inequality implies $\mu_s(X) \geq 1$.

Now $v(\mathbf{1}) = \mathbf{1}$ and $v(g) = \alpha g$ together with the integral representation of $v$ yield $\alpha g(s) = \int g(t) \, d\nu_s(t)$. Since $|\nu_s| \leq \mu_s$ and $\int d\mu_s \leq \|u\|/r$, a standard argument shows that for each $s$, $\nu_s$ is supported on the set where $g(t) = \alpha g(s)$; moreover, $\nu_s$ is a positive measure and $\mu_s(X) = 1$. From this it follows that for any eigenvalue $r\beta$ of $u$ with eigenfunction $h$, the rotated function $s \mapsto h(s) \exp(-i\theta \arg g(s))$ is an eigenfunction for $r\beta \alpha^{-1}$, establishing the rotational invariance of $\sigma(u)$. The multiplicity-$1$ property for arbitrary peripheral eigenvalues follows similarly from the argument above applied to $v$.

**(iv):** If the peripheral point spectrum contains an isolated point $r\alpha_0$, then by cyclicity (ii), the set of all peripheral eigenvalues is $\{r\alpha_0^n: n \in \mathbb{Z}\}$. Since this set is contained in the compact spectral circle, if it is infinite it must accumulate somewhere, contradicting the isolation of $r\alpha_0$ unless the set is finite. Hence the set is of the form $rH$ where $H$ is a finite cyclic group, i.e., the group of $n$th roots of unity for some $n \geq 1$.

**(v):** If one point $r\alpha$ of the peripheral point spectrum is a pole of the resolvent, then by the rotational invariance established in (iii), every point of the peripheral point spectrum is a pole of the same order. By (3.2)(i), this common order is $1$.

**(vi):** Suppose $\lambda f = u(f)$ with $0 \neq f \geq 0$. Then $\lambda \langle f, \mu_0 \rangle = \langle u(f), \mu_0 \rangle = r \langle f, \mu_0 \rangle$, and since $\langle f, \mu_0 \rangle > 0$ we obtain $\lambda = r$.

Let $r\alpha$, where $\alpha$ is a primitive $n$th root of unity ($n \geq 2$), be an eigenvalue of $u$ with eigenfunction $f = |f|g$. Define $v(h) = r^{-1}|f|^{-1} u(|f|h)$; then $\alpha g = v(g)$ and $v$ satisfies the hypothesis of Lemma 2. Set $M_k = g^{-1}(\alpha^k)$ for $k = 0, 1, \ldots$. Without loss of generality, assume $M_0 \neq \emptyset$, i.e., $g(t) = 1$ for some $t \in X$. As in the proof of Lemma 2, write $v(h)(s) = \int h(t) \, d\mu_s(t)$ $(s \in X)$ and conclude from $\alpha g = v(g)$, $|g| = 1$, that whenever $s \in M_k$, the support of $\mu_s$ is contained in $M_{k+1}$ (indices modulo $n$). Since the sets $M_k$ are pairwise disjoint for incongruent indices modulo $n$, the map $v$ induces a cyclic permutation $M_k \to M_{k-1}$ ($k \bmod n$). The closed solid sublattice $F \subset \mathcal{C}_{\mathbb{R}}(X)$ of functions vanishing on $M = \bigcup_{0}^{n-1} M_k$ is invariant under $v$ and hence under $u$. By (3.1), $F = \{0\}$, so $M = X$. But if $X$ is connected, this decomposition of $X$ into $n \geq 2$ disjoint closed (since $g$ is continuous) sets is impossible. Thus no root of unity $\alpha \neq 1$ can appear in the peripheral point spectrum when $X$ is connected.
