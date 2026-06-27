---
role: proof
locale: en
of_concept: a-star-a-positive-c-star
source_book: gtm015
source_chapter: "Chapter 7: C*-Algebras"
source_section: "58. Preliminaries"
---

# Proof of Elements of the Form a*a are Positive

Proof. Let $B = \{a^*a\}''$ (the bicommutant of $a^*a$ in $A$) and write $B = \%(T)$, $T$ compact (59.2). Since $a^*a$ is self-adjoint, it may be viewed as a real-valued continuous function on $T$; one may therefore write

$$a^*a = b - c,$$

with $b, c \in \{a^*a\}''$, $b \geq 0$, $c \geq 0$, and $bc = 0$. It will suffice to show that $c = 0$. Set $x = ac$; then

$$x^*x = c(a^*a)c = c(b - c)c = -c^3,$$

thus $-x^*x = c^3 \geq 0$ (by the functional representation);

{Proof: Writing $B = \{b\}^n$, the bicommutant of $b$ in $A$, we have $B = \mathcal{C}(T)$ for a suitable compact space $T$ (59.2); then $b$ is a real-valued function on $T$ with $-\|b\| \leq b(t) \leq \|b\|$ for all $t \in T$. Since $\|b\| 1 - b$ is a continuous function on $T$ with nonnegative values, we may define $c = (\|b\| 1 - b)^{1/2} \in \mathcal{C}(T) = B$; then

$$f(\|b\| 1 - b) = f(c^2) = f(c^*c) \geq 0,$$

thus $f(b) \leq \|b\| f(1)$. Similarly $f(b) \geq -\|b\| f(1)$. Combining (ii) and (iii), we have, for every $a$ in $A$,

$$|f(a)|^2 \leq f(aa^*)f(1) \leq \|a^*a\| f(1)^2 = \|a\|^2 f(1)^2,$$

thus $|f(a)| \leq \|a\| f(1)$. This shows that $f$ is continuous and $\|f\| \leq f(1)$. On the other hand, $\|f\| \geq f(1)$ results from $\|1\| = 1$.

(b) implies (a): Suppose $f$ is a continuous linear form on $A$ such that $f(1) = \|f\| > 0$. Replacing $f$ by $f(1)^{-1}f$, we can suppose that $\|f\| = f(1) = 1$.

Let $a \in A$; it is to be shown that $f(a^*a) \geq 0$. Writing $I$ for the closed interval $[0, \|a^*a\|]$, we know from (61.8) that $\sigma(a^*a) \subset I$
