---
role: proof
locale: en
of_concept: prop-for-type-i-random-walk-1
source_book: gtm034
source_chapter: "7"
source_section: "015"
---

Proof: It will suffice to prove (a). For suppose every type I random walk obeys (a). If we reverse such a random walk it will still be of type I and its potential kernel will be $a^*(x) = a(-x)$. But if $a^*(x)$ satisfies (a), then $a(x)$ is easily seen to satisfy (b). (Actually our method of proof is capable of giving both (a) and (b).)

We define

$$\Delta(x) = a(x) - a(x - 1), \quad x \geq 1.$$

The inequality of P4 can then be written

(1) $$\Delta(x + 1) + \Delta(x + 2) + \cdots + \Delta(x + y) \leq \Delta(1) + \Delta(2) + \cdots + \Delta(y)$$

whenever $x \geq 1$ and $y \geq 1$. According to P5,

(2) $$\lim_{|x| \to \infty} [\Delta(x + 1) - \Delta(x)] = 0.$$

In view of (2), letting $x \to +\infty$ in (1) gives

(3) $$y \lim_{x \to +\infty} \Delta(x) \leq \Delta(1) + \Delta(2) + \cdots + \Delta(y)$$

for every $y \geq 1.$

The last step consists of dividing both sides in (3) by $y$, and then letting $y \to +\infty$. Using P3 that leads to

$$\lim_{x \to +\infty} \Delta(x) \leq \lim_{y \to +\infty} \frac{1}{y} [\Delta(1) + \Delta(2)

is a non-negative constant, which we shall call $\mu$. (If it depended on $x$ it would be a nonconstant bounded regular function, which is impossible. This argument should be familiar from P11.4). Now P1 can be written in the form

$$H_C(x,0) = \mu - [a(x) - a(x - 1)]\Pi_C(0,c),$$

and since $\Pi_C(0,c) > 0$ we get from P6
