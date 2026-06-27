---
role: proof
locale: en
of_concept: exponent-rules
source_book: gtm028
source_chapter: "I"
source_section: "1"
---

Define $a^1 = a$ and $a^n = a^{n-1}a$ for $n > 1$ (inductive definition). The rules hold by definition for $n = 1$.

For rule (1) $a^m a^n = a^{m+n}$: Fix $m$ (positive). For $n = 1$, $a^m a^1 = a^m a = a^{m+1}$ by definition. Assuming it holds for $n-1$, we have $a^m a^n = a^m (a^{n-1}a) = (a^m a^{n-1})a = a^{m+n-1}a = a^{m+n}$. Thus (1) holds for all positive $n$ by induction.

For rule (2) $(a^m)^n = a^{mn}$: For $n = 1$, $(a^m)^1 = a^m = a^{m \cdot 1}$. Assuming it holds for $n-1$, $(a^m)^n = (a^m)^{n-1} a^m = a^{m(n-1)} a^m = a^{m(n-1)+m} = a^{mn}$ by rule (1).

For rule (3): If $a$ and $b$ commute ($ab = ba$), we first show by induction that any powers of $a$ and $b$ commute. For $n = 1$, $a b = ba$. Assuming $a^n b = b a^n$, then $a^{n+1}b = a(a^n b) = a(b a^n) = (ab)a^n = (ba)a^n = b a^{n+1}$. Similarly, $a^m b^n = b^n a^m$ for all $m, n$. For $(ab)^n = a^n b^n$: true for $n = 1$. Assuming true for $n-1$, $(ab)^n = (ab)^{n-1}(ab) = (a^{n-1}b^{n-1})(ab) = a^{n-1}(b^{n-1}a)b = a^{n-1}(a b^{n-1})b = (a^{n-1}a)(b^{n-1}b) = a^n b^n$, using that $b^{n-1}$ and $a$ commute.

If $G$ has identity $e$, define $a^0 = e$; then the three rules trivially hold for arbitrary non-negative exponents.

If $a$ possesses an inverse $a'$, negative powers are defined by the relation $a^m = a^{m+1}a'$ for all non-negative $m$, taken as an inductive definition for negative $m$. Thus $a^m a = a^{m+1}$ for all $m$ (positive or negative). Rule (1) is then true for any fixed $m$ provided $n = 1$; it can be proved for arbitrary positive $n$ by induction from $n-1$ to $n$ and for negative $n$ by induction from $n+1$ to $n$. Since $a^m a^{-m} = e = a^{-m}a^m$, we observe that $a^m$ has $a^{-m}$ as inverse, so that $(a^m)^n$ is defined for every $n$. Rule (2) can now be proved by the two inductions used for rule (1).
