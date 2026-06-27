---
role: proof
locale: en
of_concept: continuity-in-pseudo-metric-spaces
source_book: gtm027
source_chapter: "4"
source_section: "B. Continuity of Functions on a Metric Space"
---

# Proof of Continuity Characterization for Functions between Pseudo-Metric Spaces

Let $f: (X, d) \to (Y, e)$ be a function between pseudo-metric spaces.

## ($\Rightarrow$) Continuity implies $\varepsilon$-$\delta$ condition

Suppose $f$ is continuous. Let $x \in X$ and $\varepsilon > 0$. The open ball $B_e(f(x), \varepsilon) = \{y \in Y : e(f(x), y) < \varepsilon\}$ is an open set in $Y$. Since $f$ is continuous, $f^{-1}(B_e(f(x), \varepsilon))$ is an open set in $X$ containing $x$. By definition of the metric topology, there exists $\delta > 0$ such that the open ball $B_d(x, \delta) = \{y \in X : d(x, y) < \delta\}$ is contained in $f^{-1}(B_e(f(x), \varepsilon))$. Equivalently, if $d(x, y) < \delta$, then $y \in f^{-1}(B_e(f(x), \varepsilon))$, so $f(y) \in B_e(f(x), \varepsilon)$, i.e., $e(f(x), f(y)) < \varepsilon$.

## ($\Leftarrow$) $\varepsilon$-$\delta$ condition implies continuity

Suppose $f$ satisfies the $\varepsilon$-$\delta$ condition. To show $f$ is continuous, it suffices to show that the inverse image of every open set is open. Let $U \subset Y$ be open and let $x \in f^{-1}(U)$. Then $f(x) \in U$, and since $U$ is open in the metric topology of $(Y, e)$, there exists $\varepsilon > 0$ such that $B_e(f(x), \varepsilon) \subset U$.

By the $\varepsilon$-$\delta$ hypothesis, there exists $\delta > 0$ such that whenever $d(x, y) < \delta$, we have $e(f(x), f(y)) < \varepsilon$, i.e., $f(y) \in B_e(f(x), \varepsilon) \subset U$. Hence $y \in f^{-1}(U)$. This means $B_d(x, \delta) \subset f^{-1}(U)$.

Since $x \in f^{-1}(U)$ was arbitrary, $f^{-1}(U)$ contains a ball around each of its points, hence is open. Therefore $f$ is continuous.
