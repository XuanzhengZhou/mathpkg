---
role: proof
locale: en
of_concept: continuous-function-on-w-constant-on-tail
source_book: gtm043
source_chapter: "5"
source_section: "5.12"
---

Every tail $W - W(\sigma)$ is countably compact (in fact, it is homeomorphic with $W$ itself). Therefore each image set $f[W - W(\sigma)]$ is a countably compact subset of $\mathbb{R}$, and hence compact. The family $\{f[W - W(\sigma)] : \sigma \in W\}$ is nested, so the intersection

$$\bigcap_{\sigma \in W} f[W - W(\sigma)]$$

is nonempty. Choose any number $r$ belonging to this intersection; then the closed set $f^{\leftarrow}(r)$ is cofinal in $W$.

Now, for every $n \in \mathbb{N}$, the closed set

$$\{x \in W : |f(x) - r| \geq 1/n\}$$

is disjoint from $f^{\leftarrow}(r)$. Since $f^{\leftarrow}(r)$ is cofinal, and by 5.12(b) any two cofinal closed sets meet, this closed set cannot be cofinal; hence it has an upper bound $\alpha_n$ in $W$. Define $\alpha = \sup_n \alpha_n$ (a countable ordinal). For any $x \in W - W(\alpha)$, we have $|f(x) - r| < 1/n$ for all $n$, so $f(x) = r$. Thus $f[W - W(\alpha)] = \{r\}$.
