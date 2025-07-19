""" Entrypoint for this LifeGen application. """
from src.generate import gen_life

# In main file, import and run function.
# Simple string printed here to verify, complexity should be exported to file output.
life = gen_life()
print(f"Generated life form: '{life}'")
