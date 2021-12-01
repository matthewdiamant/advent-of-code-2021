main = do
  contents <- readFile "input.txt"
  print (solve (depths contents) 0 0)
  print (solve (depths contents) 2 0)

depths :: [Char] -> [Int]
depths contents = map read (lines contents)

solve :: [Int] -> Int -> Int -> Int
solve (x:xs) idx count =
  if length xs == idx
  then count
  else
    solve xs idx (count + countIncrease (x < (xs !! idx)))

countIncrease :: Bool -> Int
countIncrease True = 1
countIncrease False = 0
