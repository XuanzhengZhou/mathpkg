---
role: proof
locale: en
of_concept: metric-uniformity-equivalence-lemma
source_book: gtm011
source_chapter: "VII"
source_section: "1.7"
---

If $\epsilon > 0$ is fixed let $p$ be a positive integer such that $\sum_{n=p+1}^{\infty} \left(\frac{1}{2}\right)^n < \frac{1}{2}\epsilon$ and put $K = K_p$. Choose $\delta > 0$ such that $0 \leq t < \delta$ gives $\frac{t}{1+t} < \frac{1}{2}\epsilon$. Suppose $f$ and $g$ are functions in $C(G, \Omega)$ that satisfy $\sup \{d(f(z), g(z)): z \in K\} < \delta$. Since $K_n \subset K_p = K$ for $1 \leq n \leq p$ we have

$$\rho_n(f,g) = \sup_{z \in K_n} d(f(z), g(z)) \leq \sup_{z \in K} d(f(z), g(z)) < \delta$$

so that $\frac{\rho_n(f,g)}{1 + \rho_n(f,g)} < \frac{1}{2}\epsilon$ for $1 \leq n \leq p$. Hence

$$\rho(f,g) = \sum_{n=1}^{p} \left(\frac{1}{2}\right)^n \frac{\rho_n}{1+\rho_n} + \sum_{n=p+1}^{\infty} \left(\frac{1}{2}\right)^n \frac{\rho_n}{1+\rho_n}$$
$$< \frac{1}{2}\epsilon \sum_{n=1}^{p} \left(\frac{1}{2}\right)^n + \sum_{n=p+1}^{\infty} \left(\frac{1}{2}\right)^n < \frac{1}{2}\epsilon + \frac{1}{2}\epsilon = \epsilon.$$

Conversely, suppose $\delta > 0$ and a compact set $K \subset G$ are given. By part (b) of Proposition 1.2 there is an integer $p$ such that $K \subset K_p$. Choose $\epsilon > 0$ such that $\epsilon < \delta(1/2)^p / (1 + \delta)$. If $\rho(f,g) < \epsilon$ then for $z \in K \subset K_p$,

$$\frac{d(f(z), g(z))}{1 + d(f(z), g(z))} \leq \rho_p(f,g) \leq 2^p \rho(f,g) < 2^p \epsilon < \frac{\delta}{1+\delta}.$$

Since the function $t \mapsto t/(1+t)$ is increasing on $[0,\infty)$, this implies $d(f(z), g(z)) < \delta$ for all $z \in K$, giving $\sup \{d(f(z), g(z)) : z \in K\} < \delta$.
