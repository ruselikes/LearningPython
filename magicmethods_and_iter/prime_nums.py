
class Primes:
    def __init__(self,N):
        self.current = 1
        self.n = N
    def __iter__(self):
        return self

    def __next__(self):
        if self.current == 1:
            self.current += 1
            return 1
        else:
            if self.current >= self.n:
                raise StopIteration
            else:

                is_prime = True

                # if all(self.current % i != 0 for i in range(2, self.current//2+1)):
                #     is_prime = self.current
                #     self.current += 1
                #     return is_prime
                # else:
                #     self.current =+ 1

                for i in range(2, self.current//2+1):
                    if self.current % i == 0:
                        is_prime = False
                        self.current += 1
                        return self.__next__()
                        break



                if is_prime == True:
                    result = self.current
                    self.current +=1
                    return result





prime_nums = Primes(50)


for i_elem in prime_nums:

    print(i_elem, end=' ')