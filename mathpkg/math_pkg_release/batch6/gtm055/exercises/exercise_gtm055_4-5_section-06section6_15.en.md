---
role: exercise
locale: en
chapter: "4-5"
section: "Section 06_Section_6"
exercise_number: 15
---

O. Let $X$ be a nonempty set and let $(Y, \rho)$ be a metric space.

(i) A net $\{f_{\lambda}\}_{\lambda \in \Lambda}$ of mappings of $X$ into $Y$ is said to be uniformly convergent to a limit $f$ (where $f$ is another mapping of $X$ into $Y$) if for every positive number $\varepsilon$ there exists an index $\lambda_0$ such that $\sigma(f(x), f_{\lambda}(x)) < \varepsilon$ for all $\lambda \geq \lambda_0$ and all $x$ in $X$. Show that if $X$ is a topological space and each $f_{\lambda}$ is continuous on $X$, then the uniform limit $f$ is also continuous on $X$.

(ii) Let $\mathcal{B}(X, Y)$ denote the set of all bounded mappings from the set $X$ into the metric space $Y$. If $f$ and $g$ belong to $\mathcal{B}(X, Y)$, we define

$$\sigma(f, g) = \sup_{x \in X} \rho(f(x), g(x)).$$

Show that $\sigma$ is a metric on $\mathcal{B}(X, Y)$ and that a net $\{f_{\lambda}\}$ in $\mathcal{B}(X, Y)$ converges uniformly to a limit $f$ if and only if it converges to $f$ with respect to the metric $\sigma$. (For this reason $\sigma$ is called the metric of uniform convergence, and the topology induced by $\sigma$ the topology of uniform convergence, on $\mathcal{B}(X, Y)$.) Show also that $\mathcal{B}(X, Y)$ is complete in the metric of uniform convergence if and only if $Y$ is complete in its metric $\rho$.

(iii) When $X$ is a topological space, we denote by $\mathcal{C}_b(X, Y)$ the set of all continuous mappings in $\mathcal{B}(X, Y)$. (Note that $\mathcal{C}_b(X, Y)$ coincides with the
...
