---
role: proof
locale: en
of_concept: invariance-of-phi-under-gamma0-q
source_book: gtm041
source_chapter: "4"
source_section: "4.7"
---
$\varphi$ is clearly meromorphic in the upper half-plane $H$. We prove that $\varphi$ is invariant under $\Gamma_0(q)$.

If $V = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \Gamma_0(q)$, then $c = c_1 q$ for some integer $c_1$. Hence
$$\Delta(V\tau) = (c\tau + d)^{12} \Delta(\tau) = (c_1 q\tau + d)^{12} \Delta(\tau).$$

On the other hand,
$$qV\tau = q \frac{a\tau + b}{c\tau + d} = \frac{a(q\tau) + bq}{c_1(q\tau) + d} = W(q\tau),$$
where
$$W = \begin{pmatrix} a & bq \\ c_1 & d \end{pmatrix}.$$
Since $\det W = ad - bq c_1 = ad - bc = 1$, we have $W \in SL(2,\mathbb{Z})$. Applying the transformation law of $\Delta$,
$$\Delta(qV\tau) = \Delta(W(q\tau)) = (c_1(q\tau) + d)^{12} \Delta(q\tau) = (c_1 q\tau + d)^{12} \Delta(q\tau).$$

Therefore
$$\varphi(V\tau) = \frac{\Delta(qV\tau)}{\Delta(V\tau)} = \frac{(c_1 q\tau + d)^{12} \Delta(q\tau)}{(c_1 q\tau + d)^{12} \Delta(\tau)} = \frac{\Delta(q\tau)}{\Delta(\tau)} = \varphi(\tau),$$
so $\varphi$ is invariant under $\Gamma_0(q)$.
