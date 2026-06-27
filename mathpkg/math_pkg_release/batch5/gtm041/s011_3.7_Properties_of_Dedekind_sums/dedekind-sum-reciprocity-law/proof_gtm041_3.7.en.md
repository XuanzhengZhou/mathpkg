---
role: proof
locale: en
of_concept: dedekind-sum-reciprocity-law
source_book: gtm041
source_chapter: "3"
source_section: "3.7"
---
The proof uses the Bernoulli periodic function $((x))$ to express Dedekind sums. From the definition,

$$s(h,k) = \sum_{r=1}^{k-1} \left(\left(\frac{hr}{k}\right)\right) \left(\left(\frac{r}{k}\right)\right).$$

Expanding $((hr/k))^2$ and using the periodicity and oddness of $((x))$, we obtain after algebraic manipulation:

$$\sum_{r=1}^{k-1} \left(\left(\frac{hr}{k}\right)\right)^2 = 2h\,s(h,k) + \sum_{r=1}^{k-1} \left[\frac{hr}{k}\right]\left(\left[\frac{hr}{k}\right]+1\right) - \frac{h^2}{k^2}\sum_{r=1}^{k-1} r^2 + \frac{k-1}{4}.$$

On the other hand, using the identity $\sum_{r=1}^{k-1} ((hr/k))^2 = \sum_{r=1}^{k-1} ((r/k))^2$ (since the fractional parts $\{hr/k\}$ run through the same values as $\{r/k\}$ modulo $k$), and evaluating the right-hand side using elementary sums, we find

$$2h\,s(h,k) + \sum_{r=1}^{k-1} \left[\frac{hr}{k}\right]\left(\left[\frac{hr}{k}\right]+1\right) = \frac{h^2+1}{k^2}\sum_{r=1}^{k-1} r^2 - \frac{1}{k}\sum_{r=1}^{k-1} r.$$

The sum involving the floor function is handled by collecting terms with a fixed value $v = [hr/k]$. For each $v$, the number of $r$ with $[hr/k] = v$ is $N(v) = [k(v+1)/h] - [kv/h]$, giving

$$\sum_{r=1}^{k-1} \left[\frac{hr}{k}\right]\left(\left[\frac{hr}{k}\right]+1\right) = \sum_{v=1}^{h-1} v(v+1)N(v+1) - h(h-1).$$

After further manipulation using the summation identity

$$\sum_{v=1}^{h-1} v\left[\frac{kv}{h}\right] = \frac{1}{2}(h-1)(k-1) + h\,s(k,h),$$

and evaluating the elementary sums $\sum r = k(k-1)/2$ and $\sum r^2 = (k-1)k(2k-1)/6$, we multiply through by $6k$ and simplify to obtain

$$12hk\bigl(s(h,k) + s(k,h)\bigr) = h^2 + k^2 + 1 - 3hk,$$

which is the reciprocity law for Dedekind sums.
