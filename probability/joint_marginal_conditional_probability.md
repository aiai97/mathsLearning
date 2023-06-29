### Joint Probability: P(A and B) = P(A) * P(B)
The Joint Probability refers to the probability of two events, A and B, occurring simultaneously.
Example: Consider rolling a fair six-sided die. Let's define event A as getting an even number (2, 4, or 6) and event B as getting a number greater than 4 (5 or 6). The joint probability, P(A and B), is the probability of rolling a number that is both even and greater than 4, which is 1/6 because there is only one outcome (6) that satisfies both conditions out of the six possible outcomes.

### Marginal Probability: P(A)
The Marginal Probability is the probability of a specific event X=A occurring, given a variable Y.
Example: Suppose we have a bag of colored marbles. Let's define event X as selecting a blue marble, and event Y as selecting a large marble. The marginal probability, P(X=A | Y), represents the probability of selecting a blue marble, given that the marble is large. In this case, the marginal probability would be the proportion of blue marbles among the large marbles in the bag.

### Conditional Probability: P(A given B) = P(A)
The Conditional Probability refers to the probability of event A occurring, given that event B has already occurred.
Example: Imagine drawing two cards from a standard deck of 52 playing cards. Let event A be drawing a heart, and event B be drawing a queen. The conditional probability, P(A | B), is the probability of drawing a heart, given that the first card drawn was a queen. Since there are four queens in the deck, and only one of them is a heart, the conditional probability would be 1/4.

### Exclusivity
If the occurrence of one event excludes the occurrence of other events, then the events are said to be mutually exclusive.


### Joint Probability of Two Variables
We may be interested in the probability of two simultaneous events, e.g. the outcomes of two different random variables.

The probability of two (or more) events is called the joint probability. The joint probability of two or more random variables is referred to as the joint probability distribution.

For example, the joint probability of event A and event B is written formally as:

P(A and B)
The “and” or conjunction is denoted using the upside down capital “U” operator “^” or sometimes a comma “,”.

P(A ^ B)
P(A, B)
The joint probability for events A and B is calculated as the probability of event A given event B multiplied by the probability of event B.

This can be stated formally as follows:

##### P(A and B) = P(A given B) * P(B)
The calculation of the joint probability is sometimes called the fundamental rule of probability or the “product rule” of probability or the “chain rule” of probability.

Here, P(A given B) is the probability of event A given that event B has occurred, called the conditional probability, described below.

The joint probability is symmetrical, meaning that P(A and B) is the same as P(B and A). The calculation using the conditional probability is also symmetrical, for example:

##### P(A and B) = P(A given B) * P(B) = P(B given A) * P(A)


A Gentle Introduction to Joint, Marginal, and Conditional Probability
by Jason Brownlee on September 27, 2019 in Probability
Tweet Tweet  Share
Last Updated on May 6, 2020

Probability quantifies the uncertainty of the outcomes of a random variable.

It is relatively easy to understand and compute the probability for a single variable. Nevertheless, in machine learning, we often have many random variables that interact in often complex and unknown ways.

There are specific techniques that can be used to quantify the probability for multiple random variables, such as the joint, marginal, and conditional probability. These techniques provide the basis for a probabilistic understanding of fitting a predictive model to data.

In this post, you will discover a gentle introduction to joint, marginal, and conditional probability for multiple random variables.

After reading this post, you will know:

Joint probability is the probability of two events occurring simultaneously.
Marginal probability is the probability of an event irrespective of the outcome of another variable.
Conditional probability is the probability of one event occurring in the presence of a second event.
Kick-start your project with my new book Probability for Machine Learning, including step-by-step tutorials and the Python source code files for all examples.

Let’s get started.

Update Oct/2019: Fixed minor typo, thanks Anna.
Update Nov/2019: Described the symmetrical calculation of joint probability.
A Gentle Introduction to Joint, Marginal, and Conditional Probability
A Gentle Introduction to Joint, Marginal, and Conditional Probability
Photo by Masterbutler, some rights reserved.

Overview
This tutorial is divided into three parts; they are:

Probability of One Random Variable
Probability of Multiple Random Variables
Probability of Independence and Exclusivity

Probability of One Random Variable
Probability quantifies the likelihood of an event.

Specifically, it quantifies how likely a specific outcome is for a random variable, such as the flip of a coin, the roll of a dice, or drawing a playing card from a deck.

Probability gives a measure of how likely it is for something to happen.

— Page 57, Probability: For the Enthusiastic Beginner, 2016.

For a random variable x, P(x) is a function that assigns a probability to all values of x.

Probability Density of x = P(x)
The probability of a specific event A for a random variable x is denoted as P(x=A), or simply as P(A).

