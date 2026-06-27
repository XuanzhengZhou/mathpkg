---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The Hoeffding inequality for the Bernoulli scheme gives a simple, explicit exponential bound on the probability that the sample mean $S_n/n$ deviates from the true mean $p$ by more than $\varepsilon$. The bound $2e^{-2n\varepsilon^2}$ does not depend on the unknown parameter $p$, making it universally applicable. This is a special case of Hoeffding's general inequality for bounded independent random variables. Compared with the optimal Chernoff bound involving the binary relative entropy $H(a)$, this bound uses the quadratic approximation $H(p \pm \varepsilon) \ge 2\varepsilon^2$, sacrificing some tightness for a cleaner, parameter-free expression.
