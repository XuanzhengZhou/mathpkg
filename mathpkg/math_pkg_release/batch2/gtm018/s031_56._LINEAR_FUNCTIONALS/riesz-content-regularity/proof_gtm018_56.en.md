---
role: proof
locale: en
of_concept: riesz-content-regularity
source_book: gtm018
source_chapter: "56"
source_section: "56. LINEAR FUNCTIONALS"
---

The fact that $\Lambda$ is positive implies that $\lambda(C) \geq 0$ for every $C$ in $\mathbf{C}$. To prove that $\lambda$ is finite, let $C$ be any compact set and let $U$ be any bounded open set containing $C$. Since there exists a function $f$ in $\mathcal{L}_+$ such that $f(x) = 1$ for $x$ in $C$ and $f(x) = 0$ for $x$ in $X - U$, it follows that $C \subset f \in \mathcal{L}_+$ and therefore

$$\lambda(C) \leq \Lambda(f) < \infty.$$

If $C$ and $D$ are compact sets, $C \supset D$, and if $C \subset f \in \mathcal{L}_+$, then $D \subset f$, and, therefore, $\lambda(D) \leq \Lambda(f)$. It follows that $\lambda(D) \leq \inf \Lambda(f) = \lambda(C)$, i.e., $\lambda$ is monotone.

If $C$ and $D$ are compact sets, and if $C \subset f \in \mathcal{L}_+$ and $D \subset g \in \mathcal{L}_+$, then

$$C \cup D \subset f + g \in \mathcal{L}_+,$$

and therefore $\lambda(C \cup D) \leq \Lambda(f + g) = \Lambda(f) + \Lambda(g)$. It follows that

$$\lambda(C \cup D) \leq \inf \Lambda(f) + \inf \Lambda(g) = \lambda(C) + \lambda(D),$$

i.e., $\lambda$ is subadditive.

If $C$ and $D$ are disjoint compact sets, then there exist disjoint bounded open sets $U$ and $V$ such that $C \subset U$ and $D \subset V$. Let $f$ and $g$ be functions in $\mathcal{L}_+$ such that $f(x) = 1$ for $x$ in $C$, $f(x) = 0$ for $x$ in $X - U$, $g(x) = 1$ for $x$ in $D$, $g(x) = 0$ for $x$ in $X - V$. Then for any $h \in \mathcal{L}_+$ with $C \cup D \subset h$, we have

$$\Lambda(f) + \Lambda(g) = \Lambda(f+g) \leq \Lambda(h),$$

since $f+g \leq h$ on $C \cup D$ and positivity implies $\Lambda(f+g) \leq \Lambda(h)$. Taking infimum over such $h$ yields $\lambda(C) + \lambda(D) \leq \lambda(C \cup D)$. Combined with subadditivity, $\lambda(C \cup D) = \lambda(C) + \lambda(D)$, so $\lambda$ is additive on disjoint compact sets.

To prove regularity of $\lambda$: Given $C \in \mathbf{C}$ and $\epsilon > 0$, choose $f \in \mathcal{L}_+$ with $C \subset f$ such that $\Lambda(f) \leq \lambda(C) + \epsilon/2$. If $\gamma$ is a real number, $0 < \gamma < 1$, and if $D = \{x : f(x) \geq \gamma\}$, then

$$C \subset \{x : f(x) \geq 1\} \subset \{x : f(x) > \gamma\} \subset D^0 \subset D \in \mathbf{C}.$$

Since $D \subset \frac{1}{\gamma} f \in \mathcal{L}_+$, it follows that

$$\lambda(D) \leq \frac{1}{\gamma} \Lambda(f) \leq \frac{1}{\gamma} \left( \lambda(C) + \frac{\epsilon}{2} \right).$$

Since $\gamma$ may be chosen so that

$$\frac{1}{\gamma} \left( \lambda(C) + \frac{\epsilon}{2} \right) \leq \lambda(C) + \epsilon,$$

it follows that $\lambda(D) \leq \lambda(C) + \epsilon$. The arbitrariness of $\epsilon$ implies that $\lambda$ is regular.

The last assertion of the theorem is an easy consequence of the regularity of $\mu$. Indeed, if $C$ is a compact set contained in a bounded open set $U$, then $C \subset f$ for any $f \in \mathcal{L}_+$ with $f = 1$ on $C$ and $f = 0$ outside $U$, and therefore

$$\mu(C) = \lambda(C) \leq \Lambda(f);$$

it follows that $\mu(U) = \sup \mu(C) \leq \Lambda(f)$.
