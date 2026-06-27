---
role: proof
locale: en
of_concept: reverse-markov-chain-property
source_book: gtm040
source_chapter: "6"
source_section: "8"
---

We verify that the functions $y_n$ satisfy the Markov property. This needs to be checked only for $n \leq N$, since for $n > N$ the process is deterministically ``stop.''

Assume $\Pr[y_0 = c_0 \land \cdots \land y_{n-1} = c_{n-1}] > 0$. Then

egin{align*}
&\Pr[y_n = c_n \mid y_0 = c_0 \land \cdots \land y_{n-1} = c_{n-1}] \
&= rac{\Pr[y_0 = c_0 \land \cdots \land y_n = c_n]}{\Pr[y_0 = c_0 \land \cdots \land y_{n-1} = c_{n-1}]} \
&= rac{\Pr[x_N = c_0 \land x_{N-1} = c_1 \land \cdots \land x_{N-n} = c_n]}{\Pr[x_N = c_0 \land x_{N-1} = c_1 \land \cdots \land x_{N-n+1} = c_{n-1}]}.
\end{align*}

By the Markov property applied forward in the original process, the numerator expands as
$$\Pr[x_{N-n} = c_n \land x_{N-n+1} = c_{n-1}] \cdot P_{c_{n-1}c_{n-2}} \cdot \cdots \cdot P_{c_1c_0}.$$

Similarly, the denominator expands as
$$\Pr[x_{N-n+1} = c_{n-1}] \cdot P_{c_{n-1}c_{n-2}} \cdot \cdots \cdot P_{c_1c_0}.$$

Canceling the common factor $P_{c_{n-1}c_{n-2}} \cdots P_{c_1c_0}$, we obtain

egin{align*}
\Pr[y_n = c_n \mid y_0 = c_0 \land \cdots \land y_{n-1} = c_{n-1}]
&= rac{\Pr[x_{N-n} = c_n \land x_{N-n+1} = c_{n-1}]}{\Pr[x_{N-n+1} = c_{n-1}]} \
&= \Pr[x_{N-n} = c_n \mid x_{N-n+1} = c_{n-1}] \
&= \Pr[y_n = c_n \mid y_{n-1} = c_{n-1}].
\end{align*}

Thus the conditional probability depends only on $y_{n-1}$, confirming the Markov property for the reversed process.

Note that the reversed process is not necessarily a (time-homogeneous) Markov chain: the reversed transition probability
$$\Pr[y_n = j \mid y_{n-1} = i] = rac{(\pi P^{N-n})_j \cdot P_{ji}}{(\pi P^{N-n+1})_i}$$
generally depends on $n$. However, if $P$ is ergodic, as $N 	o \infty$ the ratio stabilizes and a limiting reverse chain exists.
