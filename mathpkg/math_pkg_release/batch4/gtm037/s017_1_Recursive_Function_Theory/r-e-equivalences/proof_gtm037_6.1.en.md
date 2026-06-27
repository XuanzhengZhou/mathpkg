---
role: proof
locale: en
of_concept: r-e-equivalences
source_book: gtm037
source_chapter: "6"
source_section: "1"
---

Obviously $(i) \Rightarrow (ii) \Rightarrow (iii)$. To show that $(iii) \Rightarrow (iv)$ we just need to show that $\emptyset$ (the empty set) is the range of some partial recursive function; and obviously the only possibility for such a function is $\emptyset$ (which is also the empty function). $\emptyset$ is partial recursive by the argument following 5.3.

$(iv) \Rightarrow (v)$. Let $A = \text{Rng } \varphi_e^1$. For any $x \in \omega$ let

$$fx \simeq \mu y((e, (y)_0, (y)_1) \in T_1 \text{ and } V(y)_1 = x).$$

Clearly then $\text{Dmn } f = \text{Rng } \varphi_e^1 = A$, and $f$ is partial recursive.

$(v) \Rightarrow (vi)$. Suppose $A = \text{Dmn } \varphi_e^1$. Then for all $x \in \omega$, $x \in A$ iff $\exists y((e, x, y) \in T_1)$, so $A \in \Sigma_1$.

$(vi) \Rightarrow (i)$. Suppose $A \in \Sigma_1$. By 5.23 choose $e \in \omega$ such that $A = \{x : \exists y((e, x, y) \in T_1)\}$. We may assume that $A \neq \emptyset$; say $a \in A$. Now for any $x \in \omega$ let

$$fx = (x)_0 \quad \text{if } (e, (x)_0, (x)_1) \in T_1,$$

$$fx = a \quad \text{otherwise.}$$

Clearly $f$ is an elementary function and $\text{Rng } f = A$, as desired.

---

An intuitive proof of the equivalence of 6.2$(iii)$ and 6.2$(v)$ is instructive. First assume that $A$ is recursively enumerable, $A \neq \emptyset$. Say $A = \text{Rng } f$, $f$ recursive. We define a function $g$...
