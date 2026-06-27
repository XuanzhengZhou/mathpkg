---
role: proof
locale: en
of_concept: proposition-17-22
source_book: gtm055
source_chapter: "16-17"
source_section: "Section 18_Section_18"
---

Proof. The winding number of $\gamma_1 - \gamma_2$ on $\mathbb{C} \setminus U$ is zero since $w_{\gamma_1} = w_{\gamma_2} = 0$ there. The winding number of $\gamma_1 - \gamma_2$ on $K$ is likewise $w_{\gamma_1} - w_{\gamma_2} = 0$. Hence $\gamma_1 - \gamma_2 \sim 0$ in $U \setminus K$, so

$$\int_{\gamma_1 - \gamma_2} \Phi(\zeta) d\zeta = 0$$

by Theorem 17.21.

We are now ready to define the concept of an analytic function of an operator $T$ on a Banach space $\mathcal{E}$. Just as in Chapter 12, however, where a similar idea was introduced for rational functions (cf. Problem 12N), it turns out that the appropriate context in which to give this definition is that of a unital Banach algebra. In this connection we note that if $a$ is an element of a Banach algebra $\mathcal{A}$, then multiplication by $a$ (on either right or left) is a bounded linear transformation on $\mathcal{A}$ (cf. Problem U). Hence if $\int_{\alpha} \Phi(\zeta) d\zeta$ is a line integral of some $\mathcal{A}$-valued mapping $\Phi$, then, according to Proposition 17.20,

$$a \left[ \int_{\alpha} \Phi(\zeta) d\zeta \right] = \int_{\alpha} a \Phi(\zeta

and $f_2$ are locally analytic functions defined on open sets $U_1$ and $U_2$, respectively, and if $f_1 = f_2$ on some open subset $V$ of $U_1 \cap U_2$ that contains $\sigma_{\mathcal{A}}(x)$, then $f_1(x) = f_2(x)$, since $\gamma$ can be chosen to be an oriented envelope of $\sigma_{\mathcal{A}}(x)$ in $V$. In particular, if $\sigma_{\mathcal{A}}(x) \subset U_1 \subset U_2$ and if $f_1 = f_2|U_1$, then $f_1(x) = f_2(x)$.

The rationale of this definition is best seen by considering the special case $\mathcal{A} = \mathbb{C}$. If $\alpha \in \mathbb{C}$ then $\sigma_{\mathbb{C}}(\alpha) = \{\alpha\}$ and $R_{\alpha}(\lambda) = 1/(\lambda - \alpha)$, $\lambda \neq \alpha$. Hence

$$f(\alpha) = \frac{1}{2\pi i} \int_{\gamma} f(\zeta) R_{\alpha}(\zeta) d\zeta$$

for any function $f$ that is analytic on some open neighborhood $U$ of $\alpha$ and any oriented envelope $\gamma$ of $\{\alpha\}$ in $U$ by the Cauchy integral formula. Thus what we are doing in the present context is, in effect, turning the Cauchy integral formula into a definition. The use of line integration to define analytic functions of matrices dates back to the nineteenth century; the bold extension of the construction presented here is due, in substance, to F. Riesz [53], N. Dunford [21] and I. Gelfand [28].

An arrangement for defining various functions of the elements of a Banach algebra $\mathcal{A}$ in a systematic and useful manner is usually referred to as a functional calculus on $\mathcal{A}$. The functional calculus introduced above is customarily known as the Riesz-Dunford functional calculus. Our first result concerning this functional calculus is a useful technicality.
