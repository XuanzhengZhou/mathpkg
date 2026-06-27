---
role: proof
locale: en
of_concept: theta-function-functional-equation
source_book: gtm007
source_chapter: "VII"
source_section: "6.2"
---
Apply the Poisson summation formula (Proposition 15) to the function $f(x) = e^{-\pi t (x \cdot x)}$ on $V$. The Fourier transform of a Gaussian is well-known: if $f(x) = e^{-\pi t Q(x)}$ where $Q(x) = x \cdot x$ is a positive definite quadratic form, then $\hat{f}(y) = t^{-n/2} e^{-\pi Q^*(y)/t}$, where $Q^*$ is the quadratic form associated to the dual inner product. Identifying $V$ with $V'$ via the bilinear form, the dual lattice $\Gamma'$ consists of $y \in V$ with $x \cdot y \in \mathbf{Z}$ for all $x \in \Gamma$.

Then the Poisson formula gives:
$$\Theta_\Gamma(t) = \sum_{x \in \Gamma} e^{-\pi t (x \cdot x)} = \frac{1}{v} \sum_{y \in \Gamma'} t^{-n/2} e^{-\pi (y \cdot y)/t} = t^{-n/2} v^{-1} \Theta_{\Gamma'}(t^{-1}).$$
The volume $v$ is given by $v = \det(A)^{1/2}$ where $A = (e_i \cdot e_j)$ is the Gram matrix of a basis $\{e_i\}$ of $\Gamma$, since $v^2 = \det(e_i \cdot e_j)$. This also shows $vv' = 1$ for dual lattices, as the dual basis has Gram matrix $A^{-1}$.
