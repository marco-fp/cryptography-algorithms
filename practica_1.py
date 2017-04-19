from timeit import time
from modular_arithmetic import euclidean
from modular_arithmetic import inverse_mod
from modular_arithmetic import pow_mod
from modular_arithmetic import miller_rabin
from modular_arithmetic import baby_step_giant_step
from modular_arithmetic import sqrt_mod
from modular_arithmetic import fermatFactor
from modular_arithmetic import pollardFactor

def main():
  print "Criptografia - Practica 1 - Aritmetica Modular"
  print "1. Euclides: (1128, 231)"
  start_time = time.time()
  print euclidean.extendedGcd(1128,231)
  elapsed_time = time.time() - start_time
  print("%0.10f" % elapsed_time)


  print "2. inverseMod: (443, 7): "
  start_time = time.time()
  print inverse_mod.inverseMod(443, 7)
  elapsed_time = time.time() - start_time
  print("%0.10f" % elapsed_time)


  print "3. powMod: (36780481, 9476407, 768479):"
  start_time = time.time()
  print pow_mod.powMod(36780481, 9476407, 768479)
  elapsed_time = time.time() - start_time
  print("%0.10f" % elapsed_time)

  print "4. Miller Rabin: (123456789101119)"
  start_time = time.time()
  print miller_rabin.miller_rabin(123456789101119, 10)
  elapsed_time = time.time() - start_time
  print("%0.10f" % elapsed_time)


  print "5. Baby step giant step: (3, 2, 29)"
  start_time = time.time()
  print baby_step_giant_step.babyStepGiantStep(3, 2, 29)
  elapsed_time = time.time() - start_time
  print("%0.10f" % elapsed_time)

  print "6. Square root in modulus: (111, 113)"
  start_time = time.time()
  print sqrt_mod.sqrtMod(111, 113)
  elapsed_time = time.time() - start_time
  print("%0.10f" % elapsed_time)

  print "7.2. Pollard factorization method: (123456789123456789)"
  start_time = time.time()
  print pollardFactor.pollardFactor(123456789123456789)
  elapsed_time = time.time() - start_time
  print("%0.10f" % elapsed_time)


  print "7.1. Fermat factorization method: (123456789123456789)"
  start_time = time.time()
  #print fermatFactor.fermatFactor(10)
  elapsed_time = time.time() - start_time
  print("%0.10f" % elapsed_time)







if __name__ == '__main__':
    main()
