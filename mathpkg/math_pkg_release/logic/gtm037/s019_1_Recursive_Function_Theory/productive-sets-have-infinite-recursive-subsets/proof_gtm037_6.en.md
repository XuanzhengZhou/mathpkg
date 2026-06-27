---
role: proof
locale: en
of_concept: productive-sets-have-infinite-recursive-subsets
source_book: gtm037
source_chapter: "6"
source_section: "Recursive Function Theory"
---

By Theorem 6.8 it suffices to show that $A$ has an infinite r.e. subset. Let $f$ be a productive function for $A$. For any $x, y$, let

$$k(y, x) \simeq \mu i\,(i \leq \mathrm{lh}(x) 	ext{ and } y = (x)_i \div 1).$$

Clearly $k$ is partial recursive; say $k = arphi_e^2$. Now for any $x \in \omega$,

$$\mathrm{Dmn}\,arphi^1(s_1^1(e, x)) = \{(x)_i \div 1 : i \leq \mathrm{lh}(x)\}.$$

In fact, for any $y \in \omega$,

$$y \in \mathrm{Dmn}\,arphi^1(s_1^1(e, x)) \quad 	ext{iff} \quad (y, x) \in \mathrm{Dmn}\,arphi_e^2 \quad 	ext{iff} \quad (y, x) \in \mathrm{Dmn}\,k$$

$$	ext{iff} \quad \exists i \leq \mathrm{lh}(x)\,(y = (x)_i \div 1).$$

Now we construct an infinite r.e. subset of $A$ by iteration using the productive function $f$. Define a recursive sequence $\langle a_n : n \in \omega angle$ by setting $a_0 = f(\langle angle)$ and $a_{n+1} = f(\langle a_0, \ldots, a_n angle)$. For each $n$, let $x_n = \langle a_0, \ldots, a_{n-1} angle$. Then $\mathrm{Dmn}\,arphi^1(s_1^1(e, x_n)) = \{a_0, \ldots, a_{n-1}\}$. Since $f$ is productive, $f(x_n) = a_n \in A \sim \mathrm{Dmn}\,arphi^1(s_1^1(e, x_n)) = A \sim \{a_0, \ldots, a_{n-1}\}$. Thus the $a_n$ are distinct and all lie in $A$, giving the desired infinite r.e. subset.
