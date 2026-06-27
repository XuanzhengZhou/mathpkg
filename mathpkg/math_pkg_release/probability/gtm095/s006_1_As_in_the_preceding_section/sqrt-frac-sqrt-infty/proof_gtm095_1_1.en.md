---
role: proof
locale: en
of_concept: sqrt-frac-sqrt-infty
source_book: gtm095
source_chapter: "1"
source_section: "1"
---

# Proof of Corollary (Equivalent Form of the Local Limit Theorem)

The local limit theorem (proved above) states that for $0 < p < 1$,

$$P_n(k) \sim \frac{1}{\sqrt{2\pi npq}} e^{-(k-np)^2/(2npq)}$$

uniformly for all $k$ such that $|k - np| = o(npq)^{2/3}$, i.e., as $n \to \infty$,

$$\sup_{\{k: |k-np| \leq \varphi(n)\}} \left| \frac{P_n(k)}{\frac{1}{\sqrt{2\pi npq}} e^{-(k-np)^2/(2npq)}} - 1 \right| \to 0,$$

where $\varphi(n) = o(npq)^{2/3}$ and $q = 1-p$.

To obtain the equivalent form, substitute

$$k = np + x\sqrt{npq}.$$

Then:

1. The integer condition $k \in \{0, 1, \ldots, n\}$ translates to $np + x\sqrt{npq}$ being an integer from $\{0, 1, \ldots, n\}$.

2. The exponent in the Gaussian factor becomes
   $$\frac{(k-np)^2}{2npq} = \frac{(x\sqrt{npq})^2}{2npq} = \frac{x^2 npq}{2npq} = \frac{x^2}{2}.$$
   Hence
   $$\frac{1}{\sqrt{2\pi npq}} e^{-(k-np)^2/(2npq)} = \frac{1}{\sqrt{2\pi npq}} e^{-x^2/2}.$$

3. The uniformity condition $|k - np| = o(npq)^{2/3}$ becomes
   $$|x|\sqrt{npq} = o(npq)^{2/3},$$
   which is equivalent to
   $$|x| = o(npq)^{1/6}.$$

Therefore, for all $x \in \mathbb{R}^1$ such that $x = o(npq)^{1/6}$ and $np + x\sqrt{npq}$ is an integer in $\{0, 1, \ldots, n\}$,

$$P_n(np + x\sqrt{npq}) \sim \frac{1}{\sqrt{2\pi npq}} e^{-x^2/2},$$

i.e., as $n \to \infty$,

$$\sup_{\{x: |x| \leq \psi(n)\}} \left| \frac{P_n(np + x\sqrt{npq})}{\frac{1}{\sqrt{2\pi npq}} e^{-x^2/2}} - 1 \right| \to 0,$$

where $\psi(n) = o(npq)^{1/6}$.

This completes the proof of the corollary. $\square$
