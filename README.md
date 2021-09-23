# General Instructions
1. Please implement all your functions (except for question 4) inside
   a single module called `solutions.py`. For question 4, please write
   your tests inside the `test_primality.py` file. Empty files with
   these names have been provided for you to get started.
1. Please make sure your functions return proper values. Otherwise,
   they will fail the auto evaluator and you will be rejected. 
1. You don't need to write `input` statements to read input from the
   user. Just implement the functions as per specification. **This is important**
1. Please make sure that the functions are named exactly as indicated
   in the question. Please make sure that your implementation is
   accurate. e.g. If the question asks you to *return* something,
   please don't just *print* it. 
1. Please write the functions as precisely and efficiently as possible. No unnecessary code. No spelling mistakes. Good variable names and control flow. 
1. Please don’t just upload onto github. Show us that you can use git properly. 
1. If you add tests for your functions, you will get bonus points. 
1. If you touch the `test_basic.py` or the `test_test_primes.py` files, your exercises will fail and you will fail the test

# Questions
1. Write a function `biggest` in python that will
   - take a list of numbers `n` as input and
   - return the largest element in the list. 

    Don't use the `sort` method of the list or the inbuilt `max`
   function. Please don't modify the input list either.

    e.g. `biggest([1,2,3,4])` should return `4`.
1. Write a function `biggest2` in python that will 
   - take a list of numbers `n` as input and
   - return the largest 2 elements in the list. 

    Don't use the `sort` of the list or the inbuilt `max`
    function. Please don't modify the input list either.

    e.g. `biggest2([1,2,3,4])` should return `[3, 4]`.
1. Write a function `biggestn` in Python that will
   - take a list of numbers `n` and a number `m` as inputs
   - and return the largest `m` numbers in the list `n`.

    Don't use the `sort` method of the list or the inbuilt `max`
   function. Please don't modify the input list either.

    e.g. `biggestn([1,2,3,4], 1)` will return
   `[4]`, `biggestn([1,2,3,4], 2)` will return `[3,4]` etc.
1. The file `isprime.py` contains this function to test whether a
   number is prime or not. Write a few test cases for this function to
   see if you can catch any errors in the implementation. These test
   cases should be written inside a module called
   `test_primality.py`. If you need any custom modules (like nose
   etc.), please modify the `requirements.txt` as necessary.


        import math
  
        def isprime(n):
           if n%2 == 0 or n%3 == 0 or n%5==0:
               return False
           for i in range(7, math.floor(math.sqrt(n)), 2):
               if n%i == 0:
                   return False
           return True
1. Write a function `ffindstring` that will take 
     - a file *name* `fname` and
     - a string `s` as input. 

   It will return whether `s` occurs inside the file. 

   Please make sure your implementation covers both the following cases.
    - It's possible that the file is extremely large so it cannot be
      read into memory in one shot. You should not just `read()` the
      file entirely into memory.
    - It’s also possible that `s` has a newline in it. You should not
      just iterate over the open file.
1. Write a function `panagram` that will 
   - take a string `s` as input 


    It will return `True` if `s` contains all letters of the alphabet
   (a to z) and `False` otherwise. 
   
   e.g. It should return `True` for
   sentences like "The quick brown fox jumps over the lazy dog".
1. Write a function `breakdown` that will
   - take an amount `amt` and
   - a dictionary `denominations` as inputs
   
   `amt` is an amount of money and `denominations` are the notes available with you. An example follows


         amt = 1256
         denominations = {
                   2000   : 10
                   500   : 10
                   100   : 20
                    50   : 0
                    20   : 10
                    10   : 5
                     5   : 10
                     2   : 10
                     1   : 10
                }
 
    The function should return a dictionary that contains how it will break down the given amount using the notes available. For example, in the above case, it would return 
 
            { 500 : 2, 100 : 2, 20 : 2, 10 :  1, 5:1, 1:1}
            
    To get `1256`, it is asking you to take `2` `500`s, `2` `100`s
    etc. Also, the `denominations` dictionary will have these amounts
    deducted from it. 
    
    If the amount cannot be returned from the available notes, you should raise a custom `NotAvailable` exception. e.g. `breakdown(1210, {100 : 20})` will raise the exception since it’s not possible to return 1210 using the available notes (Twenty `100`s). Also, if you cannot return the amount, the denominations dictionary should not be modified at all.
 
# Testing your code

To test your code, do the following
1. Create a `virtualenv` and activate it.
2. Install all the requirements mentioned in the `requirements.txt` file using `pip install -r requirements.txt`
3. Type `py.test -v test_basic.py test_test_primes.py` to run the tests. All should pass.

# Submitting your code

Once you've finished your implementation, commit the files and push
them to the repo you cloned from. Github will automatically grade your
solutions. Please send an email to `nanditha@hamon.in` with the link
to your repository.


