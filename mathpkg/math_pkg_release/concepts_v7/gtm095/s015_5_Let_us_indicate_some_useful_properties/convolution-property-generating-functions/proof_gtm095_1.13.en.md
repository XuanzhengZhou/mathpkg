---
role: proof
locale: en
of_concept: convolution-property-generating-functions
source_book: gtm095
source_chapter: "1"
source_section: "13"
---

# Proof of the Convolution Property of Generating Functions

Let $(a_n)_{n \geq 0}$ and $(b_n)_{n \geq 0}$ be two sequences whose generating functions are

$$A(x) = \sum_{n \geq 0} a_n x^n, \qquad B(x) = \sum_{n \geq 0} b_n x^n.$$

Consider the product $A(x)B(x)$. Multiplying the two series term by term, we obtain

$$
A(x)B(x) = \left(\sum_{i \geq 0} a_i x^i\right)\!\left(\sum_{j \geq 0} b_j x^j\right)
= \sum_{i,j \geq 0} a_i b_j \, x^{i+j}.
$$

Group the terms according to the total power $n = i + j$. For a fixed $n \geq 0$, the sum of all terms with $i + j = n$ is

$$
\left(\sum_{i=0}^{n} a_i b_{n-i}\right) x^n.
$$

Hence

$$
A(x)B(x) = \sum_{n \geq 0} \left(\sum_{i=0}^{n} a_i b_{n-i}\right) x^n.
$$

The coefficient of $x^n$ in $A(x)B(x)$ is precisely the discrete convolution $\sum_{i=0}^{n} a_i b_{n-i}$ of the two sequences. Therefore, in the bijective correspondence $(c_n)_{n \geq 0} \leftrightarrow C(x)$ between sequences and their generating functions, we have

$$
\boxed{\left(\sum_{i=0}^{n} a_i b_{n-i}\right)_{n \geq 0} \;\longleftrightarrow\; A(x)B(x)}.
$$

This is the convolution property. In probabilistic terms, if $\xi$ and $\eta$ are independent nonnegative integer-valued random variables with generating functions $G_\xi(x)$ and $G_\eta(x)$, then the generating function of their sum is $G_{\xi+\eta}(x) = G_\xi(x)G_\eta(x)$. $\square$
