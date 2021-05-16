def GraphChallenge(strArr):

  longest_path = -1

  hashmap = {}

  # add all nodes to a dictionary in the style of an undirected graph
  for item in strArr:
    item = item.split('-')
    if item[0] in hashmap:
      hashmap[item[0]].append(item[1])
    else:
      hashmap[item[0]] = [item[1]]
    if item[1] in hashmap:
      hashmap[item[1]].append(item[0])
    else:
      hashmap[item[1]] = [item[0]]

  # give each node a chance to be the starting node
  for k, v in hashmap.items():

    # get the longest path from that node
    path = dfs(hashmap, k)

    # if it is longer than our path so far
    if path > longest_path:

      # we have a new longest path
      longest_path = path

  return longest_path

  # DFS
def dfs(hashmap, starting_node):

  # keep track of what we have visited
  visited = []

  stack = [starting_node]
  path_len = 0

  while stack:

    # pop off the top node
    node = stack.pop(0)
    # we have visited this node now
    visited.append(node)
    # increase the path len
    path_len += 1
    # get the children
    values = hashmap[node]

    # if we have visited all children, these variables will be useful
    already_visited = 0
    num_children = 0

    # for each child
    for item in values:
      num_children += 1
      # if we haven't visited them
      if item not in visited:
        # add to stack if not visited
        stack.append(item)

      # if already visited
      else:
        already_visited += 1

      # if we have visited all children
      if num_children == already_visited:
        return path_len
      break

# keep this function call here 
print(GraphChallenge(input()))
