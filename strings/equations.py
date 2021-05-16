def MathChallenge(strParam):

  # separate the left side and right side of equation
  right_side = strParam.split('=')[1].strip()
  left_side = strParam.split('=')[0]
 
  # find where the x is
  side_with_x = find_x(left_side, right_side)

  # split the left side further to work with below
  left_side_split = left_side.split(" ")
  part1 = left_side_split[0]
  op = left_side_split[1]
  part2 = left_side_split[2]

  opp_operator = {
    "+": lambda x, y: x - y,
    "-": lambda x, y: x + y,
    "/": lambda x, y: x * y,
    "*": lambda x, y: x // y
  }

  same_operator = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x // y,
    "*": lambda x, y: x * y,
  }

  # if x in right side
  if side_with_x == right_side:
    # find length of right side
    len_right_side = len(right_side)
    result = same_operator[op](int(part1), int(part2))
    if len_right_side == 1:
      return result
    elif right_side[-1] == 'x':
      result = result // int(right_side[:-1])
      return result
    # if x inside digit
    else:
      ind = right_side.index('x')
      result = str(result)[ind]
      return result
   
  # if x in part 1
  elif part1.find('x') != -1:
    len_part1 = len(part1)
    result = opp_operator[op](int(right_side), int(part2))
    if len_part1 == 1:
      return result
    elif part1[-1] == 'x':
      result = result // int(part1[:-1])
      return result
    else:
      ind = part1.index('x')
      result = str(result)[ind]
      return result
  
  # if x in part 2
  else:
    len_part2 = len(part2)
    result = opp_operator[op](int(right_side), int(part1))
    if len_part2 == 1:
      return result
    elif part2[-1] == 'x':
      result = result // int(part2[:-1])
      return result
    else:
      ind = part2.index('x')
      result = str(result)[ind]
      return result


def find_x(left_side, right_side):
  # if x in left side
  if left_side.find('x') != -1:
    return left_side

  # if right side contains x
  else:
    return right_side
