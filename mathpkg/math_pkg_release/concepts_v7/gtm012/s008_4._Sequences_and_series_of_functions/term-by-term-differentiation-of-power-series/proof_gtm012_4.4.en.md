---
role: proof
locale: en
of_concept: term-by-term-differentiation-of-power-series
source_book: gtm012
source_chapter: "4"
source_section: "4. Sequences and series of functions"
---

# Proof of Theorem 4.4: Term-by-term differentiation of power series

**Theorem 4.4.** Let the power series

$$f(x) = \sum_{n=0}^{\infty} a_n (x - x_0)^n$$

have radius of convergence $R > 0$. Then $f$ is differentiable on $(x_0 - R, x_0 + R)$, and

$$f'(x) = \sum_{n=1}^{\infty} n a_n (x - x_0)^{n-1}, \quad |x - x_0| < R.$$

Moreover, the differentiated series also has radius of convergence $R$.

*Proof.* To simplify notation we shall assume $x_0 = 0$. We claim first that the two series

$$\sum_{n=1}^{\infty} n a_n x^{n-1}, \qquad \sum_{n=2}^{\infty} n^2 |a_n| r^{n-2}$$

converge uniformly for $|x| \leq r < R$. Take $r < s < R$. As in the proof of Theorem 4.3, there exists $M$ such that

$$|a_n| \leq M s^{-n}, \quad n = 0, 1, 2, \ldots. \tag{4.5}$$

Set $\delta = r/s < 1$. Choose $\varepsilon > 0$ so small that $(1 + \varepsilon)\delta < 1$. By Exercise 4 of Chapter 1, Section 3, $m \leq (1 + \varepsilon)^m$ for all sufficiently large $m$. Therefore there is a constant $M'$ such that

$$m \leq M'(1 + \varepsilon)^m, \quad m = 1, 2, 3, \ldots.$$

Now,

$$
\begin{aligned}
\sum_{m=1}^{n} |m a_m x^{m-1}|
&\leq M \sum_{m=1}^{n} m \, s^{-m} r^{m-1} \\
&= \frac{M}{r} \sum_{m=1}^{n} m \delta^{m} \\
&\leq \frac{M M'}{r} \sum_{m=1}^{n} (1 + \varepsilon)^m \delta^{m}.
\end{aligned}
$$

Since $(1 + \varepsilon)\delta < 1$, the geometric series $\sum (1 + \varepsilon)^m \delta^m$ converges. Hence the first series in (4.8) converges uniformly (and absolutely) for $|x| \leq r$, by the Weierstrass $M$-test.

Similarly, using the fact that $m^2 \leq M''(1 + \varepsilon)^m$ for large $m$ (with a possibly larger constant $M''$), the second series in (4.8) also converges uniformly for $|x| \leq r$.

Now let $g$ be the function defined by the first series in (4.8):

$$g(x) = \sum_{n=1}^{\infty} n a_n x^{n-1}, \quad |x| < R.$$

We must show that $f'(x) = g(x)$, i.e., that

$$\frac{f(y) - f(x)}{y - x} - g(x) \to 0 \quad \text{as } y \to x. \tag{4.9}$$

Assume $|x| < r$, $|y| < r$. Then

$$
\begin{aligned}
\frac{f(y) - f(x)}{y - x} - g(x)
&= \sum_{n=1}^{\infty} a_n \frac{y^n - x^n}{y - x} - \sum_{n=1}^{\infty} n a_n x^{n-1} \\
&= \sum_{n=2}^{\infty} a_n \left[ \frac{y^n - x^n}{y - x} - n x^{n-1} \right],
\end{aligned}
$$

since the $n = 1$ term vanishes. Using the algebraic identity

$$\frac{y^n - x^n}{y - x} = y^{n-1} + y^{n-2}x + \cdots + y x^{n-2} + x^{n-1}$$

and noting that $n x^{n-1} = x^{n-1} + x^{n-1} + \cdots + x^{n-1}$ ($n$ terms), we obtain

$$
\begin{aligned}
\frac{y^n - x^n}{y - x} - n x^{n-1}
&= \sum_{k=0}^{n-1} \bigl( y^{n-1-k} x^{k} - x^{n-1} \bigr) \\
&= (y - x) \sum_{k=0}^{n-2} y^{n-2-k} x^{k},
\end{aligned}
$$

where the second equality follows from factoring $(y - x)$ from each term $y^{n-1-k} x^k - x^{n-1} = x^k (y^{n-1-k} - x^{n-1-k})$ and summing. More precisely, for $|x|, |y| \leq r$,

$$\left| \frac{y^n - x^n}{y - x} - n x^{n-1} \right| \leq |y - x| \cdot n^2 r^{n-2}.$$

Indeed, each of the $n-1$ terms in the sum $y^{n-1} + y^{n-2}x + \cdots + x^{n-1}$ differs from $x^{n-1}$ by at most $|y - x| \cdot (n-1) r^{n-2}$, and there are $n$ such differences being summed (or more directly, one may bound each difference by $|y-x| \cdot n r^{n-2}$ and sum over $n$ terms, yielding the $n^2$ factor).

Therefore,

$$
\left| \frac{f(y) - f(x)}{y - x} - g(x) \right|
\leq |y - x| \sum_{n=2}^{\infty} n^2 |a_n| r^{n-2}.
$$

Since the series $\sum n^2 |a_n| r^{n-2}$ converges (as shown above), we have

$$\frac{f(y) - f(x)}{y - x} - g(x) = O(|y - x|) \to 0 \quad \text{as } y \to x.$$

Thus $f'(x) = g(x)$ for all $|x| < R$.

Finally, to see that the differentiated series has the same radius of convergence $R$, note that

$$\limsup_{n \to \infty} |n a_n|^{1/n} = \limsup_{n \to \infty} n^{1/n} |a_n|^{1/n} = \limsup_{n \to \infty} |a_n|^{1/n} = \frac{1}{R},$$

since $n^{1/n} \to 1$. Hence the radius of convergence of $\sum n a_n x^{n-1}$ is also $R$. $\square$
