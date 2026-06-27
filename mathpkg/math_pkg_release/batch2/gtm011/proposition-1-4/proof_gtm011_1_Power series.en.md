---
role: proof
locale: en
of_concept: proposition-1-4
source_book: gtm011
source_chapter: "Elementary Properties and Examples of Analytic Functions"
source_section: "1. Power series"
---

Proof. Again assume that $a = 0$ and let $\alpha = \lim |a_n/a_{n+1}|$, which we suppose to exist. Suppose that $|z| < r < \alpha$ and find an integer $N$ such that $r < |a_n/a_{n+1}|$ for all $n \geq N$. Let $B = |a_N|r^N$; then $|a_{N+1}|r^{N+1} = |a_{N+1}|rr^N < |a_N|r^N = B$; $|a_{N+2}|r^{N+2} = |a_{N+2}|rr^{N+1} < |a_{N+1}|r^{N+1} < B$; continuing we get $|a_nr^n| \leq B$ for all $n \geq N$. But then $|a_nz^n| = |a_nr^n| \frac{|z|^n}{r^n} \leq B \frac{|z|^n}{r^n}$ for all $n \geq N$. Since $|z| < r$ we get that $\sum_{n=1}^{\infty}|a_nz^n|$ is dominated by a convergent series and hence converges. Since $r < \alpha$ was arbitrary this gives that $\alpha \leq R$.

On the other hand if $|z| > r > \alpha$, then $|a_n| < r|a_{n+1}|$ for all $n$ larger than some integer $N$. As before, we get $|a_nr^n| \geq B = |a_Nr^N|$ for $n \geq N$. This gives $|a_nz^n| \geq B \frac{|z|^n}{|r|^n}$ which approaches $\infty$ as $n$ does. Hence, $\sum a_nz^n$ diverges and so $R \leq \alpha$. Thus $R = \alpha$.

Analytic functions

$$\sum (a_n + b_n) (z - a)^n = \left[ \sum a_n (z - a)^n + \sum b_n (z - a)^n \right]$$
$$\sum c_n (z - a)^n = \left[ \sum a_n (z - a)^n \right] \left[ \sum b_n (z - a)^n \right]$$
for $|z - a| < r$.

Proof. We only give an outline of the proof. If $0 < s < r$ then for $|z| \leq s$, we get $\sum |a_n + b_n| |z|^n \leq \sum |a_n| s^n + \sum |b_n| s^n < \infty$; $\sum |c_n| |z|^n \leq \left( \sum |a_n| s^n \right) \left( \sum |b_n| s^n \right) < \infty$. From here the proof can easily be completed.

Exercises

1. Prove Proposition 1.5.
2. Give the details of the proof of Proposition 1.6.
3. Prove that $\limsup (a_n + b_n) \leq \limsup a_n + \limsup b_n$ and $\liminf (a_n + b_n) \geq \liminf a_n + \liminf b_n$ for bounded sequences of real numbers $\{a_n\}$ and $\{b_n\}$.
4. Show that $\liminf a_n \leq \limsup a_n$ for any sequence in $\mathbb{R}$.
5. If $\{a_n\}$ is a convergent sequence in $\mathbb{R}$ and $a = \lim a_n$, show that $a = \lim inf a_n = \lim sup a_n$.
6. Find the radius of convergence for each of the following power series:
   (a) $\sum_{n=0}^{\infty} a_n z^n$, $a \in \mathbb{C}$; (b) $\sum_{n=0}^{\infty} a_n^2 z^n$, $a \in \mathbb{C}$; (c) $\sum_{n=0}^{\infty} k_n z^n$, $k$ an integer

The following was surely predicted by the reader.
