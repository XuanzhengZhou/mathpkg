---
role: proof
locale: en
of_concept: hadamard-three-lines-maximum-modulus
source_book: gtm011
source_chapter: "3"
source_section: "3.9"
---

Since $\log M(x)$ is convex, it is bounded by $\max\{\log M(a), \log M(b)\}$. That is, for $a \leq x \leq b$,

$$M(x) \leq \max\{M(a), M(b)\}.$$

Now note that $M(a) \leq \sup\{|f(w)| : w \in \partial G\}$ and $M(b) \leq \sup\{|f(w)| : w \in \partial G\}$. Therefore, for any $z = x + iy \in G$,

$$|f(z)| \leq M(x) \leq \max\{M(a), M(b)\} \leq \sup\{|f(w)| : w \in \partial G\}.$$

If equality held at some interior point $z_0$, then by the Maximum Modulus Principle $f$ would be constant, contradicting the hypothesis. Hence the inequality is strict for all $z \in G$.
