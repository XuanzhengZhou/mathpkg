---
role: proof
locale: en
of_concept: cramer-rao-inequality
source_book: gtm095
source_chapter: "1"
source_section: "7"
---

# Proof of the Cramér–Rao Inequality (Information Inequality)

Let $(\Omega, \mathcal{A}, P_\theta)$ be the Bernoulli probabilistic-statistical model, where $\Omega = \{\omega : \omega = (x_1, \ldots, x_n), \, x_i \in \{0,1\}\}$, $\theta \in \Theta = [0,1]$ is the unknown probability of success, and

$$p_\theta(\omega) = \theta^{\sum x_i} (1-\theta)^{\sum (1-x_i)}.$$

Let $T_n = T_n(\omega)$ be an unbiased estimator of $\theta$, i.e., $E_\theta[T_n] = \theta$ for all $\theta \in \Theta$.

**Step 1: Log-likelihood and its derivative.** Define the log-likelihood function
$$L_\theta(\omega) = \log p_\theta(\omega).$$

For the Bernoulli scheme,
$$L_\theta(\omega) = \left( \sum_{i=1}^{n} x_i \right) \log \theta + \left( \sum_{i=1}^{n} (1-x_i) \right) \log(1-\theta),$$
and its derivative with respect to $\theta$ is
$$\frac{\partial L_\theta(\omega)}{\partial \theta} = \frac{\sum_{i=1}^{n} (x_i - \theta)}{\theta(1-\theta)}.$$

**Step 2: Differentiating the identity $E_\theta[1] = 1$.** Since $\sum_{\omega} p_\theta(\omega) = 1$, differentiating under the sum yields
$$0 = \sum_{\omega} \frac{\partial p_\theta(\omega)}{\partial \theta} = \sum_{\omega} \frac{\partial p_\theta(\omega)}{\partial \theta} \cdot \frac{p_\theta(\omega)}{p_\theta(\omega)} = \sum_{\omega} \frac{\partial \log p_\theta(\omega)}{\partial \theta} \, p_\theta(\omega) = E_\theta\!\left[ \frac{\partial L_\theta(\omega)}{\partial \theta} \right].$$

**Step 3: Differentiating the unbiasedness condition.** Since $T_n$ is unbiased, $\theta = E_\theta[T_n] = \sum_{\omega} T_n(\omega) p_\theta(\omega)$. Differentiating,
$$1 = \sum_{\omega} T_n(\omega) \frac{\partial p_\theta(\omega)}{\partial \theta} = \sum_{\omega} T_n(\omega) \frac{\partial L_\theta(\omega)}{\partial \theta} p_\theta(\omega) = E_\theta\!\left[ T_n \frac{\partial L_\theta(\omega)}{\partial \theta} \right].$$

**Step 4: Combining the two identities.** Subtracting $\theta$ times the first identity from the second,
$$1 = E_\theta\!\left[ (T_n - \theta) \frac{\partial L_\theta(\omega)}{\partial \theta} \right].$$

**Step 5: Cauchy–Bunyakovskii (Cauchy–Schwarz) inequality.** Applying the Cauchy–Schwarz inequality $(E[UV])^2 \leq E[U^2] E[V^2]$ with $U = T_n - \theta$ and $V = \partial L_\theta / \partial \theta$,
$$1 \leq E_\theta[(T_n - \theta)^2] \cdot E_\theta\!\left[ \left( \frac{\partial L_\theta(\omega)}{\partial \theta} \right)^2 \right].$$

**Step 6: Fisher information.** Define the Fisher information
$$I_n(\theta) = E_\theta\!\left[ \left( \frac{\partial L_\theta(\omega)}{\partial \theta} \right)^2 \right].$$

Then the inequality becomes the **Cramér–Rao lower bound**:
$$E_\theta[(T_n - \theta)^2] \geq \frac{1}{I_n(\theta)}.$$

**Step 7: Computation for the Bernoulli scheme.** Using the expression for $\partial L_\theta / \partial \theta$,
$$I_n(\theta) = E_\theta\!\left[ \left( \frac{\sum (x_i - \theta)}{\theta(1-\theta)} \right)^2 \right] = \frac{E_\theta[(S_n - n\theta)^2]}{\theta^2(1-\theta)^2} = \frac{n\theta(1-\theta)}{\theta^2(1-\theta)^2} = \frac{n}{\theta(1-\theta)}.$$

Hence, for any unbiased estimator $T_n$ of $\theta$ in the Bernoulli scheme,
$$\operatorname{Var}_\theta(T_n) = E_\theta[(T_n - \theta)^2] \geq \frac{\theta(1-\theta)}{n}.$$

The estimator $T_n^* = S_n / n$ achieves this bound with equality, since $\operatorname{Var}_\theta(T_n^*) = \theta(1-\theta)/n$, confirming that $T_n^*$ is an efficient estimator.
