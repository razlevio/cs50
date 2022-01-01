# WIP
Questions
1. With a linear page table, you need a single register to locate the
page table, assuming that hardware does the lookup upon a TLB
miss. How many registers do you need to locate a two-level page
table? A three-level table?
2. Use the simulator to perform translations given random seeds 0,
1, and 2, and check your answers using the -c flag. How many
memory references are needed to perform each lookup?
3. Given your understanding of how cache memory works, how do
you think memory references to the page table will behave in the
cache? Will they lead to lots of cache hits (and thus fast accesses?)
Or lots of misses (and thus slow accesses)?