Probability of Event A = P(A)
Probability is calculated as the number of desired outcomes divided by the total possible outcomes, in the case where all outcomes are equally likely.

Probability = (number of desired outcomes) / (total number of possible outcomes)
This is intuitive if we think about a discrete random variable such as the roll of a die. For example, the probability of a die rolling a 5 is calculated as one outcome of rolling a 5 (1) divided by the total number of discrete outcomes (6) or 1/6 or about 0.1666 or about 16.666%.

The sum of the probabilities of all outcomes must equal one. If not, we do not have valid probabilities.

Sum of the Probabilities for All Outcomes = 1.0.
The probability of an impossible outcome is zero. For example, it is impossible to roll a 7 with a standard six-sided die.

Probability of Impossible Outcome = 0.0
The probability of a certain outcome is one. For example, it is certain that a value between 1 and 6 will occur when rolling a six-sided die.

Probability of Certain Outcome = 1.0
The probability of an event not occurring, called the complement.

This can be calculated by one minus the probability of the event, or 1 – P(A). For example, the probability of not rolling a 5 would be 1 – P(5) or 1 – 0.166 or about 0.833 or about 83.333%.

Probability of Not Event A = 1 – P(A)
Now that we are familiar with the probability of one random variable, let’s consider probability for multiple random variables.

Want to Learn Probability for Machine Learning
Take my free 7-day email crash course now (with sample code).

Click to sign-up and also get a free PDF Ebook version of the course.

Download Your FREE Mini-Course


Probability of Multiple Random Variables
In machine learning, we are likely to work with many random variables.

For example, given a table of data, such as in excel, each row represents a separate observation or event, and each column represents a separate random variable.

Variables may be either discrete, meaning that they take on a finite set of values, or continuous, meaning they take on a real or numerical value.

As such, we are interested in the probability across two or more random variables.

This is complicated as there are many ways that random variables can interact, which, in turn, impacts their probabilities.

This can be simplified by reducing the discussion to just two random variables (X, Y), although the principles generalize to multiple variables.

And further, to discuss the probability of just two events, one for each variable (X=A, Y=B), although we could just as easily be discussing groups of events for each variable.

Therefore, we will introduce the probability of multiple random variables as the probability of event A and event B, which in shorthand is X=A and Y=B.

We assume that the two variables are related or dependent in some way.

As such, there are three main types of probability we might want to consider; they are:

Joint Probability: Probability of events A and B.
Marginal Probability: Probability of event X=A given variable Y.
Conditional Probability: Probability of event A given event B.
These types of probability form the basis of much of predictive modeling with problems such as classification and regression. For example:

The probability of a row of data is the joint probability across each input variable.
The probability of a specific value of one input variable is the marginal probability across the values of the other input variables.
The predictive model itself is an estimate of the conditional probability of an output given an input example.
Joint, marginal, and conditional probability are foundational in machine learning.

Let’s take a closer look at each in turn.


### Joint Probability of Two Variables
We may be interested in the probability of two simultaneous events, e.g. the outcomes of two different random variables.

The probability of two (or more) events is called the joint probability. The joint probability of two or more random variables is referred to as the joint probability distribution.

For example, the joint probability of event A and event B is written formally as:

P(A and B)
The “and” or conjunction is denoted using the upside down capital “U” operator “^” or sometimes a comma “,”.

P(A ^ B)
P(A, B)
The joint probability for events A and B is calculated as the probability of event A given event B multiplied by the probability of event B.

This can be stated formally as follows:

P(A and B) = P(A given B) * P(B)
The calculation of the joint probability is sometimes called the fundamental rule of probability or the “product rule” of probability or the “chain rule” of probability.

Here, P(A given B) is the probability of event A given that event B has occurred, called the conditional probability, described below.

The joint probability is symmetrical, meaning that P(A and B) is the same as P(B and A). The calculation using the conditional probability is also symmetrical, for example:

P(A and B) = P(A given B) * P(B) = P(B given A) * P(A)

### Marginal Probability
We may be interested in the probability of an event for one random variable, irrespective of the outcome of another random variable.

For example, the probability of X=A for all outcomes of Y.
There is no special notation for the marginal probability; it is just the sum or union over all the probabilities of all events for the second variable for a given fixed event for the first variable.

##### P(X=A) = sum P(X=A, Y=yi) for all y
This is another important foundational rule in probability, referred to as the “sum rule.”

### Conditional Probability
We may be interested in the probability of an event given the occurrence of another event.

The probability of one event given the occurrence of another event is called the conditional probability. The conditional probability of one to one or more random variables is referred to as the conditional probability distribution.

For example, the conditional probability of event A given event B is written formally as:

P(A given B)
The “given” is denoted using the pipe “|” operator; for example:

P(A | B)
The conditional probability for events A given event B is calculated as follows:

