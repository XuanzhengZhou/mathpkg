---
role: proof
locale: en
of_concept: gauss-lemma
source_book: gtm051
source_chapter: "5"
source_section: "5.3"
---

Let $(U,g)$ be a coordinate system on $M$. Define

$$\phi: V := ]-\rho,\rho[ \times ]-\pi,\pi[ \to B_\rho(u_0),$$

$$(v^1,v^2) \mapsto \exp_{u_0}(v^1\cos v^2\,e_1+v^1\sin v^2\,e_2)=:(u^1,u^2).$$

We shall show that this is a geodesic coordinate system when $v^1>0$. To do this we use (4.3.6 (iii)), which means we must show that in these coordinates $\tilde{g}_{11}=1$, $\tilde{g}_{12}=0$, and $\tilde{g}_{22}>0$. Now consider

$$\tilde{g}_{ij} = \sum_{k,l} g_{kl}\frac{\partial u^k}{\partial v^i}\frac{\partial u^l}{\partial v^j}$$

on $V$. Since $u^k(0,v^2)=u^0_k=$ constant for $k=1,2$, $\tilde{g}_{12}(0,v^2)=0$. Fixing $v^2=v^0_2$ and letting $v^1=t\in]-\rho,\rho[$ vary parameterizes a unit-speed geodesic. Therefore $\tilde{g}_{11}=1$ and, for $v^1>0$, the metric is positive definite in these coordinates. By the previously established characterization of geodesic coordinates (4.3.6 (iii)), this proves that $\phi$ yields geodesic coordinates based on a geodesic circle.
