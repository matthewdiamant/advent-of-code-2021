main = do
  contents <- readFile "input.txt"
  print (solve_part_1 contents)

solve_part_1 input = drive (parseInput input) 0 0

parseInput :: String -> [(String, Int)]
parseInput input = map createInstruction (lines input)

createInstruction :: String -> (String, Int)
createInstruction line = (head (words line), read (words line !! 1) :: Int)

drive :: [(String, Int)] -> Int -> Int -> Int
drive [] horizontal depth = horizontal * depth
drive (x:xs) horizontal depth = drive xs (changeHorizontal horizontal x) (changeDepth depth x)

changeHorizontal :: Int -> (String, Int) -> Int
changeHorizontal horizontal (direction, value) =
    if direction == "forward"
       then horizontal + value
       else horizontal

changeDepth :: Int -> (String, Int) -> Int
changeDepth depth (direction, value)
  | direction == "up" = depth - value
  | direction == "down" = depth + value
  | otherwise = depth
