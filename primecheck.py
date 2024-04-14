def is_prime(number):
  """
  Check if a number is prime.

  Args:
    number: The number to check.

  Returns:
    True if the number is prime, False otherwise.
  """

  # If the number is 1, it is not prime.
  if number == 1:
    return False

  # Iterate over all numbers from 2 to the square root of the number.
  for i in range(2, int(number ** 0.5) + 1):
    # If the number is divisible by any number from 2 to its square root, it is not prime.
    if number % i == 0:
      return False

  # If the number is divisible by no number from 2 to its square root, it is prime.
  return True

