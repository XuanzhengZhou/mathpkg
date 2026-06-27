---
role: proof
locale: en
of_concept: dedekind-reciprocity-law
source_book: gtm041
source_chapter: "3"
source_section: "3.8"
---

The Dedekind sum can be expressed in terms of the sawtooth function:
$$s(h,k) = \sum_{r=1}^{k-1} \left(\left(\frac{r}{k}\right)\right) \left(\left(\frac{hr}{k}\right)\right).$$

Using the periodicity of $((x))$, one computes
$$\sum_{r=1}^{k} \left(\left(\frac{hr}{k}\right)\right)^2 = \sum_{r=1}^{k-1} \left(\frac{hr}{k} - \left[\frac{hr}{k}\right] - \frac{1}{2}\right)^2.$$

Expanding the square:
\begin{align*}
\sum_{r=1}^{k} \left(\left(\frac{hr}{k}\right)\right)^2 &= \sum_{r=1}^{k-1} \left( \frac{h^2 r^2}{k^2} + \left[\frac{hr}{k}\right]^2 + \frac{1}{4} - \frac{hr}{k} + \left[\frac{hr}{k}\right] - \frac{2hr}{k}\left[\frac{hr}{k}\right] \right) \\
&= 2h \sum_{r=1}^{k-1} \frac{r}{k}\left(\frac{hr}{k} - \left[\frac{hr}{k}\right] - \frac{1}{2}\right) \\
&\quad + \sum_{r=1}^{k-1} \left[\frac{hr}{k}\right]\left(\left[\frac{hr}{k}\right] + 1\right) - \frac{h^2}{k^2}\sum_{r=1}^{k-1} r^2 + \frac{1}{4}\sum_{r=1}^{k-1} 1.
\end{align*}

Recognizing the Dedekind sum in the first term and using the identity
$$\sum_{r=1}^{k-1} \left(\left(\frac{r}{k}\right)\right)^2 = \sum_{r=1}^{k-1} \left(\frac{r}{k} - \frac{1}{2}\right)^2 = \frac{(k-1)(k-2)}{12k},$$
one obtains after simplification:
$$2h\,s(h,k) + \sum_{r=1}^{k-1} \left[\frac{hr}{k}\right]\left(\left[\frac{hr}{k}\right] + 1\right) = \frac{h^2 + 1}{k^2}\sum_{r=1}^{k-1} r^2 - \frac{1}{k}\sum_{r=1}^{k-1} r.$$

Now, for a fixed integer $v$, the number of $r \in \{1,\dots,k-1\}$ with $[hr/k] = v$ is
$$N(v) = \left[\frac{k(v+1)}{h}\right] - \left[\frac{kv}{h}\right].$$

Summing by parts and using telescoping sums yields
$$\sum_{r=1}^{k-1} \left[\frac{hr}{k}\right]\left(\left[\frac{hr}{k}\right] + 1\right) = 2h\,s(k,h) - \frac{2k}{h}\sum_{v=1}^{h-1} v^2 + \sum_{v=1}^{h-1} v + h(h-1)(k-1).$$

Substituting this back and multiplying by $6k$ gives
$$12hk\bigl(s(h,k) + s(k,h)\bigr) = h^2 + k^2 + 1 - 3hk,$$
which is the reciprocity law. $\square$
