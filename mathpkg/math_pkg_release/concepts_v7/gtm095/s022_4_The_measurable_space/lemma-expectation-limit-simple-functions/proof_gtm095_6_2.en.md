---
role: proof
locale: en
of_concept: lemma-expectation-limit-simple-functions
source_book: gtm095
source_chapter: "6"
source_section: "2"
---

# Proof of Lemma on Expectation Limit for Simple Functions

Let $\varepsilon > 0$ and

$$A_n = \{\omega : \xi_n \geq \eta - \varepsilon\}.$$

It is clear that $A_n \uparrow \Omega$ and

$$\xi_n = \xi_n I_{A_n} + \xi_n I_{\overline{A}_n} \geq \xi_n I_{A_n} \geq (\eta - \varepsilon)I_{A_n}.$$

Hence by the properties of the expectations of simple random variables we find that

$$E\xi_n \geq E[(\eta - \varepsilon)I_{A_n}] \geq E\eta - \varepsilon - c P(\overline{A}_n),$$

where $c = \max_\omega \eta(\omega)$ (finite since $\eta$ is simple). As $n \to \infty$, $P(\overline{A}_n) \to 0$, and since $\varepsilon > 0$ is arbitrary, we obtain

$$\lim_n E\xi_n \geq E\eta.$$

This inequality establishes that the limit $\lim_n E\xi_n$ is independent of the choice of the approximating sequence. Indeed, if $\xi_n \uparrow \xi$ and $\eta_m \uparrow \xi$, where $\{\eta_m\}$ is another sequence of simple functions, then for each fixed $m$ we have $\xi_n \uparrow \xi \geq \eta_m$, so by the lemma $\lim_n E\xi_n \geq E\eta_m$. Letting $m \to \infty$ gives $\lim_n E\xi_n \geq \lim_m E\eta_m$. By symmetry the reverse inequality holds, hence

$$\lim_n E\xi_n = \lim_m E\eta_m.$$

Thus the expectation is well defined for nonnegative random variables.
