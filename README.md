# partial_maxima
algorithm to store partial maxima in an efficient way for fast queries
## Synopsis
This is my code for the solution to the "partial maxima problem" from MIT's Introduction to Algorithm's course, which I self studied.

**A description of the problem is:**

6.006 student, Mike Velli, wants to build a website where the user can input a time interval in history, and the website will return the most exciting sports event that occurred during this interval. Formally, suppose that Mike has a chronologically sorted list of n sports events with associated integer “excitement factors” e1, . . . , en. You can assume for simplicity that n is a power of 2. A user’s query will consist of a pair (i, j) with 1 ≤ i < j ≤ n, and the site is supposed to return max(ei, ei+1, . . . , ej ).

Mike wishes to minimize the amount of computation per query, since there will be a lot of traffic to the website. If he precomputes and stores max(ei, . . . , ej ) for every possible input (i, j), he can respond to user queries quickly, but he needs storage Ω(n2) which is too much.

In order to reduce storage requirements, Mike is willing to allow a small amount of computation per query. He wants to store a cleverer selection of precomputed values than just max(ei, . . . , ej ) for every (i, j), so that for any user query, the server can retrive two precomputed values and take the maximum of the two to return the final answer. Show that now only O(n log n) values need to be precomputed.

http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/recitation-videos/MIT6_006F11_rec11.pdf

## Code Example

import partial_maxima

events = partial_maxima.EventList()  #optionally can pass in parameter for size of the EventList, defaults to 10^5

events.most_exciting_event(5, 55)   #query: start_index = 5, end_index = 55

events.print_events

The EventList is an object that contains a list of Event objects. An Event contains an index and an excitement variable. The excitement variable is simply a number between 0 to 1 that measures how important or exciting an event was. It is assumed that the indices represent ordering of the events in a chronological sense. 

The constructor initializes the list of Event objects by randomly assigning to each an excitement level. 

The function most_exciting_events takes in two indices, one for the start and the other for the end of the query. The latter asks the question: "what is the event with the largest excitment level for events with index between start index and end index?"

In order for this query to run in constant time, O(nlgn) storage must be used (where n is the number of events) to precompute partial maxima. This is done in the function precompute, which recursively calculates the most exciting event in the necessary ranges (O(nlgn) of them).



