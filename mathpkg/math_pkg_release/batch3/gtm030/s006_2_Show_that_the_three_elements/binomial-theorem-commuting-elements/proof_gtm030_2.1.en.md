---
role: proof
locale: en
of_concept: binomial-theorem-commuting-elements
source_book: gtm030
source_chapter: "2"
source_section: "1"
---

If $a$ and $b$ commute ($ab = ba$), then the powers of $a$ commute with the powers of $b$. We prove the binomial theorem by induction on $n$.

**Base case $n = 1$:** The formula is evident:
$$(a + b)^1 = a^1 + b^1 = \binom{1}{0}a^1 + \binom{1}{1}b^1.$$

**Inductive step:** Assume the formula holds for $n = r$:
$$(a + b)^r = \sum_{k=0}^{r} \binom{r}{k} a^{k} b^{r-k},$$
with the convention $0! = 1$ so that $\binom{r}{0} = \binom{r}{r} = 1$.

Multiply both sides by $a + b$:
\begin{align*}
(a + b)^{r+1} &= (a + b)\sum_{k=0}^{r} \binom{r}{k} a^{k} b^{r-k} \\
&= \sum_{k=0}^{r} \binom{r}{k} a^{k+1} b^{r-k} + \sum_{k=0}^{r} \binom{r}{k} a^{k} b^{r-k+1}.
\end{align*}

Re-index the first sum with $j = k+1$ and the second sum with $j = k$:
$$(a + b)^{r+1} = \sum_{j=1}^{r+1} \binom{r}{j-1} a^{j} b^{r+1-j} + \sum_{j=0}^{r} \binom{r}{j} a^{j} b^{r+1-j}.$$

Collecting coefficients of $a^j b^{r+1-j}$ for $1 \leq j \leq r$, and using the binomial coefficient identity:
\begin{align*}
\binom{r}{j-1} + \binom{r}{j} &= \frac{r!}{(j-1)!(r-j+1)!} + \frac{r!}{j!(r-j)!} \\
&= \frac{r!(r-j+1) + r!j}{j!(r-j+1)!} \\
&= \frac{(r+1)!}{j!(r+1-j)!} = \binom{r+1}{j}.
\end{align*}

For $j = 0$ the coefficient is $\binom{r}{0} = 1 = \binom{r+1}{0}$, and for $j = r+1$ the coefficient is $\binom{r}{r} = 1 = \binom{r+1}{r+1}$. Thus:
$$(a + b)^{r+1} = \sum_{j=0}^{r+1} \binom{r+1}{j} a^{j} b^{r+1-j}.$$

Hence the formula holds for $n = r+1$, completing the induction.
