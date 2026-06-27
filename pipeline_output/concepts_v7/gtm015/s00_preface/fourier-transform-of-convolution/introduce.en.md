---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The Fourier transform converts convolution in $\ell^1(\mathbb{Z})$ to pointwise multiplication in the Wiener algebra $\mathcal{A}$. This fundamental identity, $\widehat{xy} = \hat{x} \cdot \hat{y}$, follows from the absolute convergence of the double series and rearrangement: the convolution sum $\sum_m (\sum_n x(m-n)y(n)) e^{imt}$ can be rewritten as $\sum_n y(n) e^{int} \sum_k x(k) e^{ikt}$ by the change of variables $k = m-n$. This makes the Fourier transform an algebra isomorphism between $(\ell^1(\mathbb{Z}), *)$ and $(\mathcal{A}, \cdot)$, and is the reason why convolution is the natural product on $\ell^1(\mathbb{Z})$.