P(A given B) = P(A and B) / P(B)
This calculation assumes that the probability of event B is not zero, e.g. is not impossible.

The notion of event A given event B does not mean that event B has occurred (e.g. is certain); instead, it is the probability of event A occurring after or in the presence of event B for a given trial.

### MachineLearningMastery.com
Click to Take the FREE Probability Crash-Course
Search...

Get Started
Blog
Topics
EBooks
FAQ
About
Contact
Go from Data to Strategy: Tepper School of Business
Go from Data to Strategy: Tepper School of Business

A Gentle Introduction to Joint, Marginal, and Conditional Probability
by Jason Brownlee on September 27, 2019 in Probability
Tweet Tweet  Share
Last Updated on May 6, 2020

Probability quantifies the uncertainty of the outcomes of a random variable.

It is relatively easy to understand and compute the probability for a single variable. Nevertheless, in machine learning, we often have many random variables that interact in often complex and unknown ways.

There are specific techniques that can be used to quantify the probability for multiple random variables, such as the joint, marginal, and conditional probability. These techniques provide the basis for a probabilistic understanding of fitting a predictive model to data.

In this post, you will discover a gentle introduction to joint, marginal, and conditional probability for multiple random variables.

After reading this post, you will know:

Joint probability is the probability of two events occurring simultaneously.
Marginal probability is the probability of an event irrespective of the outcome of another variable.
Conditional probability is the probability of one event occurring in the presence of a second event.
Kick-start your project with my new book Probability for Machine Learning, including step-by-step tutorials and the Python source code files for all examples.

Let’s get started.

Update Oct/2019: Fixed minor typo, thanks Anna.
Update Nov/2019: Described the symmetrical calculation of joint probability.
A Gentle Introduction to Joint, Marginal, and Conditional Probability
A Gentle Introduction to Joint, Marginal, and Conditional Probability
Photo by Masterbutler, some rights reserved.

Overview
This tutorial is divided into three parts; they are:

Probability of One Random Variable
Probability of Multiple Random Variables
Probability of Independence and Exclusivity

Probability of One Random Variable
Probability quantifies the likelihood of an event.

Specifically, it quantifies how likely a specific outcome is for a random variable, such as the flip of a coin, the roll of a dice, or drawing a playing card from a deck.

Probability gives a measure of how likely it is for something to happen.

— Page 57, Probability: For the Enthusiastic Beginner, 2016.

For a random variable x, P(x) is a function that assigns a probability to all values of x.

Probability Density of x = P(x)
The probability of a specific event A for a random variable x is denoted as P(x=A), or simply as P(A).

Probability of Event A = P(A)
Probability is calculated as the number of desired outcomes divided by the total possible outcomes, in the case where all outcomes are equally likely.

Probability = (number of desired outcomes) / (total number of possible outcomes)
This is intuitive if we think about a discrete random variable such as the roll of a die. For example, the probability of a die rolling a 5 is calculated as one outcome of rolling a 5 (1) divided by the total number of discrete outcomes (6) or 1/6 or about 0.1666 or about 16.666%.

The sum of the probabilities of all outcomes must equal one. If not, we do not have valid probabilities.

Sum of the Probabilities for All Outcomes = 1.0.
The probability of an impossible outcome is zero. For example, it is impossible to roll a 7 with a standard six-sided die.

Probability of Impossible Outcome = 0.0
The probability of a certain outcome is one. For example, it is certain that a value between 1 and 6 will occur when rolling a six-sided die.

Probability of Certain Outcome = 1.0
The probability of an event not occurring, called the complement.

This can be calculated by one minus the probability of the event, or 1 – P(A). For example, the probability of not rolling a 5 would be 1 – P(5) or 1 – 0.166 or about 0.833 or about 83.333%.

Probability of Not Event A = 1 – P(A)
Now that we are familiar with the probability of one random variable, let’s consider probability for multiple random variables.

Want to Learn Probability for Machine Learning
Take my free 7-day email crash course now (with sample code).

Click to sign-up and also get a free PDF Ebook version of the course.

Download Your FREE Mini-Course


Probability of Multiple Random Variables
In machine learning, we are likely to work with many random variables.

For example, given a table of data, such as in excel, each row represents a separate observation or event, and each column represents a separate random variable.

Variables may be either discrete, meaning that they take on a finite set of values, or continuous, meaning they take on a real or numerical value.

As such, we are interested in the probability across two or more random variables.

This is complicated as there are many ways that random variables can interact, which, in turn, impacts their probabilities.

This can be simplified by reducing the discussion to just two random variables (X, Y), although the principles generalize to multiple variables.

And further, to discuss the probability of just two events, one for each variable (X=A, Y=B), although we could just as easily be discussing groups of events for each variable.

