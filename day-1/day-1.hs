main = do
  contents <- readFile "input.txt"
  let input = map read (lines contents)
  print (solve input 0 0)
  print (solve input 2 0)

solve :: [Int] -> Int -> Int -> Int
solve (x:xs) idx count =
  if length xs == idx
  then count
  else
    solve xs idx (count + countIncrease x (xs !! idx))

countIncrease a b = if b > a then 1 else 0
