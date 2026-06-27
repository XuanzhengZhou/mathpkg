---
role: proof
locale: en
of_concept: fermat-two-square-theorem
source_book: gtm050
source_chapter: "2"
source_section: "2.6 Addendum on sums of two squares"
---

Euler's proof is an indirect proof, an argument by contradiction which shows that if a prime of the form $4n+1$ is not the sum of two squares then an infinitely descending sequence of positive integers could be found. Therefore it does not solve Fermat's problem of finding a constructive method. A more careful study of the proof by contradiction shows that it can be modified to give a constructive proof.

Step (5) of Euler's proof is quite constructive. It says that if $4n+1$ is prime then at least one of the numbers

$$1^{2n} + 2^{2n}, \; 2^{2n} + 3^{2n}, \; \ldots, \; (4n-1)^{2n} + (4n)^{2n}$$

must be divisible by $4n+1$. In Fermat's example $4n+1 = 53$ one easily finds that the first number $1 + 2^{26}$ of this list is divisible by $53$. Using the notation of congruences, one finds

$$2^6 = 64 \equiv 11 \pmod{53}, \quad 2^{12} \equiv 11^2 = 121 \equiv 15 \pmod{53}, \quad 2^{13} \equiv 30 \pmod{53},$$

$$2^{26} \equiv 30^2 = 900 \equiv -1 \pmod{53},$$

so $2^{26} + 1$ is divisible by $53$. This gives a representation of some multiple of $53$ as a sum of two squares, namely

$$53 \cdot 17 \cdot 17 = 53 \cdot 289 = (30)^2 + 1^2.$$

Then, factoring $k$ into its prime factors, writing each such factor as a sum of two squares, and dividing by them one-by-one. In the case at hand, $k = 17$ is itself a prime and is easy to write as a sum of two squares: $17 = 1^2 + 4^2$. The division process uses the identity

$$(a^2 + b^2)(c^2 + d^2) = (ac \mp bd)^2 + (ad \pm bc)^2.$$

Thus $17 \cdot 17 \cdot 53 = (1^2 + 4^2)(30^2 + 1^2) = (30 \mp 4)^2 + (1 \pm 120)^2$, and choosing the signs in such a way that division by $17$ is possible gives

$$53 = \left(\frac{34}{17}\right)^2 + \left(\frac{119}{17}\right)^2 = 2^2 + 7^2.$$

This method reduces the problem of writing the prime $p$ as a sum of two squares to the problem of writing smaller primes of the form $4n+1$, namely, the prime factors of $k$, as sums of two squares. This may be the method which Fermat himself had in mind when he described his proof by infinite descent: "If a chosen prime number which is one greater than a multiple of $4$ were not the sum of two squares there would be a prime number of the same nature less than the given one, and after that yet a third, etc. descending infinitely until you arrived at $5$, which is the least of all of this nature, which it would follow was not the sum of two squares, even though it is. From which one must infer, by deduction to the impossible, that all those of this nature are consequently sums of two squares." (letter to Carcavi [F5])
