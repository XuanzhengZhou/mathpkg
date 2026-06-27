---
role: proof
locale: en
of_concept: gcd-linear-combination-euclidean
source_book: gtm028
source_chapter: "I"
source_section: "14"
---

Let $I$ denote the set of all elements of $E$ which are linear combinations $Aa + Bb$ of $a$ and $b$, with $A, B \in E$. $I$ is non-empty (it contains $a = 1\cdot a + 0\cdot b$). Among the non-zero elements of $I$, select an element $d$ for which $\varphi(d)$ is minimum. Write $d = \alpha a + \beta b$ with $\alpha, \beta \in E$.

We claim $d$ divides $a$. Apply E2 to $a$ and $d$: there exist $q, r \in E$ such that $a = dq + r$ with $\varphi(r) < \varphi(d)$. Then

$$r = a - dq = a - (\alpha a + \beta b)q = (1 - \alpha q)a + (-\beta q)b,$$

so $r \in I$. If $r \neq 0$, then $\varphi(r) < \varphi(d)$, contradicting the minimality of $\varphi(d)$ among non-zero elements of $I$. Hence $r = 0$, so $d \mid a$. Similarly, $d \mid b$.

If $c$ is any common divisor of $a$ and $b$, then $c \mid (\alpha a + \beta b) = d$, so $d$ is a greatest common divisor of $a$ and $b$.
