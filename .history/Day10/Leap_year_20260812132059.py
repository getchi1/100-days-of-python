"""              Is it divisible by 4?
                    |
             +------+------+
             YES           NO
              |             |
       Is it divisible?    ❌ Not
          by 100?          leap
          /    \
        YES     NO
         |       |
   Divisible?    ✅ Leap
    by 400?
      /   \
    YES    NO
     |      |
   ✅ Leap  ❌ Not leap"""

def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 or number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        else:
            print([number])