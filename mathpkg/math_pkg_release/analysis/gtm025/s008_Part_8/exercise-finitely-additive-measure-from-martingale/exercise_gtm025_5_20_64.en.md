---
role: exercise
locale: en
chapter: "5"
section: "20"
exercise_number: 64
---

Let $X = [0, 1[$. For each $n \in N$, let $\mathcal{M}_n$ be the sigma-algebra of sets periodic with period $2^{-n}$ on $X$. Note that $\mathcal{M}_1 \supset \mathcal{M}_2 \supset \cdots$. Let $\mu$ be Lebesgue measure restricted to $\mathcal{M}_1$ and let $(f_n)$ be a sequence of $\mathcal{M}_n$-measurable functions such that

(ii) $\int_A f_n d\mu = \int_A f_{n+1} d\mu$ for all $A \in \mathcal{M}_n$ and all $n \in N$;

(iii) $\int_X f_n d\mu = 1$ for all $n \in N$.

(a) Prove that there is a finitely additive measure $\eta$ on $\bigcup_{n=1}^{\infty} \mathcal{M}_n$ such that

(iv) $\eta(A) = \int_A f_n d\mu$ for all $A \in \mathcal{M}_n$ and all $n \in N$.

(b) Prove by giving an example that $\eta$ need not be countably additive.

(c) Prove that $\lim_{n \to \infty} f_n$ exists and is finite $\mu$-almost everywhere on $X$.

[Hints. Consider the set $\Omega$ of all finitely additive measures $\omega$ on $\bigcup_{n=1}^{\infty} \mathcal{M}_n$ that assume only the values 0 and 1 and vanish for $\mu$-null sets. Make $\Omega$ into a topological space by neighborhoods $\Delta_A = \{\omega \in \Omega : \omega(A) = 1\}$, for $A \in \bigcup_{n=1}^{\infty} \mathcal{M}_n$. Then $\Omega$ is a compact Hausdorff space. Transfer $\mu$ and $\eta$ to $\Omega$, apply (20.56), and go back to $X$.]
