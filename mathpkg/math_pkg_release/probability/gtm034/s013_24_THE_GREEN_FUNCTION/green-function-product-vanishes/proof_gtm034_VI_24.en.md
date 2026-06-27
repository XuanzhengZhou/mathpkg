---
role: proof
locale: en
of_concept: green-function-product-vanishes
source_book: gtm034
source_chapter: "VI"
source_section: "24"
---

For \(x \neq 0\), let \(T_x = \min\{k \geq 1 : x_k = x\}\). Then \(S(x) = E_0[\sum_{k=T_x}^{\infty} \delta(x_k,0)] = P_0[T_x < \infty] G(x,0) = G(0,x)G(x,0)/G(0,0)\) by the Markov property. Also \(S(x) = \sum_{k=0}^{\infty} P_0[x_k = 0; T_x \leq k] \leq \sum_{k=0}^{n} P_0[T_x \leq k] + \sum_{k=n+1}^{\infty} P_0[x_k = 0]\). Since the walk is transient, the tail sum is arbitrarily small for large \(n\). For each fixed \(k\), \(P_0[T_x \leq k] \to 0\) as \(|x| \to \infty\). Hence \(S(x) \to 0\).
