---
role: proof
locale: en
of_concept: "let-be-a-real-normed-linear-space-and"
source_book: gtm025
source_chapter: "Abstract Banach Spaces"
source_section: "14.11"
---

For each $\varepsilon > 0$, define $A_{\varepsilon} = \{x \in A : \|x\| < \varepsilon\}$ and $B_{\varepsilon} = \{y \in B : \|y\| < \varepsilon\}$. Let $\varepsilon > 0$ be

Since $0 \in V_n - V_n$ and $V_n - V_n = \cup \{V_n - x : x \in V_n\}$ is open in $B$, there exists a $\delta_n > 0$ such that

$$B_{\delta_1} \subset V_n - V_n \subset [T(A_{\varepsilon_n})]^{-}. \tag{1}$$

We may suppose that $\delta_n < \frac{1}{n}$ for every $n \in N$. We will now show that $B_{\delta_1} \subset T(A_{\varepsilon})$.

To this end, let $y$ be any element of $B_{\delta_1}$. We must find an $x \in A_{\varepsilon}$ such that $T(x) = y$. By (1), there exists $x_1 \in A_{\varepsilon_1}$ such that $\|y - T(x_1)\| < \delta_2$, so that $y - T(x_1) \in B_{\delta_2}$. In view of (1) there exists $x_2 \in A_{\varepsilon_2}$ such that $\|y - T(x_1) - T(x_2)\| < \delta_3$. Continuing by finite induction, we find a sequence $(x_n)_{n=1}^{\infty}$ such that for each $n \in N$, $x_n$ is in $A_{\varepsilon_n}$ and

$$\left\|y - \sum_{k=1}^{n} T(x_k)\right\| < \delta_{n+1}. \tag{2}$$

Let $z_n = x_1 + x_2 + \cdots + x_n$. For $m < n$, we have

$$\|z_n - z_m\| \leq \sum_{k=m+1}^{n} \|x_k\| < \sum_{k=m+1}^{\infty} \frac{\varepsilon}{2^k} = \frac{\varepsilon}{2^m},$$

which has limit 0 as $m \to \infty$. Thus $(z_n)$ is a Cauchy sequence in $A$; since $A$ is complete, there is an $x \in A$ such that $\|x - z_n\| \

Proof. Consider the identity mapping on $E$ as a linear transformation from the Banach space $(E, \| \|)$ onto the Banach space $(E, \| \|')$. We leave the details as an exercise.
