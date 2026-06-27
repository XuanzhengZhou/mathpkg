---
role: proof
locale: en
of_concept: theorem-14-b-adic-embedding
source_book: gtm027
source_chapter: "0"
source_section: "Algebraic Concepts"
---

# Proof of Theorem 14: $b$-Adic Expansion Representation of Real Numbers

**Theorem 14.** Let $E$ be the set of $b$-adic expansions, let $R$ be the set of rational expansions, and for $a$ in $R$ let $r(a)$ be the corresponding $b$-adic rational number. Then there is a unique function $\bar{r}$ on $E$ to the real numbers such that $\bar{r}$ is order-preserving and $\bar{r}(a) = r(a)$ for $a$ in $R$.

*Proof.* First, we prove that for non-negative real numbers $x$ and $y$, if $x < y$, then there is $a$ in $R$ such that $x < r(a) < y$. Because $b^p > p$ for each non-negative integer $p$ (a fact which is easily proved by induction), and because the set of non-negative integers is not bounded, there is an integer $p$ such that $b^p > 1/(y-x)$. Then $b^{-p} < (y-x)$. There is an integer $q$ such that $q b^{-p} \geq y$ because the ordering is Archimedean, and since there is a smallest such integer $q$, it may be supposed that $(q-1)b^{-p} < y$. It follows that $(q-1)b^{-p} > x$ because $b^{-p}$ is less than $(y-x)$, and this proves that there is a $b$-adic rational $(q-1)b^{-p}$, which is the image of a member of $R$, lying between $x$ and $y$. Consequently the correspondence $\bar{r}$ is unique.

Next, we show that the correspondence $\bar{r}$ is one-to-one on $E \setminus R$. Suppose that $a \in E$, $c \in E \setminus R$, and $a < c$. Then for the first value of $p$ such that $a_p$ and $c_p$ are different, $a_p < c_p$. The expansion $d$, such that for $q < p$, $d_q = a_q$, for $q > p$, $d_q = 0$, and $d_p = a_p + 1$, is a member of $R$ which is greater than $a$, and since $c$ does not have a last non-zero digit, $a < d < c$. Repeating, there is a member $e$ of $R$ such that $a < d < e < c$. Then, since on $R$ the function $\bar{r}$ is one-to-one, $\bar{r}(a) \leq \bar{r}(d) < \bar{r}(e) \leq \bar{r}(c)$, so that $\bar{r}(a) < \bar{r}(c)$.

Finally, we show that every non-void subset $F$ of $E$ which has an upper bound has a supremum. Let $p$ be the smallest integer such that $a_p \neq 0$ for some $a$ in $F$. Define $c_q$ to be zero for $q < p$, let $F_p$ be the set of all members $a$ of $F$ with non-zero $p$-th digit $a_p$, and let $c_p = \max\{a_p : a \in F_p\}$. Continue inductively, letting $F_{p+1}$ be the set of all members $a$ of $F_p$ such that $a_q = c_q$ for $q = p$, and let $c_{p+1} = \max\{a_{p+1} : a \in F_{p+1}\}$. No one of the sets $F_p$ can be void, and without difficulty one sees that the expansion $c$ obtained by this construction is an upper bound of $F$, in fact a supremum, and that $c \in E \setminus R$.
