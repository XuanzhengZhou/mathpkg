---
role: proof
locale: en
of_concept: properties-of-distributional-laplace-transform
source_book: gtm012
source_chapter: "6"
source_section: "§6. Laplace transforms of distributions"
---

# Proof of Properties of the Laplace Transform of Distributions

**Proposition 6.1.** Suppose $F, G \in \mathcal{L}'$ and suppose each satisfies a bound of the form

$$|F(u)| \leq K |u|_{k,a,M}, \quad u \in \mathcal{L}.$$

Then the Laplace transforms of $F$ and $G$ are defined for $\operatorname{Re} z > a$, and the following identities hold:

(5) $L(F+G) = LF + LG$.

(6) $L(cF) = c\,LF$ for any constant $c \in \mathbb{C}$.

(7) $L(T_s F)(z) = e^{-zs}\,LF(z)$, where $T_s$ is the translation operator.

(8)--(10) Analogous identities for the operators $D^k$, $e_w$, and multiplication by $t^n$.

(11) The distribution $e_w F$ is defined by $e_w F(u) = F(e_w u)$, $u \in \mathcal{L}$, where $e_w(t) = e^{-wt}$.

(12) If $F$ is the regular distribution defined by a function $f$, i.e. $F = F_f$, then $LF = Lf$, where $Lf$ is the classical Laplace transform of $f$.

*Proof.* The identities (5) and (6) follow immediately from the definitions. If $(u_n)_{1}^{\infty} \subset \mathcal{L}$ satisfies

$$|u_n - e_z|_{k,a,M} \to 0 \quad \text{as } n \to \infty,$$

then the sequence $(T_{-s} u_n)_{1}^{\infty}$ approximates $T_{-s} e_z$ in the same sense. But

$$T_{-s} e_z(t) = e_z(t+s) = e^{-z(t+s)} = e^{-zs} e^{-zt} = e^{-zs} e_z(t),$$

so

$$L(T_s F)(z) = \lim_{n \to \infty} T_s F(u_n) = \lim_{n \to \infty} F(T_{-s} u_n) = e^{-zs} \lim_{n \to \infty} F(u_n) = e^{-zs} LF(z).$$

This proves (7), and the proofs of (8), (9), and (10) are similar. Note that $u \in \mathcal{L}$ implies $e_w u \in \mathcal{L}$, and

$$u_n \to u \quad (\mathcal{L})$$

implies

$$e_w u_n \to e_w u \quad (\mathcal{L}).$$

Therefore (11) does define a distribution.

Finally, (12) follows from the definitions. $\square$
