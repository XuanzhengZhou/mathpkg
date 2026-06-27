---
role: proof
locale: en
of_concept: plurisubharmonic-exhaustion-for-polynomially-convex
source_book: gtm035
source_chapter: "Chapter 22"
source_section: "22.4"
---
# Proof of Plurisubharmonic Exhaustion for Polynomially Convex Sets

**Lemma 22.4.** Let $K$ be polynomially convex in $\mathbb{C}^n$ with $K \subseteq U$, where $U$ is open and bounded. Then there exists a smooth strictly plurisubharmonic function $\rho : \mathbb{C}^n \to \mathbb{R}$ and $R > 0$ such that:

(i) $\rho < 0$ on $K$ and $\rho > 0$ on $\mathbb{C}^n \setminus U$;

(ii) $\rho(z) = |z|^2$ for $|z| > R$; and

(iii) $\rho$ is a Morse function on $\mathbb{C}^n$.

**Proof.** We first construct a smooth strictly plurisubharmonic function $v$ on $\mathbb{C}^n$ satisfying (i).

Choose $C > \max\{|z|^2 : z \in K\}$. Let $L = \{z \in \mathbb{C}^n : |z|^2 - C \leq 0\} \setminus U$. Then $L$ is compact and disjoint from $K$.

For each $x \in L$, since $K$ is polynomially convex, there exists a polynomial $p_x$ such that $|p_x(x)| > 1$ and $|p_x| \leq 1$ on $K$. By continuity, $|p_x| > 1$ on some neighborhood of $x$. By compactness of $L$, finitely many such neighborhoods cover $L$; let the corresponding polynomials be $p_1, \ldots, p_s$.

Define

$$v(z) = \max\{|z|^2 - C, \; \varepsilon(|p_1(z)|^2 - 1), \ldots, \varepsilon(|p_s(z)|^2 - 1)\}$$

for a sufficiently small $\varepsilon > 0$. The function $|z|^2 - C$ is strictly plurisubharmonic, and each $|p_j(z)|^2$ is plurisubharmonic. For $\varepsilon$ small enough, the maximum of finitely many strictly plurisubharmonic functions can be approximated by a smooth strictly plurisubharmonic function (by a standard regularization argument using convolution with a smooth mollifier and the fact that the plurisubharmonic functions form a convex cone closed under taking maxima).

Thus we obtain a smooth strictly plurisubharmonic function $v$ such that $v < 0$ on $K$ and $v > 0$ on $\mathbb{C}^n \setminus U$.

Now choose $R > 0$ large enough so that $U \subset B(0, R)$. Define

$$\rho(z) = \chi(|z|^2/R^2) \cdot v(z) + (1 - \chi(|z|^2/R^2)) \cdot |z|^2,$$

where $\chi : \mathbb{R} \to [0,1]$ is a smooth cutoff function with $\chi(t) = 1$ for $t \leq 1/2$ and $\chi(t) = 0$ for $t \geq 1$. Then $\rho$ is smooth on $\mathbb{C}^n$, strictly plurisubharmonic (as a convex combination of two strictly plurisubharmonic functions is strictly plurisubharmonic), and satisfies (i) and (ii).

Finally, by the Morse Lemma (Section 22.1), we can make a small smooth perturbation of $\rho$ on the ball $B(0, R)$ so that it becomes a Morse function while preserving properties (i) and (ii). This perturbation can be chosen small enough that strict plurisubharmonicity and the sign conditions are maintained. Thus (iii) is also satisfied.
