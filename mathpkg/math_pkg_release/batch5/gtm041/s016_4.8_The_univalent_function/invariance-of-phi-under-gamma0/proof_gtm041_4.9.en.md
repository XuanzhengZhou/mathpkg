---
role: proof
locale: en
of_concept: invariance-of-phi-under-gamma0
source_book: gtm041
source_chapter: "4"
source_section: "4.9"
---

If $q = 2$ we have $r = 24$ and $\Phi(\tau) = \Delta(q\tau)/\Delta(\tau)$. In this case the theorem was already proved in Theorem 4.7. Therefore we assume that $q \geq 3$.

Let $V = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \Gamma_0(q)$, so that $c \equiv 0 \pmod{q}$. Write $c = q c_1$ for some integer $c_1$. The transformation formula for the Dedekind eta function gives
$$\eta(V\tau) = \varepsilon(V)\{-i(c\tau + d)\}^{1/2}\eta(\tau),$$
where $\varepsilon(V)$ is the Dedekind multiplier. Applying this to $\eta(qV\tau)$, we write
$$qV\tau = \frac{a(q\tau) + bq}{c_1(q\tau) + d}.$$
Define
$$V_1 = \begin{pmatrix} a & bq \\ c_1 & d \end{pmatrix}.$$
Since $\det V = ad - bc = 1$ and $c = qc_1$, we have $ad - bq c_1 = 1$, so $V_1 \in \Gamma = SL(2,\mathbb{Z})$. Then
$$\eta(qV\tau) = \eta(V_1 q\tau) = \varepsilon(V_1)\{-i(c_1 q\tau + d)\}^{1/2}\eta(q\tau).$$

Combining this with the transformation of $\eta(\tau)$, we obtain
$$\Phi(V\tau) = \left(\frac{\eta(qV\tau)}{\eta(V\tau)}\right)^r = \left(\frac{\varepsilon(V_1)}{\varepsilon(V)}\right)^r \Phi(\tau).$$

Now the Dedekind multiplier ratio satisfies
$$\left(\frac{\varepsilon(V_1)}{\varepsilon(V)}\right)^r = e^{-\pi i r \delta},$$
where
$$\delta = \left\{\frac{a + d}{12c} + s(-d, c)\right\} - \left\{\frac{a + d}{12c_1} + s(-d, c_1)\right\},$$
and $s(h,k)$ denotes the Dedekind sum.

Since $ad - bc = 1$ we have $ad \equiv 1 \pmod{c}$ and $ad \equiv 1 \pmod{c_1}$, so $s(-d, c) = -s(a, c)$ and $s(-d, c_1) = -s(a, c_1)$. Therefore
$$\delta = \frac{a+d}{12c} - s(a,c) - \frac{a+d}{12c_1} + s(a,c_1).$$

Theorem 3.11 (the reciprocity law for Dedekind sums) implies that $r\delta$ is an even integer. Hence $e^{-\pi i r\delta} = 1$, and consequently
$$\Phi(V\tau) = \Phi(\tau)$$
for every $V \in \Gamma_0(q)$. Thus $\Phi$ is automorphic under $\Gamma_0(q)$.
