---
role: proof
locale: en
of_concept: montels-theorem
source_book: gtm011
source_chapter: "VII"
source_section: "2"
---

**($\Leftarrow$)** Suppose $\mathcal{F}$ is locally bounded. Then $\mathcal{F}$ is uniformly bounded on each compact subset of $G$ (Lemma 2.8). By Cauchy's estimate, for any closed disk $\overline{B}(a; r) \subset G$ with $\overline{B}(a; 2r) \subset G$, there exists $M$ such that $|f(z)| \leq M$ for all $f \in \mathcal{F}$ and $z \in \overline{B}(a; 2r)$. Cauchy's estimate gives

$$|f'(z)| \leq \frac{M}{r}$$

for all $f \in \mathcal{F}$ and $z \in \overline{B}(a; r)$. Thus $\mathcal{F}$ is equicontinuous on $\overline{B}(a; r)$. By the Arzela-Ascoli Theorem, $\mathcal{F}$ is a normal family in $C(G, \mathbb{C})$. By Theorem 2.1, any limit of a convergent subsequence is analytic, so $\mathcal{F}$ is normal in $H(G)$.

**($\Rightarrow$)** Suppose $\mathcal{F}$ is normal but not locally bounded. Then there exists a compact set $K \subset G$ such that $\sup\{|f(z)| : z \in K, f \in \mathcal{F}\} = \infty$. Hence there is a sequence $\{f_n\} \subset \mathcal{F}$ with $\sup_{z \in K} |f_n(z)| \geq n$. By normality, some subsequence $\{f_{n_k}\}$ converges uniformly on compact sets to a function $f \in H(G)$. But then $\sup_{z \in K} |f_{n_k}(z) - f(z)| \to 0$, which contradicts $\sup_{z \in K} |f_{n_k}(z)| \geq n_k \to \infty$ unless $K$ is empty (impossible). Thus $\mathcal{F}$ must be locally bounded.
