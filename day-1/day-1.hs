main = do
  contents <- readFile "input.txt"
  let input = map read (lines contents)
  print (solve_part_1 input 0)

solve_part_1 :: [Int] -> Int -> Int
solve_part_1 [x] count = count
solve_part_1 (x:xs) count =
  solve_part_1 xs (count + countIncrease x (head xs))

countIncrease a b = if b > a then 1 else 0
