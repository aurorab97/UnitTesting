def add(a: int | float, b: int | float) -> int | float:
  """
  Just adds two numbers together.
  """
  return a + b

def subtract(a: int | float, b: int | float) -> int | float:
  """
  Just subtracts two numbers.
  """
  return a - b

def divide(a: int | float, b: int | float) -> float:
  """
  Just divides two numbers.
  """
  if b == 0:
    raise ValueError("You cannot divide by zero!")
  return a / b 
  
