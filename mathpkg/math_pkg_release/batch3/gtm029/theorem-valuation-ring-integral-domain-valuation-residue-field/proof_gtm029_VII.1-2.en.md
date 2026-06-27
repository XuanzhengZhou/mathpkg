---
role: proof
locale: en
of_concept: theorem-valuation-ring-integral-domain-valuation-residue-field
source_book: gtm029
source_chapter: "VII"
source_section: "1-2"
---

Since $\mathbf{o}(X_i)=1$, $i=1, 2, \cdots, n$, $\mathbf{o}(X_i/X_n)=0$, and the first assertion is proved. Let now $F(X_1, X_2, \cdots, X_{n-1})$ be any non-zero polynomial in $n-1$ indeterminates, with coefficients in $A$, and let $m$ be the degree of $F$. We set $g=g_m(X_1, X_2, \cdots, X_n)=X_n^mF(X_1/X_n, X_2/X_n, \cdots, X_{n-1}/X_n)$. Then $g$ is a form of degree $m$ in $X_1, X_2, \cdots, X_n$, with coefficients in $A$. We have $\mathbf{o}(g)=m=\mathbf{o}(X_n^m)$, hence the $\mathbf{o}$-residue of the quotient $g/X_n^m$ is different from zero. Since $g/X_n^m=F(X_1/X_n, X_2/X_n, \cdots, X_{n-1}/X_n)$ and since $\mathbf{o}$ is trivial on $A$, it follows that $F(t_1, t_2, \cdots, t_{n-1})\neq 0$, showing that $t_1, t_2, \cdots, t_{n-1}$ are algebraically independent over $A$.

The

integers, it follows that $f + g$ and $fg$ are near $f_0 + g_0$ and $f_0g_0$ respectively provided $f$ and $g$ are sufficiently near $f_0$ and $g_0$; in other words, the ring operations in $S$ are indeed continuous. Note that in view of the relation $\bigcap_{q=1}^{\infty} \mathfrak{X}^q = (0)$, $S$ is a Hausdorff space. As a matter of fact, the topology of $S$ can be induced by a suitable metric in $S$; namely, fix a real number $r > 1$ and define the distance $d(f, g)$ between any two elements $f, g$ of $S$ by the formula $d(f, g) = r^{-q}$, where $q = \mathbf{o}(f - g)$.

The space $S$ is complete, i.e., every Cauchy sequence $\{f^i\}$ of elements $f^i$ of $S$ converges in $S$. For let $f^i = \left(f_0^i, f_1^i, \cdots, f_q^i, \cdots\right)$. Since we are dealing with a Cauchy sequence, we must have $f_q^i = f_q^j$ for all $i, j \geq n(q)$, where $n(q)$ is an integer depending on $q$. We set $f_q = f_q^i$ for $i = n(q)$ and $f = \left(f_0, f_1, \cdots, f_q, \cdots\right)$. Then $\mathbf{o}(f - f^i) > q$ if $i \geq \max\{n(0), n(1), \cdots, n(q)\}$, showing that the sequence $\{f^i\}$ converges to $f$.

It follows in the usual way that if $\{f^i\}$ and $\{g^i\}$ are two Cauchy sequences, then

(5) $\lim (f^i + g^i) = \lim f^i + \lim g^i,$

