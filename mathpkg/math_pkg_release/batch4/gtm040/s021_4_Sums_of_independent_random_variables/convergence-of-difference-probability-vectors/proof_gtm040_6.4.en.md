---
role: proof
locale: en
of_concept: convergence-of-difference-probability-vectors
source_book: gtm040
source_chapter: "6"
source_section: "4"
---

Define the sets
$$E = \{n \mid (eta P^n)_s \leq (\gamma P^n)_s\}, \qquad F = \{n \mid (eta P^n)_s \geq (\gamma P^n)_s\}.$$
Note that $E \cup F = \mathbb{N}_0$. By Lemma 6-36, either
$$\Pr_{eta}[x_n = s 	ext{ for infinitely many } n \in E] = 1$$
or
$$\Pr_{\gamma}[x_n = s 	ext{ for infinitely many } n \in F] = 1.$$
By symmetry we may assume the former alternative holds.

Define $h^{(n)}$ to be the statement that $x_m = s$ for some $m \in E$ with $m < n$, and let
$$eta_k^{(n)} = \Pr_{eta}[x_n = k \land \sim h^{(n)}].$$
Then $eta^{(n)}$ is the sub-probability vector representing mass that has not yet visited $s$ at a time in $E$ before $n$. We have
$$\|eta^{(n)}\| = eta^{(n)}1 = \Pr_{eta}[\sim h^{(n)}] 	o 0$$
by the assumption that visits in $E$ occur infinitely often with probability 1.

The evolution of $eta^{(n)}$ satisfies $eta^{(0)} = eta$ and
$$eta_k^{(n+1)} = egin{cases} \sum_j eta_j^{(n)} P_{jk} & 	ext{if } n 
otin E \ \sum_{j 
eq s} eta_j^{(n)} P_{jk} & 	ext{if } n \in E. \end{cases}$$

Define the vector $\delta^{(n)}$ whose only possible nonzero component is $\delta_s^{(n)} = eta_s^{(n)}$ when $n \in E$, and $\delta^{(n)} = 0$ otherwise. Then
$$eta^{(n+1)} = eta^{(n)}P - \delta^{(n)}P.$$

Next, define
$$\gamma^{(n)} = eta^{(n)} + (\gamma - eta)P^n.$$
We have $\gamma^{(0)} = \gamma$, and a direct computation shows
$$\gamma^{(n+1)} = \gamma^{(n)}P + eta^{(n+1)} - eta^{(n)}P = (\gamma^{(n)} - \delta^{(n)})P.$$

We now prove by induction that $\gamma^{(n)} \geq \delta^{(n)}$ componentwise. First, $\gamma^{(0)} = \gamma \geq 0$. If $0 
otin E$, then $\delta^{(0)} = 0 \leq \gamma^{(0)}$. If $0 \in E$, then $\gamma_s^{(0)} = \gamma_s \geq eta_s = eta_s^{(0)} = \delta_s^{(0)}$ by definition of $E$. Thus $\gamma^{(0)} \geq \delta^{(0)}$.

Suppose $\gamma^{(n-1)} \geq \delta^{(n-1)}$. Then $\gamma^{(n)} = (\gamma^{(n-1)} - \delta^{(n-1)})P \geq 0$ since $P \geq 0$. If $n 
otin E$, then $\delta^{(n)} = 0$ and $\gamma^{(n)} \geq \delta^{(n)}$ trivially. If $n \in E$, then $[(\gamma - eta)P^n]_s \geq 0$ by the definition of $E$, and hence
$$\gamma_s^{(n)} = eta_s^{(n)} + [(\gamma - eta)P^n]_s \geq eta_s^{(n)} = \delta_s^{(n)}.$$
Thus $\gamma^{(n)} \geq \delta^{(n)}$ for every $n$. In particular, $\gamma^{(n)} \geq 0$.

Now compute the total mass of $\gamma^{(n)}$:
$$\|\gamma^{(n)}\| = \gamma^{(n)}1 = eta^{(n)}1 + [(\gamma - eta)P^n]1 = eta^{(n)}1 + (\gamma - eta)1 = eta^{(n)}1,$$
since $eta 1 = \gamma 1 = 1$ for probability vectors. Therefore $\|\gamma^{(n)}\| = \|eta^{(n)}\| 	o 0$.

Since $\gamma^{(n)} \geq 0$ and $\|\gamma^{(n)}\| 	o 0$, we have $\gamma^{(n)} 	o 0$ componentwise. But
$$\gamma^{(n)} = eta^{(n)} + (\gamma - eta)P^n,$$
and $eta^{(n)} 	o 0$, so $(\gamma - eta)P^n 	o 0$ componentwise. Hence
$$\lim_{n 	o \infty} \|(eta - \gamma)P^n\| = 0.$$
