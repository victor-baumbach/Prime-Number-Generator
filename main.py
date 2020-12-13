def FindPrimeNumbers (end):
  primeNumbers = [2];
  i = 3;
  while i < end:
    isPrime = True;
    for number in primeNumbers:
      if i % number == 0:
        isPrime = False;
    if isPrime:
      primeNumbers.append(i);
    i += 2;
  return primeNumbers;

print(FindPrimeNumbers(1000));