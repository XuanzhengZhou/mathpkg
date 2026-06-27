---
role: proof
locale: en
of_concept: pullback-epi-abelian-category
source_book: gtm005
source_chapter: "VIII"
source_section: "4"
---

Let the pullback square be

\[
\begin{CD}
s @>f'>> d \\
@V{g'}VV @VV{g}V \\
b @>f>> c
\end{CD}
\]

with $f$ epi. Express the pullback $s$ via the standard construction: $s = \ker(f p_1 - g p_2 : b \oplus d \rightarrow c)$, with $g' = p_1 m$ and $f' = p_2 m$, where $m = \ker(f p_1 - g p_2)$.

Now suppose $u f' = 0$ for some $u$. Since $f' = p_2 m$, we have $u p_2 m = 0$, so $u p_2$ factors through $\operatorname{coker} m = f p_1 - g p_2$ as $u p_2 = u'(f p_1 - g p_2)$. But $p_2 i_1 = 0$ (where $i_1 : b \rightarrow b \oplus d$ is the first coproduct injection), so

$$0 = u p_2 i_1 = u'(f p_1 - g p_2) i_1 = u' f p_1 i_1 = u' f.$$

Since $f$ is epi, $u' = 0$; therefore $u = 0$, proving that $f'$ is epi.

For the kernel factorization: let $k = \ker f : a \rightarrow b$. The pair of arrows $k : a \rightarrow b$ and $0 : a \rightarrow d$ satisfy $f k = 0 = g 0$, so by the universal property of the pullback $s$, there exists a unique arrow $k' : a \rightarrow s$ with $g' k' = k$ and $f' k' = 0$. Since $k$ is monic, $k'$ is also monic.

To show $k' = \ker f'$: consider any arrow $v$ with $f' v = 0$. Then $f g' v = g f' v = 0$, so $g' v$ factors through $k = \ker f$ as $g' v = k v'$ for some $v'$. Thus $g' v = g'(k' v')$ and $f' v = 0 = f'(k' v')$. By the uniqueness in the definition of a pullback, $v = k' v'$. Therefore $k' = \ker f'$.

In particular, given a short exact sequence $a \xrightarrow{k} b \xrightarrow{f} c$, where $k = \ker f$ and $f = \operatorname{coker} k$, pulling back along any $g : d \rightarrow c$ yields $a \xrightarrow{k'} s \xrightarrow{f'} d$ with $k' = \ker f'$, which is again a short exact sequence.
