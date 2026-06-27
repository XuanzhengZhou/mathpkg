---
role: proof
locale: en
of_concept: hecke-operator-composition-formula
source_book: gtm041
source_chapter: "6"
source_section: "6.10"
---

Commutativity follows from (28) since the right member is symmetric in $m$ and $n$. If $(m, n) = 1$ formula (28) reduces to (26). Therefore, to prove (28) it suffices to treat the case when $m$ and $n$ are powers of the same prime $p$. First we consider the case $m = p$ and $n = p^r$, where $r \geq 1$. In this case we are to prove that

$$T(p)T(p^r) = T(p^{r+1}) + p^{k-1}T(p^{r-1}).$$

We use the representation in (17) and note that the divisors of $p^r$ have the form $p^t$ where $0 \leq t \leq r$. Hence we have

$$\{T(p^r)f\}(\tau) = p^{-r} \sum_{\substack{0 \leq t \leq r \\ 0 \leq b_t < p^t}} p^{(r-t)k} f\!\left(\frac{p^{r-t}\tau + b_t}{p^t}\right).$$

By (14) we have

$$\{T(p)g\}(\tau) = p^{k-1}g(p\tau) + p^{-1} \sum_{b=0}^{p-1} g\!\left(\frac{\tau + b}{p}\right).$$

Dividing each $b_t$ by $p^{t-1}$ we can write

$$b_t = q_t p^{t-1} + r_t,$$

where $0 \leq r_t < p^{t-1}$ and $q_t$ runs through a complete residue system mod $p$. Since $f$ is periodic with period 1 we have

$$f\!\left(\frac{p^{r-t}\tau + b_t}{p^{t-1}}\right) = f\!\left(\frac{p^{r-t}\tau + r_t}{p^{t-1}}\right),$$

so as $q_t$ runs through a complete residue system mod $p$ each term is repeated $p$ times. Replacing the index $t$ by $t-1$ we see that the last sum is $p^{k-1}$ times the sum defining $\{T(p^{r-1})f\}(\tau)$. This proves (29).

Now we consider general powers of the same prime, say $m = p^s$ and $n = p^r$. Without loss of generality we can assume that $r \leq s$. We will use induction on $r$ to prove that

$$T(p^r)T(p^s) = \sum_{t=0}^{r} p^{t(k-1)}T(p^{r+s-2t}) = \sum_{d \mid (p^r, p^s)} d^{k-1}T\!\left(\frac{p^{r+s}}{d^2}\right)$$

for all $r$ and all $s \geq r$. When $r=1$, (31) follows for all $s \geq 1$ from (29). Therefore we assume that (31) holds for $r$ and all smaller powers and all $s \geq r$, and prove it also holds for $r+1$ and all $s \geq r+1$.

By (29) we have

$$T(p)T(p^r)T(p^s) = T(p^{r+1})T(p^s) + p^{k-1}T(p^{r-1})T(p^s),$$

and by the induction hypothesis we have

$$T(p)T(p^r)T(p^s) = T(p)\sum_{t=0}^{r} p^{t(k-1)}T(p^{r+s-2t}).$$

Equating these two expressions and simplifying using (29) again yields the formula for $r+1$, completing the induction.
