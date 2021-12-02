main = do
  contents <- readFile "input.txt"
  print (solvePart1 contents)
  print (solvePart2 contents)

solvePart1 :: String -> Int
solvePart1 input = drive1 (parseInput input) 0 0

parseInput :: String -> [(String, Int)]
parseInput input = map createInstruction (lines input)

createInstruction :: String -> (String, Int)
createInstruction line = (head (words line), read (words line !! 1) :: Int)

drive1 :: [(String, Int)] -> Int -> Int -> Int
drive1 [] horizontal depth = horizontal * depth
drive1 (x:xs) horizontal depth = drive1 xs (changeHorizontal horizontal x) (changeDepth depth x)

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

solvePart2 :: String -> Int
solvePart2 input = drive2 (parseInput input) (0, 0) 0

drive2 :: [(String, Int)] -> (Int, Int) -> Int -> Int
drive2 [] (horizontal, depth) aim = horizontal * depth
drive2 (x:xs) (horizontal, depth) aim = drive2 xs (goForward (horizontal, depth) aim x) (changeAim aim x)

goForward :: (Int, Int) -> Int -> (String, Int) -> (Int, Int)
goForward (horizontal, depth) aim (direction, value) =
    if direction == "forward"
       then (horizontal + value, depth + aim * value)
       else (horizontal, depth)

changeAim :: Int -> (String, Int) -> Int
changeAim aim (direction, value)
  | direction == "up" = aim - value
  | direction == "down" = aim + value
  | otherwise = aim
