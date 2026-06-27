---
role: proof
locale: en
of_concept: proposition-2-4
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. This proposition will be proved by showing that the set

$$T = \{t \in [0, 1]: [f_t]_{\gamma(t)} = [g_t]_{\gamma(t)}\}$$

is both open and closed in $[0, 1]$; since $T$ is non-empty ($0 \in T$) it will follow that $T = [0, 1]$ so that, in particular, $1 \in T$.

The easiest part of the proof is to show that $T$ is open. So fix $t$ in $T$ and assume $t \neq 0$ or 1. (If $t = 1$ the proof is complete; if $t = 0$ then the argument about to be given will also show that $[a, a + \delta) \subset T$ for some $\delta > 0$.) By the definition of analytic continuation there is a $\delta > 0$ such that for $|s - t| < \delta$, $\gamma(s) \in D_t \cap B_t$ and

$$\begin{cases} [f_s]_{\gamma(s)} = [f_t]_{\gamma(s)}. \\ [g_s]_{\gamma(s)} = [g_t]_{\gamma(s)}. \end{cases}$$

Let $H$ be a connected subset of $D_t \cap B_t$ which contains $\gamma(s)$ and $\gamma(t)$. But since

A collection of germs $\mathcal{F}$ is called a complete analytic function if there is a function element $(f, G)$ such that $\mathcal{F}$ is the complete analytic function obtained from $(f, G)$.

Notice that the point $a$ in the definition is immaterial; any point in $G$ can be chosen since $G$ is an open connected subset of $\mathbb{C}$ (see II. 2.3). Also, if $\mathcal{F}$ is the complete analytic function associated with $(f, G)$ then $[f]_z \in \mathcal{F}$ for all $z$ in $G$.

Although there is no ambiguity in the definition of a complete analytic function there is an incompleteness about it. Is it a function? We should refrain from calling an object a function unless it is indeed a function. To make $\mathcal{F}$ a function one must manufacture a domain (the range will be $\mathbb{C}$) and show that $\mathcal{F}$ gives a "rule". This is easy. In a sense we let $\mathcal{F}$ be its own domain; more precisely, let

$$\mathcal{R} = \{(z, [f]_z): [f]_z \in \mathcal{F}\}.$$

Define $\mathcal{F} : \mathcal{R} \to \mathbb{C}$ by $\mathcal{F}(z, [f]_z) = f(z)$. In this way $\mathcal{F}$ becomes an "honest" function. Nevertheless there is still a lingering dissatisfaction. To have a satisfying solution a structure will be imposed on $\mathcal{R}$ which will make it possible to discuss the concept of analyticity for functions defined on $\mathcal{R}$. In this setting, the function $\mathcal{F}$ defined above becomes analytic; moreover, it reflects the behavior of each function element belonging to a germ that is in $\mathcal{F}$. The introduction of this structure is postponed until Section 5.

Exercises

1. The collection $\{D_0, D_1, \ldots, D_n\}$ of open disks is called a chain of disks if $D_{j-1} \cap D_j \neq \emptyset$ for $1 \leq j \leq n$. If $\

(b) Find an analytic continuation $\{(g_t, B_t): 0 \leq t \leq 1\}$ of $(f_0, D_0)$ along $\sigma$ and show that $[g_1]_1 = [g_0]_1$.

3. Let $f$ be an entire function, $D_0 = B(0; 1)$, and let $\gamma$ be a path from 0 to $b$. Show that if $\{(f_t, D_t): 0 \leq t \leq 1\}$ is a continuation of $(f, D_0)$ along $\gamma$ then $f_1(z) = f(z)$ for all $z$ in $D_1$. (This exercise is rather easy; it is actually an exercise in the use of the terminology.)

4. Let $\gamma: [0, 1] \to \mathbb{C}$ be a path and let $\{(f_t, D_t): 0 \leq t \leq 1\}$ be an analytic continuation along $\gamma$. Show that $\{(f'_t, D_t): 0 \leq t \leq 1\}$ is also a continuation along $\gamma$.

5. Suppose $\gamma: [0, 1] \to \mathbb{C}$ is a closed path with $\gamma(0) = \gamma(1) = a$ and let $\{(f_t, D_t): 0 \leq t \leq 1\}$ be an analytic continuation along $\gamma$ such that $[f_1]_a = [f_0]_a$ and $f_0 \neq 0$. What can be said about $(f_0, D_0)$?

6. Let $D_0 = B(1; 1)$ and let $f_0$ be the restriction to $D_0$ of the principal branch of the logarithm. For an integer $n$ let $\gamma(t) = \exp(2\pi int)$, $0 \leq t \leq 1$. Find a continuation $\{(f_t, D_t): 0 \leq t \leq 1\}$ along $\gamma$ of $(f_0, D_0)$ and show that $[f_1]_1 = [

sion at $z = a$. The first step in proving the Monodromy Theorem is to investigate the behavior of the radius of convergence for an analytic continuation along a curve.
