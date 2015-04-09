import glopen

def MR_init(args, params, frame):
  from copy import deepcopy
  ans = {"words" : {}}
  base = deepcopy(ans)
  jobs = []
  ans["fname"] = "/tmp/Dickens/TaleOfTwoCities.txt"
  jobs.append(((0, 16271), params, args, deepcopy(ans)))
  ans["fname"] = "/tmp/Dickens/ChristmasCarol.txt"
  jobs.append(((0, 4236), params, args, deepcopy(ans)))
  ans["fname"] = "/tmp/Dickens/HardTimes.txt"
  jobs.append(((0, 12036), params, args, deepcopy(ans)))
  ans["fname"] = "/tmp/Dickens/GreatExpectations.txt"
  jobs.append(((0, 20415), params, args, deepcopy(ans)))
  ans["fname"] = "/tmp/Dickens/DavidCopperfield.txt"
  jobs.append(((0, 38588), params, args, deepcopy(ans)))
  ans["fname"] = "/tmp/Dickens/BleakHouse.txt"
  jobs.append(((0, 40234), params, args, deepcopy(ans)))
  ans["fname"] = "/tmp/Dickens/PickwickPapers.txt"
  jobs.append(((0, 36613), params, args, deepcopy(ans)))
  ans["fname"] = "/tmp/Dickens/OliverTwist.txt"
  jobs.append(((0, 19202), params, args, deepcopy(ans)))


  return jobs, base

def map_(pos, nelm_to_read, params, ans, last):
  if "input_file" not in ans:
    ans["glopen"] = glopen.glopen(ans["fname"], "r", endpoint="maxhutch#alpha-admin")
    ans["input_file"] = ans["glopen"].__enter__()

  for i in range(nelm_to_read):
    line = ans["input_file"].readline()
    for tok in line.split():
      word = tok.strip('.,;:?!_/\\--"`')
      if word in ans["words"]:
        ans["words"][word] += 1
      else:
        ans["words"][word] = 1

  if last and False:
    ans["glopen"].__exit__(None, None, None)
    del ans["glopen"]
    del ans["input_file"]

  return ans

def reduce_(whole, part):
  for word in part["words"]:
    if word in whole["words"]:
      whole["words"][word] += part["words"][word]
    else:
      whole["words"][word]  = part["words"][word]
  return
