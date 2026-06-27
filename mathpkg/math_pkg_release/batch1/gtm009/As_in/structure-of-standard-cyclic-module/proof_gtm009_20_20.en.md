---
role: proof
locale: en
of_concept: structure-of-standard-cyclic-module
source_book: gtm009
source_chapter: "20"
source_section: "20.2"
---

**Proof.** (a) By the PBW Theorem (Corollary C of Theorem 17.3), $\mathfrak{U}(L)$ has basis consisting of monomials $\prod_{\alpha \in \Phi^+} y_\alpha^{i_\alpha} \prod_{h \in \text{basis of } H} h^{j_h} \prod_{\alpha \in \Phi^+} x_\alpha^{k_\alpha}$ where $x_\alpha \in L_\alpha$, $y_\alpha \in L_{-\alpha}$. Since $v^+$ is killed by all $x_\alpha$ and $H$ acts on $v^+$ by the scalar $\lambda(h)$, applying such a monomial to $v^+$ yields a scalar multiple of a vector of the form $y_{\beta_1}^{i_1} \cdots y_{\beta_m}^{i_m} \cdot v^+$. Hence these vectors span $V$.

(b) Each $y_\beta$ ($\beta \in \Phi^+$) has weight $-\beta$, so the vector in (a) has weight $\lambda - \sum i_j \beta_j$, which is $\preceq \lambda$. Since the sum is over positive roots, the difference $\lambda - \mu$ is a sum of positive roots.

(c) For a fixed $\mu = \lambda - \sum i_j \beta_j$, there are only finitely many ways to represent $\mu$ in this form (because $\sum i_j \beta_j$ is fixed in the root lattice and the $i_j$ are nonnegative integers and $\beta_j$ are positive roots). Hence $\dim V_\mu < \infty$. The weight space $V_\lambda$ corresponds to all $i_j = 0$, giving only $v^+$ (up to scalar), so $\dim V_\lambda = 1$.

(d) Let $W$ be a nonzero submodule of $V$. For any $w \in W$, write $w = \sum v_i$ with $v_i \in V_{\mu_i}$ for distinct weights. We claim each $v_i \in W$. If not, choose $w = v_1 + \cdots + v_n$ with minimal $n > 1$ and no $v_i \in W$. Find $h \in H$ with $\mu_1(h) \neq \mu_2(h)$. Then $h \cdot w = \sum \mu_i(h) v_i \in W$, and $(h - \mu_1(h)\cdot 1) \cdot w = (\mu_2(h) - \mu_1(h)) v_2 + \cdots + (\mu_n(h) - \mu_1(h)) v_n \neq 0$ also lies in $W$. By minimality of $n$, $v_2 \in W$, a contradiction. Hence $W = \bigoplus (W \cap V_\mu)$ is the direct sum of its weight spaces.

(e) From (c) and (d), each proper submodule of $V$ lies in the sum of weight spaces other than $V_\lambda$. Therefore the sum of all proper submodules is still proper (it does not contain $V_\lambda$), so $V$ has a unique maximal submodule. $V$ cannot be a direct sum of two proper submodules, since each would be contained in the maximal one. Hence $V$ is indecomposable and has a unique irreducible quotient.

(f) If $\phi: V \to W$ is a nonzero module homomorphism, then $\phi(v^+)$ is nonzero (otherwise $\phi$ vanishes on the generator and hence on all of $V$). Since $\phi(v^+)$ is again a maximal vector of weight $\lambda$ and generates $W$, $W$ is standard cyclic of weight $\lambda$. $\square$
