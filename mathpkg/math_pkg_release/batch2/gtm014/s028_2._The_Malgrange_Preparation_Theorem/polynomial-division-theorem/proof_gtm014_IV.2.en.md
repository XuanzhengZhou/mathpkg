---
role: proof
locale: en
of_concept: polynomial-division-theorem
source_book: gtm014
source_chapter: "IV"
source_section: "2"
---

The proof follows the same strategy as the proof of Theorem 1.4, but uses Green's Theorem (Lemma 2.3) in place of the Cauchy Integral Formula.

Let $\tilde{G}(t, x, \lambda) = G(t, x)$ for all real $t$. Extend $\tilde{G}$ to a smooth function on $\mathbf{C} \times \mathbf{R}^n \times \mathbf{C}^k$ such that $\partial \tilde{G}/\partial \bar{z}$ vanishes to infinite order on the zero set of $P_k(z, \lambda)$ and for real $z$. (The existence of such an extension is the content of Proposition 2.4.)

Then define, using the generalized Cauchy formula of Lemma 2.3,
$$q(w, x, \lambda) = \frac{1}{2\pi i} \int_{\gamma} \frac{\tilde{G}(\eta, x, \lambda)}{P_k(\eta, \lambda)} \frac{d\eta}{(\eta - w)} + \frac{1}{2\pi i} \iint_D \frac{(\partial \tilde{G}/\partial \bar{z})(\eta, x, \lambda)}{P_k(\eta, \lambda)} \frac{d\eta \wedge d\bar{\eta}}{(\eta - w)}$$
and
$$r_i(x, \lambda) = \frac{1}{2\pi i} \int_{\gamma} \frac{\tilde{G}(\eta, x, \lambda)}{P_k(\eta, \lambda)} s_i(\eta, \lambda) \, d\eta + \frac{1}{2\pi i} \iint_D \frac{(\partial \tilde{G}/\partial \bar{z})(\eta, x, \lambda)}{P_k(\eta, \lambda)} s_i(\eta, \lambda) \, d\eta \wedge d\bar{\eta}$$
where $s_i(\eta, \lambda)$ are the coefficients in the partial fraction decomposition of $1/P_k$. The first integrals are well-defined and smooth because $\gamma$ avoids the zeroes of $P_k$. The second integrals are well-defined because $\partial \tilde{G}/\partial \bar{z}$ vanishes on the zeroes of $P_k$, making the integrands bounded. Lemma 2.3 then guarantees that $q$ and $r_i$ are smooth. The identity $G = qP_k + r$ follows from the generalized Cauchy formula applied to $\tilde{G} - qP_k - r$.

The "moreover" part follows by taking real parts: since $P_k$ is real-valued, equating the real parts of both sides yields the result for real-valued $G$.
