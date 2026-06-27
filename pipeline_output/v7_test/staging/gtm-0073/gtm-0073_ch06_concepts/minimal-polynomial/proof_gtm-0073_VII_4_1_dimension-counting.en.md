---
role: proof
source_book: gtm-0073
chapter: VII
section: "VII.4"
proof_technique: dimension-counting
locale: en
content_hash: ""
written_against: ""
---
(i) The evaluation map $\zeta_\phi : K[x] \to \operatorname{Hom}_K(E,E)$ is a $K$-algebra homomorphism. Since $\operatorname{Hom}_K(E,E)$ is $n^2$-dimensional over $K$ and $K[x]$ is infinite-dimensional, $\operatorname{Ker} \zeta_\phi \neq 0$ by Corollary IV.2.14. Since $K[x]$ is a PID whose units are nonzero constants (Corollary III.6.4), $\operatorname{Ker} \zeta_\phi = (q)$ for some monic $q \in K[x]$ with $\deg q \geq 1$. If $(q_1)$ also generates the kernel with $q_1$ monic, then $q \mid q_1$ and $q_1 \mid q$, so $q = q_1$.

(ii) Same argument with $\operatorname{Mat}_n K$ replacing $\operatorname{Hom}_K(E,E)$.

(iii) Let $\theta : \operatorname{Hom}_K(E,E) \cong \operatorname{Mat}_n K$ be the isomorphism of Theorem 1.2 sending $\phi \mapsto A$. The diagram commutes: $\theta \zeta_\phi = \zeta_A$ (since $\theta \zeta_\phi(x) = \theta(\phi) = A = \zeta_A(x)$ and $\theta \zeta_\phi(k) = \theta(k 1_E) = k I_n = \zeta_A(k)$). Hence $\operatorname{Ker} \zeta_\phi = \operatorname{Ker} \zeta_A$ via $\theta$, so $q_\phi = q_A$.
