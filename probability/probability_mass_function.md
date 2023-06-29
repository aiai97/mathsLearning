### Discrete Random Variable
Analysts denote the variable as X and its possible values as x1, x2, …, xn.
The probability of X having a value of x for its ith observation equals pi: P (X = xi) = pi.

｜ PMF	                      ｜                                PDF｜
|------------------------------|-----------------------------------|-----|
｜Use for discrete random variables.｜Use for continuous random variables.｜
｜Finds the probability that the variable can take on one of its discrete values.｜Finds the probability that the variable will lie within a range of values.｜
### continuous randon variable
Analysts denote a continuous random variable as X and its possible values as x, just like the discrete version. However, unlike discrete random variables, the chances of X taking on a specific value for continuous data is zero. 
In other words: P (X = x) = 0, where x is any specific value.
Probabilities for all ranges of X are greater than or equal to zero: P(a ≤ X ≤ b) ≥ 0.
The total area under the curve equals one: P(-∞ ≤ X ≤ + ∞) = 1.

The following are common types of PDFs:
Normal Distribution
Exponential Distribution
Lognormal Distribution
Weibull Distribution
Before using a PDF for a continuous random variable, Identify the Distribution of Your Data. 
### probability mass function (PMF) 
is a mathematical function that calculates the probability a discrete random variable will be a specific value.
The standard notation for a probability mass function is P(X = x) = f (x). Where:

X is the discrete random variable.
x is one of the possible discrete values.
f (x) is a mathematical function that calculates the likelihood for the value of x.
So, putting it all together, P(X = x) = f (x) means: The chance of variable X assuming the specific value of x equals f (x).

Probability Mass Function: Definition, Uses & Example
By Jim Frost Leave a Comment

What is a Probability Mass Function?
A probability mass function (PMF) is a mathematical function that calculates the probability a discrete random variable will be a specific value. PMFs also describe the probability distribution for the full range of values for a discrete variable. A discrete random variable can take on a finite or countably infinite number of possible values, such as the number of heads in a series of coin flips or the number of customers who visit a store on a given day.

Probability mass functions find the likelihood of a particular outcome. For example, we can use a PMF to calculate the probability of getting exactly three heads in a series of coin flips. This process involves plugging the value into the correct probability mass function and calculating the likelihood.

Using a PMF to calculate the likelihoods for all possible values of the discrete variable produces its probability distribution.

Read on to learn more about using probability mass functions, work through an example, and learn about the various types.

Learn more about Random Variables: Discrete & Continuous.

PMF vs PDF
PMFs and probability density functions (PDFs) both find likelihoods for random variables and can produce probability distributions. The table below summarizes their differences.

PMF	PDF
Use for discrete random variables.	Use for continuous random variables.
Finds the probability that the variable can take on one of its discrete values.	Finds the probability that the variable will lie within a range of values.
Related posts: Discrete vs. Continuous, Probability Density Functions (PDFs), and Probability Distributions.

Probability Mass Function Notation and Details
For a discrete random variable, each possible value must have a non-zero likelihood. Additionally, the probabilities for all possible values must sum to one. Because the total chance is 1, one of the values must occur for each opportunity.

For example, the chance of rolling a particular number on a die is 1/6. The total probability for all six outcomes equals one. For a single roll of a die, you inevitably obtain one of the possible values. Or, when you flip a coin five times, you’ll always get 0 to 5 heads because each outcome has a non-zero chance and they sum to 1.

If the probability mass function has a finite number of values, you can list all the outcomes and their likelihoods in a table, producing its probability distribution, which I’ll show in the next section.

The standard notation for a probability mass function is P(X = x) = f (x). Where:

X is the discrete random variable.
x is one of the possible discrete values.
f (x) is a mathematical function that calculates the likelihood for the value of x.
So, putting it all together, P(X = x) = f (x) means: The chance of variable X assuming the specific value of x equals f (x).

For example, when considering three heads in a series of coin tosses, the PMF notation is: P(Heads = 3) = f (x).
Probability Mass Function Example
The coin flip scenario requires the binomial distribution because it calculates the probability of exactly x events occurring in n trials. For example, it can find the likelihood of 3 heads occurring in five coin flips.

F (x) = nCx * px * (1 – p)n – x

Probability Mass Function: Definition, Uses & Example
By Jim Frost Leave a Comment

What is a Probability Mass Function?
A probability mass function (PMF) is a mathematical function that calculates the probability a discrete random variable will be a specific value. PMFs also describe the probability distribution for the full range of values for a discrete variable. A discrete random variable can take on a finite or countably infinite number of possible values, such as the number of heads in a series of coin flips or the number of customers who visit a store on a given day.

Probability mass functions find the likelihood of a particular outcome. For example, we can use a PMF to calculate the probability of getting exactly three heads in a series of coin flips. This process involves plugging the value into the correct probability mass function and calculating the likelihood.

Using a PMF to calculate the likelihoods for all possible values of the discrete variable produces its probability distribution.

Read on to learn more about using probability mass functions, work through an example, and learn about the various types.

Learn more about Random Variables: Discrete & Continuous.

PMF vs PDF
PMFs and probability density functions (PDFs) both find likelihoods for random variables and can produce probability distributions. The table below summarizes their differences.

PMF	PDF
Use for discrete random variables.	Use for continuous random variables.
Finds the probability that the variable can take on one of its discrete values.	Finds the probability that the variable will lie within a range of values.
Related posts: Discrete vs. Continuous, Probability Density Functions (PDFs), and Probability Distributions.

Probability Mass Function Notation and Details
For a discrete random variable, each possible value must have a non-zero likelihood. Additionally, the probabilities for all possible values must sum to one. Because the total chance is 1, one of the values must occur for each opportunity.

For example, the chance of rolling a particular number on a die is 1/6. The total probability for all six outcomes equals one. For a single roll of a die, you inevitably obtain one of the possible values. Or, when you flip a coin five times, you’ll always get 0 to 5 heads because each outcome has a non-zero chance and they sum to 1.

If the probability mass function has a finite number of values, you can list all the outcomes and their likelihoods in a table, producing its probability distribution, which I’ll show in the next section.

The standard notation for a probability mass function is P(X = x) = f (x). Where:

X is the discrete random variable.
x is one of the possible discrete values.
f (x) is a mathematical function that calculates the likelihood for the value of x.
So, putting it all together, P(X = x) = f (x) means: The chance of variable X assuming the specific value of x equals f (x).

For example, when considering three heads in a series of coin tosses, the PMF notation is: P(Heads = 3) = f (x).

### Probability Mass Function Example
The coin flip scenario requires the binomial distribution because it calculates the probability of exactly x events occurring in n trials. For example, it can find the likelihood of 3 heads occurring in five coin flips.

F (x) = nCx * px * (1 – p)n – x

Where:

n = number of trials.
x = number of successes
p = probability of success.
nCx = number of combinations without repetition.
For this example, I’ll skip the calculations. However, read my post about the Binomial Distribution for a more in-depth look and a worked example.