(5') $\lim f^i g^i = \lim f^i \

$= \sum_{i,j=0}^{q} g^i h^j$, while the right-hand side is the limit of the sequence $\{\psi^q\}$, where $\psi^q = \sum_{i+j \leq q} g^i h^j$. Hence $\varphi^q - \psi^q$ is a sum of terms $g^i h^j$ in which at least one of the integers $i, j$ is $\geq |q/2|$. Since $o(g^i)$ and $o(h^i)$ tend to $+\infty$ with $i$, it follows that the two sequences $\{\varphi^q\}$ and $\{\psi^q\}$ have the same limit, and this proves $(6')$.

We note that $(6')$ implies the distributive law

$(6'') \quad h \sum_{i} g^i = \sum_{i} hg^i.$

We also note that if we have $h^i = 0$ for all sufficiently large values of $i$, say for $i > m$, so that the sequence $\{h^i\}$ is essentially a finite sequence, then the infinite sum $\sum_{i} h^i$ coincides with the sum of the elements $h^0, h^1, \cdots, h^m$ in the ring $S$.

We note that the inequality (3) generalizes to infinite sums, i.e., we have for any convergent series $\sum_{i} h^i$:

$(7) \quad o\left(\sum_{i} h^i\right) \geq \min_i o\left(h^i\right).$

The notion of infinite sums allows us to write every power series $f = \left(f_0, f_1, f_2, \cdots, f_q, \cdots\right)$, where $f_q$ is a form of degree $q$ (or is zero), as an infinite sum; namely, we have

$(8) \quad f = \sum_{i=0}^{\infty} f_i$, or $f = f_0 + f_1 + \cdots + f_q + \cdots.$

In this form, $f$ appears as an actual power series in $X_1, X_2, \cdots, X_n$. The

of $L$). Since $n > q$, the inequality $o(f - f_q) \geq n$ implies that $f_q$ is the initial form of $f$. Note that in this part of the proof we have not used the assumption that $L$ is a subring of $S$.

Conversely, assume that $L$ has the property stated in the lemma. Let $f$ be any element of $S$. We shall construct an infinite sequence $\{f^i\}$, $f^i \in L$, such that $o(f - f^i) \geq i$, whence $f = \text{Lim} f^i$. For $i = 0$ we simply set $f^0 = 0$. Let us assume that we have already defined the $n$ elements $f^0, f^1, \cdots, f^{n-1}$ in $L$ and that we have then $o(f - f^i) \geq i$ for $i = 0, 1, \cdots, n-1$. If $o(f - f^{n-1}) \geq n$ we set $f^n = f^{n-1}$. If $o(f - f^{n-1}) = n-1$, let $g_{n-1}$ be the initial form of $f - f^{n-1}$ and let $h^{n-1}$ be some element of $L$ whose initial form is $g_{n-1}$. If we set $f^n = f^{n-1} + h^{n-1}$, then $f^n \in L$, since $L$ is a subring of $S$, and we have $o(f - f^n) = o(f - f^{n-1} - h^{n-1}) \geq n$, since both $f - f^{n-1}$ and $h^{n-1}$ are of order $n-1$ and have the same initial form $g_{n-1}$. This completes the proof of the lemma.

We have seen in Vol. I, Ch. I that in any polynomial in $A[X_1, X_2, \cdots, X_n]$ one can substitute for the indeterminates elements of any overring of $A$ (

of $A[[Y_1, Y_2, \cdots, Y_m]]$ into $A[[X_1, X_2, \cdots, X_n]]$. We shall refer to (10) as the substitution mapping (relative to the substitution $Y_i \rightarrow f^i$). It follows easily from the rules (6) and (6') of addition and multiplication of infinite sums, that the substitution mapping (10) is a homomorphism. Furthermore, the mapping (10) is continuous (with respect to the topology introduced earlier in power series rings). To see this it is sufficient to show that if $\mathfrak{Y}$ denotes the ideal generated in $A[[Y_1, Y_2, \cdots, Y_m]]$ by $Y_1, Y_2, \cdots, Y_m$, then the transform of $\mathfrak{Y}^i$ by (10) is contained in $\mathfrak{X}^{\rho(i)}$, where $\rho(i)$ tends to $\infty$ with $i$. This, however, is obvious, since from the definition of the substitution mapping it follows that if $g \in \mathfrak{Y}^i$ then $g(f^1, f^2, \cdots, f^m)$ belongs to $\mathfrak{X}^i$.

The image of the ring $A[[Y_1, Y_2, \cdots, Y_m]]$ under the substitution mapping (10) is a subring of $A[[X_1, X_2, \cdots, X_n]]$. We shall denote this subring by $A[[f^1, f^2, \cdots, f^m]]$.

It is not difficult to see that any continuous homomorphism $\tau$ of $A[[Y_1, Y_2, \cdots, Y_m]]$ into $A[[X_1, X_2, \cdots, X_n]]$ is a substitution mapping. For let $\tau(Y_i) = f^i$. The continuity of $\tau$ requires that high powers of $f^i$ belong to high powers of the ideal $\mathfrak{X}$. Hence $f^i \in \mathfrak{X}$, $i = 1,

Hence $g(f^1, f^2, \cdots, f^n) \neq 0$, and thus $g$ is not in the kernel of $\varphi$. Observe that we have shown here the following: $g$ and $g(f^1, f^2, \cdots, f^n)$ have the same initial form.

We next show that $\varphi$ maps $A[[X_1, X_2, \cdots, X_n]]$ onto itself, i.e., that $A[[f^1, f^2, \cdots, f^n]] = A[[X_1, X_2, \cdots, X_n]]$. If $g_s(X_1, X_2, \cdots, X_n)$ is any form, with coefficients in $A$, then we have just seen that $g_s(X_1, X_2, \cdots, X_n)$ is the initial form of the element $g_s(f^1, f^2, \cdots, f^n)$ of the ring $A[[f^1, f^2, \cdots, f^n]]$. It follows therefore from Lemma 1 that the ring $A[[f^1, f^2, \cdots, f^n]]$ is everywhere dense in $A[[X_1, X_2, \cdots, X_n]]$, and in order to prove the lemma we have only to show that $A[[f^1, f^2, \cdots, f^n]]$ is a closed subset of $A[[X_1, X_2, \cdots, X_n]]$. Assume then that we have an element $h$, such that $h = \lim_{i \to \infty} g_i(f^1, f^2, \cdots, f^n)$, where $g_i(X_1, X_2, \cdots, X_n)$ is in $A[[X_1, X_2, \cdots, X_n]]$. The order of $g_i(f^1, f^2, \cdots, f^n)$ $- g_j(f^1, f^2, \cdots, f^n)$ is the same as the order of $g_i(X_1, X_2, \cdots,

has an initial form of degree $s$ (to see this it is sufficient to pass to the quotient field of $A$).

If $m=n$ and if the determinant of the coefficients of the linear forms $f_1^1, f_1^2, \cdots, f_1^n$ is a unit in $A$, then, for each integer $q$, the linear substitution $X_i \rightarrow f_1^i$ maps onto itself the set of forms of degree $q$ in $X_1, X_2, \cdots, X_n$, with coefficients in $A$. It follows that also in the present case the ring $A[[f^1, f^2, \cdots, f^n]]$ has the property of containing power series with arbitrarily preassigned initial forms, with coefficients in $A$, and the rest of the proof of the lemma is now applicable without any change.
