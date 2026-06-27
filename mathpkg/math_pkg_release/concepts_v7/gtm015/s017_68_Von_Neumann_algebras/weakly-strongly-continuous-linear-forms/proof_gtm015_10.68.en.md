---
role: proof
locale: en
of_concept: weakly-strongly-continuous-linear-forms
source_book: gtm015
source_chapter: "10"
source_section: "68"
---

# Proof of Equivalence of weakly and strongly continuous linear forms on L(H)

Proof. In statements (a) and (b), it is assumed that $M$ bears the relative weak and relative strong operator topologies, respectively.

(a) implies (b): This is immediate from $\tau_s \supset \tau_w$.

(b) implies (c): By the Hahn-Banach theorem (34.8) we can suppose without loss of generality that $M = \mathcal{L}(H)$. Since, by hypothesis, the set

$$\{T \in \mathcal{L}(H) : |f(T)| \leq 1\}$$

is a strong neighborhood of 0, there exist vectors $x_1, \ldots, x_n$ in $H$ such that

$$\{T : \|Tx_i\| \leq 1 \text{ for } i = 1, \ldots, n\} \subset \{T : |f(T)| \leq 1\}$$

(cf. (68.5)). Note that if $Tx_i = \theta$ for all $i$ then $f(T) = 0$. {Proof: For each $\varepsilon > 0$ we have $(\varepsilon T)x_i = \varepsilon(Tx_i) = \theta$ for all $i$, therefore $|f(\varepsilon T)| \leq 1$ by (*); thus $|f(T)| \leq \varepsilon^{-1}$ for all $\varepsilon > 0$, whence $f(T) = 0$.} Better yet,

$$|f(T)| \leq \sum_{i=1}^n \|Tx_i\|$$

for all $T \in \mathcal{L}(H)$. Consider the linear subspace $N = \{(Tx_1, \ldots, Tx_n) : T \in \mathcal{L}(H)\}$ of $H^n$; define $\tilde{f}$ on $N$ by $\tilde{f}(Tx_1, \ldots, Tx_n) = f(T)$. The above inequality shows $\tilde{f}$ is well-defined and continuous. Extend $\tilde{f}$ to a continuous linear form on $H^n$ (Hahn-Banach); by the Riesz representation theorem for Hilbert space direct sums, there exist $y_1, \ldots, y_n \in H$ such that

$$\tilde{f}(z_1, \ldots, z_n) = \sum_{i=1}^n (z_i | y_i)$$

for all $z = (z_1, \ldots, z_n)$ in $N$. In particular, for all $T \in \mathcal{L}(H)$ we have

$$f(T) = \tilde{f}(Tx_1, \ldots, Tx_n) = \sum_{i=1}^{n} (Tx_i | y_i),$$

thus $f = \omega_{x_1, y_1} + \cdots + \omega_{x_n, y_n}$ as desired.

(c) implies (a): This is immediate from the fact that the weak topology is defined as the coarsest topology on $\mathcal{L}(H)$ for which all of the linear forms $\omega_{x,y}$ are continuous.