Therefore, we will introduce the probability of multiple random variables as the probability of event A and event B, which in shorthand is X=A and Y=B.

We assume that the two variables are related or dependent in some way.

As such, there are three main types of probability we might want to consider; they are:

Joint Probability: Probability of events A and B.
Marginal Probability: Probability of event X=A given variable Y.
Conditional Probability: Probability of event A given event B.
These types of probability form the basis of much of predictive modeling with problems such as classification and regression. For example:

The probability of a row of data is the joint probability across each input variable.
The probability of a specific value of one input variable is the marginal probability across the values of the other input variables.
The predictive model itself is an estimate of the conditional probability of an output given an input example.
Joint, marginal, and conditional probability are foundational in machine learning.

Let’s take a closer look at each in turn.


Joint Probability of Two Variables
We may be interested in the probability of two simultaneous events, e.g. the outcomes of two different random variables.

The probability of two (or more) events is called the joint probability. The joint probability of two or more random variables is referred to as the joint probability distribution.

For example, the joint probability of event A and event B is written formally as:

P(A and B)
The “and” or conjunction is denoted using the upside down capital “U” operator “^” or sometimes a comma “,”.

P(A ^ B)
P(A, B)
The joint probability for events A and B is calculated as the probability of event A given event B multiplied by the probability of event B.

This can be stated formally as follows:

P(A and B) = P(A given B) * P(B)
The calculation of the joint probability is sometimes called the fundamental rule of probability or the “product rule” of probability or the “chain rule” of probability.

Here, P(A given B) is the probability of event A given that event B has occurred, called the conditional probability, described below.

The joint probability is symmetrical, meaning that P(A and B) is the same as P(B and A). The calculation using the conditional probability is also symmetrical, for example:

P(A and B) = P(A given B) * P(B) = P(B given A) * P(A)

Marginal Probability
We may be interested in the probability of an event for one random variable, irrespective of the outcome of another random variable.

For example, the probability of X=A for all outcomes of Y.

The probability of one event in the presence of all (or a subset of) outcomes of the other random variable is called the marginal probability or the marginal distribution. The marginal probability of one random variable in the presence of additional random variables is referred to as the marginal probability distribution.

It is called the marginal probability because if all outcomes and probabilities for the two variables were laid out together in a table (X as columns, Y as rows), then the marginal probability of one variable (X) would be the sum of probabilities for the other variable (Y rows) on the margin of the table.

There is no special notation for the marginal probability; it is just the sum or union over all the probabilities of all events for the second variable for a given fixed event for the first variable.

P(X=A) = sum P(X=A, Y=yi) for all y
This is another important foundational rule in probability, referred to as the “sum rule.”

The marginal probability is different from the conditional probability (described next) because it considers the union of all events for the second variable rather than the probability of a single event.


Conditional Probability
We may be interested in the probability of an event given the occurrence of another event.

The probability of one event given the occurrence of another event is called the conditional probability. The conditional probability of one to one or more random variables is referred to as the conditional probability distribution.

For example, the conditional probability of event A given event B is written formally as:

P(A given B)
The “given” is denoted using the pipe “|” operator; for example:

P(A | B)
The conditional probability for events A given event B is calculated as follows:

P(A given B) = P(A and B) / P(B)
This calculation assumes that the probability of event B is not zero, e.g. is not impossible.

The notion of event A given event B does not mean that event B has occurred (e.g. is certain); instead, it is the probability of event A occurring after or in the presence of event B for a given trial.


### Probability of Independence and Exclusivity
Joint Probability: P(A and B) = P(A) * P(B)
As we might intuit, the marginal probability for an event for an independent random variable is simply the probability of the event.

It is the idea of probability of a single random variable that are familiar with:

Marginal Probability: P(A)
We refer to the marginal probability of an independent probability as simply the probability.

Similarly, the conditional probability of A given B when the variables are independent is simply the probability of A as the probability of B has no effect. For example:

Conditional Probability: P(A given B) = P(A)

### Exclusivity
If the occurrence of one event excludes the occurrence of other events, then the events are said to be mutually exclusive.

The probability of the events are said to be disjoint, meaning that they cannot interact, are strictly independent.

If the probability of event A is mutually exclusive with event B, then the joint probability of event A and event B is zero.

P(A and B) = 0.0
Instead, the probability of an outcome can be described as event A or event B, stated formally as follows:

P(A or B) = P(A) + P(B)
The “or” is also called a union and is denoted as a capital “U” letter; for example:

P(A or B) = P(A U B)
If the events are not mutually exclusive, we may be interested in the outcome of either event.

The probability of non-mutually exclusive events is calculated as the probability of event A and the probability of event B minus the probability of both events occurring simultaneously.

This can be stated formally as follows:

P(A or B) = P(A) + P(B) – P(A and B)
