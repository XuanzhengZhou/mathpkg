---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The Berry--Esseen theorem quantifies the rate of convergence in the Central Limit Theorem for sums of i.i.d. random variables with finite third absolute moment. It states that the Kolmogorov distance between the standardized sum distribution $F_n$ and the standard normal $\Phi$ is bounded by $C \cdot E|\xi_1|^3/(\sigma^3\sqrt{n})$, where $C$ is an absolute constant. The currently known optimal bounds are $0.4097 < C < 0.469$ (Shevtsova, 2013). The proof uses the smoothing inequality relating the uniform distance to an $L^1$ distance of characteristic functions, combined with a Taylor expansion estimate for $|f_n(t) - \varphi(t)|$ valid up to $T = \sqrt{n}/(5\beta_3)$. The $\sqrt{n}$ rate is sharp, as shown by the Bernoulli case.
