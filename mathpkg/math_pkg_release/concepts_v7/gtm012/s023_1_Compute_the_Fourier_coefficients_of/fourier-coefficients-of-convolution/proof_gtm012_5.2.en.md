---
role: proof
locale: en
of_concept: fourier-coefficients-of-convolution
source_book: gtm012
source_chapter: "5"
source_section: "§2. Fourier series, convolutions, and approximation"
---

# Proof of Fourier Coefficients of Convolutions of Distributions

Let $F, G \in \mathcal{P}'$ have Fourier coefficients $(a_n)_{n=-\infty}^{\infty}$ and $(b_n)_{n=-\infty}^{\infty}$, respectively. Let $u \in \mathcal{P}$ have Fourier coefficients $(c_n)_{n=-\infty}^{\infty}$.

Recall the definitions of convolution for periodic distributions (Section 2):

$$(F * u)(x) = F(T_x u), \qquad (F * G)(\varphi) = F(G^\sim * \varphi),$$

where $T_x$ denotes translation and $G^\sim(\varphi) = G(\varphi^\sim)$ with $\varphi^\sim(y) = \varphi(-y)$.

**Proof.** First compute $F * u$. Let $e_n(x) = e^{inx}$. Then

$$(T_x e_n)(y) = e_n(x - y) = e^{in(x-y)} = e^{inx} e^{-iny} = e_n(x) e_{-n}(y).$$

Hence

$$(F * e_n)(x) = F(T_x e_n) = F(e_n(x) e_{-n}) = e_n(x) F(e_{-n}) = a_n e_n(x).$$

By linearity and continuity, for any trigonometric polynomial we have

$$F * \left(\sum_{n=-N}^{N} c_n e_n\right) = \sum_{n=-N}^{N} a_n c_n e_n.$$

Taking the limit as $N \to \infty$ (justified by the continuity of convolution with a distribution), it follows that $F * u$ has Fourier coefficients $(a_n c_n)_{n=-\infty}^{\infty}$.

Now compute $F * G$. Observe that

$$(G^\sim * e_n)(x) = G^\sim(T_x e_n) = G^\sim(e_n(x) e_{-n}) = e_n(x) G^\sim(e_{-n}) = e_n(x) G(e_n) = b_{-n} e_n(x).$$

Therefore

$$(F * G)(e_{-n}) = F(G^\sim * e_{-n}) = F(b_n e_{-n}) = b_n F(e_{-n}) = a_n b_n.$$

Thus the $n$-th Fourier coefficient of $F * G$ is $a_n b_n$, completing the proof. $\square$

As an immediate application: if $u \in \mathcal{P}$ and $G = F_u$ (the distribution corresponding to $u$), then $F * G = F_v$ where $v = F * u$, since $F * G$ and $F * u$ have the same Fourier coefficients and the Fourier coefficient map is injective.
