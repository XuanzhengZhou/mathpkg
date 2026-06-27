---
role: proof
locale: en
of_concept: exterior-derivative-squared-zero
source_book: gtm035
source_chapter: "4"
source_section: "4.8"
---

# Proof of Exterior Derivative Satisfies $d^2 = 0$

**Lemma 4.8.** $d^2 = 0$ for every $k$; that is, if $\omega^k \in \wedge^k(\Omega)$ for arbitrary $k$, then $d(d\omega^k) = 0$.

## Proof

We first verify the case $k = 0$ and then extend to general $k$.

**Case $k = 0$:** Let $f \in C^\infty(\Omega) = \wedge^0(\Omega)$. By Definition 4.8,
$$df = \sum_{i=1}^{N} \frac{\partial f}{\partial x_i} dx_i.$$

Applying $d$ again:
$$d(df) = d\left(\sum_{i=1}^{N} \frac{\partial f}{\partial x_i} dx_i\right) = \sum_{i=1}^{N} \sum_{j=1}^{N} \frac{\partial}{\partial x_j}\left(\frac{\partial f}{\partial x_i}\right) dx_j \wedge dx_i$$
$$= \sum_{i<j} \left(\frac{\partial^2 f}{\partial x_i \partial x_j} - \frac{\partial^2 f}{\partial x_j \partial x_i}\right) dx_i \wedge dx_j.$$

Since $f \in C^\infty$, the mixed partial derivatives are equal: $\frac{\partial^2 f}{\partial x_i \partial x_j} = \frac{\partial^2 f}{\partial x_j \partial x_i}$. Hence each coefficient vanishes, and $d(df) = 0$. This proves $d^2 = 0$ on $\wedge^0(\Omega)$.

**General case $k \geq 1$:** Let $\omega^k \in \wedge^k(\Omega)$ be expressed in terms of its basis representation (Lemma 4.6):
$$\omega^k = \sum_{i_1 < \cdots < i_k} C_{i_1 \cdots i_k} \, dx_{i_1} \wedge \cdots \wedge dx_{i_k},$$
where the coefficients $C_{i_1 \cdots i_k} \in C^\infty(\Omega)$.

By Definition 4.8, the exterior derivative is
$$d\omega^k = \sum_{i_1 < \cdots < i_k} dC_{i_1 \cdots i_k} \wedge dx_{i_1} \wedge \cdots \wedge dx_{i_k}.$$

Applying $d$ a second time:
$$d(d\omega^k) = \sum_{i_1 < \cdots < i_k} d\Big(dC_{i_1 \cdots i_k} \wedge dx_{i_1} \wedge \cdots \wedge dx_{i_k}\Big).$$

For the exterior derivative of a wedge product, we use the graded Leibniz rule:
$$d(\alpha \wedge \beta) = d\alpha \wedge \beta + (-1)^{\deg \alpha} \alpha \wedge d\beta.$$

Let $\alpha = dC_{i_1 \cdots i_k}$ (degree 1) and $\beta = dx_{i_1} \wedge \cdots \wedge dx_{i_k}$ (degree $k$). Then
$$d(dC \wedge dx_{i_1} \wedge \cdots \wedge dx_{i_k}) = d(dC) \wedge dx_{i_1} \wedge \cdots \wedge dx_{i_k} + (-1)^1 dC \wedge d(dx_{i_1} \wedge \cdots \wedge dx_{i_k}).$$

Now, $d(dC) = 0$ by the $k=0$ case proved above. Moreover,
$$d(dx_{i_1} \wedge \cdots \wedge dx_{i_k}) = d(1) \wedge dx_{i_1} \wedge \cdots \wedge dx_{i_k} = 0,$$
since each $dx_j = d(x_j)$ and $d(d(x_j)) = 0$, so repeated application of the Leibniz rule with $d^2 = 0$ on functions yields zero.

Therefore each term in the sum vanishes, giving $d(d\omega^k) = 0$.

Thus $d^2 = 0$ on $\wedge^k(\Omega)$ for all $k$. $\square$

**Remark.** The identity $d^2 = 0$ is fundamental to de Rham cohomology: the space of closed $k$-forms ($d\omega = 0$) modulo exact $k$-forms ($\omega = d\eta$) forms the de Rham cohomology group $H^k_{\text{dR}}(\Omega)$.
